# Unpluged-Al

Strateegiline ja hariduslik dokumentatsioon — Operation Mirror, HY1, DP1.

## Paketid

| Kood | Sisu | Failid |
|------|------|--------|
| **HY1** | Hüpnoteraapia algajale (EMDR eeskuju vorming) | `hypnoteraapia-algaja-juhend.md` · `Hypnoteraapia-HY1.docx` |
| **TLP** | Perekonna ehitamine (5 etappi) | `plaankonspekt-tlp-ranger-perekonna-ehitamine.md` · `Plaankonspekt-TLP-Ranger-Perekonna-Ehitamine.docx` |
| **DP1** | Diplomaatia sõltlasega | `diplomaatia-soltlasega-*.md` · `Diplomaatia-DP1.docx` |
| **Raport** | Hüpnoteraapia + ohvriabi | `hupnoteraapia-teenused-ohvriabi-raport.md` |
| **S7** | Sündikaat 7 — avasõna ja peatükid I–VI | [`sundikaat-7/Sundikaat7_raamat.md`](sundikaat-7/Sundikaat7_raamat.md) · [`sundikaat-7/Sundikaat7_raamat.docx`](sundikaat-7/Sundikaat7_raamat.docx) |

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

## S7 — Sündikaat 7

Renee Aluste raamat: avasõna ning peatükid I–VI (Kaitseliit, 1991/1995 KGB arhiivid ja OkupS arvud, 2023–2026 RKIK/Kaitseliidu hankeanalüüs, Protei Europa OÜ, Margus Vene lugu, Operatsioon Peegel / Õlessanded). Kaustas on ka avalike registrite ja kohtuallikate tugifailid.

- [Raamat (Markdown)](sundikaat-7/Sundikaat7_raamat.md)
- [Raamat (Word)](sundikaat-7/Sundikaat7_raamat.docx)
- [Kaitseliidu tõendid](sundikaat-7/kaitseliit_toendid.md)
- [Kaitsehangete analüüs 2023–2026](sundikaat-7/kaitsehanked_analuus.md)
- [KGB: dokumenteeritud faktid](sundikaat-7/kgb_dokumenteeritud.md)
- [KGB mõju kontroll (13.10.2026)](sundikaat-7/kgb_kontroll_2026-10-13.md)
- [Protei allikad](sundikaat-7/protei_allikad_2.md)
