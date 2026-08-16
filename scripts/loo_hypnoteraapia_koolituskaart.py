#!/usr/bin/env python3
"""Prinditav HY1 hüpnoosi koolituskaart — 1 leht."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT = "/workspace/hypnoteraapia-algaja-koolituskaart.pdf"

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
        title="HY1 — Hüpnoosi algaja koolituskaart",
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
    story.append(Paragraph("HY1 — HÜPNOOSI ALGAJA KOOLITUSKAART", title))
    story.append(
        Paragraph(
            "Unpluged-Al · 15–25 min · iga mees kaaslasele · v1.2 · 2026 · "
            "Hariduslik — ei asenda spetsialisti",
            sub,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=GREEN))

    story.append(Paragraph("OLULINE — loe enne alustamist", h2))
    for line in [
        "Kerge stress, uni, fookus — <b>MITTE</b> trauma / PTSD / kriis.",
        "Sa saad igal hetkel silmad avada ja lõpetada.",
        "STOP kohe, kui distress &gt; 8/10 või tunned end „õhust väljas”.",
    ]:
        story.append(Paragraph(f"• {line}", body))

    story.append(Paragraph("PROTSESS (kiire viide)", h2))
    story.append(
        Paragraph(
            "Ankur (3× hingetõmme) → Keha skaneering → Turvakoht → "
            "Suggestioon 8–12 min → Tagasi 5-1 → Vesi → „Mis muutus?”",
            body,
        )
    )

    story.append(Paragraph("SUGGESTIOON", h2))
    story.append(
        Paragraph(
            "<i>„Ma rahunen loomulikult. Mu keha teab, kuidas tulla rahule. "
            "Ma olen turvaliselt. Iga hingetõmme toob rohkem kergust.”</i>",
            body,
        )
    )

    table = Table(
        [
            ["EESMÄRK (vali ÜKS)", "MÄRGE"],
            ["□ Rahunemine  □ Uni  □ Fookus", "Stress enne: ___ /10"],
            ["□ Enne debriefi/KOV (5 min)", "Stress pärast: ___ /10"],
        ],
        colWidths=[95 * mm, 75 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("GRID", (0, 0), (-1, -1), 0.4, GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(Spacer(1, 4))
    story.append(table)

    story.append(Spacer(1, 6))
    story.append(Paragraph("STOP KORRAL", h2))
    story.append(
        Paragraph(
            "Ava silmad · Jalad põrandale · 5-4-3-2-1 maandamine · Vesi · Kõnni · Spetsialist vajadusel",
            body,
        )
    )

    rules = Table(
        [
            ["KEELATUD", "KOHUSTUSLIK"],
            ["Trauma avamine ilma oskuseta", "Üks eesmärk korraga"],
            ["Sund / „sa ei mäleta”", "Nõusolek enne alustamist"],
            ["Diagnoosimine", "1 lause integratsioon / debrief"],
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

    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Seotud: hypnoteraapia-algaja-juhend.md · hypnoteraapia-algaja-plaankonspekt.md · "
            "debrief-kaart-malevapealik.pdf",
            small,
        )
    )
    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
