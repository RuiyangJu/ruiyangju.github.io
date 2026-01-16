from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime, timezone
import os
import time

AUTHOR_ID = "r8F35p8AAAAJ"
OUT_DIR = "results"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def setup_proxy():
    pg = ProxyGenerator()
    ok = pg.FreeProxies()
    if not ok:
        # Not fatal; scholarly can still try without proxy
        print("[warn] FreeProxies() failed to initialize. Will try without proxy.")
        return None

    scholarly.use_proxy(pg)
    print("[info] Proxy enabled via FreeProxies().")
    return pg

def safe_fill(author: dict, sections, max_retries=5, base_sleep=2.0):
    last_exc = None
    for i in range(max_retries):
        try:
            filled = scholarly.fill(author, sections=sections)
            return filled, True, None
        except Exception as e:
            last_exc = e
            wait = base_sleep * (i + 1)
            print(f"[warn] fill(sections={sections}) failed (try {i+1}/{max_retries}): {repr(e)}")
            time.sleep(wait)
    return author, False, last_exc

def publications_list_to_dict(pubs):
    if not isinstance(pubs, list):
        return {}

    out = {}
    for idx, v in enumerate(pubs):
        if not isinstance(v, dict):
            continue
        key = v.get("author_pub_id") or v.get("pub_url") or (v.get("bib", {}) or {}).get("title") or f"idx_{idx}"
        out[str(key)] = v
    return out

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    setup_proxy()
    author = None
    last_exc = None
    for i in range(5):
        try:
            author = scholarly.search_author_id(AUTHOR_ID, filled=False)
            break
        except Exception as e:
            last_exc = e
            print(f"[warn] search_author_id failed (try {i+1}/5): {repr(e)}")
            time.sleep(2 * (i + 1))

    if author is None:
        err_path = os.path.join(OUT_DIR, "gs_error.json")
        with open(err_path, "w", encoding="utf-8") as f:
            json.dump(
                {"updated": now_iso(), "author_id": AUTHOR_ID, "error": repr(last_exc)},
                f,
                ensure_ascii=False,
                indent=2,
            )
        raise RuntimeError(f"Failed to fetch author profile after retries: {repr(last_exc)}")
   
    author["updated"] = now_iso()

    author, ok1, e1 = safe_fill(author, sections=["basics", "indices", "counts"], max_retries=5)
    if not ok1:
        print("[warn] Could not fill basics/indices/counts reliably; continuing with partial data.")

    author, ok2, e2 = safe_fill(author, sections=["publications"], max_retries=5)
    if not ok2:
        print("[warn] Could not fill publications (likely blocked). Continuing without publications.")

    author["publications"] = publications_list_to_dict(author.get("publications", []))

    out_path = os.path.join(OUT_DIR, "gs_data.json")
    with open(out_path, "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    citedby = author.get("citedby")
    if citedby is None:
        # Some partial profiles might not have it
        citedby = "N/A"

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{citedby}",
    }

    shield_path = os.path.join(OUT_DIR, "gs_data_shieldsio.json")
    with open(shield_path, "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

    print("[info] Done. Wrote:")
    print(" -", out_path)
    print(" -", shield_path)

if __name__ == "__main__":
    main()
