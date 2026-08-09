#!/usr/bin/env python3
"""Generate Maria puhastusplaan (Lisa BD) as Word .docx."""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
LISAD = BASE.parent / "lisad"
MD_FILE = LISAD / "lisa-bd-maria-puhastusplaan-co-parenting.md"
DOCX_FILE = BASE / "Maria-puhastusplaan.docx"


def main() -> None:
    if not MD_FILE.exists():
        print(f"Missing source: {MD_FILE}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        "pandoc",
        str(MD_FILE),
        "-o",
        str(DOCX_FILE),
        "--from=markdown",
        "--to=docx",
        "--metadata",
        "title=Maria puhastusplaan - co-parenting Clean-Up (Lisa BD)",
        "--metadata",
        "author=Renee Aluste",
        "--metadata",
        "lang=et-EE",
    ]
    subprocess.run(cmd, check=True)
    size_kb = DOCX_FILE.stat().st_size / 1024
    print(f"Generated: {DOCX_FILE} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
