# Operatsioon „Peegel“ — OPORD

Eesti keeles koostatud viiepunktiline **paranemis-teekond** (OPORD-formaat) vastutegevuseks psühholoogilisele mõjutamisele.

> *Paranemine algab sellel hetkel, kui sa mõistad, et sa pole katki olnudki.*

> *Kohtleme kõiki asjaosalisi nagu terveid, täiesti normaalseid inimesi.*

> *Kui inimesel on roll, eesmärk ja konkreetsed juhised — ta tihti teebki seda.*

## Allalaadimine

### Esimene kontakt (K0 — soovitatav)

| Formaat | Link |
|---------|------|
| **PEEGEL TUUM (PDF)** | [PEEGEL_TUUM.pdf](PEEGEL_TUUM.pdf) |
| **PEEGEL TUUM (Markdown)** | [PEEGEL_TUUM.md](PEEGEL_TUUM.md) |
| **Sidepakkide ZIP** | [Operatsioon-Peegel-sidepakkid.zip](Operatsioon-Peegel-sidepakkid.zip) |

### Lugejateed (K1)

| Tee | PDF |
|-----|-----|
| A — Isa kriisis | [PEEGEL_TEE_A.pdf](PEEGEL_TEE_A.pdf) |
| B — Skeptik | [PEEGEL_TEE_B.pdf](PEEGEL_TEE_B.pdf) |
| C — Pere | [PEEGEL_TEE_C.pdf](PEEGEL_TEE_C.pdf) |
| D — Demomees | [PEEGEL_TEE_D.pdf](PEEGEL_TEE_D.pdf) |
| E — Venekeelne | [PEEGEL_RU_KIHT0.pdf](PEEGEL_RU_KIHT0.pdf) |
| F — Juht | [PEEGEL_TEE_F.pdf](PEEGEL_TEE_F.pdf) |

Skeem: [Lisa AQ](lisad/lisa-aq-sidepakkide-jaotus-skeem.md)

### Täielik pakett (K2)

| Formaat | Link |
|---------|------|
| **DOCX** | [OPERATSIOON_PEEGEL_KOOS_LISADEGA.docx](OPERATSIOON_PEEGEL_KOOS_LISADEGA.docx) |
| **ZIP — kogu pakett** | [Operatsioon-Peegel-kogu-pakett.zip](Operatsioon-Peegel-kogu-pakett.zip) |
| **PDF (täielik OPORD)** | [OPERATSIOON_PEEGEL_OPORD.pdf](OPERATSIOON_PEEGEL_OPORD.pdf) |
| **Markdown** | [OPERATSIOON_PEEGEL_OPORD.md](OPERATSIOON_PEEGEL_OPORD.md) |
| **Pull request** | [PR #1](https://github.com/reneealuste-commits/Unpluged-Al/pull/1) |

### Prinditavad tööriistad

| Tööriist | Link |
|----------|------|
| Taskukaardid | [TASKUKAARDID_PRINT.pdf](TASKUKAARDID_PRINT.pdf) · [rahakott](TASKUKAARDID_RAHAKOTT.pdf) |
| Lendleht | [LENDLEHT_PRINT.pdf](LENDLEHT_PRINT.pdf) |
| Toidu uurimustöö | [TOITUMINE_UURIMUSTOO.pdf](TOITUMINE_UURIMUSTOO.pdf) |

## PDF uuendamine

```bash
cd opord
python3 generate_pdf.py          # K0, teed A–F + täielik OPORD
python3 generate_packages.py     # sidepakkide ZIP
python3 generate_toidu_pdf.py
python3 generate_taskukaardid_pdf.py
```

## Kihtide arhitektuur (Lisa AQ)

| Kiht | Mis see on |
|------|------------|
| **K0** | PEEGEL_TUUM — esimene kontakt |
| **K1** | Tee PDF-id A–F |
| **K2** | Täielik OPERATSIOON_PEEGEL_OPORD.pdf |
| **K3** | Spetsialist (Lisa T, AL, AA jne) — nõudmisel |

Auditi skoor: **7,8/10** (Lisa AP). Valmis piiratud levituseks demomeestele.

## Struktuur

Dokument järgib Maakaitse käsiraamatu viiepunktilist OPORD-formaati:

1. Olukord
2. Põhiülesanne
3. Täideviimine
4. Lahinguteenindus
5. Juhtimine ja side

Lisa A–AQ: Tugeva Isa seeria, lisad, SWOT, sidepakkide skeem.
