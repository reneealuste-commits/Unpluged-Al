# Operatsioon „Peegel" — OPORD

Eesti keeles koostatud viiepunktiline **paranemis-teekond** (OPORD-formaat) vastutegevuseks psühholoogilisele mõjutamisele.

> *Paranemine algab sellel hetkel, kui sa mõistad, et sa pole katki olnudki.*

> *Kohtleme kõiki asjaosalisi nagu terveid, täiesti normaalseid inimesi.*

> *Kui inimesel on roll, eesmärk ja konkreetsed juhised — ta tihti teebki seda.*

## Allalaadimine

| Formaat | Link |
|---------|------|
| **PDF** (soovitatav) | [Laadi alla OPERATSIOON_PEEGEL_OPORD.pdf](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf) |
| **Markdown** | [OPERATSIOON_PEEGEL_OPORD.md](https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.md) |
| **Pull request** | [PR #1](https://github.com/reneealuste-commits/Unpluged-Al/pull/1) |

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
