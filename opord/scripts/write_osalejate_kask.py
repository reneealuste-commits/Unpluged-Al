#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate participant email list and customized per-person instructions."""
import csv
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "kommunikatsioon"
CSV_FILE = OUT_DIR / "osalejate-emailid.csv"
KASK_FILE = OUT_DIR / "osalejate-kohandatud-kask.md"
KIRJAD_DIR = OUT_DIR / "kirjad"

# Each entry: name, email, org, roll, eesmark, ulesanded (list), kaitumine, pakett, kanal, märkus
PARTICIPANTS = [
    {
        "name": "Tanel J\u00e4ppinen",
        "email": "",
        "org": "Parenting Solutions / Laste Superm\u00e4ngud",
        "roll": "Noorte- ja peretasandi juht; Laste Superm\u00e4ngud",
        "eesmark": "Noorte praktiline vastutus enne algoritmi",
        "ulesanded": [
            "Integreeri PEEGEL_TEE_C (pere) noorte programmidesse kui sobib",
            "Vanemate mentorlus: \u00fcks tegu p\u00e4evas, mitte loeng",
            "Suuna kriisis olevad isad Lisa H-le (PEEGEL_TEE_A)",
            "Anna tagasiside: mis t\u00f6\u00f6tab 7\u201312-aastastega",
        ],
        "kaitumine": "M\u00e4nguline, soe. Lapsed = turvalisus enne sisu. \u00c4ra suru.",
        "pakett": "P1-C-PERE + P1-A-KRIIS (suunamine)",
        "kanal": "E-kiri / kohtumine",
        "markus": "Lisa K \u00a74.5",
    },
    {
        "name": "Marge Sillaste",
        "email": "margemargarethe@gmail.com",
        "org": "Supervisioon / tervishoid",
        "roll": "Juhtide supervisioon ja coaching",
        "eesmark": "Inimeste juhtimine, mitte protsesside kontroll",
        "ulesanded": [
            "Loe Lisa I (Steiger) ja Lisa P (trauma) enne juhtidega t\u00f6\u00f6d",
            "Peegelda juhtidele: turvalisus enne tulemust",
            "Anna tagasiside Reneele supervisiooni vajaduste kohta",
            "Kasuta kuldset taganemisteed kui keegi soovib nime eemaldada",
        ],
        "kaitumine": "Rahulik FM-DJ. Kuula ilma parandamiseta. Konfidentsiaalsus.",
        "pakett": "P1-F-JUHT",
        "kanal": "E-kiri privaatne",
        "markus": "Lisa K \u00a73.11",
    },
    {
        "name": "Ott P\u00e4rna",
        "email": "info@techno.ee",
        "org": "Techno TLN",
        "roll": "Direktor; haridustaseme strateegiline partner",
        "eesmark": "Kutse- ja tehnoloogiaharidus noorte vastupanuv\u00f5imes",
        "ulesanded": [
            "Tutvu PEEGEL_TEE_F (juht/koolitus) \u2014 isiklik link",
            "Hinda: kas Steigeri p\u00f5him\u00f5tted sobivad \u00f5ppekavaga (Lisa I)",
            "Suuna kriisiteemad koolips\u00fchholoogile, mitte debatile",
            "Vastus \u00fcks lausega: kas ja kuidas edasi",
        ],
        "kaitumine": "Austav keel (teietamine). Ametlik toon. Ei propaganda.",
        "pakett": "P1-F-JUHT",
        "kanal": "Ametlik e-kiri",
        "markus": "Lisa J; isiklik email puudub repos",
    },
    {
        "name": "Kristel Bankier",
        "email": "kristel.bankier@techno.ee",
        "org": "Techno TLN",
        "roll": "Finants / partnerlus",
        "eesmark": "Siduda haridus ja kogukonna partnerid",
        "ulesanded": [
            "Loe Lisa AM (realistlik maht) enne partnerluse otsust",
            "Hinda koost\u00f6\u00f6v\u00f5imalusi ilma ulmeliste numbriteta",
            "Suuna tehnilised k\u00fcsimused Ott P\u00e4rnale",
        ],
        "kaitumine": "Professionaalne, faktip\u00f5hine. \u00c4ra v\u00e4lju kontekstist.",
        "pakett": "P0-TUUM",
        "kanal": "E-kiri",
        "markus": "Lisa J",
    },
    {
        "name": "Kristel Martis",
        "email": "kristel.martis@techno.ee",
        "org": "Techno TLN",
        "roll": "Turundus / kogukond",
        "eesmark": "Kogukonna sidumine ja aus kommunikatsioon",
        "ulesanded": [
            "Tutvu Lisa Q (side SOP) enne mis tahes levitust",
            "Mitte masspostitus \u2014 ainult opt-in kanalid",
            "Soovita P0-TUUM esimene kontakt",
        ],
        "kaitumine": "M\u00e4nguline h\u00e4\u00e4l v\u00e4ljas, mitte sarkasm haava peal.",
        "pakett": "P0-TUUM",
        "kanal": "E-kiri",
        "markus": "Lisa J",
    },
    {
        "name": "Johan-Elias Seljamaa",
        "email": "johan-elias.seljamaa@mil.ee",
        "org": "Kaitsev\u00e4e Akadeemia",
        "roll": "Rektor",
        "eesmark": "Juhtide areng ja kriitiline m\u00f5tlemine",
        "ulesanded": [
            "Loe Lisa I + Lisa P (trauma kriisis)",
            "Hinda: kas materjal sobib akadeemilisele kontekstile",
            "Suuna Aarne Ermusile akadeemiline tagasiside",
            "Kuldne taganemistee kehtib ka ametlikul tasemel",
        ],
        "kaitumine": "Austav, struktureeritud. L\u00fchikesed laused kriisis.",
        "pakett": "P1-F-JUHT",
        "kanal": "Ametlik e-kiri @mil.ee",
        "markus": "Lisa J",
    },
    {
        "name": "Rainek Kuura",
        "email": "rainek.kuura@mil.ee",
        "org": "Kaitsev\u00e4e Akadeemia",
        "roll": "\u00d5ppeosakonna \u00fclem",
        "eesmark": "\u00d5ppekava ja juhtimiskultuuri sidumine",
        "ulesanded": [
            "Tutvu PEEGEL_TEE_F",
            "Anna tagasiside: mis sobiks kadettidele vs juhtidele",
            "Trauma-teadlikkus (Lisa P) enne \u00f5ppetundi",
        ],
        "kaitumine": "Selge, assertiivne kui vaja. Mitte dominants.",
        "pakett": "P1-F-JUHT",
        "kanal": "Ametlik e-kiri",
        "markus": "Lisa J",
    },
    {
        "name": "Sirje Toomla-\u00d5ige",
        "email": "sirje.toomla@ramkool.edu.ee",
        "org": "Rocca al Mare Kool",
        "roll": "Direktor",
        "eesmark": "Kooli kriisivalmidus ja pere tugi",
        "ulesanded": [
            "Loe Lisa H (kriis isale) ja Lisa W (Montessori austus)",
            "Jaga P1-C-PERE lapsevanematele ainult vabatahtlikult",
            "Suuna kriis Eluliinile / koolips\u00fchholoogile",
            "Koosk\u00f5lasta Helin Vaheriga (lapsevanem)",
        ],
        "kaitumine": "Turvalisus enne loogikat. Ei s\u00fc\u00fcdista vanemaid.",
        "pakett": "P1-C-PERE",
        "kanal": "E-kiri kool",
        "markus": "Lisa J; Elmar Vaher lapsevanem",
    },
    {
        "name": "Kristina \u0160anin",
        "email": "kristina.sanin@waldorf.ee",
        "org": "Tallinna Vaba Waldorfkool",
        "roll": "Kooli juhataja",
        "eesmark": "Holistiline tugi ja kogukonna sidumine",
        "ulesanded": [
            "Tutvu Ave Osaga (v\u00f5tmeisik) enne otsust",
            "Loe PEEGEL_TEE_C ja Lisa W",
            "Anna tagasiside: kas materjal sobib Waldorfi konteksti",
        ],
        "kaitumine": "Austav, aeglane tempo. Laps-keskne keel.",
        "pakett": "P1-C-PERE",
        "kanal": "E-kiri",
        "markus": "Lisa J",
    },
    {
        "name": "Ave Osa",
        "email": "tallinn@waldorf.ee",
        "org": "Tallinna Vaba Waldorfkool",
        "roll": "V\u00f5tmeisik; holistiline tugi",
        "eesmark": "Sidestada kogukond ja paranemis-teadlik tugi",
        "ulesanded": [
            "Loe Lisa AI (Epp K\u00e4rsin) ja Lisa W kontekstis",
            "Hinda P1-C-PERE sobivust kogukonnale",
            "Suuna intiimsuse teemad Epp K\u00e4rsinile (Lisa AA)",
            "Kontakt telefon: +372 5690 4407",
        ],
        "kaitumine": "Soe, mitte survav. Vabatahtlikkus.",
        "pakett": "P1-C-PERE",
        "kanal": "E-kiri + telefon",
        "markus": "Lisa J; org email",
    },
    {
        "name": "Ruth Maria Roosi-Ott",
        "email": "info@mariamontessori.ee",
        "org": "Montessori v\u00f5rgustik",
        "roll": "AMI juhendaja; instituudi juhatus",
        "eesmark": "Austus lapse vastu algusest (0\u20133)",
        "ulesanded": [
            "Loe Lisa W ja Lisa M (identiteet)",
            "Jaga P1-C-PERE Montessori \u00f5petajatele vabatahtlikult",
            "Anna tagasiside: mis t\u00f6\u00f6tab lasteaias",
        ],
        "kaitumine": "Rahulik, austav. Laps ei ole projekt.",
        "pakett": "P1-C-PERE",
        "kanal": "E-kiri info@",
        "markus": "Lisa J",
    },
    {
        "name": "Epp K\u00e4rsin",
        "email": "epood@eppkarsin.com",
        "org": "Amare Luna / teadlik intiimsus",
        "roll": "Intiimsuse koolitaja",
        "eesmark": "H\u00e4bist vabanemine; stress kehast v\u00e4lja",
        "ulesanded": [
            "Tutvu Lisa AA ja Lisa AI",
            "Suuna huvilised eppkarsin.com \u2014 pane end kirja",
            "Anna tagasiside: kas Peegel ja sinu t\u00f6\u00f6 klapivad",
        ],
        "kaitumine": "Aus, soe. Mitte tabu murdmine ilma turvalisuseta.",
        "pakett": "P1-C-PERE (t\u00e4iendus)",
        "kanal": "E-kiri / Instagram @epp.karsin",
        "markus": "Tel 5362 8568",
    },
    {
        "name": "Jelena Pribylski",
        "email": "jelena.pribylski@pk.ee",
        "org": "PK (pereteraapia)",
        "roll": "Koordinaator",
        "eesmark": "Pereteraapia v\u00f5rgustiku sidumine",
        "ulesanded": [
            "Tutvu Lisa P ja Lisa H (kriis)",
            "Hinda suunamise v\u00f5imalust peredele",
            "Trauma-teadlik suunamine \u2014 mitte diagnoosimine",
        ],
        "kaitumine": "Professionaalne konfidentsiaalsus. Valideerimine.",
        "pakett": "P1-A-KRIIS (suunamine)",
        "kanal": "E-kiri",
        "markus": "Lisa M",
    },
    {
        "name": "Tiit Trofimov",
        "email": "info@tiittrofimov.ee",
        "org": "Eneseareng",
        "roll": "Emotsioonide ja teadlikkuse t\u00f6\u00f6",
        "eesmark": "Meeste ringid; taastumine p\u00e4rast p\u00f5hja",
        "ulesanded": [
            "Loe Lisa H ja raamat F (murra ring)",
            "Suuna mehi, kes on p\u00f5hjas, PEEGEL_TEE_A-sse",
            "Anna tagasiside: mis t\u00f6\u00f6tab meeste ringis",
        ],
        "kaitumine": "Aus, mitte \u00fcleolev. Keha enne m\u00f5istust.",
        "pakett": "P1-A-KRIIS",
        "kanal": "E-kiri / tel +372 5626 2454",
        "markus": "Lisa M",
    },
    {
        "name": "\u00dclo Vooglaid",
        "email": "ylo@vooglaid.org",
        "org": "Sihtasutus \u00dclo Vooglaiu m\u00f5ttep\u00e4rand",
        "roll": "Kodaniku-m\u00f5tleja eeskuju; demonstraator",
        "eesmark": "N\u00e4idata, et elanikust kodanikuks on Eestis juba kirjas",
        "ulesanded": [
            "Soovita *Elanikust kodanikuks* enne OPORD-i (tee B)",
            "Anna tagasiside: kas Peegel ja Vooglaid klapivad",
            "Jaga ainult vabatahtlikult \u2014 mitte surve all",
        ],
        "kaitumine": "Rahulik, kriitiline. Austa autonoomiat. Lisa P teiste suhtes.",
        "pakett": "P1-B-SKEPTIK (vooglaid tuum)",
        "kanal": "E-kiri isiklik / sihtasutus@vooglaid.org",
        "markus": "Lisa AR; 90 a. 2025",
    },
    {
        "name": "Indrek Paal",
        "email": "sihtasutus@vooglaid.org",
        "org": "\u00dclo Vooglaiu Kirjastus / Vana-Viru Kaubaveod",
        "roll": "Praktiline demonstraator; m\u00f5ttep\u00e4randa hoidja",
        "eesmark": "Tuua Vooglaidi tuum k\u00e4tte \u2014 raamat, vestlus",
        "ulesanded": [
            "Levita *Vanaisa uued lood* (2025) sobivates ringkondades",
            "Siduda sihtasutus ja Peegel ainult Vooglaidi n\u00f5usolekul",
            "Anna tagasiside: mis formaat t\u00f6\u00f6tab",
        ],
        "kaitumine": "Asjatundlik, praktiline. Lisa Q austav keel. Mitte masspostitus.",
        "pakett": "P0-TUUM + Lisa AR",
        "kanal": "E-kiri / tel 667 0111",
        "markus": "Lisa AR; Elanikust kodanikuks kolleegium",
    },
]

