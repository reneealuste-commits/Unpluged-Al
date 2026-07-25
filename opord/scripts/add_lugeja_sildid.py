#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 3-line lugeja-sildid to key lisad if not present."""
from pathlib import Path

LISAD = Path(__file__).resolve().parents[1] / "lisad"

SILDID = {
    "lisa-h-kiirjuhend-kriisis-isale.md": (
        "**Lugeja saab:** kiire abi ja turvalisuse sammud kriisis.  \n",
        "**Loe seda kui:** oled p\u00f5hjas v\u00f5i peres on kriis.  \n",
        "**\u00c4ra loe kui:** oled rahulik skeptik \u2014 alusta TUUM-ist (tee B).\n",
    ),
    "lisa-n-aluste-kool.md": (
        "**Lugeja saab:** demomehe p\u00e4evase checklisti ja SOK \u00fclesanded.  \n",
        "**Loe seda kui:** oled v\u00f5i tahad saada demomeheks (tee D).  \n",
        "**\u00c4ra loe kui:** oled esimene kord \u2014 alusta PEEGEL_TUUM.pdf.\n",
    ),
    "lisa-i-inimesekeskne-juhtimine.md": (
        "**Lugeja saab:** Steigeri inimesekeskse juhtimise raamistiku.  \n",
        "**Loe seda kui:** juhid inimesi v\u00f5i koolitad (tee D/F).  \n",
        "**\u00c4ra loe kui:** otsid kiiret kriisiabi \u2014 alusta Lisa H.\n",
    ),
    "lisa-q-side-eeskirjad-ja-suhtlus.md": (
        "**Lugeja saab:** h\u00e4\u00e4le, GOTWA, kata ja liigu ning austava keele SOP.  \n",
        "**Loe seda kui:** suhtled iga p\u00e4ev inimestega (demomees).  \n",
        "**\u00c4ra loe kui:** pole veel Lisa P trauma-reeglit lugenud.\n",
    ),
    "lisa-r-kes-ma-olen-ja-taust.md": (
        "**Lugeja saab:** koordinaatori tausta ja usaldusv\u00e4\u00e4rsuse fakte.  \n",
        "**Loe seda kui:** kahtled, kes see inimene on (tee B).  \n",
        "**\u00c4ra loe kui:** usaldus on juba olemas \u2014 vali oma tee.\n",
    ),
    "lisa-t-valitsuse-ipb-analuus.md": (
        "**Lugeja saab:** hetke-anal\u00fc\u00fcsi, KPI ja ministrite profiilid.  \n",
        "**Loe seda kui:** tahad fakte ja konteksti (tee B/F, K3).  \n",
        "**\u00c4ra loe kui:** otsid lihtsat igap\u00e4evategu \u2014 alusta TUUM-ist.\n",
    ),
    "lisa-p-takistused-ja-valideerimine.md": (
        "**Lugeja saab:** trauma-reegli ja valideerimise t\u00f6\u00f6riistad.  \n",
        "**Loe seda kui:** suhtled kellelegi, kes on \u00e4revuses v\u00f5i kriisis.  \n",
        "**\u00c4ra loe kui:** pole valmis kehakesksele l\u00e4henemisele.\n",
    ),
    "lisa-m-kodaniku-identiteet-ja-vanne.md": (
        "**Lugeja saab:** kodaniku identiteedi ja LIHTSUS reegli.  \n",
        "**Loe seda kui:** tugevdad pere v\u00f5i enda identiteeti (tee C).  \n",
        "**\u00c4ra loe kui:** oled kriisis \u2014 alusta Lisa H.\n",
    ),
    "lisa-an-venekeelne-sihtruhm-ja-inimesekeskne-levitus.md": (
        "**Lugeja saab:** venekeelse kanali loogika ja levitamise reeglid.  \n",
        "**Loe seda kui:** t\u00f6\u00f6tad RU auditooriumiga (tee E).  \n",
        "**\u00c4ra loe kui:** oled ainult eestikeelne lugeja.\n",
    ),
    "lisa-ao-ultimate-power-kokkuvote.md": (
        "**Lugeja saab:** Buffalmano filtreeritud kokkuv\u00f5tte demomehele.  \n",
        "**Loe seda kui:** oled demomees v\u00f5i sportlane (tee D).  \n",
        "**\u00c4ra loe kui:** otsid trauma-teadlikku peresuhtlust \u2014 alusta Lisa P.\n",
    ),
    "lisa-ak-kodaniku-taskuraamat-peegel.md": (
        "**Lugeja saab:** taskuraamatu tr\u00fcki plaani ja formaadi.  \n",
        "**Loe seda kui:** planeerid f\u00fc\u00fcsilist tr\u00fcki (side quest).  \n",
        "**\u00c4ra loe kui:** piisab digitaalsest TUUM-ist.\n",
    ),
    "lisa-ap-swot-ja-lugeja-audit.md": (
        "**Lugeja saab:** SWOT ja 10-punkti auditi tulemuse.  \n",
        "**Loe seda kui:** tahad n\u00e4ha, kas materjal on valmis levitamiseks.  \n",
        "**\u00c4ra loe kui:** otsid praktilist igap\u00e4evategu.\n",
    ),
    "kiht0-ru-tuum-1-leht.md": (
        "**Lugeja saab:** 1-lehek\u00fcljeline venekeelne tuum.  \n",
        "**Loe seda kui:** oled venekeelne kodanik Eestis (tee E).  \n",
        "**\u00c4ra loe kui:** eesti keel on sulle piisav.\n",
    ),
    "lisa-aq-sidepakkide-jaotus-skeem.md": (
        "**Lugeja saab:** sidepakkide jaotuse skeemi.  \n",
        "**Loe seda kui:** saadad v\u00f5i koordineerid materjali.  \n",
        "**\u00c4ra loe kui:** oled lihtsalt lugeja \u2014 alusta TUUM-ist.\n",
    ),
}

MARKER = "**Lugeja saab:**"


def insert_sildid(path: Path, lines: tuple[str, str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    block = "> " + lines[0] + "> " + lines[1] + "> " + lines[2] + "\n\n"
    parts = text.split("\n", 1)
    if len(parts) < 2:
        return False
    first_line, rest = parts
    # Insert after title line and metadata before first ---
    if rest.startswith("\n"):
        rest = rest[1:]
    insert_at = 0
    if "---" in rest:
        idx = rest.index("---")
        new_text = first_line + "\n\n" + block + rest[:idx].rstrip() + "\n\n" + rest[idx:]
    else:
        new_text = first_line + "\n\n" + block + rest
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    for fname, sildid in SILDID.items():
        path = LISAD / fname
        if not path.exists():
            print(f"SKIP (missing): {fname}")
            continue
        if insert_sildid(path, sildid):
            print(f"Updated: {fname}")
        else:
            print(f"Already has sildid: {fname}")


if __name__ == "__main__":
    main()
