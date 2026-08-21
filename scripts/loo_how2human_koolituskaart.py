#!/usr/bin/env python3
"""Prinditav H2H How2Human + Elicitation koolituskaart — 1 leht."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT = "/workspace/how2human-elicitation-koolituskaart.pdf"

BROWN = colors.HexColor("#4E342E")
LIGHT = colors.HexColor("#EFEBE9")
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
        title="H2H — How2Human + Elicitation koolituskaart",
        author="Unpluged-Al",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=15,
        textColor=BROWN,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=8, textColor=GRAY, spaceAfter=6)
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontSize=10,
        textColor=BROWN,
        spaceBefore=4,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9, leading=12, textColor=DARK)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=7.5, textColor=GRAY, leading=9)

    story = []
    story.append(Paragraph("H2H — How2Human + Elicitation", title))
    story.append(
        Paragraph(
            "Juht / mentor / malevapealik · 20 min kiir · enne rasket vestlust · v1.0",
            sub,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=BROWN))

    story.append(Paragraph("ENNE — 60 sekundit", h2))
    for line in [
        "Keha enne sõna (3 sek) · üks eesmärk · kas olen valmis kuulma?",
        "Konfidentsiaalsus — mis ruumis, jääb ruumi (v.a. oht).",
    ]:
        story.append(Paragraph(f"• {line}", body))

    story.append(Paragraph("4 oskust", h2))
    skills = [
        ["Kehakeel", "Loed enne kuulamist — kaitse, kõhkumine, tempo"],
        ["Mirroring", "Subtle — postuur, tempo, 1–2 sõna (mitte karikatuur)"],
        ["Reflecting", "„Ma kuulen, et…“ — PEATU, ära lahenda kohe"],
        ["Elicitation", "Too tõde välja ilma uurimisena (E1–E5 all)"],
    ]
    t1 = Table(skills, colWidths=[28 * mm, 130 * mm])
    t1.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.5, BROWN),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, BROWN),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(t1)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Elicitation E1–E5", h2))
    elicit = [
        "E1 Eeldus: „Enamik juhte kurdavad, et meeskond kuuleb, aga ei tee…“",
        "E2 Eksitus: „Mulle tundus, et kõik olid nõus.“",
        "E3 Vahemik: „Nädalaid või kuudeks?“",
        "E4 Kolmas: „Mõni on maininud, et protsess on aeglane…“",
        "E5 Vaikus: nods + 5 sek pärast osalist vastust",
    ]
    for line in elicit:
        story.append(Paragraph(f"• {line}", body))

    story.append(Paragraph("Keha → tegevus", h2))
    body_map = [
        ["Kaitse (eemale, ristis)", "E1/E4 — ära uuri otse"],
        ["Kõhkumine enne „jah“", "E2 tahtlik eksitus"],
        ["Kiire üldine jutt", "E3 + E5 vaikus"],
    ]
    t2 = Table(body_map, colWidths=[55 * mm, 103 * mm])
    t2.setStyle(
        TableStyle(
            [
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("BOX", (0, 0), (-1, -1), 0.5, BROWN),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, BROWN),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(t2)
    story.append(Spacer(1, 4))

    story.append(Paragraph("20 min protokoll", h2))
    story.append(
        Paragraph(
            "Keha skaneering 2 min → 1 eesmärk → vestlus (reflect + elicit) → "
            "„Mis ma kuulsin?“ → debrief 3 küsimust → 1 samm 72h",
            body,
        )
    )

    story.append(Paragraph("Debrief", h2))
    for line in [
        "1. Mis ma kuulsin, mida varem ei kuulnud?",
        "2. Milline reflect / E1–E5 töötas?",
        "3. Mis on üks samm 72h jooksul?",
    ]:
        story.append(Paragraph(line, body))

    story.append(Paragraph("STOP", h2))
    story.append(
        Paragraph(
            "Oht → 112 · kriis → spetsialist / 116 123 · teine ütleb STOP → lõpeta",
            body,
        )
    )

    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "EI TEE: karikatuur mirror · manipulatsioon · vastust relvana kasutada · "
            "Hariduslik — ei asenda spetsialisti · Unpluged-Al · H2H v1.0 · Maleva Nõukogu",
            small,
        )
    )
    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
