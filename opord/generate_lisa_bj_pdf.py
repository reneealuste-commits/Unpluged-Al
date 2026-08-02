#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate standalone Lisa BJ PDF from markdown."""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate

import generate_pdf as gp

BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "lisad" / "lisa-bj-erica-komisar-lapse-attachement-ja-tehnoloogia.md"
PDF_FILE = BASE / "LISA_BJ_KOMISAR_PRINT.pdf"


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
        title="Lisa BJ Komisar",
        author="Renee Aluste",
    )
    story = gp.build_story(md, styles)
    doc.build(story, onFirstPage=gp.add_header_footer, onLaterPages=gp.add_header_footer)
    print(f"Generated: {PDF_FILE}")


if __name__ == "__main__":
    main()
