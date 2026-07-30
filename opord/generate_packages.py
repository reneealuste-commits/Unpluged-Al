#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build sidepakk ZIP archives from tiered PDFs."""
import shutil
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
SIDEPAKKID = BASE / "sidepakkid"
ZIP_SIDEPAKKID = BASE / "Operatsioon-Peegel-sidepakkid.zip"
ZIP_KOGU = BASE / "Operatsioon-Peegel-kogu-pakett.zip"

PACKAGES = {
    "P0-TUUM": {
        "pdfs": ["PEEGEL_TUUM.pdf", "TASKUKAARDID_RAHAKOTT.pdf"],
        "readme": "K0 TUUM \u2014 esimene kontakt. Anna see k\u00e4est-k\u00e4tte v\u00f5i QR-iga.\n",
    },
    "P1-TEE-A-KRIIS": {
        "pdfs": ["PEEGEL_TEE_A.pdf", "LOO_TASKUKAARDID_RAHAKOTT.pdf"],
        "readme": "Tee A \u2014 isa kriisis. Privaatne kanal, 1:1.\n",
    },
    "P1-TEE-B-SKEPTIK": {
        "pdfs": ["PEEGEL_TEE_B.pdf"],
        "readme": "Tee B \u2014 skeptik. Anna p\u00e4rast vestlust, mitte enne.\n",
    },
    "P1-TEE-C-PERE": {
        "pdfs": ["PEEGEL_TEE_C.pdf"],
        "readme": "Tee C \u2014 pere tugevdamine.\n",
    },
    "P1-TEE-D-DEMO": {
        "pdfs": [
            "PEEGEL_TEE_D.pdf",
            "SUHTE_HINDAMISE_TOOVIHIK_KATA_JA_LIIGU.pdf",
            "PEER_HINDAMINE_RAHAKOTT.pdf",
        ],
        "readme": "Tee D \u2014 demomees (Aluste_kool).\nS\u00f5jakooli deviis: EE \u00b7 S\u00f5naga m\u00f5\u00f5ga vastu \u2014 Verbo contra gladium.\nSuhte hindamise t\u00f6\u00f6vihik + peer taskukaart.\n",
    },
    "P1-TEE-E-RU": {
        "pdfs": ["PEEGEL_RU_KIHT0.pdf"],
        "readme": "Tee E \u2014 venekeelne kanal (eraldi Heli kanalist).\n",
    },
    "P1-TEE-F-JUHT": {
        "pdfs": ["PEEGEL_TEE_F.pdf"],
        "readme": "Tee F \u2014 juht / koolitus.\n",
    },
    "P2-TAIS": {
        "pdfs": ["OPERATSIOON_PEEGEL_OPORD.pdf"],
        "readme": "K2 \u2014 t\u00e4ielik OPORD. Anna ainult kui inimene k\u00fcsib (Lisa AJ).\n",
    },
    "P3-SPETSIALIST": {
        "pdfs": [],
        "readme": (
            "K3 \u2014 spetsialist. Lisa T, AL, AA, AF, AC, Y \u2014 ainult n\u00f5udmisel.\n"
            "Failid: lisad/lisa-t-valitsuse-ipb-analuus.md jne.\n"
        ),
    },
    "P4-RIIK-PEEGEL": {
        "pdfs": [
            "PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf",
            "PEEGEL_RIIK_PLANKETT.pdf",
            "PEER_HINDAMINE_RAHAKOTT.pdf",
            "PEER_HINDAMINE_SOP_PRINT.pdf",
            "SUHTE_HINDAMISE_TOOVIHIK_KATA_JA_LIIGU.pdf",
        ],
        "readme": (
            "Riiklik peegel \u2014 Lisa BD + BE.\n"
            "Kvartal (vorm) + iga paev (peer). Luurekusimus + uks tegu.\n"
        ),
    },
}

SKIP_IN_KOGU = {".git", "__pycache__", "sidepakkid", ".DS_Store"}
SKIP_SUFFIXES = {".zip"}


def build_sidepakkid() -> None:
    if SIDEPAKKID.exists():
        shutil.rmtree(SIDEPAKKID)
    SIDEPAKKID.mkdir()

    for pkg_name, cfg in PACKAGES.items():
        pkg_dir = SIDEPAKKID / pkg_name
        pkg_dir.mkdir()
        (pkg_dir / "README.txt").write_text(cfg["readme"], encoding="utf-8")
        for pdf_name in cfg["pdfs"]:
            src = BASE / pdf_name
            if src.exists():
                shutil.copy2(src, pkg_dir / pdf_name)
            else:
                print(f"  WARN missing PDF for {pkg_name}: {pdf_name}")

    with zipfile.ZipFile(ZIP_SIDEPAKKID, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SIDEPAKKID.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(BASE))
    print(f"Generated: {ZIP_SIDEPAKKID}")


def build_kogu_pakett() -> None:
    with zipfile.ZipFile(ZIP_KOGU, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(BASE.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(BASE)
            if rel.parts[0] in SKIP_IN_KOGU:
                continue
            if rel.suffix == ".pyc" or rel.suffix in SKIP_SUFFIXES:
                continue
            zf.write(path, rel)
    print(f"Generated: {ZIP_KOGU}")


if __name__ == "__main__":
    build_sidepakkid()
    build_kogu_pakett()
