#!/usr/bin/env python3
"""Roheline vaikuse uuring — PDF lasteaedadele (lihtne keel, 5-aastasele)."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
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
from reportlab.graphics.shapes import Circle, Ellipse, Group, Rect, String
from reportlab.graphics import renderPDF
from reportlab.platypus import Flowable

OUTPUT = "/workspace/roheline-vaikuse-uuring-lasteaedadele.pdf"

# Rohelised toonid — rahulik, looduslik
GREEN_DARK = colors.HexColor("#2E7D32")
GREEN_MID = colors.HexColor("#66BB6A")
GREEN_LIGHT = colors.HexColor("#E8F5E9")
GREEN_SOFT = colors.HexColor("#C8E6C9")
SKY = colors.HexColor("#E3F2FD")
DARK = colors.HexColor("#37474F")
GRAY = colors.HexColor("#78909C")
WHITE = colors.white


class GreenBanner(Flowable):
    """Pehme roheline taust plokk."""

    def __init__(self, width, height, text="", fontsize=14):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.text = text
        self.fontsize = fontsize

    def draw(self):
        c = self.canv
        c.setFillColor(GREEN_LIGHT)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        c.setFillColor(GREEN_DARK)
        c.setFont("Helvetica-Bold", self.fontsize)
        c.drawCentredString(self.width / 2, self.height / 2 - 5, self.text)


class LeafDecoration(Flowable):
    """Lihtne roheline lehe/dekoratiivne element."""

    def __init__(self, width=170 * mm, height=25 * mm):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        # Pehmed ringid — nagu pärja lehed
        for x, r, g in [(20, 18, GREEN_SOFT), (50, 12, GREEN_MID), (140, 15, GREEN_SOFT), (165, 10, GREEN_LIGHT)]:
            c.setFillColor(g)
            c.circle(x, 12, r, fill=1, stroke=0)
        c.setFillColor(GREEN_MID)
        c.setFont("Helvetica-Oblique", 9)
        c.drawString(60, 8, "Rahulik hetk — nagu roheline aas")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title", parent=base["Heading1"], fontSize=22, textColor=GREEN_DARK,
            spaceAfter=8, fontName="Helvetica-Bold", alignment=TA_CENTER,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle", parent=base["Normal"], fontSize=11, textColor=GRAY,
            spaceAfter=12, alignment=TA_CENTER,
        ),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading1"], fontSize=15, textColor=GREEN_DARK,
            spaceBefore=12, spaceAfter=8, fontName="Helvetica-Bold",
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontSize=12, textColor=GREEN_DARK,
            spaceBefore=8, spaceAfter=5, fontName="Helvetica-Bold",
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontSize=11, leading=16,
            textColor=DARK, alignment=TA_JUSTIFY,
        ),
        "simple": ParagraphStyle(
            "Simple", parent=base["Normal"], fontSize=12, leading=18,
            textColor=DARK, fontName="Helvetica", alignment=TA_JUSTIFY,
        ),
        "quote": ParagraphStyle(
            "Quote", parent=base["Normal"], fontSize=12, leading=18,
            textColor=GREEN_DARK, fontName="Helvetica-Oblique",
            leftIndent=15, rightIndent=15, alignment=TA_CENTER,
        ),
        "step": ParagraphStyle(
            "Step", parent=base["Normal"], fontSize=11, leading=16,
            leftIndent=10, textColor=DARK,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["Normal"], fontSize=8, leading=10, textColor=GRAY,
        ),
        "box": ParagraphStyle(
            "Box", parent=base["Normal"], fontSize=11, leading=15,
            textColor=DARK, backColor=GREEN_LIGHT, borderPadding=8,
        ),
    }


def hr(story):
    story.append(HRFlowable(width="100%", thickness=1, color=GREEN_MID, spaceAfter=8, spaceBefore=4))


def green_box(story, text, s):
    t = Table([[Paragraph(text, s["body"])]], colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_LIGHT),
        ("BOX", (0, 0), (-1, -1), 1, GREEN_MID),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))


def cover(story, s):
    story.append(Spacer(1, 15 * mm))
    story.append(LeafDecoration())
    story.append(Spacer(1, 8))
    story.append(Paragraph("ROHELINE VAIKUSE HETK", s["title"]))
    story.append(Paragraph("Lihtne uuring lasteaedadele", s["subtitle"]))
    story.append(Spacer(1, 6))
    story.append(GreenBanner(170 * mm, 12 * mm, "Mida üks laps meile õpetas — ja mida SINA saad proovida", 11))
    story.append(Spacer(1, 14))
    story.append(
        Paragraph(
            "See lugu on kirjutatud <b>nagu 5-aastasele</b> — et ka laps saaks aru. "
            "Aga ka täiskasvanu (õpetaja, vanem) saab seda kasutada.",
            s["simple"],
        )
    )
    story.append(Spacer(1, 10))
    meta = [
        ["Autor:", "Renee Aluste / Unpluged-Al"],
        ["Versioon:", "1.0 · august 2026"],
        ["Kestus:", "5–10 minutit ühe lapsega"],
        ["Eesmärk:", "Rahulik hetk — mitte ravi"],
    ]
    t = Table(meta, colWidths=[35 * mm, 135 * mm])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TEXTCOLOR", (0, 0), (0, -1), GREEN_DARK),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 16))
    green_box(
        story,
        "<b>Oluline:</b> See ei ole arstiabi ega EMDR-ravi. See on lihtne, turvaline "
        "rahustav harjutus — nagu pikk südametukk enne uinakut. Kui laps on väga "
        "hädas, pöördu spetsialisti poole.",
        s,
    )
    story.append(PageBreak())


def lugu(story, s):
    story.append(Paragraph("1. LUGU — ÜKS LAPS", s["h1"]))
    hr(story)
    story.append(LeafDecoration())
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "Kujutle väikest last. Ta on mõnikord nii elevil, et ei jaksa istuda. "
            "Või on ta kukkunud ja nutab. Või lihtsalt vajab paike.",
            s["simple"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Mis aitas?", s["h2"]))
    for line in [
        "<b>Roheline kaart</b> — kui õpetaja võttis rohelise paberi, teadsid kõik: nüüd on vaikne hetk.",
        "<b>5 minutit ühe lapsega</b> — mitte kiirustades, vaid ainult tema jaoks.",
        "<b>Hingamine</b> — nagu puhur ookeani — sisse… välja…",
        "<b>Kerge koputus</b> — õlgadele vasak-parem (nagu EMDR-stiilis rütm, aga väga õrnalt).",
        "<b>Turvaline koht</b> — 'Kujutle, et sa oled rohelisel aasal. Päike soojendab. Sa oled turvaliselt.'",
    ]:
        story.append(Paragraph(f"- {line}", s["step"]))
    story.append(Spacer(1, 10))
    green_box(
        story,
        "<b>Mis muutus?</b> Laps rahunes 3–5 minutiga. Ei pidanud rääkima, miks ta nuttis. "
        "Piisas, et keegi oli temaga — rahulikult, ilma kiirustamata.",
        s,
    )
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "<i>See lugu põhineb ühe pere kogemusel. Iga laps on erinev. "
            "Proovi ja vaata, mis sinu rühmas toimib.</i>",
            s["small"],
        )
    )
    story.append(PageBreak())


def juhend(story, s):
    story.append(Paragraph("2. JUHEND — 5 SAMMU", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "Nii nagu 5-aastasele selgitaksid. Loe aeglaselt. Vaata last silma, aga ära sunni.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))

    steps = [
        ("SAMM 1 — Roheline märk", "Võta roheline paber või kaart. Ütle: 'Nüüd on meie vaikne hetk. Sa oled turvaliselt.'"),
        ("SAMM 2 — Hinga", "'Hingame nagu meri. Sisse — 1, 2, 3, 4. Välja — 1, 2, 3, 4, 5, 6.' Kolm korda."),
        ("SAMM 3 — Keha", "'Tunne jalad põrandas. Tunne käed. Sa oled siin. Sa oled OK.'"),
        ("SAMM 4 — Koputus (valikuline)", "Koputa õrnalt lapse õlgadele: vasak… parem… vasak… parem… Aeglaselt. Nagu laulurütm."),
        ("SAMM 5 — Turvaline koht", "'Kujutle rohelist aeda. Päike. Puu. Sa võid seal olla nii kaua, kui tahad.'"),
        ("LÕPP — Tagasi", "'Loeme 5, 4, 3, 2, 1. Ava silmad. Kuidas sa end tunned?'"),
    ]
    for i, (head, text) in enumerate(steps, 1):
        story.append(Paragraph(head, s["h2"]))
        story.append(Paragraph(text, s["simple"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())


def turvalisus(story, s):
    story.append(Paragraph("3. TURVALISUS — MILLAL STOP", s["h1"]))
    hr(story)
    stop_items = [
        "Laps ütleb STOP või tahab minna ära → lase tal minna.",
        "Laps hakkab nutma rohkem (distress kasvab) → lõpeta, kallista, vesi.",
        "Laps on väga hirmul, karjub, lööb → mitte harjutus, vaid tähelepanu ja vajadusel abi.",
        "Trauma, väärkohtlemine, kriis → pöördu spetsialisti poole (lastekaitse, psühholoog).",
    ]
    for item in stop_items:
        story.append(Paragraph(f"STOP: {item}", s["step"]))
    story.append(Spacer(1, 10))
    green_box(
        story,
        "<b>Reegel:</b> Laps juhib. Sina oled kaaslane, mitte arst. "
        "Kui midagi tundub vale, lõpeta kohe.",
        s,
    )
    story.append(Spacer(1, 12))
    story.append(Paragraph("4. MIKS LASTEAED?", s["h1"]))
    hr(story)
    for line in [
        "Lasteaias on aega — <b>üks laps korraga</b>, mitte terve klass korraga.",
        "Pärast konflikti, enne uinakut, enne uut mängu — lühike hetk aitab.",
        "Õpetaja ei pea olema terapeut — piisab rahulikust häälest ja 5 minutist.",
        "Saad proovida ka <b>kodus oma lastega</b> — sama sammude järjekord.",
    ]:
        story.append(Paragraph(f"• {line}", s["step"]))
    story.append(PageBreak())


def kodus(story, s):
    story.append(Paragraph("5. PROOVI KODUS", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "Vanemad saavad seda sama teha. Õhtul enne und. Pärast tülitsemist. "
            "Kui laps on üle elevil.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Lihtne logi (valikuline)", s["h2"]))
    log = [
        ["Kuupäev", "Laps", "Enne (1–10)", "Pärast (1–10)", "Mis muutus?"],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
    ]
    t = Table(log, colWidths=[25 * mm, 30 * mm, 28 * mm, 28 * mm, 59 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOX", (0, 0), (-1, -1), 0.5, GREEN_MID),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, GREEN_SOFT),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 14))
    story.append(Paragraph("6. KOKKUVÕTE", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "'Roheline vaikuse hetk' on nagu väike aed lapse südames. "
            "Sa ei pea seda igapäev tegema. Proovi korra nädalas. Vaata, mis toimib.",
            s["quote"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Kui soovite seda oma lasteaias proovida või jagada tagasisidet, "
            "võtke ühendust: [TÄIDA: e-post, telefon]",
            s["body"],
        )
    )
    story.append(Spacer(1, 16))
    story.append(LeafDecoration())
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "Unpluged-Al · Roheline vaikuse uuring · v1.0 · august 2026 · "
            "Hariduslik materjal — ei asenda spetsialisti",
            s["small"],
        )
    )


def build():
    s = styles()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title="Roheline vaikuse hetk — uuring lasteaedadele",
        author="Renee Aluste",
    )
    story = []
    cover(story, s)
    lugu(story, s)
    juhend(story, s)
    turvalisus(story, s)
    kodus(story, s)
    doc.build(story)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