# Additional emails from Lisa J table (org-level or secondary contacts)
EXTRA_EMAILS = [
    ("Techno TLN", "info@techno.ee", "info@techno.ee", "Techno TLN", "Organisatsiooni postkast", "P0-TUUM", "Lisa J"),
    ("Techno TLN", "sisseastumine@techno.ee", "sisseastumine@techno.ee", "Techno TLN", "Sisseastumine", "P0-TUUM", "Lisa J"),
    ("Toivo P\u00e4rnpuu", "toivo.parnpuu@techno.ee", "Techno TLN", "IT", "P0-TUUM", "Lisa J"),
    ("Mari Vavulski", "mari.vavulski@techno.ee", "Techno TLN", "Muudatuste projektijuht", "P0-TUUM", "Lisa J"),
    ("Birgit Vilgats", "birgit.vilgats@techno.ee", "Techno TLN", "\u00d5ppejuht", "P1-F-JUHT", "Lisa J"),
    ("Andra Piirsalu", "andra.piirsalu@techno.ee", "Techno TLN", "Personalijuht", "P1-F-JUHT", "Lisa J"),
    ("Ander Sile", "ander.sile@techno.ee", "Techno TLN", "Inseneriharidus", "P1-F-JUHT", "Lisa J"),
    ("T\u00f5nu Armulik", "tonu.armulik@techno.ee", "Techno TLN", "Arendusdirektor", "P1-F-JUHT", "Lisa J"),
    ("Indrek Ojasoo", "indrek.ojasoo@mil.ee", "KVA", "Akadeemia veebel", "P1-F-JUHT", "Lisa J"),
    ("RaM Kool", "info@ramkool.edu.ee", "RaM Kool", "Info", "P1-C-PERE", "Lisa J"),
    ("Rein Rebane", "rein.rebane@ramkool.edu.ee", "RaM Kool", "Direktor emeeritus", "P1-C-PERE", "Lisa J"),
    ("Katrin Rodi", "katrin.rodi@ramkool.edu.ee", "RaM Kool", "Pearaamatupidaja", "P0-TUUM", "Lisa J"),
    ("Maarika Eha-M\u00fcller", "maarika.eha@ramkool.edu.ee", "RaM Kool", "Personalijuht", "P1-C-PERE", "Lisa J"),
    ("Anneli Paat", "anneli.paat@ramkool.edu.ee", "RaM Kool", "Infojuht", "P0-TUUM", "Lisa J"),
    ("Peep Valjaste", "peep.valjaste@ramkool.edu.ee", "RaM Kool", "Juhtkond", "P0-TUUM", "Lisa J"),
    ("Rivo Raaper", "rivo.raaper@ramkool.edu.ee", "RaM Kool", "Juhtkond", "P0-TUUM", "Lisa J"),
    ("Helin Vaher", "helin.vaher@agendapr.ee", "RaM Kool", "Lapsevanem, kommunikatsioon", "P1-C-PERE", "Lisa J"),
    ("Kairi J\u00e4rvik-Elvisto", "kairi.jarvik-elvisto@waldorf.ee", "TVW Waldorf", "Tugiteenused", "P1-C-PERE", "Lisa J"),
    ("Waldorf selts", "selts@waldorf.ee", "TVW Waldorf", "Selts", "P0-TUUM", "Lisa J"),
    ("Indrek Paal", "sihtasutus@vooglaid.org", "\u00dclo Vooglaiu Kirjastus", "Demonstraator, levitaja", "P0-TUUM", "Lisa AR"),
    ("\u00dclo Vooglaid", "ylo@vooglaid.org", "Sihtasutus", "Kodaniku-m\u00f5tleja", "P1-B-SKEPTIK", "Lisa AR"),
]

