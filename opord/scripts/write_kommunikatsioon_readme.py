#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "kommunikatsioon" / "README.md"
OUT.write_text(
    "# Kommunikatsioon \u2014 osalejate levitus\n\n"
    "| Fail | Kirjeldus |\n"
    "|------|----------|\n"
    "| `osalejate-emailid.csv` | K\u00f5ik teadaolevad e-postid (47 rida) |\n"
    "| `osalejate-kohandatud-kask.md` | 16 t\u00e4ielikku kohandatud k\u00e4sku |\n"
    "| `kirjad/kask-*.md` | \u00dcksikud e-kirja mustandid kopeerimiseks |\n"
    "| `vastus-heli-illipe-sootak.md` | Heli vastus |\n"
    "| `kandidaat-mihhail-usakov.md` | RU kanal |\n"
    "| `vastus-kuldne-taganemine.md` | Taganemise mall |\n\n"
    "**Reegel:** Isiklik e-kiri, mitte masspost (Lisa AJ, Lisa AQ).\n\n"
    "Uuenda: `python3 scripts/write_osalejate_kask.py`\n",
    encoding="utf-8",
)
print(f"Wrote {OUT}")
