#!/usr/bin/env python3
"""DP1 demo soorituste koordinaator — ohutusloendid ja stsenaariumid.

Kasutus:
  python3 scripts/dp1_demo_koordinaator.py --list
  python3 scripts/dp1_demo_koordinaator.py --demo DP1-D01 --check
  python3 scripts/dp1_demo_koordinaator.py --demo DP1-D02 --run
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from typing import List

VERSION = "1.0"
PACKAGE = "DP1"

STOP_CONTACTS = [
    ("112", "Hädaabi"),
    ("116 123", "Eluliin"),
    ("116 006", "Ohvriabi infotelefon"),
    ("palunabi.ee", "Ohvriabi ja TTTVT"),
]

SAFETY_CHECKLIST = [
    "Ruum on turvaline; väljapääs vaba",
    "Keegi ei ole päris joobes / intox",
    "STOP numbrid nähtaval (112, 116 123, 116 006)",
    "Demo kood valitud",
    "Rollid selged (A=pereliige, B=sõltlane, C=vaatleja vajadusel)",
    "Koolitaja andis signaali 'Demo algab'",
    "Osalejad teavad signaali 'STOP — demo katkeb'",
]

FORBIDDEN = [
    "Füüsiline kontakt",
    "Karjumine üle 8/10 distress",
    "Solvangud rollis",
    "Päris raha / alkohol / narkootikum",
    "Demo ilma ohutusloendita",
    "Jätkamine pärast STOP signaali",
]


@dataclass
class DemoStep:
    order: int
    action: str
    minutes: int


@dataclass
class DemoScenario:
    code: str
    title: str
    duration_min: int
    roles: List[str]
    observer_required: bool
    steps: List[DemoStep] = field(default_factory=list)


DEMOS = {
    "DP1-D01": DemoScenario(
        code="DP1-D01",
        title="Esimene kontakt pärast relapsi",
        duration_min=8,
        roles=["A: pereliige", "B: sõltlane (roll)"],
        observer_required=False,
        steps=[
            DemoStep(1, "Ohutusloend (vt diplomaatia-soltlasega-demo-ohutusjuhend.md II)", 2),
            DemoStep(2, "A: 'Ma märkan, et see on raske. Kas räägime ühest asjast?'", 3),
            DemoStep(3, "B (roll): vastab vastuoluliselt", 3),
            DemoStep(4, "STOP kontroll — kas distress > 8?", 1),
            DemoStep(5, "Debrief: 1 lause 'mis muutus?'", 1),
        ],
    ),
    "DP1-D02": DemoScenario(
        code="DP1-D02",
        title="Keeldumine raha / ostmisest",
        duration_min=6,
        roles=["A: pereliige", "B: sõltlane (roll)"],
        observer_required=False,
        steps=[
            DemoStep(1, "Ohutusloend", 2),
            DemoStep(2, "B (roll): palub raha 'ainult üks kord'", 2),
            DemoStep(3, "A: piir ilma enablinguta", 3),
            DemoStep(4, "Debrief: 1 lause", 1),
        ],
    ),
    "DP1-D03": DemoScenario(
        code="DP1-D03",
        title="Kriis — de-eskalatsioon",
        duration_min=8,
        roles=["A: pereliige", "B: sõltlane (roll)", "C: vaatleja (KOHUSTUSLIK)"],
        observer_required=True,
        steps=[
            DemoStep(1, "Ohutusloend + vaatleja C kohustuslik", 2),
            DemoStep(2, "B (roll): nutab, ähvardab 'kui sa mind ei aita…'", 4),
            DemoStep(3, "A: peegeldab, ei enablinguta, STOP valmis", 4),
            DemoStep(4, "Debrief", 2),
        ],
    ),
    "DP1-D04": DemoScenario(
        code="DP1-D04",
        title="Suunamine abile (ÕnneKlubi / arst)",
        duration_min=6,
        roles=["A: pereliige", "B: sõltlane (roll)"],
        observer_required=False,
        steps=[
            DemoStep(1, "Ohutusloend", 2),
            DemoStep(
                2,
                "A: 'Ma ei ravi sind. Ma võin rääkida abist, kui sina tahad.'",
                4,
            ),
            DemoStep(3, "B (roll): vastab skeptiliselt", 3),
            DemoStep(4, "Debrief", 1),
        ],
    ),
}


def print_header():
    print(f"{'=' * 60}")
    print(f"  {PACKAGE} DEMO KOORDINAATOR v{VERSION}")
    print(f"  Seotud: diplomaatia-soltlasega-demo-ohutusjuhend.md")
    print(f"{'=' * 60}\n")


def cmd_list():
    print_header()
    print("SAADAVAL DEMOD:\n")
    for code, demo in DEMOS.items():
        obs = " [vaatleja KOHUSTUSLIK]" if demo.observer_required else ""
        print(f"  {code}  {demo.title}  (~{demo.duration_min} min){obs}")
    print("\nSTOP kontaktid:")
    for num, label in STOP_CONTACTS:
        print(f"  {num:12} {label}")
    print()


def cmd_check(demo_code: str) -> int:
    if demo_code not in DEMOS:
        print(f"VIGA: Tundmatu demo '{demo_code}'. Kasuta --list", file=sys.stderr)
        return 1

    demo = DEMOS[demo_code]
    print_header()
    print(f"DEMO: {demo.code} — {demo.title}\n")
    print("OHUTUSLOEND (kõik peavad olema JA):\n")
    for i, item in enumerate(SAFETY_CHECKLIST, 1):
        print(f"  [ ] {i}. {item}")
    print("\nKEELATUD:\n")
    for item in FORBIDDEN:
        print(f"  ✗ {item}")
    if demo.observer_required:
        print("\n⚠ HOIATUS: Selle demo puhul on vaatleja C KOHUSTUSLIK.")
    print("\nKui kõik on JA → demo võib alata. Signaal: 'Demo algab'")
    print("STOP signaal: 'STOP — demo katkeb' või tõstetud käsi\n")
    return 0


def cmd_run(demo_code: str) -> int:
    if demo_code not in DEMOS:
        print(f"VIGA: Tundmatu demo '{demo_code}'.", file=sys.stderr)
        return 1

    demo = DEMOS[demo_code]
    print_header()
    print(f"DEMO SOORITUS: {demo.code} — {demo.title}\n")
    print("Rollid:", ", ".join(demo.roles))
    print(f"Kestus: ~{demo.duration_min} min\n")
    print("JÄRJEKORD:\n")
    for step in demo.steps:
        print(f"  {step.order}. [{step.minutes} min] {step.action}")
    print("\nPärast demot: debrief 1 lause (vt debrief-kaart-malevapealik.pdf)\n")
    return 0


def main():
    parser = argparse.ArgumentParser(description="DP1 demo koordinaator")
    parser.add_argument("--list", action="store_true", help="Näita demo nimekirja")
    parser.add_argument("--demo", type=str, help="Demo kood (nt DP1-D01)")
    parser.add_argument(
        "--check", action="store_true", help="Näita ohutusloendit enne demot"
    )
    parser.add_argument(
        "--run", action="store_true", help="Näita demo soorituse järjekorda"
    )
    args = parser.parse_args()

    if args.list:
        cmd_list()
        return 0

    if not args.demo:
        parser.print_help()
        return 1

    if args.check:
        return cmd_check(args.demo)
    if args.run:
        return cmd_run(args.demo)

    return cmd_check(args.demo)


if __name__ == "__main__":
    sys.exit(main())