NO_EMAIL = [
    ("Riho \u00dchtegi", "Strateegiline juht", "Avalik kanal", "Lisa K \u00a74.1"),
    ("Rene Toomse", "Riigi tase", "Avalik kanal", "Lisa K \u00a74.1"),
    ("Eerik Heldna", "Kriisireguleerimine", "PPA", "Lisa K \u00a74.1"),
    ("Elmar Vaher", "RKIK", "kaitseinvesteeringud.ee", "Lisa K \u00a74.1"),
    ("Heli Illipe-Sootak", "Steiger peakirjastaja", "Messenger / otsing", "kommunikatsioon/vastus-heli-illipe-sootak.md"),
    ("Mihhail U\u0161akov", "RU peer-educator (kandidaat)", "Isiklik kohtumine", "kommunikatsioon/kandidaat-mihhail-usakov.md"),
    ("Ain Anslan", "Viru vangla", "Vanglateenistus", "Lisa K \u00a74.7"),
    ("Aigar Ojaots", "Pertinax", "MT\u00dc reg 80634291", "Lisa K \u00a74.6"),
    ("Peeter J\u00e4rvsoo", "Noorte Kotkad", "nooredkotkad.ee", "Lisa K \u00a73.10"),
    ("Andrei Ambros", "Harku judo", "estjutsu.ee", "Lisa K \u00a73.10"),
    ("Eero Kinnunen", "Veteranid", "ekvv.ee", "Lisa K \u00a73.11"),
    ("Margus L\u00f5oke", "KV mustri tunnistaja", "Isiklik kontakt Renee", "Lisa K \u00a73.2b"),
]

