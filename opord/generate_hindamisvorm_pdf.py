#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate print-ready Peegel hindamisvorm and unit plankett (Lisa AV)."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
GREEN = colors.HexColor("#1a3a2a")
GRAY = colors.HexColor("#444444")
LIGHT = colors.HexColor("#e8efe8")

FORM_PDF = BASE / "PEEGEL_HINDAMISVORM_PRINT.pdf"
PLANKETT_PDF = BASE / "PEEGEL_HINDAMISVORM_PLANKETT.pdf"
MINI_PDF = BASE / "PEEGEL_HINDAMISVORM_RAHAKOTT.pdf"
RIIK_FORM_PDF = BASE / "PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf"
RIIK_PLANKETT_PDF = BASE / "PEEGEL_RIIK_PLANKETT.pdf"
PEER_MINI_PDF = BASE / "PEER_HINDAMINE_RAHAKOTT.pdf"
PEER_SOP_PDF = BASE / "PEER_HINDAMINE_SOP_PRINT.pdf"

CRITERIA = [
    ("Initsiatiiv", "Kas ta teeb ara ilma, et keegi palub?"),
    ("Tookindlus", "Kas ta viib asjad lopuni?"),
    ("Meeskonnatoo", "Kas ta aitab teisi (kata ja liigu)?"),
    ("Tahelepanu", "Kas ta markab detaile - sonu, peret, allikaid?"),
    ("Teadlikkus", "Kas ta teab plaani ja kontrollib infot?"),
    ("Vastupidavus", "Uni, liikumine, taastumine - kas hoiab masinat?"),
]

RIIK_EXTRA = [
    ("Austus ja lugupidamine", "Kas teine tunneb end vaartustatuna? Ei solva ega habista."),
    ("Turvalisus ja selgus", "Kas teatab ohtudest ja jargib protsessi?"),
]


def draw_line_field(c, x, y, label, width, label_w=42 * mm):
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GRAY)
    c.drawString(x, y, label)
    c.setStrokeColor(colors.HexColor("#999999"))
    c.line(x + label_w, y - 1 * mm, x + width, y - 1 * mm)
    return y - 7 * mm


def draw_comment_box(c, x, y, w, title, hint, lines=3):
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.drawString(x, y, title)
    c.setFont("Helvetica", 6.5)
    c.setFillColor(GRAY)
    c.drawString(x, y - 3.5 * mm, hint)
    box_top = y - 5 * mm
    box_h = lines * 5 * mm + 2 * mm
    c.setStrokeColor(colors.HexColor("#bbbbbb"))
    c.setFillColor(colors.white)
    c.rect(x, box_top - box_h, w, box_h, fill=1, stroke=1)
    for i in range(lines):
        ly = box_top - box_h + (lines - i) * 5 * mm - 2 * mm
        c.line(x + 2 * mm, ly, x + w - 2 * mm, ly)
    return box_top - box_h - 3 * mm


def draw_circle_choice(c, x, y, label):
    c.setStrokeColor(GREEN)
    c.circle(x, y, 3 * mm, fill=0, stroke=1)
    c.setFont("Helvetica", 8)
    c.setFillColor(GRAY)
    c.drawString(x + 5 * mm, y - 1 * mm, label)


