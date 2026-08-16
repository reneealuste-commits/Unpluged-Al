#!/usr/bin/bin/env python3
"""Prinditav HY1 koolituskaart — EMDR eeskuju kompaktne vorm."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/hypnoteraapia-algaja-koolituskaart.pdf"

GREEN = colors.HexColor("#1B5E20")
GRAY = colors.HexColor("#757575")
DARK = colors.HexColor("#212121")


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="HY1 — Hüpnoteraapia juhised algajale",
        author="Unpluged-Al",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title", parent=styles["Heading1"], fontSize=14, textColor=GREEN,
        fontName="Helvetica-Bold", spaceAfter=2,
    )
    sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=9, textColor=GRAY, spaceAfter=4)
    h2 = ParagraphStyle(
        "H2", parent=styles["Heading2"], fontSize=10, textColor=GREEN,
        fontName="Helvetica-Bold", spaceBefore=5, spaceAfter=2,
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9, leading=12, textColor=DARK)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=7.5, textColor=GRAY, leading=9)

    story = []
    story.append(Paragraph("Hüpnoteraapia juhised algajale", title))
    story.append(Paragraph("Iseendale ja paarilisele kodus · 15–25 min · HY1 v2.0", sub))
    story.append(HRFlowable(width="100%", thickness=0.5, color=GREEN))

    story.append(Paragraph("OLULINE — loe enne alustamist", h2))
    for line in [
        "Kerge stress, uni, fookus — <b>MITTE</b> trauma / PTSD / kriis.",
        "Distress &gt; <b>8/10</b> → STOP.",
        "Üks eesmärk. Kaaslane võib igal hetkel silmad avada.",
        "Iga mees saab juhtida oma kaaslasele.",
    ]:
        story.append(Paragraph(f"• {line}", body))

    story.append(Paragraph("Kiire viide", h2))
    story.append(
        Paragraph(
            "Ankur → Keha skaneering → Turvakoht → Suggestioon 8–12 min → "
            "Tagasi 5-1 → Vesi → „Mis muutus?”",
            body,
        )
    )

    story.append(Paragraph("Suggestioon", h2))
    story.append(
        Paragraph(
            '<i>„Ma rahunen loomulikult. Mu keha teab, kuidas tulla rahule. '
            'Ma olen turvaliselt. Iga hingetõmme toob rohkem kergust.”</i>',
            body,
        )
    )

    story.append(Paragraph("Paariline — enne algust", h2))
    story.append(
        Paragraph(
            '<i>„Sul on alati kontroll. Ava silmad igal hetkel.”</i> '
            "Ei diagnoosi · ei suru · STOP kui partner ütleb.",
            body,
        )
    )

    story.append(Paragraph("STOP", h2))
    story.append(
        Paragraph(
            "Paanika · dissotsiatsioon · flashback → ava silmad · 5-4-3-2-1 · vesi · 116 123",
            body,
        )
    )

    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Hariduslik — ei asenda spetsialisti · Unpluged-Al · HY1 v2.0",
            small,
        )
    )
    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
