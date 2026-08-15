#!/usr/bin/env python3
"""1-lehekuline Debrief kaart malevapealikutele — Operation Mirror / Olessanded."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

OUTPUT = "/workspace/debrief-kaart-malevapealik.pdf"

GREEN = colors.HexColor("#1B5E20")
LIGHT_GREEN = colors.HexColor("#E8F5E9")
DARK = colors.HexColor("#212121")
GRAY = colors.HexColor("#757575")


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Debrief kaart — malevapealik",
        author="Operation Mirror / Olessanded",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=16,
        textColor=GREEN,
        spaceAfter=4,
        fontName="Helvetica-Bold",
    )
    subtitle = ParagraphStyle(
        "Sub",
        parent=styles["Normal"],
        fontSize=9,
        textColor=GRAY,
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontSize=11,
        textColor=GREEN,
        spaceBefore=6,
        spaceAfter=4,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=10,
        leading=13,
        textColor=DARK,
    )
    small = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontSize=8,
        textColor=GRAY,
        leading=10,
    )
    step = ParagraphStyle(
        "Step",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        leftIndent=8,
        textColor=DARK,
    )

    story = []

    story.append(Paragraph("DEBRIEF KAART — MALEVAPEALIK", title))
    story.append(
        Paragraph(
            "Operation Mirror · Õlessanded allüksustele · Extreme Ownership · v1.0 · 2026",
            subtitle,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1, color=GREEN, spaceAfter=8))

    story.append(
        Paragraph(
            "<b>Eesmärk:</b> Iga kuu 30 min. Juht tunnistab esimesena. "
            "Eesmärk on õpe, mitte süüdistus.",
            body,
        )
    )
    story.append(Spacer(1, 6))

    meta_data = [
        ["Malev:", "_________________________", "Kuupäev:", "_______________"],
        ["Malevapealik:", "_____________________", "Koht:", "________________"],
        ["Osalejad (min 3):", "_______________________________________________", "", ""],
    ]
    meta = Table(meta_data, colWidths=[22 * mm, 58 * mm, 18 * mm, 52 * mm])
    meta.setStyle(
        TableStyle(
            [
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(meta)
    story.append(Spacer(1, 8))

    steps = [
        ("1. MIS LÄKS HÄSTI?", "Mis toimis? Mida jäätame? (2–3 punkti)"),
        ("2. MIS LÄKS VALESTI?", "<b>Juht alustab.</b> Ausalt, ilma vabandusteta."),
        ("3. MINU OTSUSE VIGA", "Mis otsuse ma tegin, mis kaasa tõi? Extreme Ownership."),
        ("4. MIDA TEEME TEISITI?", "Üks otsus + omanik + tähtaeg:"),
        ("5. TSIVIILI MÕJU", "Kuidas see mõjutas elanikke / KOV / farmerit / kooli?"),
    ]

    for head, desc in steps:
        story.append(Paragraph(head, h2))
        story.append(Paragraph(desc, step))
        box = Table(
            [[""], [""], [""]],
            colWidths=[174 * mm],
            rowHeights=[5 * mm, 5 * mm, 5 * mm],
        )
        box.setStyle(
            TableStyle(
                [
                    ("BOX", (0, 0), (-1, -1), 0.5, GRAY),
                    ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                    ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ]
            )
        )
        story.append(box)
        story.append(Spacer(1, 4))

    story.append(Paragraph("KEELATUD / KOHUSTUSLIK", h2))
    rules = Table(
        [
            ["KEELATUD", "KOHUSTUSLIK"],
            ['"Kes on süüdi?"', "Juht tunnistab esimesena"],
            ["Süüdistamine alluvatele", "Lahendus + omanik + kuupäev"],
            ["Debrief ilma protokollita", "1 lk raport esindajatekogule"],
        ],
        colWidths=[87 * mm, 87 * mm],
    )
    rules.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("BOX", (0, 0), (-1, -1), 0.5, GREEN),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("BACKGROUND", (0, 1), (-1, -1), LIGHT_GREEN),
            ]
        )
    )
    story.append(rules)
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "<b>Allkiri:</b> Malevapealik _________________________ "
            "Kuupäev ______________",
            body,
        )
    )
    story.append(Spacer(1, 4))
    story.append(
        Paragraph(
            "Seotud: OPORD-sise.md · juhtimisvideo-riho-remo-oppejuhend.md · "
            "Remo Ojaste / Combat Ready — Extreme Ownership",
            small,
        )
    )
    story.append(
        Paragraph(
            "Lahinguväljal näeme. Eesti eest. Võimatut pole olemas.",
            small,
        )
    )

    doc.build(story)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
