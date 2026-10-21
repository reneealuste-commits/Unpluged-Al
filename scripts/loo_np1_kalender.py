#!/usr/bin/env python3
"""Genereerib NP1 protokolli kalendrikutsed (.ics) ja Google Calendar lingid."""

import urllib.parse
from datetime import date
from pathlib import Path

CAL_DIR = Path("/workspace/np1-calendar")
TODAY = date.today()

# Kellaaegad (kohalik Eesti aeg), kestused minutites
EVENTS = [
    {
        "id": "hommik",
        "file": "NP1-hommik.ics",
        "summary": "NP1 Hommik — MB, Mag, seened, nikotiin",
        "start": "07:00",
        "duration_min": 30,
        "description": (
            "NEUROLOGY PROTOCOL — hommik\\n"
            "• Methylene Blue 1 mg/kg\\n"
            "• Neuro Mag (Mg L-Threonate) 3×144 mg\\n"
            "• Lion's Mane 2000 mg\\n"
            "• Turkey Tail 2000 mg\\n"
            "• Nikotiin (vajadusel)"
        ),
        "google_title": "NP1 Hommik — MB, Mag, seened",
    },
    {
        "id": "keskpäev",
        "file": "NP1-keskpaev.ics",
        "summary": "NP1 Keskpäev — punane valgus + toidulisandid",
        "start": "12:30",
        "duration_min": 30,
        "description": (
            "NEUROLOGY PROTOCOL — keskpäev\\n"
            "• Punane valgus 63 mW/cm², 20 min\\n"
            "• Peet 3000 mg\\n"
            "• Omega-3 1280 mg\\n"
            "• Pärm 1–3 spl\\n"
            "• Kurkumiin 400 mg"
        ),
        "google_title": "NP1 Keskpäev — valgus + lisandid",
    },
    {
        "id": "loodus",
        "file": "NP1-loodus.ics",
        "summary": "NP1 Õhtu — 1 h looduses",
        "start": "17:30",
        "duration_min": 60,
        "description": (
            "NEUROLOGY PROTOCOL — loodus\\n"
            "• 1 tund looduses (mets, park, raba)\\n"
            "• Tallinn: Pääsküla raba, Nõmme, Kadriorg"
        ),
        "google_title": "NP1 Õhtu — 1 h looduses",
    },
    {
        "id": "loojang",
        "file": "NP1-loojang.ics",
        "summary": "NP1 Päikeseloojang — melatoniin + glutatioon",
        "start": "20:30",
        "duration_min": 15,
        "description": (
            "NEUROLOGY PROTOCOL — loojang\\n"
            "• Melatoniin 200 mg\\n"
            "• L-Glutathione 250 mg\\n"
            "• Kohanda kellaaega hooajaliselt"
        ),
        "google_title": "NP1 Loojang — melatoniin + glutatioon",
    },
    {
        "id": "meditatsioon",
        "file": "NP1-meditatsioon.ics",
        "summary": "NP1 Öö — meditatsioon 35 min",
        "start": "22:00",
        "duration_min": 35,
        "description": (
            "NEUROLOGY PROTOCOL — öö\\n"
            "• Meditatsioon / mindfulness 35 min\\n"
            "• Insight Timer või vaikus"
        ),
        "google_title": "NP1 Meditatsioon 35 min",
    },
    {
        "id": "varahommik",
        "file": "NP1-varahommik.ics",
        "summary": "NP1 Varahommik — mikrodose",
        "start": "05:30",
        "duration_min": 15,
        "description": "NEUROLOGY PROTOCOL — varahommik (protokolli järgi)",
        "google_title": "NP1 Varahommik",
    },
]


def _parse_time(t: str) -> tuple[int, int]:
    h, m = t.split(":")
    return int(h), int(m)


def _add_minutes(h: int, m: int, delta: int) -> tuple[int, int]:
    total = h * 60 + m + delta
    return total // 60 % 24, total % 60


def _fmt_dt(d: date, h: int, m: int) -> str:
    return f"{d.strftime('%Y%m%d')}T{h:02d}{m:02d}00"


