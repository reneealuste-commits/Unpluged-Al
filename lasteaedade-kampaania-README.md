# Lasteaedade kampaania — Roheline vaikuse uuring

Tasuta uuring lasteaedade direktoritele: 5–10 minutine rahulik hetk ühe lapsega.

## Failid

| Fail | Kirjeldus |
|------|-----------|
| `roheline-vaikuse-uuring-lasteaedadele.pdf` | **Saada lasteaedadele** — lihtne uuring (nagu 5-aastasele) |
| `lasteaedade-email-mustand.md` | E-kirja tekst direktoritele |
| `data/lasteaedade-andmebaas.csv` | ~656 lasteaeda (OSM + teatmik) |
| `data/lasteaedade-kontakt-list.csv` | **185 lasteaeda telefoniga ja/või emailiga** |
| `data/lasteaedade-andmebaas.json` | Sama andmebaas JSON-is |
| `scripts/loo_lasteaedade_andmebaas.py` | Andmebaasi uuendamine |
| `scripts/loo_roheline_vaikuse_uuring.py` | PDF genereerimine |

## Kiirstart

```bash
# Uuenda andmebaasi (OpenStreetMap)
python3 scripts/loo_lasteaedade_andmebaas.py

# Genereeri PDF uuesti
python3 scripts/loo_roheline_vaikuse_uuring.py
```

## Kuidas saata

1. Täida `[TÄIDA]` väljad email-mustandis ja PDF-is
2. Alusta **5–10 lasteaiaga** (pilot)
3. Manusta PDF
4. Kasuta `data/lasteaedade-email-list.csv` mass-saatmiseks

## Andmeallikad

- **OpenStreetMap** — ~648 lasteaeda, 151 email (praegu)
- **EHIS** (enda.ehis.ee/avaandmed) — rikkalikum, API hetkel ebastabiilne
- **teatmik.haridus.ee** — direktorite emailid (Tallinn jt), vajab käsitsi/scraping

## Sisu

Uuring põhineb ühe lapse kogemusel — lihtne rahustav hetk:
- Roheline kaart = vaikne hetk
- Hingamine, keha, turvaline koht
- Kerge koputus (EMDR-stiilis rütm, mitte ravi)
- 5–10 min ühe lapsega lasteaias

**Ei ole** arstiabi ega EMDR-ravi.
