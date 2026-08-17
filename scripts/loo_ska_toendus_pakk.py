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
LIGHT = colors.HexColor("#E8EAF6")
DARK = colors.HexColor("#212121")
GRAY = colors.HexColor("#616161")
RED = colors.HexColor("#B71C1C")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Heading1"],
            fontSize=18,
            textColor=NAVY,
            spaceAfter=6,
            fontName="Helvetica-Bold",
            alignment=TA_CENTER,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontSize=10,
            textColor=GRAY,
            spaceAfter=10,
            alignment=TA_CENTER,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontSize=14,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=6,
            fontName="Helvetica-Bold",
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontSize=11,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=4,
            fontName="Helvetica-Bold",
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK,
            alignment=TA_JUSTIFY,
        ),
        "body_bold": ParagraphStyle(
            "BodyBold",
            parent=base["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK,
            fontName="Helvetica-Bold",
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontSize=10,
            leading=14,
            leftIndent=12,
            textColor=DARK,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontSize=8,
            leading=10,
            textColor=GRAY,
        ),
        "fill": ParagraphStyle(
            "Fill",
            parent=base["Normal"],
            fontSize=10,
            leading=14,
            textColor=RED,
            fontName="Helvetica-Oblique",
        ),
        "deadline": ParagraphStyle(
            "Deadline",
            parent=base["Normal"],
            fontSize=11,
            textColor=RED,
            fontName="Helvetica-Bold",
            alignment=TA_CENTER,
            spaceAfter=8,
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
        style.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        )
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
        ["Koostatud:", "12.08.2026"],
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
            "1. Olen lapse peamine igapäevane hooldaja",
            [
                "Olen lapse isa Renee Aluste. Olen praegu <b>vanemapuhkusel</b> (töötamisregistri andmed).",
                "Olen lapse eest hoolitsenud alates sündimisest.",
                "Laps Indie Eva Alexandra Aluste sündis meie ühises elukohas aadressil:",
                "<i>[TÄIDA: korteri täisaadress, linn]</i>",
                "Elasime emaga selles korteris koos umbes 1–2 aastat. See on lapse kodune keskkond alates sündimisest.",
            ],
        ),
        (
            "2. Laps ei elanud ema juures taotluse esitamise ajal",
            [
                "<b>Juuli lõpp 2026 (umbes 21.–31. juuli):</b> Ema Maria-Isabelle Aluste kolis välja meie ühisest elukohast oma eraldi korterisse.",
                "<b>Oluline:</b> Laps <b>jäi minu juurde</b>. Ema lahkus üksi — laps ei kolinud koos temaga.",
                "<b>31. juuli – 12. august 2026:</b> Olin lapse ainus igapäevane hooldaja (~2 nädalat).",
                "<b>12. august 2026:</b> Ema võttis lapse minu juurest ilma minu nõusolekuta.",
                "<b>11. august 2026</b> (Teie kirja kuupäev): Ema esitas taotluse, viidates, et laps elab temaga. "
                "<b>See ei vastanud tõele</b> — laps elas minu juures kuni 12.08.2026.",
                "Lapse tegelik elukoht on minu korter, kus ta on elanud alates sündimisest.",
            ],
        ),
        (
            "3. Kehtiv finantskokkulepe — ema saab juba raha",
            [
                "Vanemahüvitis jääb mulle (~84 €/päev), maksan emale igakuiselt tema õigustatud osa (~31 €/päev ≈ ~930 €/kuus).",
                "Kokkulepe on ellu viidud pangas sildistatud ülekannetega (vt finantstõendid).",
                "Viimane makse: <b>07.08.2026 — 977,43 € ('vanemapalk')</b> — pärast ema väljakolimist.",
                "Ema taotluse eesmärk <b>ei ole lapse rahaline huvi</b> — ema saab juba raha, mida ta vanemahüvitise korral saaks.",
            ],
        ),
        (
            "4. Ema taotlus kahjustab lapse huve",
            [
                "Kui vanemahüvitis läheks emale (~31 €/päev), kaotaks pere <b>~53 € päevas</b> ehk <b>~1590 € kuus</b>, "
                "mis praegu läheb lapse kasvatamiseks.",
            ],
        ),
        (
            "5. Palun uurida tegelikku olukorda",
            [
                "Palun teha päring lapse elukohajärgsele kohalikule omavalitsusele ja vajadusel <b>koduvisiit</b>.",
                "Selgitada: kus laps elas enne 12.08.2026; kes igapäevaselt hoolitseb; kas ema väide vastab tõele.",
            ],
        ),
        (
            "6. Kontaktisikud uurimisel",
            [
                "Sotsiaaltöötaja: [TÄIDA: nimi, amet, telefon, e-post]",
                "Lastekaitse: [TÄIDA: nimi, üksus, telefon]",
                "Politsei: [TÄIDA: juhtumi number, kontakt]",
            ],
        ),
    ]

    for head, items in sections:
        story.append(Paragraph(head, s["h2"]))
        for item in items:
            story.append(Paragraph(f"• {item}", s["bullet"]))
        story.append(Spacer(1, 4))

    story.append(Paragraph("PALVE", s["h2"]))
    story.append(
        Paragraph(
            "Palun <b>jätkata vanemahüvitise maksmist mulle</b> kuni Teie lõpliku otsuseni. "
            "Palun <b>mitte määrata</b> vanemahüvitist emale.",
            s["body"],
        )
    )
    story.append(Spacer(1, 12))
    story.append(Paragraph("Lugupidamisega,", s["body"]))
    story.append(Spacer(1, 6))
    sign = [
        ["Renee Aluste", ""],
        ["Isikukood:", "[TÄIDA]"],
        ["Telefon:", "[TÄIDA]"],
        ["E-post:", "[TÄIDA]"],
        ["Aadress:", "[TÄIDA: korteri täisaadress]"],
        ["Kuupäev:", "12.08.2026"],
    ]
    story.append(table(sign, [35 * mm, 135 * mm]))
    story.append(PageBreak())


