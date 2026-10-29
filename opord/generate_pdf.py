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
    "lisa-bd-riiklik-peegel-hindamisvorm.md",
    "lisa-be-kaaslase-hindamine-ranger.md",
    "lisa-bf-suhte-hindamise-toovihik.md",
    "kiht0-ru-tuum-1-leht.md",
    "renee-aluste-profiil.md",
]

# Tiered PDF packages (K0–K1). K2 = full OPORD; K3 = on-demand lisas.
PACKAGE_PDFS = {
    "PEEGEL_TUUM.pdf": [BASE / "PEEGEL_TUUM.md"],
    "PEEGEL_TEE_A.pdf": [
        LISAD_DIR / "lisa-h-kiirjuhend-kriisis-isale.md",
        LISAD_DIR / "raamat-06-murra-ring.md",
        LISAD_DIR / "lisa-p-takistused-ja-valideerimine.md",
        LISAD_DIR / "lisa-ba-keha-vabastamine-tasuta.md",
        LISAD_DIR / "lisa-ad-lood-konversiooni-checklist-ja-taskukaardid.md",
    ],
    "PEEGEL_TEE_B.pdf": [
        BASE / "PEEGEL_TUUM.md",
        LISAD_DIR / "lisa-r-kes-ma-olen-ja-taust.md",
        LISAD_DIR / "lisa-t-valitsuse-ipb-analuus.md",
    ],
    "PEEGEL_TEE_C.pdf": [
        LISAD_DIR / "raamat-01-unplugged-ava-silmad.md",
        LISAD_DIR / "raamat-04-tugev-isa.md",
        LISAD_DIR / "raamat-05-pere-rindejoon.md",
        LISAD_DIR / "lisa-m-kodaniku-identiteet-ja-vanne.md",
        LISAD_DIR / "lisa-bc-digitaalne-detoks-ja-nuputelefon.md",
    ],
    "PEEGEL_TEE_D.pdf": [
        LISAD_DIR / "lisa-n-aluste-kool.md",
        LISAD_DIR / "lisa-i-inimesekeskne-juhtimine.md",
        LISAD_DIR / "lisa-q-side-eeskirjad-ja-suhtlus.md",
        LISAD_DIR / "lisa-ao-ultimate-power-kokkuvote.md",
        LISAD_DIR / "lisa-x-taskukaardid-valjasuhtlus.md",
    ],
    "PEEGEL_RU_KIHT0.pdf": [
        LISAD_DIR / "kiht0-ru-tuum-1-leht.md",
        LISAD_DIR / "lisa-an-venekeelne-sihtruhm-ja-inimesekeskne-levitus.md",
    ],
    "PEEGEL_TEE_F.pdf": [
        LISAD_DIR / "lisa-i-inimesekeskne-juhtimine.md",
        LISAD_DIR / "lisa-p-takistused-ja-valideerimine.md",
        LISAD_DIR / "lisa-l-ministeeriumid-ja-tai.md",
    ],
}


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


def make_header_footer(header_left: str, header_right: str = "AVALIK — EESTI RAHVALE"):
    def add_header_footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#1a3a2a"))
        canvas.setLineWidth(1)
        canvas.line(2 * cm, A4[1] - 1.5 * cm, A4[0] - 2 * cm, A4[1] - 1.5 * cm)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.setFillColor(colors.HexColor("#1a3a2a"))
        canvas.drawString(2 * cm, A4[1] - 1.2 * cm, header_left)
        canvas.drawRightString(A4[0] - 2 * cm, A4[1] - 1.2 * cm, header_right)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(2 * cm, 1 * cm, "24. juuli 2026 | Renee Aluste, operatsiooni koordinaator")
        canvas.drawRightString(A4[0] - 2 * cm, 1 * cm, f"Lehekülg {doc.page}")
        canvas.line(2 * cm, 1.3 * cm, A4[0] - 2 * cm, 1.3 * cm)
        canvas.restoreState()

    return add_header_footer


add_header_footer = make_header_footer("OPERATSIOON PEEGEL — PARANEMIS-TEEKOND (OPORD)")


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


def generate_pdf_from_files(
    output_path: Path,
    md_files: list[Path],
    title: str,
    header_left: str,
) -> None:
    global doc_width
    doc_width = A4[0] - 4 * cm
    styles = build_styles()
    story: list = []
    header_fn = make_header_footer(header_left)

    for idx, md_path in enumerate(md_files):
        if not md_path.exists():
            print(f"  SKIP missing: {md_path}")
            continue
        if idx > 0:
            story.append(PageBreak())
        story.extend(build_story(md_path.read_text(encoding="utf-8"), styles))

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=title,
        author="Renee Aluste",
    )
    doc.build(story, onFirstPage=header_fn, onLaterPages=header_fn)
    print(f"Generated: {output_path}")


def generate_full_opord() -> None:
    generate_pdf_from_files(
        PDF_FILE,
        [MD_FILE] + [LISAD_DIR / book for book in BOOK_FILES],
        "OPERATSIOON PEEGEL — OPORD",
        "OPERATSIOON PEEGEL — PARANEMIS-TEEKOND (OPORD)",
    )


def generate_tiered_pdfs() -> None:
    headers = {
        "PEEGEL_TUUM.pdf": "PEEGEL TUUM — K0 ESIMENE KONTAKT",
        "PEEGEL_TEE_A.pdf": "PEEGEL TEE A — ISA KRIISIS",
        "PEEGEL_TEE_B.pdf": "PEEGEL TEE B — SKEPTIK",
        "PEEGEL_TEE_C.pdf": "PEEGEL TEE C — PERE",
        "PEEGEL_TEE_D.pdf": "PEEGEL TEE D — DEMOMEES",
        "PEEGEL_RU_KIHT0.pdf": "PEEGEL KIHT 0 — VENEKEELNE TUUM",
        "PEEGEL_TEE_F.pdf": "PEEGEL TEE F — JUHT / KOOLITUS",
    }
    for pdf_name, md_files in PACKAGE_PDFS.items():
        generate_pdf_from_files(
            BASE / pdf_name,
            md_files,
            pdf_name.replace(".pdf", "").replace("_", " "),
            headers.get(pdf_name, "OPERATSIOON PEEGEL"),
        )


if __name__ == "__main__":
    generate_full_opord()
    generate_tiered_pdfs()
