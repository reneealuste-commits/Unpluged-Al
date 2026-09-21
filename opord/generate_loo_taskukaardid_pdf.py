#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate print-ready story checklist and pocket cards (Lisa AD)."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GRAY = colors.HexColor("#444444")

CHECKLIST_PDF = BASE / "LOO_CHECKLIST_PRINT.pdf"
CARDS_PDF = BASE / "LOO_TASKUKAARDID_PRINT.pdf"
MINI_PDF = BASE / "LOO_TASKUKAARDID_RAHAKOTT.pdf"


def draw_card_header(c, x, y, w, h, title, subtitle=""):
    c.setFillColor(GREEN)
    c.rect(x, y + h - 14 * mm, w, 14 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + w / 2, y + h - 9 * mm, title)
    if subtitle:
        c.setFont("Helvetica", 7)
        c.drawCentredString(x + w / 2, y + h - 12.5 * mm, subtitle)
    c.setFillColor(GRAY)


def draw_bullets(c, x, y, lines, font_size=7.5, leading=10):
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
            c.drawString(x + 2 * mm, y, line[1:].strip()[:95])
            c.setFont("Helvetica", font_size)
            y -= leading
            continue
        c.drawString(x + 2 * mm, y, "- " + line)
        y -= leading
    return y


CHECKLIST_LINES = [
    "## Konversiooniloo checklist - 7 sammu (Lisa AD)",
    "1. KOHAL - uks koht (nt ma kondisin...)",
    "2. AEG - uks aeg (eile / kolm aastat tagasi)",
    "3. INIMENE - uks (voi mina)",
    "4. ENNE - uks lause: mida ma tundsin",
    "5. HELK - uks hetk, mitte kogu elulugu",
    "6. TUNNE - kehas (to heal is to feel)",
    "7. SILD - uks kusimus: Kas see kolab tuttavalt?",
    "",
    "## Enne vestlust",
    "[ ] Uks teema valitud (Lisa X)",
    "[ ] OPSEC - ei avalda saladusi",
    "[ ] Valmistan uhe lause vastupanu jaoks (TK 3)",
    "",
    "## Parast vestlust",
    "[ ] Uks lause paevikus - mida ma kuulsin?",
    "[ ] Kas keegi vajab Lisa H numbreid?",
    "",
    "## Taida (uks vestlus)",
    "KUUPAEV: _______________  TEEMA: _______________",
    "KOHAL:   _________________________________________",
    "AEG:     _________________________________________",
    "INIMENE: _________________________________________",
    "ENNE:    _________________________________________",
    "HELK:    _________________________________________",
    "TUNNE:   _________________________________________",
    "SILD:    Kas ____________________________________?",
]

CARD1_LINES = [
    "## Loo skeem - 7 sammu",
    "1. KOHAL - uks koht",
    "2. AEG - uks aeg",
    "3. INIMENE - uks",
    "4. ENNE - uks lause tunne",
    "5. HELK - uks hetk",
    "6. TUNNE - kehas",
    "7. SILD - Kas see kolab tuttavalt?",
    "## Reegel",
    "Uks vestlus = uks lugu = uks teema (Lisa X).",
    "Lugu on checklist - mitte improv.",
]

CARD2_LINES = [
    "## Kuidas alustada",
    "Ma ei muu midagi. Kas uks hetk?",
    "Mul juhtus uks asi - kas relevant?",
    "Ma kuulsin sind. Uks lugu - sobib?",
    "Kas sa oled kunagi... + uks kusimus",
    "## Parast lugu",
    "Vaikus. Uks kusimus. Mitte kolm opetust.",
]

CARD3_LINES = [
    "## Kui keegi...",
    "Kes sa oled? -> Kodanik. Kontrolli voi lahku.",
    "Sa muud? -> Tasuta. Vota voi jata.",
    "Raagi otse -> Uks lause + kusimus.",
    "Pole aega -> 30 sek voi numbrid (Lisa H).",
    "Vandenou? -> Kontrolli allikaid. Ma ei sunni.",
    "Eksid? -> Mis osa ei klapi? (Lisa P)",
    "Trigger? -> Spordikommentaator. Anna ruumi.",
    "Assitaja? -> Ei voitlusse. Kas tahad kuulda?",
    "Liituda -> SMS 56980062 Peegel",
]

