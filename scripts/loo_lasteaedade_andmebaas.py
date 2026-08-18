#!/usr/bin/env python3
"""Ehita Eesti lasteaedade andmebaas OpenStreetMap andmetest."""

import csv
import json
import re
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CSV_OUT = DATA_DIR / "lasteaedade-andmebaas.csv"
JSON_OUT = DATA_DIR / "lasteaedade-email-list.json"
EMAIL_CSV = DATA_DIR / "lasteaedade-email-list.csv"

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
UA = "Unpluged-Al/1.0 (lasteaedade-andmebaas; contact: reneealuste@gmail.com)"

QUERY = """
[out:json][timeout:120];
area["ISO3166-1"="EE"][admin_level=2]->.ee;
(
  node["amenity"="kindergarten"](area.ee);
  way["amenity"="kindergarten"](area.ee);
  relation["amenity"="kindergarten"](area.ee);
);
out center tags;
"""


def fetch_osm():
    cache = Path("/tmp/osm_kg.json")
    if cache.exists():
        return json.loads(cache.read_text()).get("elements", [])
    r = requests.post(
        OVERPASS_URL,
        data={"data": QUERY},
        headers={"User-Agent": UA},
        timeout=120,
    )
    r.raise_for_status()
    return r.json().get("elements", [])


def parse_element(el):
    tags = el.get("tags", {})
    name = tags.get("name") or tags.get("official_name") or ""
    if not name:
        return None
    lat = el.get("lat") or (el.get("center") or {}).get("lat")
    lon = el.get("lon") or (el.get("center") or {}).get("lon")
    addr = ", ".join(
        p
        for p in [
            tags.get("addr:street"),
            tags.get("addr:housenumber"),
            tags.get("addr:city") or tags.get("addr:place"),
        ]
        if p
    )
    email = tags.get("email") or tags.get("contact:email") or ""
    phone = tags.get("phone") or tags.get("contact:phone") or ""
    web = tags.get("website") or tags.get("contact:website") or ""
    reg = tags.get("ref:EHIS") or tags.get("ref") or ""
    return {
        "nimi": name.strip(),
        "reg_kood": reg,
        "aadress": addr,
        "omavalitsus": tags.get("addr:city") or tags.get("addr:place") or "",
        "maakond": tags.get("addr:state") or "",
        "telefon": phone,
        "email": email.lower() if email else "",
        "veebileht": web,
        "direktor_email": "",
        "lat": lat,
        "lon": lon,
        "allikas": "OpenStreetMap",
        "markus": "",
    }


def dedupe(rows):
    seen = {}
    for row in rows:
        key = re.sub(r"\s+", " ", row["nimi"].lower())
        if key not in seen:
            seen[key] = row
        else:
            old = seen[key]
            for field in ("email", "telefon", "veebileht", "aadress", "reg_kood"):
                if not old[field] and row[field]:
                    old[field] = row[field]
    return list(seen.values())


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print("Laen OpenStreetMap andmeid...")
    elements = fetch_osm()
    rows = [r for el in elements if (r := parse_element(el))]
    rows = dedupe(rows)
    rows.sort(key=lambda x: (x["omavalitsus"], x["nimi"]))
    print(f"Lasteaedu kokku: {len(rows)}")
    print(f"Emailiga: {sum(1 for r in rows if r['email'])}")

    fields = [
        "nimi", "reg_kood", "aadress", "omavalitsus", "maakond",
        "telefon", "email", "veebileht", "direktor_email",
        "lat", "lon", "allikas", "markus",
    ]
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with JSON_OUT.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    email_rows = [r for r in rows if r["email"]]
    with EMAIL_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["nimi", "email", "omavalitsus", "aadress", "telefon"])
        w.writeheader()
        for r in email_rows:
            w.writerow({k: r[k] for k in w.fieldnames})

    print(f"Salvestatud: {CSV_OUT}")
    print(f"Salvestatud: {JSON_OUT}")
    print(f"Email-list ({len(email_rows)}): {EMAIL_CSV}")


if __name__ == "__main__":
    main()
