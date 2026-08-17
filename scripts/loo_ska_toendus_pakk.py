#!/usr/bin/env python3
"""Tõenduspakk PDF — Sotsiaalkindlustusametile (vanemahüvitis)."""

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

OUTPUT = "/workspace/toendus-pakk-SKA.pdf"

NAVY = colors.HexColor("#1A237E")
DARK = colors.HexColor("#212121")
GRAY = colors.HexColor("#616161")
RED = colors.HexColor("#B71C1C")
GREEN = colors.HexColor("#1B5E20")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title", parent=base["Heading1"], fontSize=18, textColor=NAVY,
            spaceAfter=6, fontName="Helvetica-Bold", alignment=TA_CENTER,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle", parent=base["Normal"], fontSize=10, textColor=GRAY,
            spaceAfter=10, alignment=TA_CENTER,
        ),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading1"], fontSize=14, textColor=NAVY,
            spaceBefore=10, spaceAfter=6, fontName="Helvetica-Bold",
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontSize=11, textColor=NAVY,
            spaceBefore=8, spaceAfter=4, fontName="Helvetica-Bold",
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontSize=10, leading=14,
            textColor=DARK, alignment=TA_JUSTIFY,
        ),
        "body_bold": ParagraphStyle(
            "BodyBold", parent=base["Normal"], fontSize=10, leading=14,
            textColor=DARK, fontName="Helvetica-Bold",
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontSize=10, leading=14,
            leftIndent=12, textColor=DARK,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["Normal"], fontSize=8, leading=10, textColor=GRAY,
        ),
        "deadline": ParagraphStyle(
            "Deadline", parent=base["Normal"], fontSize=11, textColor=RED,
            fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=8,
        ),
        "highlight": ParagraphStyle(
            "Highlight", parent=base["Normal"], fontSize=10, leading=14,
            textColor=GREEN, fontName="Helvetica-Bold",
        ),
    }


def hr(story):
    story.append(HRFlowable(width="100%", thickness=0.8, color=NAVY, spaceAfter=8, spaceBefore=4))


