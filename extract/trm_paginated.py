import json
import datetime as dt
import pathlib
import time

import requests

URL = "https://www.datos.gov.co/resource/32sa-8pi3.json"
PAGE_SIZE = 1000

out = pathlib.Path("data/bronze/trm") / f"ingest_date={dt.date.today()}"
out.mkdir(parents=True, exist_ok=True)

offset = 0
page = 1
all_rows = []

while True:
    params = {
        "$order": "vigenciadesde ASC",
        "$limit": PAGE_SIZE,
        "$offset": offset,
    }
    resp = requests.get(URL, params=params, timeout=30)
    resp.raise_for_status()
    rows = resp.json()

    if not rows:
        print(f"Page {page} is empty -> done.")
        break

    page_file = out / f"page_{page:04d}.json"
    page_file.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    print(f"Page {page}: offset={offset}, rows={len(rows)} -> {page_file.name}")

    all_rows.extend(rows)
    offset += PAGE_SIZE
    page += 1
    time.sleep(1)

# Check: did we get everything, with no duplicates?
count_resp = requests.get(URL, params={"$select": "count(*)"}, timeout=30)
count_resp.raise_for_status()
expected = int(count_resp.json()[0]["count"])
unique_dates = len({row["vigenciadesde"] for row in all_rows})

print(f"Downloaded: {len(all_rows)} | API says: {expected} | Unique start dates: {unique_dates}")