def build_form_pdf(riik=False):
    """A4 kirjalik hindamisvorm - uks taitmine lehe kohta."""
    out = RIIK_FORM_PDF if riik else FORM_PDF
    criteria = CRITERIA + (RIIK_EXTRA if riik else [])
    c = canvas.Canvas(str(out), pagesize=A4)
    pw, ph = A4
    m = 12 * mm
    w = pw - 2 * m

    # Header band
    c.setFillColor(GREEN)
    c.rect(m, ph - m - 16 * mm, w, 16 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(pw / 2, ph - m - 7 * mm, "PEEGLI HINDAMISVORM" + (" — RIIK" if riik else ""))
    c.setFont("Helvetica", 8)
    sub = "Lisa BD | Riigisektor | Konfidentsiaalne | Vahemalt 2 hindajat" if riik else "Lisa AV | Kirjalik | Konfidentsiaalne | Vahemalt 2 hindajat"
    c.drawCentredString(pw / 2, ph - m - 12 * mm, sub)

    y = ph - m - 22 * mm
    c.setFillColor(GRAY)

    # Meta fields
    y = draw_line_field(c, m, y, "Hinnatav:", w * 0.55)
    y2 = ph - m - 29 * mm
    y2 = draw_line_field(c, m + w * 0.58, y2, "Kuupaev:", w * 0.38, label_w=18 * mm)
    y = min(y, y2) - 2 * mm
    y = draw_line_field(c, m, y, "Uksus / pere:", w * 0.55)
    y2 = y + 7 * mm
    y2 = draw_line_field(c, m + w * 0.58, y2, "Vorm:", w * 0.38, label_w=18 * mm)
    c.setFont("Helvetica", 7)
    c.drawString(m + w * 0.58 + 18 * mm, y2 - 4 * mm, "PERE / MEESKOND / SOK / RIIK" if riik else "PERE / MEESKOND / SOK")
    y -= 2 * mm
    y = draw_line_field(c, m, y, "Hindaja (nimi):", w)
    y -= 4 * mm

    # Criteria boxes (2 columns)
    col_w = (w - 6 * mm) / 2
    left_x = m
    right_x = m + col_w + 6 * mm
    y_left = y
    y_right = y
    for i, (title, hint) in enumerate(criteria):
        if i % 2 == 0:
            y_left = draw_comment_box(c, left_x, y_left, col_w, title, hint, lines=2)
        else:
            y_right = draw_comment_box(c, right_x, y_right, col_w, title, hint, lines=2)
    y = min(y_left, y_right) - 2 * mm

    # Luure question box - centerpiece
    box_h = 28 * mm
    c.setFillColor(LIGHT)
    c.setStrokeColor(GREEN)
    c.setLineWidth(1.2)
    c.rect(m, y - box_h, w, box_h, fill=1, stroke=1)
    c.setLineWidth(0.5)
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(pw / 2, y - 8 * mm, "Kas sa selle inimesega luurele laheksid?")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    c.drawCentredString(
        pw / 2,
        y - 13 * mm,
        "Luure = usaldus otsustada uksi, vaikida kui vaja, tulla tagasi toega. Keegi ei vaata ule ola.",
    )
    cx = pw / 2
    draw_circle_choice(c, cx - 22 * mm, y - 21 * mm, "JAH")
    draw_circle_choice(c, cx + 8 * mm, y - 21 * mm, "EI")
    y -= box_h + 4 * mm

    # Development K/H/P
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(GREEN)
    c.drawString(m, y, "Areng:")
    y -= 6 * mm
    draw_circle_choice(c, m + 4 * mm, y, "K Kasv - rohkem vastutust")
    draw_circle_choice(c, m + 52 * mm, y, "H Hoia - kinnita, treeni")
    draw_circle_choice(c, m + 100 * mm, y, "P Paus - vahenda koormust")
    y -= 8 * mm
    y = draw_line_field(c, m, y, "Uks lause miks:", w, label_w=28 * mm)

    # Hinnatava vastus (after dialogue)
    y -= 2 * mm
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.drawString(m, y, "Hinnatava vastus (taidab ise parast vestlust):")
    y -= 5 * mm
    for label in [
        "Mida ma kuulsin:",
        "Mida ma votan omaks (uks asi):",
        "Mida ma ei vota (uks asi):",
        "Uks tegu jargmiseks perioodiks:",
    ]:
        y = draw_line_field(c, m, y, label, w, label_w=52 * mm)

    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(GRAY)
    c.drawCentredString(
        pw / 2,
        m,
        "Ennast keegi ise ei hinda | Turvalisus enne loogikat (Lisa P) | Prindi uus leht iga hindaja kohta",
    )
    c.save()
    print(f"Generated: {out}")


def build_plankett_pdf(riik=False):
    """A5/A4 plankett - seinale / kausta kaanele."""
    out = RIIK_PLANKETT_PDF if riik else PLANKETT_PDF
    pagesize = A4 if riik else A5
    c = canvas.Canvas(str(out), pagesize=pagesize)
    pw, ph = pagesize
    m = 10 * mm

    c.setFillColor(GREEN)
    c.rect(0, ph - 22 * mm, pw, 22 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(pw / 2, ph - 10 * mm, "PEEGLI PLANKETT" + (" — RIIK" if riik else ""))
    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, ph - 16 * mm, "Lisa BD | Asutus ja riigisektor" if riik else "Lisa AV | Iga pere ja uksus")

    y = ph - 30 * mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(pw / 2, y, "Kas sa selle inimesega")
    y -= 7 * mm
    c.drawCentredString(pw / 2, y, "luurele laheksid?")
    y -= 10 * mm

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    rules = [
        "1. Kirjalikult. Prindi vorm. Taida enne vestlust.",
        "2. Vahemalt KAKS hindajat. Iseenda hinnang ei loe.",
        "3. Kvartal (juhtkond) voi 2x aastas (esiliin)." if riik else "3. Kuus (pere) voi kvartal (meeskond).",
        "4. Uks tegu parast - mitte ainult kriitika.",
        "5. Konfidentsiaalne. Mitte grupivestlusesse.",
    ]
    for r in rules:
        c.drawString(m, y, r)
        y -= 5.5 * mm

    y -= 3 * mm
    c.setStrokeColor(GREEN)
    c.line(m, y, pw - m, y)
    y -= 6 * mm

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.drawString(m, y, "8 kriteeriumi (Lisa BD):" if riik else "6 kriteeriumi (kirjuta konkreetsed naited vormile):")
    y -= 5 * mm
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    all_c = list(CRITERIA) + (list(RIIK_EXTRA) if riik else [])
    for title, _ in all_c:
        c.drawString(m + 2 * mm, y, f"- {title}")
        y -= 4.5 * mm

    y -= 2 * mm
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    c.drawString(m, y, "Areng: K Kasv | H Hoia | P Paus")
    y -= 8 * mm

    c.setFillColor(LIGHT)
    c.rect(m, y - 12 * mm, pw - 2 * m, 12 * mm, fill=1, stroke=0)
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(pw / 2, y - 5 * mm, "Inimesena on meil pimenurgad.")
    c.drawCentredString(pw / 2, y - 9 * mm, "Peegel naitab seda, mida ise ei nae.")

    c.setFont("Helvetica", 6)
    c.drawCentredString(pw / 2, 6 * mm, ("PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf" if riik else "PEEGEL_HINDAMISVORM_PRINT.pdf") + " | Lamineeri | Hoia uksuse kaustas")
    c.save()
    print(f"Generated: {out}")


def build_mini_pdf():
    """85x55 mm taskukaart - luurekusimus + meeldetuletus."""
    c = canvas.Canvas(str(MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)

    lines = [
        "LUUREKUSIMUS",
        "Kas sa selle inimesega",
        "luurele laheksid?",
        "",
        "Kirjalikult. 2 hindajat.",
        "PEEGEL_HINDAMISVORM_PRINT",
    ]

    for i in range(6):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gap_x + col * (cw + gap_x)
        y = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        c.setFillColor(GREEN)
        c.rect(x, y + ch - 10 * mm, cw, 10 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(x + cw / 2, y + ch - 6.5 * mm, "PEEGEL AV")
        c.setFillColor(GRAY)
        c.setFont("Helvetica-Bold", 6.5)
        ty = y + ch - 14 * mm
        for line in lines:
            if line == "LUUREKUSIMUS":
                c.setFont("Helvetica-Bold", 7)
            else:
                c.setFont("Helvetica", 6)
            c.drawCentredString(x + cw / 2, ty, line)
            ty -= 4 * mm

    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "85x55 mm | Lisa AV | Hindamisvorm")
    c.save()
    print(f"Generated: {MINI_PDF}")


def build_peer_mini_pdf():
    """85x55 mm — igapaevane kaaslase hindamine (Lisa BE)."""
    c = canvas.Canvas(str(PEER_MINI_PDF), pagesize=A4)
    pw, ph = A4
    cw, ch = 85 * mm, 55 * mm
    cols, rows = 2, 4
    gap_x = (pw - cols * cw) / (cols + 1)
    gap_y = (ph - rows * ch) / (rows + 1)

    fields = [
        "KAASLASE HINDAMINE",
        "Lisa BE | Ranger mudel",
        "",
        "OLUKORD:",
        "MIS TOIMIS:",
        "MIS VOIB TEISITI:",
        "UKS SOOVITUS:",
        "Luure uuesti? J / E",
    ]

    for i in range(6):
        col = i % cols
        row = rows - 1 - (i // cols)
        x = gap_x + col * (cw + gap_x)
        y = gap_y + row * (ch + gap_y)
        c.setStrokeColor(GREEN)
        c.rect(x, y, cw, ch, fill=0, stroke=1)
        c.setFillColor(GREEN)
        c.rect(x, y + ch - 9 * mm, cw, 9 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(x + cw / 2, y + ch - 5.5 * mm, "PEER | Iga paev")
        c.setFillColor(GRAY)
        ty = y + ch - 12 * mm
        for line in fields:
            c.setFont("Helvetica-Bold" if line.endswith(":") else "Helvetica", 5.5 if line.endswith(":") else 5)
            c.drawString(x + 2 * mm, ty, line)
            ty -= 3.8 * mm

    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, 5 * mm, "85x55 mm | Lisa BE | Kaaslase hindamine")
    c.save()
    print(f"Generated: {PEER_MINI_PDF}")


def build_peer_sop_pdf():
    """A5 — millal ja kuidas (Lisa BE)."""
    c = canvas.Canvas(str(PEER_SOP_PDF), pagesize=A5)
    pw, ph = A5
    m = 10 * mm

    c.setFillColor(GREEN)
    c.rect(0, ph - 20 * mm, pw, 20 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(pw / 2, ph - 9 * mm, "KAASLASE HINDAMINE")
    c.setFont("Helvetica", 7)
    c.drawCentredString(pw / 2, ph - 15 * mm, "Lisa BE | Ranger School mudel")

    y = ph - 28 * mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(m, y, "Millal:")
    y -= 6 * mm
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    for t in [
        "ALGUSES — 60 sek: eesmark, rollid, STOP, debrief aeg (nagu GOTWA)",
        "PARAST — sobival hetkel: 4 lauset (olukord, nain, mojutas, soovitus)",
        "IGA PAEV — vahemalt uks aus tagasiside kaaslasele",
    ]:
        c.drawString(m + 2 * mm, y, f"- {t}")
        y -= 5 * mm

    y -= 3 * mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(m, y, "4 lauset:")
    y -= 6 * mm
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7.5)
    for t in [
        "1. OLUKORD: mis juhtus",
        "2. NAGIN: konkreetne tegu (mitte silt)",
        "3. MOJUTAS: kuidas see mojutas",
        "4. SOOVITUS: uks asi jargmiseks",
    ]:
        c.drawString(m + 2 * mm, y, t)
        y -= 4.5 * mm

    y -= 3 * mm
    c.setFillColor(LIGHT)
    c.rect(m, y - 14 * mm, pw - 2 * m, 14 * mm, fill=1, stroke=0)
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(pw / 2, y - 5 * mm, "Iga paev = mikropeegel (BE)")
    c.drawCentredString(pw / 2, y - 9 * mm, "Kuu/kvartal = sugav peegel (Lisa AV)")
    c.drawCentredString(pw / 2, y - 13 * mm, "Turvalisus enne loogikat (Lisa P)")

    c.setFont("Helvetica", 6)
    c.drawCentredString(pw / 2, 6 * mm, "PEER_HINDAMINE_RAHAKOTT.pdf | Lamineeri")
    c.save()
    print(f"Generated: {PEER_SOP_PDF}")


def main():
    build_form_pdf(riik=False)
    build_plankett_pdf(riik=False)
    build_mini_pdf()
    build_form_pdf(riik=True)
    build_plankett_pdf(riik=True)
    build_peer_mini_pdf()
    build_peer_sop_pdf()


if __name__ == "__main__":
    main()