def ajajoon(story, s):
    story.append(Paragraph("2. AJAJOON", s["h1"]))
    hr(story)
    rows = [
        ["Kuupäev / periood", "Sündmus", "Tähendus"],
        ["~2024–2025", "Ühine elu Renee korteris", "Lapse kodune keskkond"],
        ["[TÄIDA: sünnikuupäev]", "Indie sündis Renee korteris", "Elukoht alates sündimisest"],
        ["Juuli lõpp 2026\n(~21.–31.07)", "Maria kolis välja", "Laps JÄI isa juurde"],
        ["31.07 – 12.08.2026", "Laps elas isa juures", "Isa ainus hooldaja (~2 nädalat)"],
        ["07.08.2026", "Makse 977,43 € ('vanemapalk')", "Kokkulepe kehtib pärast lahkumist"],
        ["11.08.2026", "SKA: ema taotlus", "Väide 'laps elab emaga' — ei vasta tõele"],
        ["12.08.2026", "Ema võttis lapse", "Ilma isa nõusolekuta"],
    ]
    story.append(table(rows, [40 * mm, 55 * mm, 75 * mm], header=True))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Olulised järeldused", s["h2"]))
    for line in [
        "Lapse kodune keskkond on Renee korter (sündimisest kuni 12.08.2026).",
        "Ema lahkus enne lapse võtmist — laps ei olnud ema juures loomulik elukoht.",
        "Ema SKA taotlus (11.08) esitati, kui laps veel elas isa juures.",
        "Lapse äravõtmine (12.08) toimus pärast taotluse esitamist — taktikaline samm.",
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
    story.append(Paragraph("Kokkulepe", s["h2"]))
    story.append(
        table(
            [
                ["Pool", "Hüvitis", "Kuusumma"],
                ["Renee Aluste (isa)", "~84 €/päev", "~2520 €/kuus"],
                ["Maria-Isabelle Aluste (ema)", "~31 €/päev", "~930 €/kuus"],
                ["Erinevus (lapse kasuks)", "~53 €/päev", "~1590 €/kuus"],
            ],
            [55 * mm, 45 * mm, 70 * mm],
            header=True,
        )
    )
    story.append(Spacer(1, 10))
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
            "<b>Kokku sildistatud maksed 2026: 5 553,44 €</b> + regulaarsed 'toiduraha (L)' maksed.",
            s["body_bold"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("Mida tõendid kinnitavad", s["h2"]))
    proof = [
        ["#", "Väide", "Tõend"],
        ["1", "Kokkulepe on reaalne", "Pangas sildistatud vanemapalk, emaduspalk, elatisraha"],
        ["2", "Ema saab juba raha", "~930–980 €/kuus — rohkem kui SKA hüvitis emale"],
        ["3", "Kokkulepe kehtib pärast lahuselu", "Viimane makse 07.08.2026"],
        ["4", "Taotluse eesmärk ei ole raha", "Ema saab juba ekvivalendi"],
        ["5", "Pere kaotaks raha", "~1590 €/kuus, kui hüvitis läheb emale"],
    ]
    story.append(table(proof, [10 * mm, 55 * mm, 105 * mm], header=True))
    story.append(PageBreak())


def olukord(story, s):
    story.append(Paragraph("4. OLUKORRA KIRJELDUS", s["h1"]))
    hr(story)
    blocks = [
        (
            "Perekonna taust",
            "Renee Aluste ja Maria-Isabelle Aluste elasid koos Renee korteris ~1–2 aastat. "
            "Tütar Indie Eva Alexandra Aluste sündis selles korteris. "
            "Renee on olnud peamine hooldaja ja on vanemapuhkusel (~84 €/päev).",
        ),
        (
            "Ema väljakolimine",
            "Juuli lõpus 2026 kolis ema välja ühisest elukohast. Laps jäi isa juurde ~2 nädalaks. "
            "Renee oli ainus igapäevane hooldaja.",
        ),
        (
            "Finantskokkulepe",
            "Isa maksab emale igakuiselt ~930–980 €. Viimane makse 07.08.2026 (977,43 €, 'vanemapalk'). "
            "Pere säilitab ~1590 €/kuus rohkem raha lapse jaoks.",
        ),
        (
            "SKA taotlus ja lapse äravõtmine",
            "11.08.2026 esitas ema taotluse — väitis, et laps elab temaga. "
            "Tegelikkuses elas laps isa juures kuni 12.08.2026, mil ema võttis ta ilma nõusolekuta.",
        ),
        (
            "E-kirjadele mitte vastamine",
            "Ema väide 'kuritarvitamine' ei vasta tõele. Isa seab piire surve eest, "
            "kuid maksab emale edasi kokkuleppe kohaselt.",
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
    ]
    story.append(table(attachments, [12 * mm, 70 * mm, 88 * mm], header=True))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Esitamise juhend", s["h2"]))
    for step in [
        "Täida punased [TÄIDA] väljad dokumendis 1. osas.",
        "Logi sisse SKA iseteenindusse.",
        "Vasta kirjale 'Arvamuse küsimine' (11.08.2026).",
        "Kopeeri vastuväide (osa 1) vastuse väljale.",
        "Lisa pangaväljavõtte ekraanipildid manusena.",
        "Saada enne tähtaega: 19.08.2026.",
    ]:
        story.append(Paragraph(f"{step}", s["bullet"]))
    story.append(Spacer(1, 16))
    story.append(
        Paragraph(
            "Renee Aluste · Tõenduspakk · 12.08.2026 · "
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
    ajajoon(story, s)
    finants(story, s)
    olukord(story, s)
    lisad(story, s)
    doc.build(story)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
