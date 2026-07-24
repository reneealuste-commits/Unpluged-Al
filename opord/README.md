# Operatsioon „Peegel" — OPORD

Eesti keeles koostatud viiepunktiline **paranemis-teekond** (OPORD-formaat) vastutegevuseks psühholoogilisele mõjutamisele.

> *Paranemine algab sellel hetkel, kui sa mõistad, et sa pole katki olnudki.*

> *Kohtleme kõiki asjaosalisi nagu terveid, täiesti normaalseid inimesi.*

> *Kui inimesel on roll, eesmärk ja konkreetsed juhised — ta tihti teebki seda.*

## Allalaadimine

| Formaat | Link |
|---------|------|
| **ZIP — kogu pakett** (kõik lisad + PDF-id + pildid) | [Laadi alla Operatsioon-Peegel-kogu-pakett.zip](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/Operatsioon-Peegel-kogu-pakett.zip) |
| **PDF** (soovitatav) | [Laadi alla OPERATSIOON_PEEGEL_OPORD.pdf](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf) |
| **Toidu uurimustöö (PDF)** | [Laadi alla TOITUMINE_UURIMUSTOO.pdf](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/TOITUMINE_UURIMUSTOO.pdf) |
| **Markdown** | [OPERATSIOON_PEEGEL_OPORD.md](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.md) |
| **Pull request** | [PR #1](https://github.com/reneealuste-commits/Unpluged-Al/pull/1) |

### ZIP-paketi sisu (81 faili)

- `OPERATSIOON_PEEGEL_OPORD.md` + `.pdf` (kõik lisad PDF-is)
- `TOITUMINE_UURIMUSTOO.pdf` + `lisad/toitumine-uurimustoo.md`
- **Lisa A–G** — Tugeva Isa seeria (7 köidet)
- **Lisa H–W** — kõik lisad (kiirjuhend, juhtimine, võrgustik, Montessori beebi, uni jne)
- `images/` — profiilipildid ja koolide fotod
- `generate_pdf.py`, `generate_toidu_pdf.py`

## Failid

| Fail | Kirjeldus |
|------|-----------|
| `OPERATSIOON_PEEGEL_OPORD.md` | Täielik OPORD lähtetekst (Google Docs'i kopeerimiseks) |
| `OPERATSIOON_PEEGEL_OPORD.pdf` | Valmis PDF-vormingus dokument |
| `generate_pdf.py` | PDF genereerimise skript |

## PDF uuendamine

```bash
cd opord
python3 generate_pdf.py
python3 generate_toidu_pdf.py   # Lisa T — toidu uurimustöö
```

## Struktuur

Dokument järgib Maakaitse käsiraamatu viiepunktilist OPORD-formaati:

1. Olukord
2. Põhiülesanne
3. Täideviimine
4. Lahinguteenindus
5. Juhtimine ja side

Eelnevalt: ülesande koosseis (osalajate profiilid), tegutsemisala piirid, info-keskkonna kirjeldus.

Lõpus: küsimused ja vastused (44 tagasiküsimust) + Lisa A–G: Tugeva Isa seeria (7 köidet).
