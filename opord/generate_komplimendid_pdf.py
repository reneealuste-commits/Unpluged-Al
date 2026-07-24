#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate print-ready compliment SOP cards (Lisa AE)."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GRAY = colors.HexColor("#444444")

SOP_PDF = BASE / "KOMPLIMENT_SOP_PRINT.pdf"
MINI_PDF = BASE / "KOMPLIMENT_TASKUKAARDID_RAHAKOTT.pdf"


def draw_header(c, x, y, w, h, title, subtitle=""):
    c.setFillColor(GREEN)
    c.rect(x, y + h - 12 * mm, w, 12 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(x + w / 2, y + h - 8 * mm, title)
    if subtitle:
        c.setFont("Helvetica", 6)
        c.drawCentredString(x + w / 2, y + h - 10.5 * mm, subtitle)
    c.setFillColor(GRAY)


def draw_lines(c, x, y, lines, size=7, lead=9):
    c.setFont("Helvetica", size)
    for line in lines:
        if line.startswith("##"):
            c.setFont("Helvetica-Bold", size + 0.5)
            c.drawString(x, y, line[2:].strip())
            c.setFont("Helvetica", size)
            y -= lead + 1
            continue
        c.drawString(x + 1 * mm, y, line[:100])
        y -= lead
    return y


SOP_LINES = [
    "## Lisa AE - Komplimendi SOP (1 lause)",
    "1. Konkreetne (mitte 'sa oled ilus')",
    "2. Mitte-seksuaalne (riietus, kond, energia)",
    "3. Uks lause - lopeta",
    "4. Avalik kontekst, paevane",
    "5. Ei oota numbrit ega vestlust",
    "## Naiteid (vali uks)",
    "Mulle meeldib su [detail] - sobib sulle.",
    "Markasin su kindla kondi - enesekindlalt.",
    "Nagen, et sa hoolid endast - tore.",
    "Ilus valik - see kombinatsioon on stiilne.",
    "Head vanemad on naha - aitah.",
    "## EI utle",
    "sexy/hot, kehaosad, number, 'naerata'",
    "## Oo blokk 0",
    "Kodus 'minu mees' omamine - lahenda enne (Lisa AC)",
    "## Oo kodus",
    "Niiskus 40-60%, ventileeri 10 min, ripu 90 sek (Lisa AB)",
]

MINI1 = ["1 lause. Konkreetne.", "Mitte-seksuaalne.", "Lopeta. Mine edasi."]
MINI2 = ["Oo: niiskus 40-60%", "Vent 10 min", "Rippu 90 sek"]
MINI3 = ["EI: sexy, keha, number", "JAH: stiil, kond, hool", "Lisa AE | Peegel"]


def build_sop_pdf():
    c = canvas.Canvas(str(SOP_PDF), pagesize=A4)
    pw, ph = A4
    m = 14 * mm
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(GREEN)
    c.drawString(m, ph - m, "OPERATSIOON PEEGEL - Komplimendi SOP (Lisa AE)")
    c.setFont("Helvetica", 8)
    c.setFillColor(GRAY)
    c.drawString(m, ph - m - 5 * mm, "Ohk kodus + liikumine + uks mitte-seksuaalne kompliment vo?o?rale")
    draw_lines(c, m, ph - m - 12 * mm, SOP_LINES, 8, 10)
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(pw / 2, m, "Tais juhend: lisa-ae-ohk-liikumine-ja-komplimendid.md")
    c.save()
    print(f"Generated: {SOP_PDF}")


def build_mini_pdf():
    c = canvas.Canvas(str(MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gx = (pw - cols * cw) / (cols + 1)
    gy = (ph - rows * ch) / (rows + 1)
    data = []
    for _ in range(2):
        data.extend([("KOMP 1", MINI1), ("KOMP 2", MINI2), ("KOMP 3", MINI3)])
    for i, (title, lines) in enumerate(data[:6]):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gx + col * (cw + gx)
        y = gy + row * (ch + gy)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        draw_header(c, x, y, cw, ch, title, "Lisa AE")
        draw_lines(c, x + 2 * mm, y + ch - 16 * mm, lines, 6, 7.5)
    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "85x55 mm - Komplimendi taskukaardid")
    c.save()
    print(f"Generated: {MINI_PDF}")


def main():
    build_sop_pdf()
    build_mini_pdf()


if __name__ == "__main__":
    main()
