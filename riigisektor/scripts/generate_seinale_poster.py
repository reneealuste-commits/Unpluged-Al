#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate single-page wall poster PDF (A4 + A3) for riigisektor respect guide."""

import subprocess
from pathlib import Path

from fpdf import FPDF

DIR = Path(__file__).resolve().parent.parent
HTML = DIR / "seinale-austus-juhend.html"
PDF_A4 = DIR / "seinale-austus-juhend.pdf"
PDF_A3 = DIR / "seinale-austus-juhend-a3.pdf"

NAVY = (26, 58, 92)
BLUE = (45, 106, 159)
GRAY = (74, 98, 120)
RED = (139, 26, 26)
WHITE = (255, 255, 255)
LIGHT = (238, 244, 250)


class PosterPDF(FPDF):
    def __init__(self, fmt="A4"):
        super().__init__(orientation="P", unit="mm", format=fmt)
        self.fmt = fmt
        self.set_auto_page_break(auto=False)
        self.add_page()
        root = Path("/usr/share/fonts/truetype/dejavu")
        self.add_font("DejaVu", "", str(root / "DejaVuSans.ttf"))
        self.add_font("DejaVu", "B", str(root / "DejaVuSans-Bold.ttf"))
        self.scale = 1.35 if fmt == "A3" else 1.0

    def s(self, mm):
        return mm * self.scale

    def set_font_s(self, style="", size=10):
        self.set_font("DejaVu", style, size * self.scale)

    def header_block(self):
        y0 = self.s(10)
        self.set_y(y0)
        self.set_font_s("B", 9)
        self.set_text_color(*GRAY)
        self.cell(0, self.s(5), "TALLINNA TEHNOLOOGIAKOLLEDZ Techno TLN  |  RIIGISEKTOR", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font_s("B", 22)
        self.set_text_color(*NAVY)
        self.cell(0, self.s(10), "Austus ja lugupidav suhtlus", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font_s("", 10)
        self.set_text_color(*GRAY)
        self.cell(0, self.s(5), "Seinale riputatav juhend  |  Selgus ja turvalisus kogu kooliperele", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*NAVY)
        self.set_line_width(self.s(0.8))
        y = self.get_y() + self.s(2)
        self.line(self.s(12), y, self.w - self.s(12), y)
        self.ln(self.s(4))

    def values_row(self):
        labels = ["Kvaliteet", "Kattesaadavus", "Hoolivus"]
        labels[1] = "K\u00e4ttesaadavus"
        gap = self.s(4)
        w = (self.w - self.s(24) - 2 * gap) / 3
        x = self.s(12)
        y = self.get_y()
        for label in labels:
            self.set_fill_color(*NAVY)
            self.set_text_color(*WHITE)
            self.set_font_s("B", 10)
            self.set_xy(x, y)
            self.cell(w, self.s(8), label, align="C", fill=True)
            x += w + gap
        self.ln(self.s(10))

    def hero_chain(self):
        y = self.get_y()
        h = self.s(18)
        self.set_fill_color(*LIGHT)
        self.set_draw_color(*NAVY)
        self.set_line_width(self.s(0.5))
        self.rect(self.s(12), y, self.w - self.s(24), h, style="DF")
        self.set_xy(self.s(12), y + self.s(2))
        self.set_font_s("B", 8)
        self.set_text_color(*GRAY)
        self.cell(self.w - self.s(24), self.s(4), "IGA P\u00c4EV  |  K\u00d5IGILE ROLLIDELE", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font_s("B", 12)
        self.set_text_color(*NAVY)
        chain = "Kuula  \u2192  Vasta  \u2192  Ole kohal  \u2192  Aita suunata  \u2192  Teata ohtu"
        self.cell(0, self.s(8), chain, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_y(y + h + self.s(4))

    def card(self, x, y, w, h, title, lines, chain=None):
        self.set_fill_color(250, 252, 254)
        self.set_draw_color(197, 212, 227)
        self.rect(x, y, w, h, style="DF")
        self.set_xy(x + self.s(3), y + self.s(2.5))
        self.set_font_s("B", 9)
        self.set_text_color(*NAVY)
        self.cell(w - self.s(6), self.s(5), title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*NAVY)
        self.line(x + self.s(3), self.get_y(), x + w - self.s(3), self.get_y())
        self.ln(self.s(1.5))
        if chain:
            self.set_x(x + self.s(3))
            self.set_font_s("B", 8.5)
            self.set_text_color(*NAVY)
            self.multi_cell(w - self.s(6), self.s(4), chain)
            self.ln(self.s(1))
        self.set_font_s("", 8.5)
        self.set_text_color(26, 46, 68)
        for line in lines:
            self.set_x(x + self.s(5))
            self.cell(w - self.s(8), self.s(4), f"\u2022 {line}", new_x="LMARGIN", new_y="NEXT")

    def grid_cards(self):
        margin = self.s(12)
        gap = self.s(4)
        w = (self.w - 2 * margin - gap) / 2
        h = self.s(34)
        y = self.get_y()
        self.card(margin, y, w, h, "ENNE KUI REAGEERID", [
            "Kas ma kuulan?",
            "Kas ma alav\u00e4\u00e4ristan?",
            "Kas on turvaline?",
            "Kuhu raporteerin?",
        ])
        y_chain = (
            "MIKS \u2192 Kuula \u2192 Ole aus \u2192 Ole kohal \u2192 Aita arendada \u2192 Tunnusta"
        )
        self.card(margin + w + gap, y, w, h, "Y-JUHTIMINE  |  JUHT JA \u00d5PETAJA", [
            "Selgita MIKS enne kui n\u00f5uad",
            "Ole treener, mitte ainult \u00fclemus",
            "S\u00f5nad ja teod peavad klappima",
        ], chain=y_chain)
        y2 = y + h + gap
        self.card(margin, y2, w, h, "EI OLE LUBATUD", [
            "Solvamine, h\u00e4bistamine, alav\u00e4\u00e4ristamine",
            "Karjumine, ignoreerimine, diskrimineerimine",
            "V\u00e4givald, \u00e4hvardus v\u00f5i \u00f5hutamine",
            "Kiusamine: reageeritakse 24 h jooksul",
        ])
        self.card(margin + w + gap, y2, w, h, "KUHU P\u00d6\u00d6RDUDA", [
            "Vahetu \u00fclemus / klassijuhataja",
            "Sotsiaalpedagoog, personal, \u00f5ppejuht",
            "info@techno.ee  |  personal@techno.ee",
            "Kriis: turvat\u00f6\u00f6, juhtkond, 112",
        ])
        self.set_y(y2 + h + self.s(4))

    def emergency_bar(self):
        y = self.get_y()
        h = self.s(9)
        self.set_fill_color(255, 243, 243)
        self.set_draw_color(204, 68, 68)
        self.rect(self.s(12), y, self.w - self.s(24), h, style="DF")
        self.set_xy(self.s(12), y + self.s(2))
        self.set_font_s("B", 9)
        self.set_text_color(*RED)
        txt = (
            "Oht elule v\u00f5i tervisele: 112   |   Vaimne kriis: 116 123   |   "
            "T\u00f6\u00f6\u00f5nnetus t\u00f6\u00f6kojas: peata t\u00f6\u00f6, teata kohe"
        )
        self.cell(self.w - self.s(24), self.s(5), txt, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_y(y + h + self.s(3))

    def question_bar(self):
        y = self.get_y()
        h = self.s(14)
        self.set_fill_color(*NAVY)
        self.rect(self.s(12), y, self.w - self.s(24), h, style="F")
        self.set_xy(self.s(12), y + self.s(2))
        self.set_font_s("B", 8)
        self.set_text_color(220, 230, 240)
        self.cell(self.w - self.s(24), self.s(4), "KUI INIMENE TUNDUB JUHTIMATU", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font_s("B", 11)
        self.set_text_color(*WHITE)
        self.cell(self.w - self.s(24), self.s(6), "Kas mina juhin nii, et ta saaks kuulda?", align="C")
        self.set_y(y + h + self.s(3))

    def footer_block(self):
        self.set_font_s("", 7.5)
        self.set_text_color(*GRAY)
        self.set_draw_color(197, 212, 227)
        y = self.get_y()
        self.line(self.s(12), y, self.w - self.s(12), y)
        self.ln(self.s(2))
        left = (
            "P\u00f5him\u00f5te: Austus on k\u00e4itumine. Lugupidamine on protsess. Turvalisus on esimene."
        )
        right = (
            "Techno TLN sisekorra eeskiri  |  Alar Ojastu, Ratsionaalne emotsionaalsus  |  techno.ee"
        )
        self.set_x(self.s(12))
        self.multi_cell((self.w - self.s(24)) / 2, self.s(3.5), left)
        self.set_xy(self.s(12) + (self.w - self.s(24)) / 2, self.get_y() - self.s(7))
        self.multi_cell((self.w - self.s(24)) / 2, self.s(3.5), right, align="R")

    def render(self):
        self.header_block()
        self.values_row()
        self.hero_chain()
        self.grid_cards()
        self.emergency_bar()
        self.question_bar()
        self.footer_block()


def build_pdf(path: Path, fmt: str):
    pdf = PosterPDF(fmt)
    pdf.render()
    pdf.output(str(path))
    print(f"Saved: {path} ({fmt}, 1 page)")


def build_html():
    """Keep HTML in sync for browser preview."""
    if HTML.exists():
        return
    # HTML maintained separately in repo


def chrome_pdf_fallback():
    if not HTML.exists():
        return
    try:
        subprocess.run(
            [
                "google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=10000",
                f"--print-to-pdf-no-header",
                f"--print-to-pdf={PDF_A4.with_suffix('.html-preview.pdf')}",
                f"file://{HTML.resolve()}",
            ],
            check=False, capture_output=True, timeout=30,
        )
    except Exception:
        pass


def main():
    build_pdf(PDF_A4, "A4")
    build_pdf(PDF_A3, "A3")


if __name__ == "__main__":
    main()
