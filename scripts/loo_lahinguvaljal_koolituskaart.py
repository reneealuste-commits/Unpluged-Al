#!/usr/bin/env python3
"""Prinditav LVJ lahinguvaljal juhtimise koolituskaart — 1 leht."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT = "/workspace/lahinguvaljal-juhtimine-koolituskaart.pdf"

GREEN = colors.HexColor("#1B5E20")
LIGHT = colors.HexColor("#E8F5E9")
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
        title="LVJ — Lahinguvaljal Juhtimine koolituskaart",
        author="Unpluged-Al",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=15,
        textColor=GREEN,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=8, textColor=GRAY, spaceAfter=6)
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontSize=10,
        textColor=GREEN,
        spaceBefore=4,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9, leading=12, textColor=DARK)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=7.5, textColor=GRAY, leading=9)

    story = []
    story.append(Paragraph("LVJ — 4 LAHINGUREEGELIT KOOLITUSKAART", title))
    story.append(
        Paragraph(
            "Renee Aluste · Combat Ready · v1.0 · 2026 · Extreme Ownership Eesti keeles",
            sub,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=GREEN))

    story.append(Paragraph("VUNDAMENT (enne reegleid)", h2))
    for line in [
        "<b>Ülim vastutus</b> — see on alati MINU süü",
        "<b>Distsipliin on vabadus</b> — järjepidevus loob valikud",
        "<b>Ego on vaenlane</b> — ausus &gt; õigus",
    ]:
        story.append(Paragraph(f"• {line}", body))

    rules = Table(
        [
            ["#", "Reegel", "Küsimus täna"],
            ["1", "Kata ja liigu", "Kes vajab täna katmist? Küsi."],
            ["2", "Lihtsus", "Anna 1 korraldus. Küsi tagasilugemist."],
            ["3", "Prioriseeri", "Mis on number üks prioriteet täna?"],
            ["4", "Hajutatud juhtimine", "Delegeeri 1 ülesanne + MIKS"],
        ],
        colWidths=[12 * mm, 45 * mm, 125 * mm],
    )
    rules.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(Spacer(1, 4 * mm))
    story.append(rules)

    story.append(Paragraph("DEBRIEF (pärast)", h2))
    story.append(
        Paragraph(
            "<i>„Mis läks hästi? Mis ei läinud? Mida teeme teisiti?“</i> — Juht tunnistab <b>ESIMESENA</b>.",
            body,
        )
    )

    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=GREEN))
    story.append(
        Paragraph(
            "Combat Ready · combatready.eu · renee.aluste@combatready.eu · lahinguvaljal-juhtimine.pdf",
            small,
        )
    )

    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