MINI1 = ["7: KOHAL AEG INIMENE", "ENNE HELK TUNNE SILD", "1 lugu = 1 teema"]
MINI2 = ["Alusta: Ma ei muu. 1 hetk?", "Lopp: 1 kusimus", "Vaikus parast lugu"]
MINI3 = ["EI debatt", "EI muuk", "JAH valideeri Lisa P", "Peegel SMS 56980062"]


def build_checklist_pdf():
    c = canvas.Canvas(str(CHECKLIST_PDF), pagesize=A4)
    pw, ph = A4
    margin = 15 * mm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(GREEN)
    c.drawString(margin, ph - margin, "OPERATSIOON PEEGEL - Konversiooniloo checklist")
    c.setFont("Helvetica", 9)
    c.setFillColor(GRAY)
    c.drawString(margin, ph - margin - 6 * mm, "Lisa AD | Inimesed moistavad maailma labi lugude")
    draw_bullets(c, margin, ph - margin - 14 * mm, CHECKLIST_LINES, 9, 12)
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(pw / 2, margin, "Prindi - taida enne vestlust - kirjuta oma lugu markmikku")
    c.save()
    print(f"Generated: {CHECKLIST_PDF}")


def build_cards_pdf():
    c = canvas.Canvas(str(CARDS_PDF), pagesize=A4)
    pw, ph = A4
    card_w = pw / 2 - 12 * mm
    card_h = (ph - 30 * mm) / 2
    margin = 10 * mm

    cards = [
        ("TK 1 - LOO SKEEM", CARD1_LINES),
        ("TK 2 - ALUSTA", CARD2_LINES),
        ("TK 3 - KUI KEEGI", CARD3_LINES),
    ]

    positions = [(0, 1), (1, 1), (0, 0)]
    for idx, (title, lines) in enumerate(cards):
        col, row = positions[idx]
        x = margin + col * (card_w + 8 * mm)
        y = margin + row * (card_h + 8 * mm)
        c.setStrokeColor(GREEN)
        c.rect(x, y, card_w, card_h, fill=0, stroke=1)
        draw_card_header(c, x, y, card_w, card_h, title, "Lisa AD | Lood")
        draw_bullets(c, x + 3 * mm, y + card_h - 20 * mm, lines)

    x = margin + card_w + 8 * mm
    y = margin
    c.setStrokeColor(GREEN)
    c.rect(x, y, card_w, card_h, fill=0, stroke=1)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(GREEN)
    c.drawString(x + 4 * mm, y + card_h - 8 * mm, "Markmikku - kirjuta oma lugu")
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    hints = [
        "Naide: kond + assitaja - ara debatti, uks kusimus.",
        "Epp: padjuke telgis - inimesed maletavad hetke.",
        "Renee: pohi -> abi - luhike, aus.",
        "",
        "Kirjuta kasitsi. Prindi fail ei asenda motlemist.",
    ]
    ty = y + card_h - 16 * mm
    for h in hints:
        c.drawString(x + 4 * mm, ty, h)
        ty -= 5 * mm
    c.setStrokeColor(colors.HexColor("#cccccc"))
    for _ in range(10):
        c.line(x + 4 * mm, ty, x + card_w - 4 * mm, ty)
        ty -= 7 * mm

    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "LOO_TASKUKAARDID_PRINT.pdf | Lisa AD")
    c.save()
    print(f"Generated: {CARDS_PDF}")


def build_mini_pdf():
    c = canvas.Canvas(str(MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)

    data = []
    for _ in range(2):
        data.extend([("LOO 1", MINI1), ("LOO 2", MINI2), ("LOO 3", MINI3)])

    for i, (title, lines) in enumerate(data[:6]):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gap_x + col * (cw + gap_x)
        y = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        draw_card_header(c, x, y, cw, ch, title, "Peegel AD")
        draw_bullets(c, x + 2 * mm, y + ch - 18 * mm, lines, 6, 7.5)

    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "85x55 mm - Lisa AD - Loo checklist")
    c.save()
    print(f"Generated: {MINI_PDF}")


def main():
    build_checklist_pdf()
    build_cards_pdf()
    build_mini_pdf()


if __name__ == "__main__":
    main()
