#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate NVC-style citizen communication pocket cards (Lisa BD)."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GRAY = colors.HexColor("#444444")

CARDS_PDF = BASE / "NVC_TASKUKAARDID_PRINT.pdf"
MINI_PDF = BASE / "NVC_TASKUKAARDID_RAHAKOTT.pdf"


def draw_card_header(c, x, y, w, h, title, subtitle=""):
    c.setFillColor(GREEN)
    c.rect(x, y + h - 14 * mm, w, 14 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + w / 2, y + h - 9 * mm, title)
    if subtitle:
        c.setFont("Helvetica", 6.5)
        c.drawCentredString(x + w / 2, y + h - 12.5 * mm, subtitle)
    c.setFillColor(GRAY)


def draw_bullets(c, x, y, w, lines, font_size=6.8, leading=8.5):
    c.setFont("Helvetica", font_size)
    for line in lines:
        if line.startswith("##"):
            c.setFont("Helvetica-Bold", font_size + 0.3)
            c.drawString(x, y, line[2:].strip())
            c.setFont("Helvetica", font_size)
            y -= leading + 1
            continue
        if line.startswith(">"):
            c.setFont("Helvetica-Oblique", font_size)
            c.drawString(x + 1.5 * mm, y, line[1:].strip()[:95])
            c.setFont("Helvetica", font_size)
            y -= leading
            continue
        text = line if line.startswith("-") else f"- {line}"
        c.drawString(x + 1.5 * mm, y, text[:98])
        y -= leading
    return y


CARD1_LINES = [
    "## 0 Turvalisus - enne OFNR",
    "Peatuge. Uks hingetomme. Sa ei pea praegu midagi otsustama.",
    "## O Tahelepanek (spordikommentaator)",
    "Fakt, mitte hinnang: Ma naen, et pilk on telefonil.",
    "Mitte: Sa ei kuula! / Sa oled laisk!",
    "## F Tunne (mina-keeles)",
    "Ma tunnen... - mitte sina teed mulle...",
    "Naited: vasinud, pettunud, arev, uksildane, rahulik",
    "## N Vajadus (inimlik)",
    "ruum, kuulamine, ausus, puhkus, selgus, lahedus, lugupidamine",
    "## R Palve (mitte kask)",
    "Kas sa saaksid 20 min panna telefoni kooki?",
    "Kas ma voin homme kell 10 helistada? (kata ja liigu)",
    "## Lisa P jarjekord",
    "turvalisus -> tahelepanek -> valideeri -> ausus -> valik",
]

CARD2_LINES = [
    "## Partner",
    "Ma tunnen uksildust. Mul on vaja 10 min ausat vestlust.",
    "Stop. Ma vajan pausi. Tulen tagasi 20 min parast.",
    "## Lapsed",
    "Perede aeg: kes viib telefoni kooki? Voitja valib muusika.",
    "Ma naen, et sul on raske. Ma olen siin.",
    "## Kriis kodus - kata ja liigu",
    "Homme kell 10 helistan. Ara oota palvet.",
    "655 8088, 116 123, 112",
    "## Vanemad",
    "Teietamine. Kas Teil on hetk aega?",
]

CARD3_LINES = [
    "## Too / kolleeg",
    "Mul on vaja prioriteeti - mis uks asi on tana oluline?",
    "Too parast 17:00 ei ole OK - jatkame homme?",
    "Enne uue kontakti: GOTWA (Lisa Q)",
    "## Pood / voeras",
    "Ma naen teist toodet. Kas saaksime vahetada?",
    "Avalik tuli: ara vota pooli. Lahku, kui vaja.",
    "## Sobr",
    "Ma armastan sind, aga see lause kortsutas kulmu.",
    "## Skeptik",
    "Ma ei muu midagi. Kas 5 minutit? Valideeri enne vastamist.",
]

CARD4_LINES = [
    "## Kui SINA oled triggeris",
    "Spordikommentaator -> 10 min paus -> ara kirjuta kohe",
    "## Piir",
    "Stop. Ma ei jatka nii. Ausalt voi lopetame tana.",
    "See on minu piir. Ma ei vasta sellele praegu.",
    "## Keegi karjub",
    "Ara karju vastu. Anna ruumi. Vaikus.",
    "## Hadaolukord",
    "Vaikus. Poora ara. Lahku.",
    "112, 655 8088, 116 123, 116 006",
]

