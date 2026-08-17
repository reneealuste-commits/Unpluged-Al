# Unpluged-Al

Strateegiline ja hariduslik dokumentatsioon — Operation Mirror, HY1, DP1, LVJ.

## Paketid

| Kood | Sisu | Failid |
|------|------|--------|
| **LVJ** | Lahinguvaljal Juhtimine (Renee Aluste, Combat Ready) | `lahinguvaljal-juhtimine.pdf` · `lahinguvaljal-juhtimine-juhend.md` |
| **HY1** | Hüpnoteraapia algajale (EMDR eeskuju vorming) | `hypnoteraapia-algaja-juhend.md` · `Hypnoteraapia-HY1.docx` |
| **TLP** | Perekonna ehitamine (5 etappi) | `plaankonspekt-tlp-ranger-perekonna-ehitamine.md` · `Plaankonspekt-TLP-Ranger-Perekonna-Ehitamine.docx` |
| **DP1** | Diplomaatia sõltlasega | `diplomaatia-soltlasega-*.md` · `Diplomaatia-DP1.docx` |
| **Raport** | Hüpnoteraapia + ohvriabi | `hupnoteraapia-teenused-ohvriabi-raport.md` |

## LVJ — lahinguvaljal juhtimine

- [Raamat PDF](lahinguvaljal-juhtimine.pdf) — 98 lk, Renee Aluste, 2026
- [Õppejuhend](lahinguvaljal-juhtimine-juhend.md)
- [Koolituskaart](lahinguvaljal-juhtimine-koolituskaart.md) · [PDF](lahinguvaljal-juhtimine-koolituskaart.pdf)
- [30-päevane plaan](lahinguvaljal-juhtimine-30paeva-plaan.md)

### LVJ v2 — TBKTS-struktuur (mustand)

- [Struktuurianalüüs: Body Keeps the Score](lahinguvaljal-juhtimine-v2-struktuurianalyys.md)
- [Isiklike lugude kaart](lahinguvaljal-juhtimine-v2-isiklike-loodude-kaart.md) — päris lood → peatükid
- [Peatükk 16 — Ema](lahinguvaljal-juhtimine-v2-peatykk16-ema.md)
- [Peatükk 17 — Andestus (Foxhole)](lahinguvaljal-juhtimine-v2-peatykk17-andestus.md)
- [Peatükk 18 — silmaliigutused](lahinguvaljal-juhtimine-v2-peatykk18-silmaliigutused.md)
- [Conversiooni lood — 5 vaatlust](lahinguvaljal-juhtimine-v2-conversiooni-lood.md)
- [Komposiitlood (varu)](lahinguvaljal-juhtimine-v2-komposiitlood-mustand.md)

```bash
python3 scripts/loo_lahinguvaljal_koolituskaart.py
```

## DP1 — kiirlinkid

- [Juhend](diplomaatia-soltlasega-juhend.md)
- [Koolituskaart PDF](diplomaatia-soltlasega-koolituskaart.pdf)
- [Word (kõik)](https://github.com/reneealuste-commits/Unpluged-Al/raw/main/Diplomaatia-DP1.docx)
- [Demo koordinaator](scripts/dp1_demo_koordinaator.py)

```bash
python3 scripts/dp1_demo_koordinaator.py --list
python3 scripts/dp1_demo_koordinaator.py --demo DP1-D01 --check
python3 scripts/loo_diplomaatia_docx.py
python3 scripts/loo_diplomaatia_koolituskaart.py
```

## TLP — perekonna ehitamine

- [Plaankonspekt](plaankonspekt-tlp-ranger-perekonna-ehitamine.md)
- [Word](https://github.com/reneealuste-commits/Unpluged-Al/raw/main/Plaankonspekt-TLP-Ranger-Perekonna-Ehitamine.docx)

```bash
python3 scripts/loo_plaankonspekt_tlp_ranger.py
```

## HY1 — kiirlinkid

- [Test nr 1 kaaslasega](hypnoteraapia-test-nr1-kaaslasega.md) — Automaadi test vorming
- [Test nr 1 PDF](hypnoteraapia-test-nr1-kaaslasega.pdf)
- [Word HY1](https://github.com/reneealuste-commits/Unpluged-Al/raw/main/Hypnoteraapia-HY1.docx)

```bash
python3 scripts/loo_hypnoteraapia_test_nr1.py
python3 scripts/loo_hypnoteraapia_docx.py
python3 scripts/loo_hypnoteraapia_koolituskaart.py
```
