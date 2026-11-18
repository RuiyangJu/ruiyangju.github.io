
from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime, timezone
import os
import time

AUTHOR_ID = "r8F35p8AAAAJ"
OUT_DIR = "results"
MAX_RETRIES = 3


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_json(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError) as e:
        print(f"[warn] Cannot read {path}: {e}")
        return {}


def save_json(path, data):
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, path)


def setup_proxy():
    # Direct connection first; optionally enable free proxies.
    mode = os.getenv("SCHOLAR_PROXY", "direct").lower()

    if mode != "free":
        print("[info] Using direct connection.")
        return

    try:
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
            print("[info] Free proxy enabled.")
        else:
            print("[warn] Free proxy unavailable; using direct connection.")
    except Exception as e:
        print(f"[warn] Proxy setup failed: {e}")


def fetch_with_retries(func, label, max_retries=MAX_RETRIES):
    for i in range(max_retries):
        try:
            result = func()
            if result is None:
                raise ValueError("Empty response")
            return result
        except Exception as e:
            print(
                f"[warn] {label} failed "
                f"({i + 1}/{max_retries}): {repr(e)}"
            )
            if i + 1 < max_retries:
                time.sleep(3 * (i + 1))
    return None


def publications_list_to_dict(pubs):
    if isinstance(pubs, dict):
        return pubs

    if not isinstance(pubs, list):
        return {}

    out = {}
    for idx, v in enumerate(pubs):
        if not isinstance(v, dict):
            continue
        key = (
            v.get("author_pub_id")
            or v.get("pub_url")
            or (v.get("bib", {}) or {}).get("title")
            or f"idx_{idx}"
        )
        out[str(key)] = v
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    data_path = os.path.join(OUT_DIR, "gs_data.json")
    shield_path = os.path.join(OUT_DIR, "gs_data_shieldsio.json")
    error_path = os.path.join(OUT_DIR, "gs_error.json")

    previous = load_json(data_path)
    setup_proxy()

    author = fetch_with_retries(
        lambda: scholarly.search_author_id(
            AUTHOR_ID, filled=False
        ),
        "search_author_id"
    )

    if author is None:
        print("[warn] Google Scholar unavailable.")

        save_json(error_path, {
            "updated": now_iso(),
            "author_id": AUTHOR_ID,
            "error": "Failed to fetch author profile"
        })

        if previous:
            print("[info] Previous data preserved.")
        else:
            print("[warn] No previous data available.")

        # Do not fail the entire GitHub Actions workflow.
        return

    # Retrieve profile statistics.
    stats = fetch_with_retries(
        lambda: scholarly.fill(
            author,
            sections=["basics", "indices", "counts"]
        ),
        "fill statistics"
    )

    if stats:
        author = stats
    else:
        print("[warn] Statistics unavailable; preserving old values.")

    # Retrieve publications.
    pubs = fetch_with_retries(
        lambda: scholarly.fill(
            author,
            sections=["publications"]
        ),
        "fill publications"
    )

    if pubs:
        author = pubs
    else:
        print("[warn] Publications unavailable; preserving old values.")

    # Merge new data with previous data.
    merged = previous.copy()

    for key, value in author.items():
        if key == "publications":
            new_pubs = publications_list_to_dict(value)
            old_pubs = publications_list_to_dict(
                previous.get("publications", {})
            )

            if new_pubs:
                old_pubs.update(new_pubs)
                merged[key] = old_pubs
            elif old_pubs:
                merged[key] = old_pubs

        elif value is not None and value != "":
            merged[key] = value

    merged["author_id"] = AUTHOR_ID
    merged["updated"] = now_iso()

    # Avoid saving a profile without useful statistics
    # when no previous data exists.
    if not previous and merged.get("citedby") is None:
        print("[warn] No citation data; skipping incomplete output.")
        return

    save_json(data_path, merged)

    citedby = merged.get("citedby")
    if citedby is None:
        citedby = "N/A"

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citedby),
    }

    save_json(shield_path, shieldio_data)

    # Remove stale error status after a successful update.
    if os.path.exists(error_path):
        os.remove(error_path)

    print("[info] Successfully updated:")
    print(" -", data_path)
    print(" -", shield_path)
    print(f"[info] Citations: {citedby}")


if __name__ == "__main__":
    main()
