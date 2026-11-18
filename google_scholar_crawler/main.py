
import os
import json
import time
from datetime import datetime, timezone

import requests

AUTHOR_ID = "r8F35p8AAAAJ"
OUT_DIR = os.path.join(os.path.dirname(__file__), "results")
API_KEY = os.getenv("SERPAPI_API_KEY")
MAX_RETRIES = 3
MAX_PAGES = 1  # 100 articles per page


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_json(path):
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            value = json.load(f)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def fetch_page(start=0):
    params = {
        "engine": "google_scholar_author",
        "author_id": AUTHOR_ID,
        "api_key": API_KEY,
        "hl": "en",
        "num": 100,
        "start": start,
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(
                "https://serpapi.com/search.json",
                params=params,
                timeout=90,
            )
            response.raise_for_status()
            data = response.json()

            if data.get("error"):
                raise RuntimeError(data["error"])

            status = data.get("search_metadata", {}).get("status")
            if status != "Success":
                raise RuntimeError(f"Search status: {status}")

            if not isinstance(data.get("author"), dict):
                raise RuntimeError("Missing author information")

            return data

        except Exception as e:
            print(f"[warn] API request {attempt}/{MAX_RETRIES}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(5 * attempt)

    return None


def parse_metrics(data):
    table = data.get("cited_by", {}).get("table", [])
    metrics = {}

    for entry in table:
        for key, value in entry.items():
            if not isinstance(value, dict):
                continue

            all_value = value.get("all")
            if all_value is None:
                continue

            normalized = key.lower().replace("-", "_")

            if normalized in ("citations",):
                metrics["citedby"] = all_value
                metrics["citedby5y"] = value.get("since_2021", 0)
            elif normalized in ("h_index", "indice_h"):
                metrics["hindex"] = all_value
                metrics["hindex5y"] = value.get("since_2021", 0)
            elif normalized in ("i10_index", "indice_i10"):
                metrics["i10index"] = all_value
                metrics["i10index5y"] = value.get("since_2021", 0)

    # The rolling 5-year fields above must be computed
    # only when the API explicitly supplies the correct period.
    for key in ("citedby5y", "hindex5y", "i10index5y"):
        if metrics.get(key) == 0:
            metrics.pop(key, None)

    graph = data.get("cited_by", {}).get("graph", [])
    if graph:
        metrics["cites_per_year"] = {
            str(row["year"]): int(row["citations"])
            for row in graph
            if "year" in row and "citations" in row
        }

    return metrics


def parse_publications(articles):
    publications = {}

    for article in articles:
        citation_id = article.get("citation_id")
        if not citation_id:
            continue

        cited_by = article.get("cited_by") or {}
        if not isinstance(cited_by, dict):
            cited_by = {}

        pub = {
            "author_pub_id": citation_id,
            "bib": {
                "title": article.get("title", ""),
                "author": article.get("authors", ""),
                "citation": article.get("publication", ""),
                "pub_year": article.get("year", ""),
            },
            "num_citations": cited_by.get("value", 0),
            "pub_url": article.get("link", ""),
            "filled": False,
        }

        publications[citation_id] = pub

    return publications


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    data_path = os.path.join(OUT_DIR, "gs_data.json")
    shield_path = os.path.join(
        OUT_DIR, "gs_data_shieldsio.json"
    )
    error_path = os.path.join(OUT_DIR, "gs_error.json")

    previous = load_json(data_path)

    if not API_KEY:
        raise RuntimeError(
            "Missing SERPAPI_API_KEY GitHub Actions secret"
        )

    print("[info] Fetching Google Scholar via SerpAPI")

    first = fetch_page(0)

    if first is None:
        save_json(error_path, {
            "updated": now_iso(),
            "author_id": AUTHOR_ID,
            "error": "SerpAPI request failed",
        })
        print("[warn] Existing data preserved.")
        return

    metrics = parse_metrics(first)

    if "citedby" not in metrics:
        print("[warn] Citation statistics missing.")
        print("[warn] Existing data preserved.")
        return

    profile = first["author"]

    merged = previous.copy()
    merged.update({
        "scholar_id": AUTHOR_ID,
        "author_id": AUTHOR_ID,
        "name": profile.get("name", previous.get("name", "")),
        "affiliation": profile.get(
            "affiliations", previous.get("affiliation", "")
        ),
        "updated": now_iso(),
    })
    merged.update(metrics)

    articles = list(first.get("articles", []))

    # Optional additional publication pages
    for page in range(1, MAX_PAGES):
        data = fetch_page(page * 100)
        if not data:
            break
        new_articles = data.get("articles", [])
        if not new_articles:
            break
        articles.extend(new_articles)

    new_pubs = parse_publications(articles)
    old_pubs = previous.get("publications", {})

    if not isinstance(old_pubs, dict):
        old_pubs = {}

    old_pubs.update(new_pubs)
    merged["publications"] = old_pubs

    save_json(data_path, merged)

    shield = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(merged["citedby"]),
    }
    save_json(shield_path, shield)

    if os.path.exists(error_path):
        os.remove(error_path)

    print("[info] Google Scholar updated successfully")
    print(f"[info] Citations: {merged['citedby']}")
    print(f"[info] Publications: {len(old_pubs)}")


if __name__ == "__main__":
    main()
