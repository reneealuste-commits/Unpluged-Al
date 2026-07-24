#!/usr/bin/env python3
"""Generate OPORD PDF from markdown source."""

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    HRFlowable,
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "OPERATSIOON_PEEGEL_OPORD.md"
PDF_FILE = BASE / "OPERATSIOON_PEEGEL_OPORD.pdf"
LISAD_DIR = BASE / "lisad"
BOOK_FILES = [
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
    "lisa-v-uni-miks-me-magame.md",
    "lisa-w-montessori-beebi-austus-algusest.md",
    "lisa-x-taskukaardid-valjasuhtlus.md",
    "lisa-y-kanep-endokannabinoid-ja-ajalugu.md",
    "lisa-z-linnad-toostusuhiskond-ja-partnerlus.md",
    "lisa-aa-intiimsuse-atlas-keha-ja-ajalugu.md",
    "lisa-ab-paljajalu-ja-rippumine-linnas.md",
    "lisa-ac-magamistuba-voim-ja-revolutsioon.md",
    "lisa-ad-lood-konversiooni-checklist-ja-taskukaardid.md",
    "lisa-ae-ohk-liikumine-ja-komplimendid.md",
    "lisa-af-meeste-erektsioon-ja-rela-hooldus.md",
    "lisa-ag-rollid-partnerlus-ja-nl-skeem.md",
    "lisa-ah-leelo-vahersalu-taust.md",
    "lisa-ai-epp-karsin-armastus-paabstab-maailma.md",
    "lisa-aj-levitamine-ja-kuldne-taganemistee.md",
    "lisa-ak-kodaniku-taskuraamat-peegel.md",
    "renee-aluste-profiil.md",
]


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocTitle",
            parent=styles["Title"],
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=6,
            textColor=colors.HexColor("#1a3a2a"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="DocSubtitle",
            parent=styles["Normal"],
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=12,
            textColor=colors.HexColor("#333333"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading1"],
            fontSize=13,
            leading=16,
            spaceBefore=14,
            spaceAfter=8,
            textColor=colors.HexColor("#1a3a2a"),
            borderPadding=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubSection",
            parent=styles["Heading2"],
            fontSize=11,
            leading=14,
            spaceBefore=10,
            spaceAfter=6,
            textColor=colors.HexColor("#2d5a3d"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["Normal"],
            fontSize=9.5,
            leading=13,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Quote",
            parent=styles["Normal"],
            fontSize=9.5,
            leading=13,
            leftIndent=20,
            rightIndent=20,
            spaceAfter=8,
            textColor=colors.HexColor("#444444"),
            fontName="Helvetica-Oblique",
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["Normal"],
            fontSize=9,
            leading=12,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="OpordBullet",
            parent=styles["Normal"],
            fontSize=9.5,
            leading=13,
            leftIndent=14,
            bulletIndent=6,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="QAQuestion",
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            spaceBefore=10,
            spaceAfter=4,
            textColor=colors.HexColor("#1a3a2a"),
            fontName="Helvetica-Bold",
        )
    )
    styles.add(
        ParagraphStyle(
            name="QAAnswer",
            parent=styles["Normal"],
            fontSize=9.5,
            leading=13,
            leftIndent=10,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
        )
    )
    return styles


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def inline_format(text: str) -> str:
    text = esc(text)
    while "**" in text:
        start = text.find("**")
        end = text.find("**", start + 2)
        if end == -1:
            break
        inner = text[start + 2 : end]
        text = text[:start] + f"<b>{inner}</b>" + text[end + 2 :]
    while "*" in text and not text.startswith("*"):
        start = text.find("*")
        end = text.find("*", start + 1)
        if end == -1:
            break
        inner = text[start + 1 : end]
        text = text[:start] + f"<i>{inner}</i>" + text[end + 1 :]
    return text


def parse_table(lines: list[str]) -> Table | None:
    if len(lines) < 2:
        return None
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue
        rows.append([Paragraph(inline_format(c), ParagraphStyle(name="t", fontSize=8.5, leading=11)) for c in cells])
    if not rows:
        return None
    col_count = max(len(r) for r in rows)
    widths = [doc_width / col_count] * col_count
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f0ea")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1a3a2a")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#1a3a2a"))
    canvas.setLineWidth(1)
    canvas.line(2 * cm, A4[1] - 1.5 * cm, A4[0] - 2 * cm, A4[1] - 1.5 * cm)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.HexColor("#1a3a2a"))
    canvas.drawString(2 * cm, A4[1] - 1.2 * cm, "OPERATSIOON PEEGEL — PARANEMIS-TEEKOND (OPORD)")
    canvas.drawRightString(A4[0] - 2 * cm, A4[1] - 1.2 * cm, "AVALIK — EESTI RAHVALE")
    canvas.setFont("Helvetica", 7)
    canvas.drawString(2 * cm, 1 * cm, "22. juuli 2026 | Renee Aluste, operatsiooni koordinaator")
    canvas.drawRightString(A4[0] - 2 * cm, 1 * cm, f"Lehekülg {doc.page}")
    canvas.line(2 * cm, 1.3 * cm, A4[0] - 2 * cm, 1.3 * cm)
    canvas.restoreState()


