#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch OPORD, Lisa K, Lisa Q for Vooglaid and Paal."""
from pathlib import Path

OPORD = Path(__file__).resolve().parents[1] / "OPERATSIOON_PEEGEL_OPORD.md"
LISA_K = Path(__file__).resolve().parents[1] / "lisad" / "lisa-k-vorgustiku-skeem-ja-ulesanded.md"
LISA_Q = Path(__file__).resolve().parents[1] / "lisad" / "lisa-q-side-eeskirjad-ja-suhtlus.md"

vooglaid_block = (
    "\n#### V\u00f5tmetegijad \u2014 demonstraatorid (kodaniku m\u00f5te)\n\n"
    "##### \u00dclo Vooglaid \u2014 Kodaniku-m\u00f5tleja eeskuju\n\n"
    "- **Roll operatsioonis:** V\u00f5tmetegija-demonstraator; filosoofiline tuum *elanikust kodanikuks*.\n"
    "- **Taust:** Emeriitprofessor, sotsiaalteadlane (s\u00fcnd 1935). Sihtasutus \u00dclo Vooglaiu m\u00f5ttep\u00e4rand.\n"
    "- **Peamised raamatud:** **Elanikust kodanikuks** (2019); *Aeg & Vaim*; *S\u00f5na on J\u00f5ud*; *Vanaisa uued lood* (2025).\n"
    "- **Kontakt:** ylo@vooglaid.org \u00b7 sihtasutus@vooglaid.org\n"
    "- **Miks ta on siin:** \u00d5petab seda, mida Peegel \u00fctleb: **\u00e4ra ole tarbija \u2014 ole kodanik**. Tee B, Lisa M.\n"
    "- **T\u00e4ielik profiil:** **Lisa AR**\n\n"
    "##### Indrek Paal \u2014 Praktiline demonstraator\n\n"
    "- **Roll operatsioonis:** M\u00f5ttep\u00e4randa praktiline levitaja ja kirjastaja.\n"
    "- **Taust:** Vana-Viru Kaubaveod O\u00dc; \u00dclo Vooglaiu Kirjastus; sihtasutuse juhatuse liige.\n"
    "- **Kontakt:** Vana-L\u00f5una 39/1, Tallinn \u00b7 tel 667 0111 \u00b7 sihtasutus@vooglaid.org\n"
    "- **Miks ta on siin:** Kannab Vooglaidi tuuma tr\u00fckis ja igap\u00e4evat\u00f6\u00f6s. **Lisa AR**\n\n"
)

lisa_k_block = (
    "\n### 4.15 V\u00f5tmetegijad \u2014 demonstraatorid\n\n"
    "#### \u00dclo Vooglaid\n"
    "- **Roll:** Kodaniku-m\u00f5tleja eeskuju\n"
    "- **\u00dclesanne:** Soovita *Elanikust kodanikuks* (tee B)\n"
    "- **Kontakt:** ylo@vooglaid.org\n\n"
    "#### Indrek Paal\n"
    "- **Roll:** M\u00f5ttep\u00e4randa levitaja\n"
    "- **\u00dclesanne:** *Vanaisa uued lood*; sidumine Vooglaidi n\u00f5usolekul\n"
    "- **Kontakt:** sihtasutus@vooglaid.org\n\n"
    "*Lisa AR*\n\n"
)

lisa_q_addition = (
    "\n### Demonstraatorite kanalid (laiendus)\n\n"
    "| Kanal | Demonstraatorid | P\u00f5him\u00f5te |\n"
    "|-------|-----------------|----------|\n"
    "| SOK / Aluste_kool | Demomehed (Lisa N) | Checklist, GOTWA |\n"
    "| Kodaniku m\u00f5te | Vooglaid, Paal (Lisa AR) | Raamat, vestlus \u2014 mitte sp\u00e4mm |\n\n"
)

opord = OPORD.read_text(encoding="utf-8")
if "\u00dclo Vooglaid \u2014 Kodaniku" not in opord:
    anchor = "- **T\u00e4ielik \u00fclesanne:** **Lisa N** \u2014 `lisa-n-aluste-kool.md`\n\n#### Martin J\u00f5esaar"
    opord = opord.replace(
        anchor,
        "- **T\u00e4ielik \u00fclesanne:** **Lisa N** \u2014 `lisa-n-aluste-kool.md`\n" + vooglaid_block + "#### Martin J\u00f5esaar",
    )

if "| Kodaniku m\u00f5te | \u00dclo Vooglaid" not in opord:
    opord = opord.replace(
        "| Demomehed (SOK) | \u00dcksus Aluste_kool | Lisa N + **Lisa Q** (viisakus, GOTWA, h\u00e4\u00e4l) |",
        "| Demomehed (SOK) | \u00dcksus Aluste_kool | Lisa N + **Lisa Q** (viisakus, GOTWA, h\u00e4\u00e4l) |\n"
        "| Kodaniku m\u00f5te | \u00dclo Vooglaid | ylo@vooglaid.org (Lisa AR) |\n"
        "| M\u00f5ttep\u00e4rand | Indrek Paal | sihtasutus@vooglaid.org (Lisa AR) |",
    )

if "**AR**" not in opord:
    opord = opord.replace(
        "| **AQ** | \u2014 | `lisad/lisa-aq-sidepakkide-jaotus-skeem.md` |",
        "| **AR** | \u2014 | `lisad/lisa-ar-vooglaid-ja-paal-demonstraatorid.md` | "
        "**Vooglaid ja Paal** \u2014 demonstraatorid, kodaniku m\u00f5te |\n"
        "| **AQ** | \u2014 | `lisad/lisa-aq-sidepakkide-jaotus-skeem.md` |",
    )

OPORD.write_text(opord, encoding="utf-8")
print(f"Updated {OPORD}")

lisa_k = LISA_K.read_text(encoding="utf-8")
if "### 4.15 V\u00f5tmetegijad" not in lisa_k:
    lisa_k = lisa_k.replace("### 4.8 Haridustase (kokkuv\u00f5te \u2014 vt Lisa J)", lisa_k_block + "### 4.8 Haridustase (kokkuv\u00f5te \u2014 vt Lisa J)")
LISA_K.write_text(lisa_k, encoding="utf-8")
print(f"Updated {LISA_K}")

lisa_q = LISA_Q.read_text(encoding="utf-8")
if "Demonstraatorite kanalid (laiendus)" not in lisa_q:
    lisa_q = lisa_q.replace(
        "**Tagasiside:** kord kuus \u2014 mis re\u017eiim aitas? mis mitte? (Renee / SOK ring)",
        "**Tagasiside:** kord kuus \u2014 mis re\u017eiim aitas? mis mitte? (Renee / SOK ring)" + lisa_q_addition,
    )
LISA_Q.write_text(lisa_q, encoding="utf-8")
print(f"Updated {LISA_Q}")
