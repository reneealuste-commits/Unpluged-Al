#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 1-1 conversation pocket card for network members (Lisa BE)."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GRAY = colors.HexColor("#444444")
PDF = BASE / "1_1_VESTLUS_TASKUKAART.pdf"


def draw_header(c, x, y, w, h, title, subtitle=""):
    c.setFillColor(GREEN)
    c.rect(x, y + h - 14 * mm, w, 14 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x + w / 2, y + h - 9 * mm, title)
    if subtitle:
        c.setFont("Helvetica", 7)
        c.drawCentredString(x + w / 2, y + h - 12.5 * mm, subtitle)
    c.setFillColor(GRAY)


def draw_lines(c, x, y, lines, font_size=7.5, leading=9.5):
    c.setFont("Helvetica", font_size)
    for line in lines:
        if line.startswith("##"):
            c.setFont("Helvetica-Bold", font_size + 0.5)
            c.drawString(x, y, line[2:].strip())
            c.setFont("Helvetica", font_size)
            y -= leading + 1
            continue
        c.drawString(x + 2 * mm, y, f"- {line}")
        y -= leading
    return y


CARD_LINES = [
    "## Nadal (80% vorgustiku toost)",
    "1x sugav 1-1 (30-60 min, Lisa P 5 sammu)",
    "3x luhikontakt (5-15 min)",
    "## Iga paev",
    "GOTWA enne kontakti (Lisa Q)",
    "1 spordikommentaatori lause",
    "## Vestluse jarjekord",
    "turvalisus -> naen/kuulen -> valideeri",
    "ausus -> valik -> 1 konkreetne samm",
    "## Parast 1-1",
    "uks lause logi: mida kuulsin?",
    "jargmine aeg kirja (kata ja liigu)",
    "## Kuu",
    "mis 1-1 samm tootas? mis mitte?",
    "EI SUNNI - demonstreerin, parandan protsessi",
]

MINI_LINES = [
    "1x nadalas: sugav 1-1",
    "3x nadalas: luhikontakt",
    "iga paev: GOTWA + 1 lause",
    "P: turvalisus->naen->valideeri->ausus->valik",
    "parast: logi + jargmine aeg",
    "Lisa BE | vorgustik",
]


def main():
    c = canvas.Canvas(str(PDF), pagesize=A4)
    pw, ph = A4
    margin = 10 * mm

    card_w = pw / 2 - 5 * mm
    card_h = ph - 20 * mm
    x, y = margin, margin
    c.setStrokeColor(GREEN)
    c.rect(x, y, card_w, card_h, fill=0, stroke=1)
    draw_header(c, x, y, card_w, card_h, "1-1 VESTLUS", "Lisa BE | vorgustikus")
    draw_lines(c, x + 3 * mm, y + card_h - 20 * mm, CARD_LINES, 8, 10)
    c.setFont("Helvetica-Oblique", 6)
    c.drawString(x + 3 * mm, y + 5 * mm, "Tekst: lisad/lisa-be-1-1-vestlus-vorgustikus.md")

    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)
    c.showPage()
    for i in range(8):
        col = i % cols
        row = rows - 1 - (i // cols)
        mx = gap_x + col * (cw + gap_x)
        my = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(mx, my, cw, ch, fill=0, stroke=1)
        draw_header(c, mx, my, cw, ch, "1-1", "Lisa BE")
        draw_lines(c, mx + 2 * mm, my + ch - 17 * mm, MINI_LINES, 6, 7.2)

    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "Loika 85x55 mm rahakotti | Unpluged-Al")
    c.save()
    print(f"Generated: {PDF}")


if __name__ == "__main__":
    main()
