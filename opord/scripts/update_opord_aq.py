#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch OPORD front page and appendix for Lisa AQ + tiered PDFs."""
from pathlib import Path

OPORD = Path(__file__).resolve().parents[1] / "OPERATSIOON_PEEGEL_OPORD.md"
text = OPORD.read_text(encoding="utf-8")

# Front page: add TUUM and sidepakkid links after PDF link line
old_pdf_line = (
    "**Allalaadimine (PDF):** [github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf]"
    "(https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf)  \n"
)
new_pdf_block = (
    "**Allalaadimine (PDF):** [github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf]"
    "(https://github.com/reneealuste-commits/Unpluged-Al/raw/cursor/opord-peegel-1a16/opord/OPERATSIOON_PEEGEL_OPORD.pdf)  \n"
    "**K0 TUUM (soovitatav esimene):** [PEEGEL_TUUM.pdf](PEEGEL_TUUM.pdf) \u00b7 [markdown](PEEGEL_TUUM.md)  \n"
    "**Sidepakkide ZIP:** [Operatsioon-Peegel-sidepakkid.zip](Operatsioon-Peegel-sidepakkid.zip) \u2014 P0\u2013P3 paketid (Lisa AQ)  \n"
)
if old_pdf_line in text and "PEEGEL_TUUM.pdf" not in text:
    text = text.replace(old_pdf_line, new_pdf_block)

# Update audit score on front page
text = text.replace(
    "Auditi skoor (2026-07-24): **6,9/10** \u2014 valmis piiratud levituseks demomeestele.",
    "Auditi skoor (2026-07-24): **7,8/10** \u2014 valmis piiratud levituseks (K0 TUUM + tee PDF-id). Skeem: **Lisa AQ**.",
)

# Add Lisa AQ to appendix table before kiht0-ru row
aq_row = (
    "| **AQ** | \u2014 | `lisad/lisa-aq-sidepakkide-jaotus-skeem.md` | "
    "**Sidepakkide jaotus** \u2014 K0\u2013K3 kihtide arhitektuur, paketid P0\u2013P3, kanalid, levitamise reeglid |\n"
)
if "**AQ**" not in text:
    text = text.replace(
        "| **AP** | \u2014 | `lisad/lisa-ap-swot-ja-lugeja-audit.md` | **SWOT ja lugeja-audit** \u2014 lugejale orienteeritud, teed A\u2013F, 10-punkti audit |\n",
        "| **AP** | \u2014 | `lisad/lisa-ap-swot-ja-lugeja-audit.md` | **SWOT ja lugeja-audit** \u2014 lugejale orienteeritud, teed A\u2013F, 10-punkti audit |\n"
        + aq_row,
    )

# Update lugejateed table with PDF column hint
old_tee_footer = "T\u00e4ielik SWOT ja lugeja-audit: **Lisa AP**. Auditi skoor"
if "| **A** | Isa kriisis | Pere kriis, kiire abi | Lisa **H**" in text:
    text = text.replace(
        "| Tee | Kellele | Alusta siit |\n|-----|---------|-------------|\n",
        "| Tee | Kellele | Alusta siit (PDF) |\n|-----|---------|------------------|\n",
    )
    replacements = [
        ("| **A** | Isa kriisis | Pere kriis, kiire abi | Lisa **H** \u2192 raamat **F** \u2192 Lisa **P** |",
         "| **A** | Isa kriisis | Pere kriis, kiire abi | `PEEGEL_TEE_A.pdf` |"),
        ("| **B** | Skeptik | Ei usu kohe, tahad fakte | See p\u00f5him\u00f5te \u2192 Lisa **R** \u2192 Lisa **T** |",
         "| **B** | Skeptik | Ei usu kohe, tahad fakte | `PEEGEL_TEE_B.pdf` |"),
        ("| **C** | Pere | Tugevdada kodu ja last | Raamat **A** \u2192 **D** \u2192 **E** \u2192 Lisa **M** |",
         "| **C** | Pere | Tugevdada kodu ja last | `PEEGEL_TEE_C.pdf` |"),
        ("| **D** | Demomees | SOK, eeskuju kogukonnas | Lisa **N** \u2192 **I** \u2192 **Q** |",
         "| **D** | Demomees | SOK, eeskuju kogukonnas | `PEEGEL_TEE_D.pdf` |"),
        ("| **E** | Venekeelne | RU kodanik Eestis | `kiht0-ru-tuum-1-leht.md` \u2192 Lisa **AN** |",
         "| **E** | Venekeelne | RU kodanik Eestis | `PEEGEL_RU_KIHT0.pdf` |"),
        ("| **F** | Juht / koolitus | KV, kool, organisatsioon | Lisa **I** \u2192 **P** \u2192 **L** |",
         "| **F** | Juht / koolitus | KV, kool, organisatsioon | `PEEGEL_TEE_F.pdf` |"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    if "Esimene kontakt alati:" not in text:
        text = text.replace(
            "T\u00e4ielik SWOT ja lugeja-audit: **Lisa AP**.",
            "Esimene kontakt alati: **`PEEGEL_TUUM.pdf`** (K0). T\u00e4ielik SWOT ja lugeja-audit: **Lisa AP**. Sidepakkide skeem: **Lisa AQ**.",
        )

OPORD.write_text(text, encoding="utf-8")
print(f"Updated {OPORD}")