PODCAST_TITLE = "Ava Oma Silmad & Ajuloputus S4 #10 \u2014 \u201eMaatriksi Lapsed\u201c"
PODCAST_ACAST = (
    "https://shows.acast.com/avaomasilmad/episodes/"
    "ee-jata-navigatsioon-vahele-loomine-avataripilt-ava-oma-silm"
)
PODCAST_APPLE = "https://podcasts.apple.com/ee/podcast/ava-oma-silmad-podcast/id1541890084"
PODCAST_YOUTUBE = "https://www.youtube.com/@AJULOPUTUS"
PODCAST_ET_WEB = "https://katrinlucas.com/podcast/"
PODCAST_REF = "kommunikatsioon/soovitus-maatriksi-lapsed.md"
MEDIA_KEEL_REEGEL = (
    "Eesti keel primaarselt \u2014 eestikeelne kanal enne v\u00f5\u00f5rkeelset."
)

PAPSID_TITLE = "Papsid.ee Podcast"
PAPSID_WEB = "https://papsid.ee/podcast/"
PAPSID_APPLE = "https://podcasts.apple.com/ee/podcast/papsid-ee-podcast/id1768003452"
PAPSID_LAAGER = "https://papsid.ee/papside-laager/"
PAPSID_REF = "kommunikatsioon/soovitus-papsid-podcast.md"
MEDIA_KEEL_DOC = "kommunikatsioon/soovitus-meedia-eesti-primaar.md"

