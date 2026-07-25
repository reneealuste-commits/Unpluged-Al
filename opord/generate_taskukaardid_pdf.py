#!/usr/bin/env python3
"""Generate print-ready pocket cards (Lisa X) and flyer PDFs."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, A5, A6
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GREEN_LIGHT = colors.HexColor("#2d5a3d")
GRAY = colors.HexColor("#444444")

CARDS_PDF = BASE / "TASKUKAARDID_PRINT.pdf"
MINI_PDF = BASE / "TASKUKAARDID_RAHAKOTT.pdf"
FLYER_PDF = BASE / "LENDLEHT_PRINT.pdf"


def draw_card_header(c, x, y, w, h, title, subtitle=""):
    """Kevadtorm-style dark green header band."""
    c.setFillColor(GREEN)
    c.rect(x, y + h - 14 * mm, w, 14 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x + w / 2, y + h - 9 * mm, title)
    if subtitle:
        c.setFont("Helvetica", 7)
        c.drawCentredString(x + w / 2, y + h - 12.5 * mm, subtitle)
    c.setFillColor(GRAY)


def draw_bullets(c, x, y, w, lines, font_size=7, leading=9):
    """Draw bullet list; returns new y position."""
    c.setFont("Helvetica", font_size)
    for line in lines:
        if line.startswith("##"):
            c.setFont("Helvetica-Bold", font_size + 0.5)
            c.drawString(x, y, line[2:].strip())
            c.setFont("Helvetica", font_size)
            y -= leading + 1
            continue
        if line.startswith(">"):
            c.setFont("Helvetica-Oblique", font_size)
            wrapped = line[1:].strip()
            c.drawString(x + 2 * mm, y, wrapped[:90])
            c.setFont("Helvetica", font_size)
            y -= leading
            continue
        c.drawString(x + 2 * mm, y, f"• {line}")
        y -= leading
    return y


CARD1_LINES = [
    "## 1. Kes sa EI ole",
    "Ei esinda valitsust, Kaitseväge, Kaitseliitu ega erakonda.",
    "Ei anna ametlikke lubadusi. Ei ole arst/psühholoog — suuna Lisa H.",
    "## 2. Mida EI avalda (OPSEC)",
    "Teiste nimesid, aadresse, telefone ilma loata.",
    "Võrgustiku plaani, kohtumiste aegu/kohti avalikult.",
    "Kellegi diagnoose, kriise, pereteemasid.",
    "Vestluse salvestamist ilma nõusolekuta.",
    "## 3. Sotsiaalmeedia",
    "Ära kahjusta mainet. Ära suhtle tundmatutega.",
    "Infopüük → lõpeta, teata koordinaatorile.",
    "JÄLGI OPSEC REEGLEID!",
    "## 4. Millest EI räägi",
    "Mitte: sa pead uskuma - vaata allikaid",
    "Mitte: debatt triggeris - spordikommentaator (Lisa P)",
    "Mitte: hirm, viha - ausus, vastutus, pere",
    "## 5. Kes te olete?",
    "> Kodanikualgatus. Ei esinda riiki. Kontrolli voi lahku.",
]

CARD2_LINES = [
    "## Viis teemat (vali ÜKS)",
    "1. Pere rindejoon — riigikaitse algab kodus.",
    "2. Infohügieen — kes võidab, kui sa vihastad?",
    "3. Uni · liikumine · suhted · toit · ekraan.",
    "4. Abi on olemas — Eluliin 655 8088, Lisa H.",
    "5. Vastutus — sa pole katki, vajad tööriistu.",
    "## Kuidas alustada",
    "Ma ei muu midagi. Kas 5 minutit?",
    "Kas ma voisin lihtsalt kuulata?",
    "## Vestluse järjekord (Lisa P+Q)",
    "Turvalisus → spordikommentaator → valideeri → üks küsimus.",
    "## Skeptik / infonäljane",
    "Ära luba midagi. Ära avalda tundlikku. GOTWA enne edasi (Lisa Q).",
    "## Kontaktid",
    "SMS 56980062 - sonum Peegel",
    "Eluliin 655 8088 · Kriisiabi 116 123 · Ohvriabi 116 006",
]

MINI_CARD1 = [
    "EI: riik, lubadused, saladused",
    "EI: hirm, debatt triggeris",
    "OPSEC: SM, tundmatud",
    "Kodanikualgatus. Kontrolli voi lahku.",
]

MINI_CARD2 = [
    "JAH: 1 teema korraga",
    "Pere · info · 5 sõna · abi · vastutus",
    "Ma ei muu. 5 min?",
    "Peegel: SMS 56980062",
    "6558088 · 116123 · 116006",
]


def build_a6_cards_pdf():
    """Two A6 cards per A4 (cut along center) — readable reference."""
    c = canvas.Canvas(str(CARDS_PDF), pagesize=A4)
    pw, ph = A4
    card_w = pw / 2 - 5 * mm
    card_h = ph - 20 * mm
    margin = 10 * mm

    for idx, (title, lines) in enumerate(
        [
            ("TASKUKAART 1", "Mida EI tee — INFOSEC"),
            ("TASKUKAART 2", "Mida ÜTLED — teemad"),
        ]
    ):
        page = idx // 2
        col = idx % 2
        if idx > 0 and col == 0:
            c.showPage()
        x = margin + col * (card_w + 5 * mm)
        y = margin
        c.setStrokeColor(GREEN)
        c.setLineWidth(0.5)
        c.rect(x, y, card_w, card_h, fill=0, stroke=1)
        draw_card_header(c, x, y, card_w, card_h, title, 'Operatsioon Peegel | Lisa X')
        inner_y = draw_bullets(c, x + 3 * mm, y + card_h - 20 * mm, card_w - 6 * mm, lines, 7.5, 10)
        c.setFont("Helvetica-Oblique", 6)
        c.drawString(
            x + 3 * mm,
            y + 5 * mm,
            "Kirjuta see märkmikku. Prindi fail ei asenda käsitsi mõtlemist.",
        )

    # Page 2: instructions + blank notebook lines
    c.showPage()
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(GREEN)
    c.drawString(margin, ph - margin, "Märkmiku koopia — kirjuta käsitsi")
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 9)
    inst = [
        "1. Esimene nädal: Taskukaart 1 (mida EI tee).",
        "2. Teine nädal: Taskukaart 2 (mida ütled).",
        "3. Kolmas nädal: lisa üks oma lause.",
        "4. Enne iga vestlust: vaata kaarti. Üks teema korraga.",
        "5. Pärast vestlust: üks lause päevikus — mida ma kuulsin?",
    ]
    ty = ph - margin - 8 * mm
    for line in inst:
        c.drawString(margin, ty, line)
        ty -= 5 * mm
    c.setStrokeColor(colors.HexColor("#cccccc"))
    ty -= 5 * mm
    for _ in range(22):
        c.line(margin, ty, pw - margin, ty)
        ty -= 7 * mm
    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, margin / 2, 'OPERATSIOON PEEGEL | Lisa X | Unpluged-Al')

    c.save()
    print(f"Generated: {CARDS_PDF}")


def build_wallet_mini_pdf():
    """8 mini cards on A4 (85×55 mm) — rahakoti vahele."""
    c = canvas.Canvas(str(MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)

    cards_data = []
    for _ in range(2):
        cards_data.append(("TK 1 · EI", MINI_CARD1))
        cards_data.append(("TK 2 · JAH", MINI_CARD2))

    for i, (title, lines) in enumerate(cards_data[:8]):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gap_x + col * (cw + gap_x)
        y = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        draw_card_header(c, x, y, cw, ch, title, "Peegel")
        draw_bullets(c, x + 2 * mm, y + ch - 18 * mm, cw - 4 * mm, lines, 6, 7.5)

    c.setFont("Helvetica", 7)
    c.drawCentredString(
        pw / 2,
        5 * mm,
        "Lõika järgi · 85×55 mm · Soovitus: kirjuta üle märkmikku enne kasutamist",
    )
    c.save()
    print(f"Generated: {MINI_PDF}")


def build_flyer_pdf():
    """A5 flyer — LENDLEHT_PRINT.pdf"""
    doc = SimpleDocTemplate(
        str(FLYER_PDF),
        pagesize=A5,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="Operatsioon Peegel — lendleht",
    )
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="FlyerTitle",
            parent=styles["Title"],
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=GREEN,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="FlyerSub",
            parent=styles["Normal"],
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            textColor=GREEN_LIGHT,
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="FlyerBody",
            parent=styles["Normal"],
            fontSize=11,
            leading=15,
            alignment=TA_LEFT,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="FlyerCenter",
            parent=styles["Normal"],
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    story = [
        Spacer(1, 0.5 * cm),
        Paragraph('OPERATSIOON PEEGEL', styles['FlyerTitle']),
        Paragraph("Riigikaitse algab kodus", styles["FlyerSub"]),
        Spacer(1, 0.3 * cm),
        Paragraph(
            "<b>See ei ole riigi ega erakonna kampaania.</b> "
            "See on kodanikualgatus: tugev pere, kriitiline mõtlemine, vastutus.",
            styles["FlyerBody"],
        ),
        Paragraph(
            "<b>Viis sõna:</b><br/>"
            "<font size='13'><b>uni · liikumine · suhted · toit · ekraan</b></font>",
            styles["FlyerCenter"],
        ),
        Spacer(1, 0.4 * cm),
        Paragraph(
            "<b>Kui sa tunned, et oled põhjas — sa ei ole üksi:</b><br/>"
            "Eluliin <b>655 8088</b> · Kriisiabi <b>116 123</b>",
            styles["FlyerBody"],
        ),
        Spacer(1, 0.3 * cm),
        Paragraph(
            "<b>Tahad rohkem teada?</b><br/>"
            'SMS <b>56980062</b> - sonum <b>Peegel</b>',
            styles["FlyerCenter"],
        ),
        Spacer(1, 0.6 * cm),
        Paragraph(
            "<i>Avalik dokument. Jagamine lubatud.</i><br/>"
            'reneealuste-commits/Unpluged-Al | Operatsioon Peegel',
            styles["FlyerCenter"],
        ),
    ]
    doc.build(story)
    print(f"Generated: {FLYER_PDF}")


def main():
    build_a6_cards_pdf()
    build_wallet_mini_pdf()
    build_flyer_pdf()


if __name__ == "__main__":
    main()
