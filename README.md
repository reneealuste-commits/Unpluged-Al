# Unpluged-Al

Strateegiline ja hariduslik dokumentatsioon — Operation Mirror, HY1, DP1.

## Paketid

| Kood | Sisu | Failid |
|------|------|--------|
| **HY1** | Hüpnoteraapia algajale (EMDR eeskuju vorming) | `hypnoteraapia-algaja-juhend.md` · `Hypnoteraapia-HY1.docx` |
| **TLP** | Perekonna ehitamine (5 etappi) | `plaankonspekt-tlp-ranger-perekonna-ehitamine.md` · `Plaankonspekt-TLP-Ranger-Perekonna-Ehitamine.docx` |
| **DP1** | Diplomaatia sõltlasega | `diplomaatia-soltlasega-*.md` · `Diplomaatia-DP1.docx` |
| **Raport** | Hüpnoteraapia + ohvriabi | `hupnoteraapia-teenused-ohvriabi-raport.md` |
| **MN×H2H** | Maleva Nõukogu × How2Human — juhtide ruum | `maleva-noukogu-how2human-plaankonspekt.md` · `how2human-elicitation-juhend.md` · `how2human-elicitation-koolituskaart.pdf` |

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

## MN×H2H — Maleva Nõukogu + How2Human

- [Plaankonspekt](maleva-noukogu-how2human-plaankonspekt.md)
- [Juhend H2H](how2human-elicitation-juhend.md)
- [Koolituskaart PDF](how2human-elicitation-koolituskaart.pdf)

```bash
python3 scripts/loo_how2human_koolituskaart.py
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
