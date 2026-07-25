#!/usr/bin/env python3
"""Generate full OPORD + all lisad as a single .docx (Google Docs compatible)."""

import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "OPERATSIOON_PEEGEL_OPORD.md"
DOCX_FILE = BASE / "OPERATSIOON_PEEGEL_KOOS_LISADEGA.docx"
LISAD_DIR = BASE / "lisad"

LISA_FILES = [
    "raamat-01-unplugged-ava-silmad.md",
    "raamat-02-peegli-efekt.md",
    "raamat-03-vota-omaks.md",
    "raamat-04-tugev-isa.md",
    "raamat-05-pere-rindejoon.md",
    "raamat-06-murra-ring.md",
    "raamat-07-juhi-ja-voida.md",
    "lisa-h-kiirjuhend-kriisis-isale.md",
    "lisa-i-inimesekeskne-juhtimine.md",
    "lisa-j-haridusasutuste-juhtkonnad.md",
    "lisa-k-vorgustiku-skeem-ja-ulesanded.md",
    "lisa-l-ministeeriumid-ja-tai.md",
    "lisa-m-kodaniku-identiteet-ja-vanne.md",
    "lisa-n-aluste-kool.md",
    "lisa-o-vaktsineerimine.md",
    "lisa-p-takistused-ja-valideerimine.md",
    "lisa-q-side-eeskirjad-ja-suhtlus.md",
    "lisa-r-kes-ma-olen-ja-taust.md",
    "lisa-s-kiusamine-aju-ja-trauma.md",
    "lisa-t-valitsuse-ipb-analuus.md",
    "lisa-u-rasv-avatud-meele-uuring.md",
    "toitumine-uurimustoo.md",
    "lisa-v-uni-miks-me-magame.md",
    "lisa-w-montessori-beebi-austus-algusest.md",
    "lisa-x-taskukaardid-valjasuhtlus.md",
    "lisa-y-kanep-endokannabinoid-ja-ajalugu.md",
    "lisa-z-linnad-toostusuhiskond-ja-partnerlus.md",
    "lisa-aa-intiimsuse-atlas-keha-ja-ajalugu.md",
    "lisa-ab-paljajalu-ja-rippumine-linnas.md",
    "lisa-ac-magamistuba-voim-ja-revolutsioon.md",
    "lisa-ad-lood-konversiooni-checklist-ja-taskukaardid.md",
    "lisa-ae-ohk-liikumine-ja-kiitus.md",
    "lisa-af-meeste-erektsioon-ja-rela-hooldus.md",
    "lisa-ag-rollid-partnerlus-ja-nl-skeem.md",
    "lisa-ah-leelo-vahersalu-taust.md",
    "lisa-ai-epp-karsin-armastus-paabstab-maailma.md",
    "lisa-aj-levitamine-ja-kuldne-taganemistee.md",
    "lisa-ak-kodaniku-taskuraamat-peegel.md",
    "lisa-al-riiklik-levitamisplaan-shveits-mudel.md",
    "lisa-am-oigused-ja-realistlik-maht.md",
    "lisa-an-venekeelne-sihtruhm-ja-inimesekeskne-levitus.md",
    "lisa-ao-ultimate-power-kokkuvote.md",
    "lisa-ap-swot-ja-lugeja-audit.md",
    "lisa-aq-sidepakkide-jaotus-skeem.md",
    "lisa-ar-vooglaid-ja-paal-demonstraatorid.md",
    "lisa-at-lihtsus-kui-kinni-jaid.md",
    "lisa-au-vastase-analuusi-taiendus.md",
    "lisa-av-peegel-hindamisvorm.md",
    "lisa-aw-motlemine-kiiresti-ja-aeglaselt.md",
    "lisa-ax-demo-perekond-ja-eeskujud.md",
    "lisa-ay-kuldne-sild-valitsus-ja-esimene-manover.md",
    "lisa-az-suur-pilt-kardashev-musk-ja-susteem.md",
    "lisa-ba-keha-vabastamine-tasuta.md",
    "lisa-bb-hannes-vorno-haridus-ja-toitumine.md",
    "lisa-bc-digitaalne-detoks-ja-nuputelefon.md",
    "lisa-bd-nvc-taskukaardid-kodanikule.md",
    "lisa-be-1-1-vestlus-vorgustikus.md",
    "renee-aluste-profiil.md",
]


def build_combined_markdown() -> str:
    parts = [
        "---\n",
        "title: \"Operatsioon Peegel - OPORD koos koigi lisadega\"\n",
        "author: Renee Aluste\n",
        "lang: et-EE\n",
        "---\n\n",
    ]
    parts.append(MD_FILE.read_text(encoding="utf-8"))
    parts.append("\n\n\\newpage\n\n# LISAD\n\n")

    for name in LISA_FILES:
        path = LISAD_DIR / name
        if not path.exists():
            print(f"Warning: missing {path}", file=sys.stderr)
            continue
        parts.append(f"\n\n\\newpage\n\n")
        parts.append(path.read_text(encoding="utf-8"))

    return "".join(parts)


def main() -> None:
    combined = build_combined_markdown()
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(combined)
        tmp_path = tmp.name

    cmd = [
        "pandoc",
        tmp_path,
        "-o",
        str(DOCX_FILE),
        "--from=markdown",
        "--to=docx",
        "--toc",
        "--toc-depth=3",
        "--metadata",
        "title=Operatsioon Peegel - OPORD koos lisadega",
    ]
    subprocess.run(cmd, check=True)
    Path(tmp_path).unlink(missing_ok=True)
    size_mb = DOCX_FILE.stat().st_size / (1024 * 1024)
    print(f"Generated: {DOCX_FILE} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
