import json, datetime as dt, pathlib, requests

URL = "https://www.datos.gov.co/resource/32sa-8pi3.json"
params = {"$order": "vigenciadesde DESC", "$limit": 10}

resp = requests.get(URL, params=params, timeout=30)   # send the GET request
print("Status:", resp.status_code)                    # expect 200
resp.raise_for_status()                               # crash loudly on 4xx/5xx

rows = resp.json()                                    # JSON text -> list of dicts
print(json.dumps(rows[:2], indent=2, ensure_ascii=False))

# Land it "Bronze-style": raw, untouched, partitioned by ingestion date
out = pathlib.Path("data/bronze/trm") / f"ingest_date={dt.date.today()}"
out.mkdir(parents=True, exist_ok=True)
(out / "trm_sample.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
print(f"Saved {len(rows)} rows to {out}")