MINI_OFNR = [
    "OFNR: Tahelepanek -> Tunne -> Vajadus -> Palve",
    "ENNE: turvalisus, hingetomme",
    "EI: hinnang, suudistus, sa pead",
    "JAH: ma naen, ma tunnen, kas sa saaksid...",
]

MINI_HAAL = [
    "HAAL (Lisa Q):",
    "soe | rahulik | selge | vaikus",
    "ABI: kata ja liigu - samm + aeg",
    "GOTWA enne valjumist",
    "6558088, 116123, 112",
]

MINI_KODU = [
    "KODUS:",
    "10 min ausalt, 17:00 nupp (BC)",
    "Perede aeg ilma nutita",
    "Ara oota palvet - helista homme",
]

MINI_VALJAS = [
    "VALJAS:",
    "Teietamine voorage",
    "Uks teema korraga",
    "Skeptik: kontrolli allikaid",
    "Lisa AT kui kinni",
]


def build_a4_cards_pdf():
    c = canvas.Canvas(str(CARDS_PDF), pagesize=A4)
    pw, ph = A4
    card_w = pw / 2 - 5 * mm
    card_h = ph / 2 - 8 * mm
    margin = 8 * mm

    cards = [
        ("KAART 1", "OFNR - neli sammu", CARD1_LINES),
        ("KAART 2", "Kodus - pere", CARD2_LINES),
        ("KAART 3", "Valjas - too, pood", CARD3_LINES),
        ("KAART 4", "Raske hetk - piir, hada", CARD4_LINES),
    ]

    for idx, (title, subtitle, lines) in enumerate(cards):
        col = idx % 2
        row = (idx % 4) // 2
        if idx > 0 and idx % 2 == 0:
            c.showPage()
        x = margin + col * (card_w + 4 * mm)
        y = ph - margin - (row + 1) * card_h - row * 4 * mm
        c.setStrokeColor(GREEN)
        c.setLineWidth(0.5)
        c.rect(x, y, card_w, card_h, fill=0, stroke=1)
        draw_card_header(c, x, y, card_w, card_h, title, f"NVC kodanik | {subtitle}")
        draw_bullets(c, x + 2.5 * mm, y + card_h - 18 * mm, card_w - 5 * mm, lines, 6.8, 8.2)
        c.setFont("Helvetica-Oblique", 5.5)
        c.drawString(x + 2.5 * mm, y + 3 * mm, "Lisa BD | Alus Lisa Q | Kirjuta markmikku")

    c.showPage()
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(GREEN)
    c.drawString(margin, ph - margin, "Lisa BD - kuidas kasutada")
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 9)
    inst = [
        "1. Nadal 1: Kaart 1 (OFNR) - uks lause paevas.",
        "2. Nadal 2: Kaart 2 voi 3 - vali uks olukord.",
        "3. Nadal 3: Kaart 4 - tea piire ja hada numbrid.",
        "4. Enne rasket vestlust: vaata kaarti.",
        "5. Taielik tekst: lisad/lisa-bd-nvc-taskukaardid-kodanikule.md",
    ]
    ty = ph - margin - 10 * mm
    for line in inst:
        c.drawString(margin, ty, line)
        ty -= 5.5 * mm

    c.save()
    print(f"Generated: {CARDS_PDF}")


def build_wallet_mini_pdf():
    c = canvas.Canvas(str(MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)

    mini_sets = [
        ("OFNR", MINI_OFNR),
        ("HAAL", MINI_HAAL),
        ("KODUS", MINI_KODU),
        ("VALJAS", MINI_VALJAS),
    ]
    cards_data = []
    for _ in range(2):
        cards_data.extend(mini_sets)

    for i, (title, lines) in enumerate(cards_data[:8]):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gap_x + col * (cw + gap_x)
        y = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        draw_card_header(c, x, y, cw, ch, title, "Lisa BD | NVC")
        draw_bullets(c, x + 2 * mm, y + ch - 17 * mm, cw - 4 * mm, lines, 5.8, 7.2)

    c.setFont("Helvetica", 7)
    c.drawCentredString(
        pw / 2,
        5 * mm,
        "Loika 85x55 mm | Alus: Lisa Q side eeskirjad | Unpluged-Al",
    )
    c.save()
    print(f"Generated: {MINI_PDF}")


def main():
    build_a4_cards_pdf()
    build_wallet_mini_pdf()


if __name__ == "__main__":
    main()
