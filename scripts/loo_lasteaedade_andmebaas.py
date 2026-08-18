#!/usr/bin/env python3
"""Ehita Eesti lasteaedade andmebaas — OSM + teatmik.haridus.ee telefonid."""

import csv
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CSV_OUT = DATA_DIR / "lasteaedade-andmebaas.csv"
JSON_OUT = DATA_DIR / "lasteaedade-andmebaas.json"
KONTAKT_CSV = DATA_DIR / "lasteaedade-kontakt-list.csv"

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
UA = "Unpluged-Al/1.0 (lasteaedade-andmebaas; contact: reneealuste@gmail.com)"
TEATMIK_UA = {"User-Agent": "Mozilla/5.0 (compatible; Unpluged-Al/1.0)"}
GENERIC_PHONES = {"3726404590", "6404590"}


def is_generic_phone(p):
    return re.sub(r"\D", "", p or "") in GENERIC_PHONES

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

FIELDS = [
    "nimi", "reg_kood", "aadress", "omavalitsus", "maakond",
    "telefon", "direktor_telefon", "email", "direktor_email",
    "veebileht", "lat", "lon", "allikas", "markus",
]


def fetch_osm():
    cache = Path("/tmp/osm_kg.json")
    if cache.exists():
        return json.loads(cache.read_text()).get("elements", [])
    r = requests.post(
        OVERPASS_URL, data={"data": QUERY}, headers={"User-Agent": UA}, timeout=120,
    )
    r.raise_for_status()
    data = r.json()
    cache.write_text(json.dumps(data))
    return data.get("elements", [])


def norm_name(name):
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def norm_phone(p):
    if not p:
        return ""
    p = re.sub(r"\s+", " ", p.strip())
    digits = re.sub(r"\D", "", p)
    if digits.startswith("372"):
        return "+" + digits
    if len(digits) in (7, 8):
        return "+372" + digits[-7:]
    return p


def pick_main_phone(phones):
    cleaned = [norm_phone(p) for p in phones if p]
    specific = [
        p for p in cleaned
        if re.sub(r"\D", "", p) not in GENERIC_PHONES
    ]
    return specific[0] if specific else (cleaned[0] if cleaned else "")


def decode_cfemail(h):
    r = int(h[:2], 16)
    return "".join(chr(int(h[i:i + 2], 16) ^ r) for i in range(2, len(h), 2))


def scrape_teatmik_id(id_):
    url = f"https://teatmik.haridus.ee/kindergartens/{id_}/"
    try:
        r = requests.get(url, headers=TEATMIK_UA, timeout=12)
        html = r.text
        if r.status_code != 200 or "Register code" not in html:
            return None
        name_m = re.search(r"<h2>([^<]+)</h2>", html)
        reg_m = re.search(
            r"Register code</span>\s*<span class=\"value\">(\d+)</span>", html,
        )
        if not name_m or not reg_m:
            return None
        name = name_m.group(1).strip()
        if "lasteaed" not in name.lower() and "lastehoid" not in name.lower():
            return None
        phones = re.findall(r'href="tel:([^"]+)"', html)
        emails = list(dict.fromkeys(
            decode_cfemail(x) for x in re.findall(r'data-cfemail="([0-9a-f]+)"', html)
        ))
        main = pick_main_phone(phones)
        direktor_tel = ""
        for row in re.findall(r"<tr>.*?</tr>", html, re.S):
            if "direktor" in row.lower():
                t = re.search(r'href="tel:([^"]+)"', row)
                if t:
                    direktor_tel = norm_phone(t.group(1))
                    break
        inst_email = next(
            (e for e in emails if e.endswith(".edu.ee") and "haridusamet" not in e and "tallinnlv" not in e),
            "",
        )
        direktor_email = next((e for e in emails if "direktor" in e.lower()), "")
        web_m = re.search(r"Homepage</span>.*?href=\"([^\"]+)\"", html, re.S)
        addr_m = re.search(
            r"Address</span>.*?class=\"value site-link\">\s*([^<]+)", html, re.S,
        )
        return {
            "nimi": name,
            "reg_kood": reg_m.group(1),
            "aadress": addr_m.group(1).strip() if addr_m else "",
            "omavalitsus": "Tallinn",
            "maakond": "Harjumaa",
            "telefon": main,
            "direktor_telefon": direktor_tel,
            "email": inst_email.lower(),
            "direktor_email": direktor_email.lower(),
            "veebileht": web_m.group(1) if web_m else "",
            "lat": "",
            "lon": "",
            "allikas": "teatmik.haridus.ee",
            "markus": f"teatmik_id={id_}",
        }
    except Exception:
        return None


def fetch_teatmik(max_id=500, workers=25):
    print(f"Laen teatmik.haridus.ee andmeid (ID 1–{max_id})...")
    results = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(scrape_teatmik_id, i) for i in range(1, max_id + 1)]
        for fut in as_completed(futs):
            row = fut.result()
            if row:
                results.append(row)
    print(f"Teatmikust: {len(results)} lasteaeda (telefoniga: {sum(1 for r in results if r['telefon'])})")
    return results