def build_story(md_text: str, styles) -> list:
    story = []
    lines = md_text.splitlines()
    i = 0
    in_code = False
    table_buf: list[str] = []
    quote_buf: list[str] = []

    def flush_table():
        nonlocal table_buf
        if table_buf:
            t = parse_table(table_buf)
            if t:
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 6))
            table_buf = []

    def flush_quote():
        nonlocal quote_buf
        if quote_buf:
            story.append(Paragraph(inline_format(" ".join(quote_buf)), styles["Quote"]))
            quote_buf = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            if not in_code:
                story.append(Spacer(1, 6))
            i += 1
            continue

        if in_code:
            story.append(Paragraph(f"<font face='Courier' size='7'>{esc(line)}</font>", styles["Body"]))
            i += 1
            continue

        if stripped.startswith("![") and "](" in stripped:
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
            if m:
                _, rel_path = m.groups()
                img_path = BASE / rel_path if not rel_path.startswith("/") else Path(rel_path)
                if img_path.exists():
                    story.append(Spacer(1, 4))
                    img = Image(str(img_path), width=3.2 * cm, height=3.2 * cm, kind="proportional")
                    img.hAlign = "LEFT"
                    story.append(img)
                    story.append(Spacer(1, 6))
            i += 1
            continue

        if stripped.startswith("|"):
            flush_quote()
            table_buf.append(stripped)
            i += 1
            continue
        flush_table()

        if stripped.startswith("> "):
            quote_buf.append(stripped[2:])
            i += 1
            continue
        flush_quote()

        if stripped == "---":
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))
            story.append(Spacer(1, 4))
            i += 1
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(inline_format(stripped[2:]), styles["DocTitle"]))
            i += 1
            continue

        if stripped.startswith("## "):
            text = stripped[3:]
            if text.startswith("OPERATSIOON") or text.startswith("1.") or text.startswith("2.") or text.startswith("3.") or text.startswith("4.") or text.startswith("5."):
                story.append(PageBreak())
            story.append(Paragraph(inline_format(text), styles["Section"]))
            i += 1
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(inline_format(stripped[4:]), styles["SubSection"]))
            i += 1
            continue

        if stripped.startswith("#### "):
            story.append(Paragraph(inline_format(stripped[5:]), styles["SubSection"]))
            i += 1
            continue

        if stripped.startswith("**K:") or stripped.startswith("**K ("):
            story.append(Paragraph(inline_format(stripped), styles["QAQuestion"]))
            i += 1
            continue

        if stripped.startswith("*Minu küsimus sulle:"):
            story.append(Paragraph(inline_format(stripped.strip("*")), styles["Quote"]))
            i += 1
            continue

        if stripped.startswith("**V:") or stripped.startswith("**V ("):
            story.append(Paragraph(inline_format(stripped), styles["QAAnswer"]))
            i += 1
            continue

        if stripped.startswith("- "):
            story.append(Paragraph(f"• {inline_format(stripped[2:])}", styles["OpordBullet"]))
            i += 1
            continue

        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            story.append(Paragraph(inline_format(stripped.strip("*")), styles["Quote"]))
            i += 1
            continue

        if not stripped:
            story.append(Spacer(1, 4))
            i += 1
            continue

        story.append(Paragraph(inline_format(stripped), styles["Body"]))
        i += 1

    flush_table()
    flush_quote()
    return story


if __name__ == "__main__":
    global doc_width
    doc_width = A4[0] - 4 * cm

    md = MD_FILE.read_text(encoding="utf-8")
    styles = build_styles()

    doc = SimpleDocTemplate(
        str(PDF_FILE),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="OPERATSIOON PEEGEL — OPORD",
        author="Renee Aluste",
    )

    story = build_story(md, styles)
    for book in BOOK_FILES:
        book_path = LISAD_DIR / book
        if book_path.exists():
            story.append(PageBreak())
            story.extend(build_story(book_path.read_text(encoding="utf-8"), styles))
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Generated: {PDF_FILE}")