def make_ics(event: dict) -> str:
    sh, sm = _parse_time(event["start"])
    eh, em = _add_minutes(sh, sm, event["duration_min"])
    uid = f"np1-{event['id']}@unpluged-al"
    desc = event["description"].replace("\\n", "\n")
    return f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Unpluged-Al//NP1-LINN//ET
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VTIMEZONE
TZID:Europe/Tallinn
BEGIN:STANDARD
DTSTART:19701025T040000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
TZOFFSETFROM:+0300
TZOFFSETTO:+0200
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700329T030000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
TZOFFSETFROM:+0200
TZOFFSETTO:+0300
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{_fmt_dt(TODAY, 10, 0)}Z
DTSTART;TZID=Europe/Tallinn:{_fmt_dt(TODAY, sh, sm)}
DTEND;TZID=Europe/Tallinn:{_fmt_dt(TODAY, eh, em)}
RRULE:FREQ=DAILY
SUMMARY:{event['summary']}
DESCRIPTION:{desc}
STATUS:CONFIRMED
BEGIN:VALARM
TRIGGER:-PT10M
ACTION:DISPLAY
DESCRIPTION:{event['summary']}
END:VALARM
END:VEVENT
END:VCALENDAR
"""


def make_google_link(event: dict) -> str:
    sh, sm = _parse_time(event["start"])
    eh, em = _add_minutes(sh, sm, event["duration_min"])
    params = {
        "action": "TEMPLATE",
        "text": event["google_title"],
        "dates": f"{_fmt_dt(TODAY, sh, sm)}/{_fmt_dt(TODAY, eh, em)}",
        "details": event["description"].replace("\\n", "\n"),
        "recur": "RRULE:FREQ=DAILY",
        "ctz": "Europe/Tallinn",
    }
    return "https://calendar.google.com/calendar/render?" + urllib.parse.urlencode(params)


def make_outlook_link(event: dict) -> str:
    sh, sm = _parse_time(event["start"])
    eh, em = _add_minutes(sh, sm, event["duration_min"])
    start = f"{TODAY.isoformat()}T{sh:02d}:{sm:02d}:00"
    end = f"{TODAY.isoformat()}T{eh:02d}:{em:02d}:00"
    params = {
        "path": "/calendar/action/compose",
        "rru": "addevent",
        "subject": event["google_title"],
        "startdt": start,
        "enddt": end,
        "body": event["description"].replace("\\n", "\n"),
        "recurrence": "daily",
    }
    return "https://outlook.live.com/calendar/0/deeplink/compose?" + urllib.parse.urlencode(params)


def make_combined_ics() -> str:
    parts = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Unpluged-Al//NP1-LINN-ALL//ET",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VTIMEZONE",
        "TZID:Europe/Tallinn",
        "BEGIN:STANDARD",
        "DTSTART:19701025T040000",
        "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU",
        "TZOFFSETFROM:+0300",
        "TZOFFSETTO:+0200",
        "END:STANDARD",
        "BEGIN:DAYLIGHT",
        "DTSTART:19700329T030000",
        "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU",
        "TZOFFSETFROM:+0200",
        "TZOFFSETTO:+0300",
        "END:DAYLIGHT",
        "END:VTIMEZONE",
    ]
    for event in EVENTS:
        sh, sm = _parse_time(event["start"])
        eh, em = _add_minutes(sh, sm, event["duration_min"])
        uid = f"np1-{event['id']}@unpluged-al"
        desc = event["description"].replace("\\n", "\n")
        parts.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{_fmt_dt(TODAY, 10, 0)}Z",
                f"DTSTART;TZID=Europe/Tallinn:{_fmt_dt(TODAY, sh, sm)}",
                f"DTEND;TZID=Europe/Tallinn:{_fmt_dt(TODAY, eh, em)}",
                "RRULE:FREQ=DAILY",
                f"SUMMARY:{event['summary']}",
                f"DESCRIPTION:{desc}",
                "STATUS:CONFIRMED",
                "BEGIN:VALARM",
                "TRIGGER:-PT10M",
                "ACTION:DISPLAY",
                f"DESCRIPTION:{event['summary']}",
                "END:VALARM",
                "END:VEVENT",
            ]
        )
    parts.append("END:VCALENDAR")
    return "\n".join(parts) + "\n"


def generate_all() -> dict:
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    links = {"google": [], "outlook": [], "ics": []}

    for event in EVENTS:
        path = CAL_DIR / event["file"]
        path.write_text(make_ics(event), encoding="utf-8")
        links["ics"].append((event["summary"], event["file"]))

    combined = CAL_DIR / "NP1-koik-meeldetuletused.ics"
    combined.write_text(make_combined_ics(), encoding="utf-8")
    links["ics"].append(("KÕIK korraga (6 meeldetuletust)", "NP1-koik-meeldetuletused.ics"))

    for event in EVENTS:
        links["google"].append((event["google_title"], make_google_link(event)))
        links["outlook"].append((event["google_title"], make_outlook_link(event)))

    return links


if __name__ == "__main__":
    generate_all()
    print(f"Salvestatud: {CAL_DIR}/ ({len(EVENTS) + 1} .ics faili)")