PODCAST_HOOK = {
    "PERE": (
        "Kui su roll on laste ja pere kaitse \u2014 see episood on sinu jaoks "
        "esimene valikuline kuulamine enne PEEGEL_TEE_C-d."
    ),
    "KRIIS": (
        "Kui oled ise elluj\u00e4\u00e4misre\u017eiimis \u2014 episood aitab m\u00f5ista, "
        "miks lapsed (ja sina) vajavad k\u00f5igepealt turvalisust, mitte loogikat."
    ),
    "JUHT": (
        "Juhi vaatenurgast: kaitse enne tulemust. Kui keegi on elluj\u00e4\u00e4misre\u017eiimis, "
        "ta ei n\u00e4e plaani (Lisa AT)."
    ),
    "DEFAULT": (
        "Valikuline teadlikkuse kanal \u2014 sobib neile, kes tahavad s\u00fcgavamat "
        "konteksti enne OPORD-i."
    ),
}


def _pakett_family_track(pakett: str) -> bool:
    p = pakett.upper()
    return "PERE" in p or "C-PERE" in p or "KRIIS" in p or "A-KRIIS" in p


def _podcast_angle(pakett: str) -> str:
    p = pakett.upper()
    if "PERE" in p or "C-PERE" in p:
        return PODCAST_HOOK["PERE"]
    if "KRIIS" in p or "A-KRIIS" in p:
        return PODCAST_HOOK["KRIIS"]
    if "JUHT" in p or "F-JUHT" in p:
        return PODCAST_HOOK["JUHT"]
    return PODCAST_HOOK["DEFAULT"]


