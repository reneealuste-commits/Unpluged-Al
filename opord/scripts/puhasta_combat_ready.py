#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove Combat Ready branding from OPORD markdown sources."""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TARGETS = [BASE / "OPERATSIOON_PEEGEL_OPORD.md", *list((BASE / "lisad").glob("*.md"))]

DISCLAIMER_OLD = (
    "> **\u26a0\ufe0f Combat Ready \u2014 br\u00e4ndi eristamine (26.07.2026):** "
    "Operatsioon \u201ePeegel\u201c on **Renee Aluste kodanikualgatus** (reneealuste.com). "
    "See **ei ole** Combat Ready O\u00dc toode, koolitus ega \u00e4rikanal. "
    "M\u00f5ned isikud OPORD-is on CR-ga seotud **isikliku kogemuse** t\u00f5ttu \u2014 "
    "see ei t\u00e4henda operatsioonilist toetust. K\u00fcsimused operatsiooni kohta: Renee. "
    "K\u00fcsimused koolituse kohta: combatready.eu. T\u00e4ielik plaan: "
    "[`strateegia-eraldumine-combat-ready.md`](kommunikatsioon/strateegia-eraldumine-combat-ready.md).\n\n"
)
DISCLAIMER_NEW = (
    "> **Operatsioon \u201ePeegel\u201c** on **Renee Aluste kodanikualgatus** (reneealuste.com). "
    "See ei ole \u00fchtegi koolitusfirma toode ega \u00e4rikanal.\n\n"
)
DISCLAIMER_PARTIAL = re.compile(
    r"> \*\*.*?br\u00e4ndi eristamine.*?\n\n",
    re.DOTALL,
)


def strip_cr_sections(text: str) -> str:
    text = re.sub(
        r"#### Remo Ojaste \u2014.*?(?=\n#### |\n## |\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"#### Combat Ready \| Her Way.*?(?=\n#### |\n## |\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    text = text.replace(
        "#### Tanel J\u00e4ppinen \u2014 Combat Ready Youth",
        "#### Tanel J\u00e4ppinen \u2014 Noorte- ja peretase (Laste Superm\u00e4ngud)",
    )
    text = text.replace(
        "## V. Combat Ready ja partnerid\n",
        "## V. Partnerid ja v\u00f5rgustik\n",
    )
    text = re.sub(
        r"\*\*K: Kas Combat Ready teenib.*?\*Minu k\u00fcsimus sulle:.*?\n---\n",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\*\*K: Mis on Combat Ready for Her.*?\*Minu k\u00fcsimus sulle:.*?\n---\n",
        "",
        text,
        flags=re.DOTALL,
    )
    return text