def table(data, col_widths, header=False):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
    ]
    if header:
        style.extend([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    t.setStyle(TableStyle(style))
    return t


def cover(story, s):
    story.append(Spacer(1, 25 * mm))
    story.append(Paragraph("TÕENDUSPAKK", s["title"]))
    story.append(Paragraph("Sotsiaalkindlustusametile", s["subtitle"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Vastuväide vanemahüvitise määramise kohta", s["subtitle"]))
    story.append(Spacer(1, 12))
    hr(story)
    meta = [
        ["Laps:", "Indie Eva Alexandra Aluste"],
        ["Isa / taotleja:", "Renee Aluste"],
        ["Ema / vastu:", "Maria-Isabelle Aluste"],
        ["SKA viide:", "Arvamuse küsimine, 11.08.2026"],
        ["Spetsialist:", "Galina Družkova (perehüvitised)"],
        ["Koostatud:", "17.08.2026"],
        ["Põhiargument:", "Vanemate finantskokkulepe ja leibkonna sissetulek"],
    ]
    story.append(table(meta, [45 * mm, 125 * mm]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("VASTAMISE TÄHTAEG: 19.08.2026", s["deadline"]))
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Esita SKA iseteeninduses (vasta kirjale 'Arvamuse küsimine') "
            "või e-postiga: info@sotsiaalkindlustusamet.ee. "
            "Lisa pangaväljavõtte ekraanipildid manusena.",
            s["body"],
        )
    )
    story.append(PageBreak())


def vastuvade(story, s):
    story.append(Paragraph("1. VASTUVÄIDE", s["h1"]))
    hr(story)
    story.append(Paragraph("Lugupeetud Galina Družkova / Sotsiaalkindlustusamet", s["body"]))
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "Vastan Teie kirjale (koostamise aeg 11.08.2026) seoses ema "
            "<b>Maria-Isabelle Aluste</b> taotlusega vanemahüvitise määramiseks "
            "lapse <b>Indie Eva Alexandra Aluste</b> kasvatamise seoses.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("OTSEVASTUS", s["h2"]))
    story.append(
        Paragraph(
            "<b>Ei nõustu</b> vanemahüvitise määramisega emale Maria-Isabelle Alustele.",
            s["body_bold"],
        )
    )
    story.append(
        Paragraph(
            "<b>Ei loobu</b> oma õigusest vanemahüvitisele ega lõpeta vanemapuhkust "
            "enne Teie lõplikku otsust.",
            s["body_bold"],
        )
    )
    story.append(Spacer(1, 8))

    sections = [
        (
            "1. Praegune olukord — laps elab emaga",
            [
                "Tunnistan, et laps <b>Indie Eva Alexandra Aluste elab hetkel ema Maria-Isabelle Alustega</b>. "
                "Ma ei vaidlusta seda fakti ega esita vastupidist väidet.",
                "Minu vastuväide <b>ei põhine elukohal</b>, vaid vanemate vahelisel "
                "<b>finantskokkuleppel</b> ja lapse/leibkonna rahalistes huvides.",
            ],
        ),
        (
            "2. Vanemate finantskokkulepe",
            [
                "Meil on kehtiv kokkulepe: vanemahüvitis jääb <b>mulle (isale)</b>, "
                "kuna minu hüvitis on <b>~84 €/päev</b> (~2520 €/kuus), "
                "ema oma nimel saaks aga vaid <b>~31 €/päev</b> (~930 €/kuus).",
                "Maksan emale igakuiselt <b>tema emapalga/vanemahüvitise summa</b> "
                "— nii saab ema oma osa ja leibkonna kogusissetulek on suurem.",
                "Kokkulepe on ellu viidud <b>järjepidevalt</b> — esitan pangatõendid (vt osa 3).",
            ],
        ),
        (
            "3. SKA ametniku algne soovitus",
            [
                "See kordade seadmine oli <b>Sotsiaalkindlustusameti ametniku soovitus</b> "
                "kohe alguses, kui vanemahüvitist taotlesime.",
                "Ametnik soovitas, et hüvitis jääks <b>kõrgema määra saajale (isale)</b>, "
                "kuna see tagab perele suurima kogusumma.",
                "[TÄIDA: lisa detailid — millal, kellega vestlesite, kui on kirjalik tõend]",
                "Palun arvestada seda algset nõustamist otsuse tegemisel.",
            ],
        ),
        (
            "4. Miks ema taotlus kahjustab leibkonda",
            [
                "Kui vanemahüvitis läheb emale (~31 €/päev), kaotab leibkond "
                "<b>~53 € päevas</b> ehk <b>~1590 € kuus</b> võrreldes praeguse korraldusega.",
                "Praegu saab ema oma osa minult igakuiselt (~930–980 €) "
                "<b>PLUSS</b> leibkond säilitab vahe (~1590 €) lapse ja pere jaoks.",
                "Ema taotlus ei suurenda pere sissetulekut — see <b>vähendab</b> seda oluliselt.",
                "See on vastuolus lapse huvidega.",
            ],
        ),
        (
            "5. Järjepidevad maksed — tõendid",
            [
                "Olen maksnud emale kokkuleppe kohaselt igakuiselt. "
                "Pangas sildistatud maksed (vt finantstõendid):",
                "06.02.2026 — 864,00 € ('1. makse')",
                "08.04.2026 — 893,68 € ('elatisraha')",
                "08.05.2026 — 515,00 € ('emaduspalk')",
                "08.06.2026 — 957,43 € ('vanema palk')",
                "08.07.2026 — 945,90 € ('emapalk')",
                "07.08.2026 — 977,43 € ('vanemapalk')",
                "Lisaks regulaarsed 'toiduraha (L)' ja muud maksed.",
                "Kokku sildistatud maksed 2026: <b>5 553,44 €</b>.",
                "Maksed jätkuvad ka pärast seda, kui ema kolis eraldi elama.",
            ],
        ),
        (
            "6. Minu palve",
            [
                "Palun <b>jätkata vanemahüvitise maksmist mulle</b> kuni lõpliku otsuseni.",
                "Palun <b>mitte määrata</b> vanemahüvitist emale, kuna see kahjustaks "
                "leibkonna sissetulekut ja on vastuolus meie kokkuleppega ning "
                "algse SKA soovitusega.",
                "Olen valmis jätkama emale igakuiselt tema õigustatud summa maksmist.",
            ],
        ),
    ]

    for head, items in sections:
        story.append(Paragraph(head, s["h2"]))
        for item in items:
            story.append(Paragraph(f"• {item}", s["bullet"]))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Lugupidamisega,", s["body"]))
    story.append(Spacer(1, 6))
    sign = [
        ["Renee Aluste", ""],
        ["Isikukood:", "[TÄIDA]"],
        ["Telefon:", "[TÄIDA]"],
        ["E-post:", "[TÄIDA]"],
        ["Aadress:", "[TÄIDA]"],
        ["Kuupäev:", "17.08.2026"],
    ]
    story.append(table(sign, [35 * mm, 135 * mm]))
    story.append(PageBreak())


def kokkulepe(story, s):
    story.append(Paragraph("2. FINANTSKOKKULEPPE LOOGIKA", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "Meie argument põhineb sellel, et vanemate kokkuleppe korral "
            "saab leibkond rohkem raha, kui hüvitis määrataks emale.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Võrdlus", s["h2"]))
    cmp_rows = [
        ["", "Variant A: hüvitis ISALE (kokkulepe)", "Variant B: hüvitis EMALE"],
        ["Isa saab SKA-st", "~2520 €/kuus", "0 €"],
        ["Ema saab SKA-st", "0 €", "~930 €/kuus"],
        ["Ema saab isalt", "~930 €/kuus", "0 €"],
        ["Ema kokku", "~930 €/kuus", "~930 €/kuus"],
        ["Isa/leibkond kokku", "~2520 €/kuus", "~930 €/kuus"],
        ["LEIBKONNA KAOTUS", "—", "~1590 €/kuus"],
    ]
    story.append(table(cmp_rows, [40 * mm, 65 * mm, 65 * mm], header=True))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Kokkuleppe sisu", s["h2"]))
    for line in [
        "Vanemahüvitis jääb isale (kõrgem määr: ~84 €/päev).",
        "Isa maksab emale igakuiselt tema õigustatud summa (~930–980 €).",
        "Ema saab oma osa — ei jää ilma.",
        "Leibkond säilitab ~1590 €/kuus rohkem raha lapse ja pere jaoks.",
        "See korraldus vastab SKA ametniku algsele soovitusele.",
    ]:
        story.append(Paragraph(f"• {line}", s["bullet"]))
    story.append(PageBreak())


def finants(story, s):
    story.append(Paragraph("3. FINANTSTÕENDID", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "Maksja: Renee Aluste → Saaja: Maria-Isabelle Aluste (varem Muljar). "
            "Konto: EE3477007710... (igapäevapangandus).",
            s["body"],
        )
    )
    story.append(Spacer(1, 6))
    story.append(Paragraph("Sildistatud maksed (2026)", s["h2"]))
    pay = [
        ["Kuupäev", "Summa", "Selgitus pangas"],
        ["06.02.2026", "864,00 €", "1. makse"],
        ["08.04.2026", "893,68 €", "elatisraha"],
        ["02.05.2026", "400,00 €", "emaduspalk 1 osa"],
        ["08.05.2026", "515,00 €", "emaduspalk"],
        ["08.06.2026", "957,43 €", "vanema palk"],
        ["08.07.2026", "945,90 €", "emapalk"],
        ["07.08.2026", "977,43 €", "vanemapalk"],
    ]
    story.append(table(pay, [35 * mm, 30 * mm, 105 * mm], header=True))
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "<b>Kokku sildistatud maksed 2026: 5 553,44 €</b> + regulaarsed "
            "'toiduraha (L)' maksed ja muud toetused.",
            s["body_bold"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("Mida tõendid kinnitavad", s["h2"]))
    proof = [
        ["#", "Väide", "Tõend"],
        ["1", "Kokkulepe on reaalne", "Pangas sildistatud: vanemapalk, emapalk, emaduspalk, elatisraha"],
        ["2", "Maksed on järjepidevad", "Igakuised ülekanded alates veebruar 2026"],
        ["3", "Ema saab oma osa", "~930–980 €/kuus — ema ei jää ilma"],
        ["4", "Kokkulepe kehtib pärast lahuselu", "Maksed jätkuvad ka pärast eraldi elama asumist"],
        ["5", "Leibkond kaotaks raha", "~1590 €/kuus, kui hüvitis läheb emale"],
    ]
    story.append(table(proof, [10 * mm, 55 * mm, 105 * mm], header=True))
    story.append(PageBreak())


def olukord(story, s):
    story.append(Paragraph("4. OLUKORRA KIRJELDUS", s["h1"]))
    hr(story)
    blocks = [
        (
            "Perekonna taust",
            "Renee Aluste ja Maria-Isabelle Aluste elasid koos umbes 1–2 aastat. "
            "Tütar Indie Eva Alexandra Aluste sündis nende ühises elukohas. "
            "Renee on vanemapuhkusel (~84 €/päev). Ema oma nimel saaks ~31 €/päev.",
        ),
        (
            "Praegune elukord",
            "Ema kolis juuli lõpus 2026 eraldi elama. "
            "Laps elab hetkel ema juures. "
            "Isa ei vaidlusta lapse elukohta — see fakt on tunnistatud.",
        ),
        (
            "Finantskokkulepe",
            "Vanemate kokkulepe: hüvitis jääb isale, isa maksab emale igakuiselt "
            "tema õigustatud summa. See tagab suurima leibkonna sissetuleku. "
            "Kokkulepe vastab SKA ametniku algsele soovitusele.",
        ),
        (
            "Ema SKA taotlus",
            "11.08.2026 esitas ema taotluse vanemahüvitise saamiseks enda nimele. "
            "See kahjustaks leibkonna sissetulekut (~1590 €/kuus kaotus) "
            "ilma et ema saaks rohkem — ta saab juba oma osa isalt.",
        ),
        (
            "Isa seisukoht",
            "Renee Aluste tunnistab, et laps elab emaga. "
            "Ta palub säilitada finantskokkuleppe, sest see on lapse ja leibkonna huvides. "
            "Ta jätkab emale maksmist ja esitab tõendid järjepidevatest maksetest.",
        ),
    ]
    for head, text in blocks:
        story.append(Paragraph(head, s["h2"]))
        story.append(Paragraph(text, s["body"]))
        story.append(Spacer(1, 4))
    story.append(PageBreak())


def lisad(story, s):
    story.append(Paragraph("5. MANUSED — LISA PANGAPILDID", s["h1"]))
    hr(story)
    story.append(
        Paragraph(
            "Lisa järgmised pangaväljavõtte ekraanipildid oma SKA vastusele manusena:",
            s["body"],
        )
    )
    story.append(Spacer(1, 6))
    attachments = [
        ["Nr", "Sisu", "Kuupäev / summa"],
        ["1", "vanemapalk", "07.08.2026 — 977,43 €"],
        ["2", "emapalk + võlgade katteks", "08.07.2026 — 945,90 € + 250 €"],
        ["3", "vanema palk", "08.06.2026 — 957,43 €"],
        ["4", "emaduspalk (2 osa)", "mai 2026 — 515 € + 400 €"],
        ["5", "elatisraha", "08.04.2026 — 893,68 €"],
        ["6", "1. makse", "06.02.2026 — 864 €"],
        ["7", "toiduraha (L) maksed", "2025–2026"],
        ["8", "Otsing 'maria' — kõik maksed", "2024–2026"],
        ["9", "[TÄIDA] SKA algne nõustamine", "Kui on kirjalik tõend ametniku soovituse kohta"],
    ]
    story.append(table(attachments, [12 * mm, 70 * mm, 88 * mm], header=True))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Esitamise juhend", s["h2"]))
    for step in [
        "Täida [TÄIDA] väljad dokumendis 1. osas.",
        "Logi sisse SKA iseteenindusse.",
        "Vasta kirjale 'Arvamuse küsimine' (11.08.2026).",
        "Kopeeri vastuväide (osa 1) vastuse väljale.",
        "Lisa pangaväljavõtte ekraanipildid manusena.",
        "Saada enne tähtaega: 19.08.2026.",
    ]:
        story.append(Paragraph(f"• {step}", s["bullet"]))
    story.append(Spacer(1, 16))
    story.append(
        Paragraph(
            "Renee Aluste · Tõenduspakk · 17.08.2026 · "
            "Sotsiaalkindlustusamet — vanemahüvitis, Indie Eva Alexandra Aluste",
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
        title="Tõenduspakk — Sotsiaalkindlustusamet",
        author="Renee Aluste",
    )
    story = []
    cover(story, s)
    vastuvade(story, s)
    kokkulepe(story, s)
    finants(story, s)
    olukord(story, s)
    lisad(story, s)
    doc.build(story)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