def papsid_email_block(pakett: str) -> str:
    """Papsid.ee podcast for PERE / KRIIS sidepacks."""
    hook = (
        "Isa ja pere rinne \u2014 vastutus, suhe, trauma, kohalolek. "
        "Praktiline, mitte lobisemine."
    )
    if "KRIIS" in pakett.upper() or "A-KRIIS" in pakett.upper():
        hook = (
            "Kui oled isa ja oled raske kohas \u2014 ausad lood ja t\u00f6\u00f6riistad "
            "ilma moraliseerimiseta (Lisa H kontekstis)."
        )
    return (
        f"\nEnne kui materjaliga edasi l\u00e4hed \u2014 \u00fcks valikuline soovitus (isa / pere):\n\n"
        f"KUULA (eesti keeles): {PAPSID_TITLE} \u2014 Kristo Tuurmann & Illimar Pilt\n\n"
        f"{hook}\n\n"
        "vastutus, aus suhtlus (NVC) ja Body Keeps the Score loogikaga haakuv sisu. "
        "P\u00e4rast episoodi \u00fcks k\u00fcsimus: \u201eMida ma \u00f5ppisin ja mida teen t\u00e4na teisiti?\u201c\n\n"
        f"Kuula: {PAPSID_WEB}\n"
        f"Apple Podcasts: {PAPSID_APPLE}\n"
        f"Papside laager (3 p\u00e4eva): {PAPSID_LAAGER}\n\n"
        f"{MEDIA_KEEL_REEGEL}\n"
        "See ei ole k\u00e4sk. V\u00e4ike samm t\u00e4na on tugevam kui t\u00e4iuslik plaan homme.\n"
    )


def podcast_email_block(pakett: str) -> str:
    """Inviting podcast snippet for kask e-mails (plain text)."""
    if _pakett_family_track(pakett):
        return papsid_email_block(pakett)
    hook = _podcast_angle(pakett)
    return (
        f"\nEnne kui materjaliga edasi l\u00e4hed \u2014 \u00fcks valikuline soovitus (~1h 20 min, **eesti keeles**):\n\n"
        f"KUULA: {PODCAST_TITLE}\n\n"
        f"{hook}\n\n"
        "Kus s\u00fcsteem tabab k\u00f5ige enne lapsi \u2014 ja miks t\u00e4iskasvanud "
        "elluj\u00e4\u00e4misre\u017eiimis ei m\u00e4rka seda. Turvalisus. Kohalolu. Kaitse. "
        "vastutusi vaimus: mitte ainult s\u00fc\u00fcdistada s\u00fcsteemi, vaid n\u00e4ha, "
        "kus sina saad ise muutust luua \u2014 pere, meeskonna v\u00f5i enda sees.\n\n"
        f"Kuula: {PODCAST_ACAST}\n"
        f"Katrin Lucas (podcast): {PODCAST_ET_WEB}\n"
        f"Apple Podcasts (EE): {PODCAST_APPLE}\n"
        f"YouTube (@AJULOPUTUS): {PODCAST_YOUTUBE} \u2014 otsi \u201eMaatriksi Lapsed\u201c\n\n"
        f"{MEDIA_KEEL_REEGEL}\n"
        "See ei ole k\u00e4sk. See on kutse avada silmad ja valida ise.\n"
    )


def podcast_markdown_block(pakett: str) -> str:
    """Shorter blockquote variant for osalejate-kohandatud-kask.md."""
    if _pakett_family_track(pakett):
        hook = "Isa / pere rinne \u2014 Lisa H, Lisa D, PEEGEL_TEE_C"
        if "KRIIS" in pakett.upper():
            hook = "Isa kriisis \u2014 Lisa H kontekstis"
        return (
            f"> **Valikuline kuulamine:** {PAPSID_TITLE}  \n"
            f"> {hook}  \n"
        f"> Kuula: [{PAPSID_WEB}]({PAPSID_WEB}) \u00b7 "
        f"[Apple EE]({PAPSID_APPLE})  \n"
            f"> T\u00e4psem: `{PAPSID_REF}`\n>\n"
        )
    hook = _podcast_angle(pakett)
    return (
        f"> **Valikuline kuulamine (~1h 20 min):** {PODCAST_TITLE}  \n"
        f"> {hook}  \n"
        f"> Kuula: [{PODCAST_ACAST}]({PODCAST_ACAST}) \u00b7 "
        f"[katrinlucas.com]({PODCAST_ET_WEB}) \u00b7 "
        f"[Apple EE]({PODCAST_APPLE}) \u00b7 "
        f"[YouTube]({PODCAST_YOUTUBE})  \n"
        f"> T\u00e4psem kokkuv\u00f5te: `{PODCAST_REF}`\n>\n"
    )


