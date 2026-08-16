#!/usr/bin/env python3
"""Prinditav DP1 diplomaatia koolituskaart — 1 leht."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT = "/workspace/diplomaatia-soltlasega-koolituskaart.pdf"

BLUE = colors.HexColor("#0D47A1")
LIGHT = colors.HexColor("#E3F2FD")
DARK = colors.HexColor("#212121")
GRAY = colors.HexColor("#757575")


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="DP1 — Diplomaatia sõltlasega koolituskaart",
        author="Unpluged-Al",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=15,
        textColor=BLUE,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=8, textColor=GRAY, spaceAfter=6)
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontSize=10,
        textColor=BLUE,
        spaceBefore=4,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9, leading=12, textColor=DARK)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=7.5, textColor=GRAY, leading=9)

    story = []
    story.append(Paragraph("DP1 — DIPLOMAATIA SÕLTLASEGA KOOLITUSKAART", title))
    story.append(
        Paragraph(
            "Unpluged-Al · 15 min kiir · v1.0 · 2026 · Hariduslik — ei asenda spetsialisti",
            sub,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=BLUE))

    story.append(Paragraph("OLULINE — enne vestlust", h2))
    for line in [
        "Füüsiline oht → <b>112</b>. STOP joobes/kriisis.",
        "Üks eesmärk korraga. Ma ei “ravi” — ma suhtlen.",
        "Ei enabling: raha, vabandused, võlgade katmine.",
    ]:
        story.append(Paragraph(f"• {line}", body))

    story.append(Paragraph("PROTSESS", h2))
    story.append(
        Paragraph(
            "Stress 0–10 → HY1 5 min (kui &gt;7) → 1 eesmärk → vestlus → "
            "Piir → STOP vajadusel → Debrief 1 lause",
            body,
        )
    )

    story.append(Paragraph("PIIRIDE NÄIDE", h2))
    story.append(
        Paragraph(
            "<i>„Ma ei osta sulle alkoholi. Ma võin rääkida abist, kui sina seda tahad.”</i>",
            body,
        )
    )

    rules = Table(
        [
            ["DO", "DON'T"],
            ["Ma kuulan", "Moraliseerimine"],
            ["Ma armastan sind", "Raha alkoholiks"],
            ["Ma ei toeta seda", "Debatt öösel"],
        ],
        colWidths=[85 * mm, 85 * mm],
    )
    rules.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.4, GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(Spacer(1, 6))
    story.append(rules)

    story.append(Spacer(1, 6))
    story.append(Paragraph("STOP / SUUNAMINE", h2))
    story.append(
        Paragraph(
            "112 · 116 123 · ÕnneKlubi 5305 3060 / 5885 8575 · Ohvriabi palunabi.ee",
            body,
        )
    )

    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Demo: DP1-D01–D04 · dp1_demo_koordinaator.py · "
            "hupnoteraapia-teenused-ohvriabi-raport.md",
            small,
        )
    )
    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
