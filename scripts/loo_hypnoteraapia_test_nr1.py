#!/usr/bin/env python3
"""Genereerib HY1 test nr. 1 PDF — kaitseväe Automaadi test vormingus."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "/workspace/hypnoteraapia-test-nr1-kaaslasega.pdf"

GREEN = colors.HexColor("#1B5E20")
DARK = colors.HexColor("#212121")
GRAY = colors.HexColor("#757575")
RED = colors.HexColor("#B71C1C")


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="HY1 test nr. 1 — Turvaline hüpnoos kaaslasega",
        author="Unpluged-Al",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=16,
        textColor=GREEN,
        spaceAfter=4,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontSize=12,
        textColor=GREEN,
        spaceBefore=10,
        spaceAfter=4,
        fontName="Helvetica-Bold",
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontSize=10,
        textColor=DARK,
        spaceBefore=6,
        spaceAfter=3,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9, leading=12, textColor=DARK)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=8, leading=10, textColor=GRAY)
    cmd = ParagraphStyle(
        "Cmd",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        leftIndent=8,
        textColor=DARK,
        fontName="Helvetica-Oblique",
    )

    story = []

    # === PEALKIRI ===
    story.append(Paragraph("Hüpnoosi test nr. 1", title))
    story.append(
        Paragraph(
            "Turvaline hüpnoos kaaslasega — iga mees saab seda õppida ja teha",
            ParagraphStyle("Sub", parent=body, alignment=TA_CENTER, fontSize=10, textColor=GRAY),
        )
    )
    story.append(Spacer(1, 4))
    story.append(
        Paragraph("Unpluged-Al · HY1 · v1.2 · 16.08.2026 · Hariduslik", small)
    )
    story.append(HRFlowable(width="100%", thickness=1, color=GREEN))
    story.append(Spacer(1, 6))

    # === A. INSTRUKTORI MÄRKMED ===
    story.append(Paragraph("A. Instruktori märkmed", h1))

    for heading, text in [
        ("Õppetunni eesmärk", "Kontrollida mehe turvalise hüpnoosi juhtimise taset kaaslasega. Iga mees suudab juhtida 15-min rahunemise, une- või fookusprotokolli ilma OT vigadeta."),
        ("Kestus", "1 × 45 min (koolitus + test) · 15–25 min (protokoll kahekesi kodus)"),
        ("Õppetunni vorm", "Hindamine — praktiline paariline sooritus."),
    ]:
        story.append(Paragraph(heading, h2))
        story.append(Paragraph(text, body))

    story.append(Paragraph("Allüksuse varustus", h2))
    varustus = Table(
        [
            ["Varustus", "Kogus"],
            ["Vaikne tuba", "1 paari kohta"],
            ["Tool / matt", "1 paari kohta"],
            ["Vesi", "1 paari kohta"],
            ["Taimer", "1 paari kohta"],
            ["Paber + pliiats", "1 paari kohta"],
            ["HY1 koolituskaart", "1 juhile"],
        ],
        colWidths=[90 * mm, 70 * mm],
    )
    varustus.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.4, GRAY),
            ]
        )
    )
    story.append(varustus)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Ettevalmistused", h2))
    for i, item in enumerate(
        [
            "Valmista ette vaikne õppekoht",
            "Hangi varustus",
            "Tutvu testi kirjelduse ja OT vigadega",
            "Valmista hindamisleht",
            "Veendu: kerge stress/uni/fookus — MITTE trauma/PTSD/kriis",
            "Lepi kokku signaal: STOP — sessioon katkeb",
        ],
        1,
    ):
        story.append(Paragraph(f"{i}. {item}", body))

    story.append(PageBreak())

    # === B. TEST ===
    story.append(Paragraph("B. Tunni läbiviimine", h1))
    story.append(Paragraph("OT vead — ohutust ohustavad vead", h2))
    story.append(
        Paragraph(
            "Test <b>mittesooritatud</b>, kui esineb vähemalt üks OT viga:",
            body,
        )
    )
    ot_rows = [["#", "OT viga"]]
    for i, ot in enumerate(
        [
            "Sundib silmi kinni / keelab lõpetamise",
            "Avab trauma ilma spetsialistita",
            "Jätkab kui distress > 8/10",
            "Diagnoosib / lubab meditsiinilist väidet",
            "Ütleb 'sa ei mäleta' / võtab kontrolli",
            "Alustab ilma nõusolekuta",
            "Proovib 'paranda kõik' — mitu eesmärki",
            "Jätkab pärast STOP signaali",
        ],
        1,
    ):
        ot_rows.append([f"OT-{i}", ot])

    ot_table = Table(ot_rows, colWidths=[18 * mm, 142 * mm])
    ot_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), RED),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.4, GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(ot_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Protseduur ja käsklused", h2))
    proc_rows = [["#", "Käsklus", "Juht (A)", "Kaaslane (B)"]]
    steps = [
        ("1", "Liikuge vaiksesse ruumi ja tehke ohutuskontroll", "Kontrollib ruumi", "Kinnitab"),
        ("2", "Lepi kokku üks eesmärk", "Küsib", "Valib ühe"),
        ("3", "Sul on alati kontroll. Ava silmad igal hetkel", "Ootab kinnitust", "Kinnitab"),
        ("4", "Hinda stress null kuni kümme", "Logib", "Ütleb"),
        ("5", "Ankur — sisse neli, välja kuus × 3", "Loeb", "Järgib"),
        ("6", "Keha skaneering", "Loeb aeglaselt", "Järgib"),
        ("7", "Turvakoht", "Loeb", "Kujutleb"),
        ("8", "Suggestioon 8–12 min", "Loeb HY1 lause", "Kuulab"),
        ("9", "Tule tagasi — viis kuni üks", "Loendab", "Avab silmad"),
        ("10", "Joo vett", "Annab vesi", "Joo"),
        ("11", "Mis muutus? Stress enne/pärast?", "Logib", "Vastab"),
    ]
    proc_rows.extend(steps)
    proc = Table(proc_rows, colWidths=[8 * mm, 52 * mm, 42 * mm, 42 * mm])
    proc.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
                ("GRID", (0, 0), (-1, -1), 0.3, GRAY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(proc)
    story.append(Spacer(1, 8))

    story.append(Paragraph("HINDAMINE", h2))
    story.append(
        Paragraph(
            "<b>Sooritatud:</b> 0 OT viga + min 14 punkti 18-st + kaaslane kinnitab: "
            "'Sain igal hetkel lõpetada.'",
            body,
        )
    )
    story.append(Spacer(1, 6))

    story.append(Paragraph("Lisa 2 — HY1 suggestioon (juhi skript)", h2))
    suggestioon = (
        '<i>„Sa rahuned loomulikult. Su keha teab, kuidas tulla rahule. '
        'Sa oled turvaliselt. Sa saad valida, mida sa mõtled. '
        'Iga hingetõmme toob rohkem kergust."</i>'
    )
    story.append(Paragraph(suggestioon, cmd))

    story.append(Spacer(1, 10))
    story.append(Paragraph("C. Tunni lõpetamine — tulemuste kokkuvõte, tagasiside, kodutöö 3×15 min", h2))
    story.append(
        Paragraph(
            "Seotud: hypnoteraapia-algaja-juhend.md · debrief-kaart-malevapealik.pdf",
            small,
        )
    )

    doc.build(story)
    print(f"Salvestatud: {OUTPUT}")


if __name__ == "__main__":
    build()