def write_csv():
    rows = []
    seen = set()
    for p in PARTICIPANTS:
        key = p["email"].lower()
        if key in seen:
            continue
        seen.add(key)
        rows.append({
            "nimi": p["name"],
            "email": p["email"],
            "organisatsioon": p["org"],
            "roll": p["roll"],
            "sidepakk": p["pakett"],
            "kanal": p["kanal"],
            "kask_valmis": "jah",
            "markus": p["markus"],
        })
    for item in EXTRA_EMAILS:
        if len(item) == 7:
            name, email, org, roll, pakett, markus = item[0], item[1], item[2], item[3], item[4], item[5]
            kanal = item[6] if len(item) > 6 else "E-kiri"
        else:
            name, email, org, roll, pakett, markus = item
            kanal = "E-kiri"
        key = email.lower()
        if key in seen:
            continue
        seen.add(key)
        rows.append({
            "nimi": name,
            "email": email,
            "organisatsioon": org,
            "roll": roll,
            "sidepakk": pakett,
            "kanal": kanal,
            "kask_valmis": "l\u00fchike",
            "markus": markus,
        })
    for name, roll, kanal, markus in NO_EMAIL:
        rows.append({
            "nimi": name,
            "email": "",
            "organisatsioon": "",
            "roll": roll,
            "sidepakk": "",
            "kanal": kanal,
            "kask_valmis": "ei",
            "markus": f"Email puudub \u2014 {markus}",
        })
    rows.sort(key=lambda r: (r["kask_valmis"] != "jah", r["nimi"]))
    with CSV_FILE.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {CSV_FILE} ({len(rows)} rida)")


def write_kask_md():
    lines = [
        "# Osalejate kohandatud k\u00e4sk\n\n",
        "**Eesm\u00e4rk:** Iga osaleja saab oma rolli, eesm\u00e4rgi ja k\u00e4itumisjuhise.  \n",
        "**Seotud:** Lisa K, Lisa Q, Lisa AJ, Lisa AQ  \n",
        "**Kuup\u00e4ev:** 24. juuli 2026  \n",
        "**Koordinaator:** Renee Aluste\n\n",
        "> **Reegel:** Isiklik e-kiri, mitte masspost. Iga saaja = isiklik link (Lisa AJ).  \n",
        "> **Kuldne taganemistee:** \u201eT\u00e4nan, palun eemalda minu nimi.\u201c \u2014 ilma surveta.\n\n",
        "---\n\n",
        "## \u00dclevaade\n\n",
        f"| Kategooria | Arv |\n",
        f"|------------|-----|\n",
        f"| Kohandatud k\u00e4sk valmis | {len(PARTICIPANTS)} |\n",
        f"| Email CSV-s kokku | vaata `osalejate-emailid.csv` |\n",
        f"| Email puudub (vaja otsida) | {len(NO_EMAIL)} |\n\n",
        "---\n\n",
        "## Podcast ja meedia (eesti keel primaarselt)\n\n",
        f"> **Reegel:** `{MEDIA_KEEL_DOC}`\n\n",
        f"**PERE / KRIIS** \u2192 [{PAPSID_TITLE}]({PAPSID_WEB}) (ET)  \n",
        f"**Muu** \u2192 {PODCAST_TITLE} (ET)\n\n",
        f"| Papsid.ee (ET) | [{PAPSID_WEB}]({PAPSID_WEB}) \u00b7 [Apple EE]({PAPSID_APPLE}) |\n",
        f"| Ava Oma Silmad (ET) | [{PODCAST_ACAST}]({PODCAST_ACAST}) \u00b7 [Apple EE]({PODCAST_APPLE}) |\n\n",
        "---\n\n",
    ]
    for i, p in enumerate(PARTICIPANTS, 1):
        lines.append(f"## {i}. {p['name']}\n\n")
        lines.append(f"| | |\n|---|---|\n")
        lines.append(f"| **E-post** | `{p['email']}` |\n")
        lines.append(f"| **Organisatsioon** | {p['org']} |\n")
        lines.append(f"| **Roll** | {p['roll']} |\n")
        lines.append(f"| **Eesm\u00e4rk** | {p['eesmark']} |\n")
        lines.append(f"| **Sidepakk** | {p['pakett']} |\n")
        lines.append(f"| **Kanal** | {p['kanal']} |\n\n")
        lines.append("### Sinu \u00fclesanded\n\n")
        for u in p["ulesanded"]:
            lines.append(f"1. {u}\n" if u == p["ulesanded"][0] else f"{p['ulesanded'].index(u)+1}. {u}\n")
        # fix numbering
        lines = lines[:-len(p["ulesanded"])]
        for j, u in enumerate(p["ulesanded"], 1):
            lines.append(f"{j}. {u}\n")
        lines.append(f"\n### K\u00e4itumisjuhis\n\n{p['kaitumine']}\n\n")
        lines.append("### E-kirja avamine (mustand)\n\n")
        lines.append(
            f"> Tere {p['name'].split()[0]},\n>\n"
            f"> Jagame sulle Operatsioon \u201ePeegel\u201c materjali \u2014 mitte k\u00e4sk, vaid paranemis-teekond. "
            f"Sinu roll: **{p['roll'].split(';')[0]}**.\n>\n"
            f"> Isiklik link: [PEEGEL_TUUM / vastav tee PDF]\n>\n"
        )
        lines.append(podcast_markdown_block(p["pakett"]))
        lines.append(
            f"> Kui soovid mitte osaleda \u2014 \u00fcks lause piisab. Austan seda.\n>\n"
            f"> Renee Aluste\n\n"
        )
        lines.append("---\n\n")
    lines.append("## Osalejad ilma e-postita (repos)\n\n")
    lines.append("| Nimi | Roll | Kuidas \u00fchenduda |\n|------|------|----------------|\n")
    for name, roll, kanal, markus in NO_EMAIL:
        lines.append(f"| {name} | {roll} | {kanal} |\n")
    lines.append("\n---\n\n*Lisa: kommunikatsioon/osalejate-kohandatud-kask.md*\n")
    KASK_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {KASK_FILE}")


