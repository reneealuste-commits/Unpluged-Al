# Operatsioon „Peegel" — OPORD

Eesti keeles koostatud viiepunktiline lahingukäsk (OPORD) vastutegevuseks Vene psühholoogilisele mõjutamisele.

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

Lõpus: küsimused ja vastused — kodanikud, poliitikud, usuringkonnad, meedia (rollimäng).
