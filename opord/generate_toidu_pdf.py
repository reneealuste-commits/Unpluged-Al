#!/usr/bin/env python3
"""Generate standalone Toitumine uurimustöö PDF from Lisa T markdown."""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate

import generate_pdf as gp

BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "lisad" / "toitumine-uurimustoo.md"
PDF_FILE = BASE / "TOITUMINE_UURIMUSTOO.pdf"


def main():
    gp.doc_width = A4[0] - 4 * cm
    md = MD_FILE.read_text(encoding="utf-8")
    styles = gp.build_styles()
    doc = SimpleDocTemplate(
        str(PDF_FILE),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Toitumine ja taastumine — uurimustöö",
        author="Renee Aluste",
    )
    story = gp.build_story(md, styles)
    doc.build(story, onFirstPage=gp.add_header_footer, onLaterPages=gp.add_header_footer)
    print(f"Generated: {PDF_FILE}")


if __name__ == "__main__":
    main()