def write_individual_letters():
    KIRJAD_DIR.mkdir(parents=True, exist_ok=True)
    for p in PARTICIPANTS:
        slug = p["name"].lower().replace(" ", "-").replace("\u00e4", "a").replace("\u00f6", "o").replace("\u00fc", "u").replace("\u0161", "s").replace("\u00f5", "o").replace("\u00e4", "a")
        slug = "".join(c for c in slug if c.isalnum() or c == "-")
        fname = KIRJAD_DIR / f"kask-{slug}.md"
        body = [
            f"# Kohandatud k\u00e4sk: {p['name']}\n\n",
            f"**Saaja:** {p['email']}  \n",
            f"**Sidepakk:** {p['pakett']}\n\n",
            "---\n\n",
            f"## Sinu roll\n\n{p['roll']}\n\n",
            f"## Sinu eesm\u00e4rk\n\n{p['eesmark']}\n\n",
            "## Konkreetsed \u00fclesanded\n\n",
        ]
        for j, u in enumerate(p["ulesanded"], 1):
            body.append(f"{j}. {u}\n")
        body.append(f"\n## K\u00e4itumisjuhis\n\n{p['kaitumine']}\n\n")
        body.append("## E-kiri (kopeeri ja saada)\n\n")
        body.append("```\n")
        body.append(f"Teema: Operatsioon Peegel \u2014 sinu roll: {p['roll'].split(';')[0]}\n\n")
        body.append(f"Tere {p['name'].split()[0]},\n\n")
        body.append(
            "Jagan sulle isiklikult Operatsioon \u201ePeegel\u201c materjali. "
            "See ei ole k\u00e4sk ega propaganda \u2014 see on kutse kriitiliselt m\u00f5elda ja valida ise.\n\n"
        )
        body.append(f"Sinu roll selles v\u00f5rgustikus: {p['roll']}.\n\n")
        body.append(f"Sinu eesm\u00e4rk: {p['eesmark']}.\n\n")
        body.append("Konkreetselt sinult:\n")
        for u in p["ulesanded"]:
            body.append(f"- {u}\n")
        body.append(f"\nMaterjal: [lisa isiklik link \u2014 {p['pakett']}]\n")
        body.append(podcast_email_block(p["pakett"]))
        body.append(
            "\nKui sa ei soovi osaleda v\u00f5i soovid nime eemaldada \u2014 "
            "\u00fcks lause piisab. T\u00e4nan aususe eest.\n\n"
            "Renee Aluste\n"
            "Operatsiooni koordinaator\n"
        )
        body.append("```\n")
        fname.write_text("".join(body), encoding="utf-8")
    print(f"Wrote {len(PARTICIPANTS)} letters to {KIRJAD_DIR}/")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv()
    write_kask_md()
    write_individual_letters()
