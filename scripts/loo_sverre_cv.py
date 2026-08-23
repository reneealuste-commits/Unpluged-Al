#!/usr/bin/env python3
"""Genereerib Wordi CV: Sverre Puustusmaa — värbamisettevõtetele."""

from datetime import date
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT = "/workspace/Sverre-Puustusmaa-CV.docx"
TODAY = date.today().strftime("%d.%m.%Y")

doc = Document()
for section in doc.sections:
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(2.2)
    section.right_margin = Cm(2.2)

NAVY = RGBColor(0x1A, 0x23, 0x7E)
DARK = RGBColor(0x21, 0x21, 0x21)
GRAY = RGBColor(0x55, 0x55, 0x55)
ACCENT = RGBColor(0x2E, 0x7D, 0x32)


def add_horizontal_line(paragraph, color="1A237E"):
    p = paragraph._p
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = NAVY
    return h


def add_normal(text, bold=False, size=10.5, color=DARK, center=False, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.color.rgb = color
    return p


def add_bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    if bold_prefix and text.startswith(bold_prefix):
        r = p.add_run(bold_prefix)
        r.bold = True
        r.font.size = Pt(10)
        rest = p.add_run(text[len(bold_prefix):])
        rest.font.size = Pt(10)
    else:
        r = p.add_run(text)
        r.font.size = Pt(10)
    return p


def add_table(headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(9)
                r.font.color.rgb = NAVY
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return table


def add_job(title, company, period, location, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(title)
    r1.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = DARK
    r2 = p.add_run(f"  ·  {company}")
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = NAVY

    meta = doc.add_paragraph()
    meta.paragraph_format.space_after = Pt(4)
    rm = meta.add_run(f"{period}  ·  {location}")
    rm.italic = True
    rm.font.size = Pt(9.5)
    rm.font.color.rgb = GRAY

    for b in bullets:
        add_bullet(b)


# === PÄIS ===
name = doc.add_paragraph()
name.alignment = WD_ALIGN_PARAGRAPH.CENTER
rn = name.add_run("Sverre Puustusmaa")
rn.bold = True
rn.font.size = Pt(22)
rn.font.color.rgb = NAVY

tag = doc.add_paragraph()
tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
rt = tag.add_run("Tegevjuht  ·  Ettevõtja  ·  Kaitse- ja kriisivaldkonna ekspert")
rt.font.size = Pt(11)
rt.font.color.rgb = GRAY

contact = doc.add_paragraph()
contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
rc = contact.add_run(
    "Viljandi, Eesti  ·  Hilden, Saksamaa\n"
    "E-post: [lisa kontakt]  ·  Telefon: [lisa kontakt]  ·  LinkedIn: linkedin.com/in/sverre-puustusmaa"
)
rc.font.size = Pt(9.5)
rc.font.color.rgb = GRAY

line_p = doc.add_paragraph()
add_horizontal_line(line_p)

# === PROFIIL ===
add_heading("Profiilikokkuvõte", level=2)
add_normal(
    "24+ aastat ettevõtluskogemust. Asutas ja juhib globaalset kriisitoidu tootmist ja eksporti "
    "(Tactical Foodpack) — 34 riiki, €5,8 mln käive (2024). Taust Kaitseväes erioperatsioonide "
    "meditsiinis ja NATO eriväelaste koolituses. Tugev kombinatsioon: strateegiline juhtimine, "
    "tootmine, rahvusvaheline müük, kriisivalmidus ja riigikaitse partnerlus."
)
add_normal(
    "Otsitavad rollid: tegevjuht (CEO), tegevdirektor (COO), juhatuse liige, kaitse- ja "
    "julgeolekusektor, toidutööstus, eksport, kriisivalmidus, strateegiline nõustamine.",
    bold=True,
    size=10,
)

# === OSKUSED ===
add_heading("Põhioskused", level=2)
add_table(
    ["Juhtimine", "Äri", "Valdkond"],
    [
        [
            "Strateegia ja skaleerimine\nMeeskonna juhtimine (22+)\nInvestorite suhted\nKriisijuhtimine",
            "Rahvusvaheline eksport (34 riiki)\nTootmine ja tarneahel\nBrändi ehitus\nFinantseerimine (€700k)",
            "Kriisitoodu ja toidujulgeolek\nKaitsevägi ja NATO partnerlus\nKriisivalmidus\nMeditsiiniline kaitsevägi taust",
        ]
    ],
)

# === TÖÖKOGEMUS ===
add_heading("Töökogemus", level=2)

add_job(
    "Tegevjuht (CEO)",
    "Tactical Solutions GmbH / Tactical Solution OÜ",
    "2016 – tänaseni",
    "Viljandi (EE) · Düsseldorf (DE)",
    [
        "Juhib kontserni, mille käive kasvas €230 000-lt (2019) €5,8 mln-ni (2024).",
        "Skaleeris tootmise kuni 500 000 pakini kuus; ekspordib 33–34 riiki.",
        "Kaasas €700 000 investoriraha Funderbeami kaudu (810 investorit).",
        "Rajas tootmise Saksamaale; säilitas R&D, brändi ja müügi Eestis.",
        "Partner Kaitseväele — tooted Exercise SIIL 2022 toidupakis.",
        "Organiseeris Ukraina humanitaarabi: 7 000+ toidupakki (2022).",
    ],
)

add_job(
    "Ettevõtja",
    "Sverreland OÜ",
    "2002 – tänaseni",
    "Viljandi",
    ["24+ aastat ettevõtluses; mitmed ettevõtted ja projektid kogu karjääri jooksul."],
)

add_job(
    "Projektidirektor",
    "Olympic Entertainment Group",
    "[aasta – lisa]",
    "[asukoht]",
    ["Juhtis suuri projekte kasiino- ja meelelahutuskontsernis."],
)

add_job(
    "Asutaja",
    "Deguster OÜ",
    "2003 – [lisa]",
    "Eesti",
    ["Varajane ettevõtluskogemus toidu- ja meelelahutusvaldkonnas."],
)

# === KAITSEVÄGI ===
add_heading("Kaitseväe ja kriisivaldkonna kogemus", level=2)
add_job(
    "Väepealik (NCO)",
    "Kaitsevägi",
    "[aasta – lisa]",
    "Eesti",
    [
        "Erioperatsioonide väejuhatuse meditsiin.",
        "NATO eriväelaste meditsiinikool — maailma suurimas sõjaväebaasis.",
        "Ukraina missioon (2014) — praktiline kogemus väljal toitmise ja logistika kitsaskohtadest.",
    ],
)

add_heading("Tunnustused", level=3)
add_table(
    ["Aasta", "Tunnustus", "Andja"],
    [
        ["2026", "Riigikaitse toetaja", "President Alar Karis, Kaitseministeerium"],
        ["2024", "Kaitseministri teenetemärk", "Kaitseministeerium"],
        ["2021", "Aasta ettevõte nominent", "Viljandi maakond"],
    ],
)

# === HARIDUS ===
add_heading("Haridus ja koolitused", level=2)
add_table(
    ["Aasta", "Koolitus / haridus"],
    [
        ["[lisa]", "NATO eriväelaste meditsiinikool"],
        ["[lisa]", "Kaitseväe meditsiinikoolitus (erioperatsioonid)"],
        ["[lisa]", "[lisa kõrgharidus, kui on]"],
    ],
)

# === KEELED ===
add_heading("Keeled", level=2)
add_table(
    ["Keel", "Tase"],
    [
        ["Eesti", "emakeel"],
        ["Inglise", "[lisa tase]"],
        ["Saksa", "[lisa tase]"],
    ],
)

# === VÄRBAMISE INFO ===
add_heading("Lisainfo värbajatele", level=2)
add_table(
    ["Väli", "Info"],
    [
        ["Saadavus", "[lisa — nt kohe / 3 kuud / projektipõhine]"],
        ["Asukoht", "Viljandi, Eesti; reisivalmidus Saksamaa, EL, NATO turud"],
        ["Töövorm", "täistööaeg, nõukogu, strateegiline nõustamine, projektid"],
        ["Palgasoodustus", "[lisa või läbirääkimistel]"],
        ["Konfidentsiaalsus", "otsing diskreetne"],
    ],
)

# === JALUS ===
doc.add_paragraph()
footer = doc.add_paragraph()
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
rf = footer.add_run(f"CV koostatud {TODAY}  ·  värbamis- ja talentifirmadele")
rf.font.size = Pt(8)
rf.font.color.rgb = GRAY
rf.italic = True

doc.save(OUTPUT)
print(f"Salvestatud: {OUTPUT}")