def parse_osm_element(el):
    tags = el.get("tags", {})
    name = tags.get("name") or tags.get("official_name") or ""
    if not name:
        return None
    email = (tags.get("email") or tags.get("contact:email") or "").lower()
    phone = norm_phone(tags.get("phone") or tags.get("contact:phone") or "")
    return {
        "nimi": name.strip(),
        "reg_kood": tags.get("ref:EHIS") or tags.get("ref") or "",
        "aadress": ", ".join(p for p in [
            tags.get("addr:street"), tags.get("addr:housenumber"),
            tags.get("addr:city") or tags.get("addr:place"),
        ] if p),
        "omavalitsus": tags.get("addr:city") or tags.get("addr:place") or "",
        "maakond": tags.get("addr:state") or "",
        "telefon": phone,
        "direktor_telefon": "",
        "email": email,
        "direktor_email": "",
        "veebileht": tags.get("website") or tags.get("contact:website") or "",
        "lat": el.get("lat") or (el.get("center") or {}).get("lat") or "",
        "lon": el.get("lon") or (el.get("center") or {}).get("lon") or "",
        "allikas": "OpenStreetMap",
        "markus": "",
    }


def merge_rows(osm_rows, teatmik_rows):
    by_reg = {r["reg_kood"]: r for r in teatmik_rows if r["reg_kood"]}
    by_name = {norm_name(r["nimi"]): r for r in teatmik_rows}

    merged = []
    used_teatmik = set()

    for row in osm_rows:
        t = None
        if row["reg_kood"] and row["reg_kood"] in by_reg:
            t = by_reg[row["reg_kood"]]
        elif norm_name(row["nimi"]) in by_name:
            t = by_name[norm_name(row["nimi"])]

        if t:
            used_teatmik.add(t["reg_kood"] or norm_name(t["nimi"]))
            for f in ("reg_kood", "telefon", "direktor_telefon", "email", "direktor_email", "veebileht", "aadress"):
                if t.get(f):
                    row[f] = t[f]
            if t["telefon"]:
                row["allikas"] = "OpenStreetMap + teatmik.haridus.ee"
            if t.get("markus"):
                row["markus"] = t["markus"]
        merged.append(row)

    osm_names = {norm_name(r["nimi"]) for r in osm_rows}
    for t in teatmik_rows:
        key = t["reg_kood"] or norm_name(t["nimi"])
        if key in used_teatmik or norm_name(t["nimi"]) in osm_names:
            continue
        merged.append(t)

    # dedupe by name
    seen = {}
    for row in merged:
        key = norm_name(row["nimi"])
        if key not in seen:
            seen[key] = row
        else:
            old = seen[key]
            for f in FIELDS:
                if f in ("lat", "lon", "allikas", "markus"):
                    continue
                if not old.get(f) and row.get(f):
                    old[f] = row[f]
            if "teatmik" in row.get("allikas", ""):
                old["allikas"] = row["allikas"]
    return list(seen.values())


def clean_phones(rows):
    """Eemalda üldine Tallinna haridusameti number; eelista direktori numbrit."""
    for row in rows:
        if is_generic_phone(row.get("telefon")):
            if row.get("direktor_telefon") and not is_generic_phone(row["direktor_telefon"]):
                row["telefon"] = row["direktor_telefon"]
            else:
                row["telefon"] = ""
    return rows


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Laen OpenStreetMap andmeid...")
    osm_rows = [r for el in fetch_osm() if (r := parse_osm_element(el))]
    teatmik_rows = fetch_teatmik()
    rows = merge_rows(osm_rows, teatmik_rows)
    rows = clean_phones(rows)
    rows.sort(key=lambda x: (x["omavalitsus"], x["nimi"]))

    print(f"\nKokku: {len(rows)} lasteaeda")
    print(f"Telefoniga: {sum(1 for r in rows if r['telefon'])}")
    print(f"Direktori telefoniga: {sum(1 for r in rows if r['direktor_telefon'])}")
    print(f"Emailiga: {sum(1 for r in rows if r['email'])}")
    print(f"Telefon VÕI email: {sum(1 for r in rows if r['telefon'] or r['email'])}")

    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    with JSON_OUT.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    kontakt_fields = [
        "nimi", "telefon", "direktor_telefon", "email", "direktor_email",
        "omavalitsus", "aadress", "reg_kood", "veebileht",
    ]
    kontakt_rows = [r for r in rows if r["telefon"] or r["email"]]
    kontakt_rows.sort(key=lambda x: x["omavalitsus"])

    with KONTAKT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kontakt_fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(kontakt_rows)

    print(f"\nSalvestatud: {CSV_OUT}")
    print(f"Salvestatud: {JSON_OUT}")
    print(f"Kontakt-list ({len(kontakt_rows)}): {KONTAKT_CSV}")


if __name__ == "__main__":
    main()
