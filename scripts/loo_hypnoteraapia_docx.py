#!/usr/bin/env python3
"""Genereerib HY1 juhendi Wordi — EMDR eeskuju vormingus (algajale, paarilisele)."""

from datetime import date
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

OUTPUT = "/workspace/Hypnoteraapia-HY1.docx"
TODAY = date.today().strftime("%d.%m.%Y")

doc = Document()
for section in doc.sections:
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

GREEN = RGBColor(0x1B, 0x5E, 0x20)
GRAY = RGBColor(0x55, 0x55, 0x55)


def add_heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = GREEN if level == 1 else GRAY
    return h


def add_normal(text, bold=False, italic=False, size=11):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    return p


def add_bullet(text):
    doc.add_paragraph(text, style="List Bullet")


def add_quote(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1)
    run = p.add_run(text)
    run.italic = True
    run.font.color.rgb = GREEN
    run.font.size = Pt(10)


# === PEALKIRI ===
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Hüpnoteraapia juhised algajale")
r.bold = True
r.font.size = Pt(18)
r.font.color.rgb = GREEN

for line in ["Iseendale ja paarilisele kodus", "Lihtsad sammud turvalise hüpnoosiga — 15–25 minutit"]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(line).font.size = Pt(11)

doc.add_paragraph()

add_heading("OLULINE — loe enne alustamist", 1)
for item in [
    "Kerge stress, uni, fookus — MITTE trauma või PTSD raviks.",
    "Raske trauma, enesetapumõtted, dissotsiatsioon → hünoterapeudi poole.",
    "Distress üle 8/10 → lõpeta kohe (punkt 5).",
    "Paariline töö nõuab usaldust. Piisab ühest kergest eesmärgist.",
    "Iga mees saab seda õppida ja teha oma kaaslasele.",
]:
    add_bullet(item)

add_heading("Mis on hüpnoteraapia?", 1)
add_normal(
    "Hüpnoteraapia kasutab hüpnoosi — fookustatud tähelepanu ja lõdvestust. "
    "Kodus lihtsustatud versioon. Ei asenda terapeuti. "
    "Sa kuuled, tunned keha, saad silmad avada."
)

add_heading("1. Valmistumine (mõlemale)", 1)
for i, item in enumerate(
    [
        "Vali vaikne koht. Istu või lama. Vesi lähedal.",
        "Vali meetod: ise · salvestis · paariline.",
        "Hinda distressi 0–10. Kirjuta üles.",
        "Vali üks eesmärk: rahunemine, uni või fookus.",
        "Sea taimer 15–25 minutile.",
    ],
    1,
):
    add_normal(f"{i}. {item}")

add_heading("2. Meetodid — vali üks", 1)
add_normal("A. Ise — loe skripti vaikselt", bold=True)
add_normal("B. Salvestis — kuula kõrvaklappidega", bold=True)
add_normal("C. Paariline — teine loeb aeglaselt", bold=True)

add_heading("3. Iseendale — samm-sammult", 1)
for title, desc in [
    ("Samm 1: Ankur (2 min)", "3 hingetõmmet: sisse 4, välja 6."),
    ("Samm 2: Keha skaneering (3 min)", "Tähelepanu peast jalgadeni. Igas kohas: Lõdvestu."),
    ("Samm 3: Turvakoht (2 min)", "Kujutle turvalist kohta. Mida näed, kuuled, tunned?"),
    ("Samm 4: Suggestioon (8–12 min)", "Too eesmärk meelde. Loe HY1 lauset."),
    ("Samm 5: Lõpeta", "Loenda 5-1. Ava silmad. Vesi. Mis muutus?"),
]:
    add_normal(title, bold=True)
    add_normal(desc)

add_quote(
    "Ma rahunen loomulikult. Mu keha teab, kuidas tulla rahule. "
    "Ma olen turvaliselt. Iga hingetõmme toob rohkem kergust."
)

add_heading("4. Paarilisele — kuidas aidata", 1)
add_normal("Sa ei pea olema terapeut. Sa juhid rütmi ja hoiad ruumi turvalisena.", bold=True)
add_normal("Enne algust: Sul on alati kontroll. Ava silmad igal hetkel.", italic=True)

add_normal("Paariline protokoll:", bold=True)
for i, item in enumerate(
    [
        "Lepi kokku: üks eesmärk, 15–25 min.",
        "A kuulab. B loeb skripti aeglaselt.",
        "Ankur → keha → turvakoht → suggestioon 8–12 min.",
        "Loendame 5-1. Ava silmad. Distress? Mis muutus?",
        "Vaheta rolid järgmisel korral.",
    ],
    1,
):
    add_normal(f"{i}. {item}")

add_normal("Mida abiline EI tee:", bold=True)
for item in [
    "Ei analüüsi ega anna nõu.",
    "Ei suru rääkima.",
    "Ei jätka, kui partner ütleb stop.",
    "Ei ütle sa oled hüpnoosis ja ei mäleta.",
]:
    add_bullet(item)

add_heading("5. Millal STOP", 1)
for item in [
    "Distress üle 8/10",
    "Pearinglus, paanika, dissotsiatsioon",
    "Tugevad flashback'id",
]:
    add_bullet(item)
add_normal(
    "STOP: ava silmad. 5-4-3-2-1 maandamine. Vesi. 116 123 vajadusel."
)

add_heading("6. Kiire viide", 1)
add_normal(
    "Ankur → Keha → Turvakoht → Suggestioon 8-12 min → Tagasi 5-1 → Vesi → Mis muutus?"
)
add_normal("Aeg: 15-25 min | Stop: distress > 8 | Meetodid: ise · salvestis · paariline")

add_heading("7. Näited algajale", 1)
add_normal("Ise — uneärevus: Eesmärk magama. Distress 6→3. 15 min.", bold=True)
add_normal("Paar — enne koosolekut: Abiline loeb. 12 min. Distress langeb.", bold=True)
add_normal("Mees kaaslasele: 15 min HY1. Debrief 1 lause.", bold=True)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(
    "See juhend on hariduslik. Ei asenda psühholoogi ega hünoterapeudi abi.\n"
    f"Unpluged-Al · HY1 v2.0 · {TODAY}"
)
run.font.size = Pt(9)
run.font.color.rgb = GRAY
run.italic = True

doc.save(OUTPUT)
print(f"Salvestatud: {OUTPUT}")