def replace_cr_phrases(text: str) -> str:
    text = DISCLAIMER_PARTIAL.sub(DISCLAIMER_NEW, text)
    reps = [
        (DISCLAIMER_OLD, DISCLAIMER_NEW),
        ("Combat Ready | Her Way (naised). ", ""),
        ("Combat Ready Youth ja Laste Superm\u00e4ngud", "Laste Superm\u00e4ngud"),
        ("Combat Ready Youth / Laste Superm\u00e4ngud", "Laste Superm\u00e4ngud"),
        ("Combat Ready Youth programmide", "noorteprogrammide"),
        ("Combat Ready Youth O\u00dc", "Parenting Solutions O\u00dc"),
        ("Combat Ready instruktor ja juhendaja", "juhtimisinstruktor ja juhendaja"),
        ("Combat Ready instruktor; ", "juhtimiskoolitaja; "),
        ("Combat Ready instruktor", "juhtimiskoolitaja (endine, 2023\u20132026)"),
        ("Combat Ready kaasasutaja", "ettev\u00f5tja ja juhtimiskoolituse kogemus"),
        ("Combat Ready tegevdirektor", "ettev\u00f5tja"),
        ("Combat Ready CEO Remo Ojaste", "ettev\u00f5tja Remo Ojaste"),
        ("Combat Ready juhtimisliini", "juhtimiskoolituse liini"),
        ("Combat Ready liikumist", "liikumist"),
        ("Combat Ready koolitusruumid", "kogukonna keskused"),
        ("Combat Ready koolituste", "v\u00f5rgustiku koolituste"),
        ("Combat Ready koolitused", "juhtimiskoolitused"),
        ("Combat Ready koolitusele", "juhtimiskoolitusele"),
        ("Combat Ready ja v\u00f5rgustiku", "v\u00f5rgustiku"),
        ("Combat Ready ja Kaitseliidu", "Kaitseliidu"),
        ("Combat Ready partnerlust", "partnerlust"),
        ("Combat Ready partner", "koost\u00f6\u00f6partner"),
        ("Combat Ready p\u00f5him\u00f5tetel", "juhtimisp\u00f5him\u00f5tetel"),
        ("Combat Ready meeskond", "v\u00f5rgustiku partnerid"),
        ("Combat Ready meeskonna", "v\u00f5rgustiku"),
        ("Combat Ready statistika", "v\u00f5rgustiku statistika"),
        ("Combat Ready blogi", "avalikud intervjuud"),
        ("Combat Ready Podcast", "Frontline podcast"),
        ("combatreadyherway.eu", "naiste enesejuhtimise kogukond"),
        ("combatready.eu", "reneealuste.com"),
        ("combatready.ee", "reneealuste.com"),
        ("@combatreadyee", "@reneealuste"),
        ("remo.ojaste@combatready.eu", "partnerlus (isiklik kontakt)"),
        ("priit.lillevali@combatready.eu", "partnerlus (isiklik kontakt)"),
        ("tanel.jappinen@combatready.eu", "partnerlus (isiklik kontakt)"),
        ("info@combatready.ee", "reneealuste.com"),
        (
            "Combat Ready (+ Her Way, Youth/Superm\u00e4ngud, Pertinax)",
            "Juhtimiskoolitus, noored (Superm\u00e4ngud), Pertinax",
        ),
        (
            "Combat Ready (+ Her Way, Youth, Pertinax)",
            "Juhtimiskoolitus, noored, Pertinax",
        ),
        ("Remo Ojaste / Combat Ready", "Remo Ojaste (isiklik taust)"),
        ("PPA / Combat Ready", "PPA"),
        ("Tanel J\u00e4ppinen / Combat Ready Youth", "Tanel J\u00e4ppinen"),
        ("Combat Ready | Her Way", "Naiste enesejuhtimise kogukond"),
        ("Combat Ready for Her / Her Way", "Naiste enesejuhtimise kogukond"),
        ("Combat Ready for Her", "Naiste enesejuhtimise kogukond"),
        ("Combat Ready Her Way", "naiste enesejuhtimise kanal"),
        ("Combat Ready Youth", "noorteprogramm"),
        ("Combat Ready ", ""),
        ("Combat Ready\n", "\n"),
        ("Combat Ready.", "."),
        ("Combat Ready,", ","),
        ("Combat Ready)", ")"),
        ("(Combat Ready", "("),
        ("| Combat Ready", "|"),
        (
            "koos Combat Ready meeskonna ja partneritega",
            "koos v\u00f5rgustiku partneritega",
        ),
        (
            "Villido ei asenda Combat Readyt ega tantralaagreid",
            "Villido ei asenda teisi teid",
        ),
        (
            "Tule Combat Ready koolitusele, kui tahad s\u00fcgavamat juhtimistreeningut. ",
            "",
        ),
        (
            "Martin J\u00f5esaar \u2014 Euroopa tase (Combat Ready kaasasutaja)",
            "Martin J\u00f5esaar \u2014 Euroopa tase",
        ),
        (
            "Echelon Fronti (Jocko Willink, Leif Babin) ametlik partner",
            "Echelon Front kogemus (isiklik taust)",
        ),
        ("CR Youth", "noorteprogramm"),
        ("CR statistika", "v\u00f5rgustiku statistika"),
        ("ei ole CR toode", "ei ole koolitusfirma toode"),
        ("koos KVA, CR)", "koos KVA)"),
        ("koost\u00f6\u00f6 CR,", "koost\u00f6\u00f6 partneritega,"),
        ("T\u00f6\u00f6, CR, kool", "T\u00f6\u00f6, kool"),
        ("KOV, ettev\u00f5tted, CR", "KOV, ettev\u00f5tted"),
        (
            "images/profiles/combat-ready-her-way.jpg",
            "images/profiles/naiste-enesejuhtimine.jpg",
        ),
        (
            "https://reneealuste.com/combat-ready-team-member-renee-aluste",
            "https://reneealuste.com",
        ),
        (
            "### (Remo Ojaste, Priit Lillev\u00e4li, meeskond)",
            "### Juhtimiskoolituse partnerid",
        ),
        (
            "**Juhtimiskett:** Renee Aluste \u2192 Remo Ojaste \u2192 v\u00f5rgustiku liikmed",
            "**Juhtimiskett:** Renee Aluste \u2192 v\u00f5rgustiku liikmed",
        ),
        ("| \u00c4ri/taktika | Remo Ojaste |", "| Juhtimiskoolitus | Partnerid |"),
        ("remo.ojaste@reneealuste.com", "partnerlus (isiklik kontakt)"),
        ("**Koordineerija:** Renee Aluste \u00b7 tugi: Remo Ojaste (isiklik taust)", "**Koordineerija:** Renee Aluste"),
        ("Remo Ojaste on pakkunud", "Partner on pakkunud"),
        ("| Levituse ja \u00e4ri | **Remo Ojaste** / |", "| Levituse ja \u00e4ri | Partnerid |"),
        ("| Toetus | Remo Ojaste (isiklik taust) |", "| Toetus | Juhtimiskoolituse partnerid |"),
    ]
    for old, new in reps:
        text = text.replace(old, new)
    text = text.replace(
        "\u2502 Combat Ready        \u2502",
        "\u2502 Juhtimiskoolitus    \u2502",
    )
    text = text.replace(
        "\u2502 \u2514\u2500 Remo, Priit\u2026     \u2502",
        "\u2502 \u2514\u2500 Priit, partnerid \u2502",
    )
    text = re.sub(
        r"\| Taktikaline \| Combat Ready.*?\|",
        "| Taktikaline | Juhtimiskoolitus, noored, Pertinax | Juhtimiskoolitus |",
        text,
    )
    text = re.sub(
        r"\| Toetus \| Remo Ojaste / Combat Ready.*?\|",
        "| Toetus | Juhtimiskoolituse partnerid | Isiklik kogemus |",
        text,
    )
    text = re.sub(
        r"### Combat Ready \(Remo Ojaste.*?\n(?:\d\..*\n)+",
        "",
        text,
    )
    text = re.sub(
        r"### Combat Ready \| Her Way.*?\n(?:\d\..*\n)+",
        "",
        text,
    )
    text = re.sub(r"  +", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def process_file(path: Path) -> bool:
    if "strateegia-eraldumine-combat-ready" in path.name:
        return False
    raw = path.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("utf-8", errors="replace")
    new = strip_cr_sections(replace_cr_phrases(text))
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for path in sorted(TARGETS):
        if path.exists() and process_file(path):
            changed.append(path.relative_to(BASE))
    print(f"Updated {len(changed)} files")
    for p in changed:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
