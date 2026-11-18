
import os
import json
from datetime import datetime, timezone

import requests

AUTHOR_ID = "r8F35p8AAAAJ"
OUT_DIR = os.path.join(os.path.dirname(__file__), "results")
API_KEY = os.environ["SERPAPI_API_KEY"]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    data_path = os.path.join(OUT_DIR, "gs_data.json")
    shield_path = os.path.join(OUT_DIR, "gs_data_shieldsio.json")

    response = requests.get(
        "https://serpapi.com/search.json",
        params={
            "engine": "google_scholar_author",
            "author_id": AUTHOR_ID,
            "api_key": API_KEY,
            "hl": "en",
        },
        timeout=60,
    )
    response.raise_for_status()
    result = response.json()

    if result.get("error"):
        raise RuntimeError(result["error"])

    # Extract total citations only
    citations = int(
        result["cited_by"]["table"][0]["citations"]["all"]
    )

    updated = datetime.now(timezone.utc).isoformat()

    # Preserve previous fields, if any
    previous = {}
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            previous = json.load(f)

    previous.update({
        "author_id": AUTHOR_ID,
        "citedby": citations,
        "updated": updated,
    })

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(previous, f, ensure_ascii=False, indent=2)

    # Shields.io badge
    shield = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations),
    }

    with open(shield_path, "w", encoding="utf-8") as f:
        json.dump(shield, f, ensure_ascii=False, indent=2)

    print(f"[info] Total citations: {citations}")
    print("[info] Google Scholar updated successfully")


if __name__ == "__main__":
    main()
