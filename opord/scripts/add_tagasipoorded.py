#!/usr/bin/env python3
"""Add Renee-style follow-up questions to Q&A answers."""

import re
from pathlib import Path

MD = Path(__file__).resolve().parents[1] / "OPERATSIOON_PEEGEL_OPORD.md"

FOLLOWUPS = [
    (r"sõda\?", "Kas sa oled täna kellegi vastu — või enda vana mustri vastu?"),
    (r"militariseerida", "Kus sinu elus on distsipliin kasulik — ja kus see muutub jäikuseks?"),
    (r"volitas", "Kelle luba sa ootad — enne kui oma pere eest vastutad?"),
    (r"nimi „Peegel", "Keda sa täna peegeldad — kas ta on keegi, kelleks sa tahad saada?"),
    (r"vandenõuteooria", "Millal sa viimati kontrollisid uudist, mis sind vihastas?"),
    (r"manipuleerin sind terveks", "Kas keegi sinu elus teeb sind tugevamaks — või sõltuvaks?"),
    (r"üksikemade", "Kes oli sinu elus eeskuju — ja kellele sina oled eeskujuks?"),
    (r"presidendiks", "Keda sina tahaksid juhina järgida — ja miks just teda?"),
    (r"19 ja elan TikTokis", "Kui palju tundi läks täna sinu elust ekraanile — ja kas see number sind rahuldab?"),
    (r"kustutama Instagrami", "Mis emotsioon tekkis viimase postituse järel — ja kes sellest võitis?"),
    (r"raske peresituatsioon", "Kas sa oled täna kellelegi aus oma murede osas?"),
    (r"perede aeg", "Millal oli viimane kord, kui olite kodus koos ilma ekraanita?"),
    (r"ainult isafiguuridele", "Kellele sina täna vaatad üles — ja kes vaatab üles sinule?"),
    (r"teenib selle pealt raha", "Kas sa ostsid viimati midagi, mis sind tõesti arendas — või lõõgastas?"),
    (r"Katrin Lukasil", "Mis on sinu tee ärkamiseni — ja kas sa oled seda ausalt otsinud?"),
    (r"Aarne Ermus", "Millist juhtimispõhimõtet sa täna oma elus rakendad?"),
    (r"täna, kohe", "Mis on üks asi, mida sa täna muudad — mitte homme?"),
    (r"liituda või aidata", "Kas sa oled valmis olema eeskuju — ilma et keegi sind kutsuks?"),
    (r"mõõdate, kas võidate", "Kuidas sa tead, et sinu peres läheb paremaks — mitte ainult sinu arvates?"),
    (r"keegi ei kuula", "Kas sa jätkad siis, kui keegi ei vaata — sest see on õige?"),
    (r"riigi tööd", "Mida sa täna teed kodus, mida riik sinu eest teha ei saa?"),
    (r"omavalitsused", "Mida sa saad oma kogukonnas teha ilma volikogu otsuseta?"),
    (r"ametlik kaitseväe", "Kas sa tead täna selgelt, mis on sinu roll — mitte riigi roll?"),
    (r"traditsioonilise pere", "Mis on sinu peres see, mida sa tahad järgmisele põlvkonnale edasi anda?"),
    (r"süüdistad üksikule", "Mida sa saad süsteemi jaoks nõuda — ja mida sa saad ise teha juba täna?"),
    (r"Euroopa Liidu", "Mida sa teed Eesti heaks — enne kui ootad Euroopat?"),
    (r"erakonda või kandidaati", "Kas sa juhid oma peres — või ootad, et poliitika seda teeks?"),
    (r"kristliku sõnumiga", "Mis on sinu väärtus, mille järgi sa last kasvatad?"),
    (r"liiga „ilmalik", "Kus sa leiad jõu — ja kas see allikas on sinu jaoks piisav?"),
    (r"mitmekultuurilisse", "Kas sa tervitad oma naabruses kedagi, kes on sinust erinev?"),
    (r"trivialiseeri depressiooni", "Kas sa oled täna aus oma vaimse seisundiga — iseendale?"),
    (r"meditatsiooni", "Millal sa viimati olid täielikult kohal — ilma telefonita?"),
    (r"ateist", "Mis paneb sind olema hea inimene — ilma et keegi sind sunniks?"),
    (r"noori kirikutesse", "Kus sinu laps või naaber laps saab täna turvalisust?"),
    (r"dokumenteeritud tõendeid", "Kas sa kontrollisid täna vähemalt ühte uudist enne jagamist?"),
    (r"turundusnarratiiv", "Kas sa usaldad inimest, kes räägib ainult võitu — mitte ka vigu?"),
    (r"järjekordsest „tee head", "Mis eristab sinu elus tõelist muutust performatiivsest kampaaniast?"),
    (r"sõnum ajakirjanikele", "Kas sa jagasid täna midagi, mida sa ise kontrollisid?"),
    (r"tulete saatesse", "Kas sa räägiksid oma loo ka siis, kui keegi ei filmiks?"),
    (r"influencer", "Kas su sõnum on sama aus offline — kui online?"),
    (r"venekeelse kogukonna", "Kas sa oled täna kellegi jaoks turvaline inimene — olenemata keelest?"),
    (r"Meta, TikTok", "Mis on üks algoritm, millele sa täna ei anna oma tähelepanu?"),
    (r"mudel teistele riikidele", "Mida sa teed oma kodus, et Eesti oleks tugevam?"),
    (r"ühe lausega, miks ma peaksin sind uskuma", "Keda sa usaldad kõige rohkem — ja kas sa ise oled selle inimene kellegi jaoks?"),
]


def pick_followup(question: str) -> str:
    for pattern, text in FOLLOWUPS:
        if re.search(pattern, question, re.I):
            return text
    return "Mida sina selle teadmisega täna teed — mitte homme?"


def main():
    text = MD.read_text(encoding="utf-8")
    before = text.count("Minu küsimus sulle:")
    parts = re.split(r"\n---\n", text)
    out = []
    for part in parts:
        block = part
        stripped = block.lstrip()
        if stripped.startswith("**K") and "**V" in block and "Minu küsimus sulle:" not in block:
            k_match = re.search(r"\*\*K[^*]+?\*\*", block)
            if k_match:
                q = block[k_match.end() :].strip().split("\n")[0]
                follow = pick_followup(q)
                block = block.rstrip() + f"\n\n*Minu küsimus sulle: {follow}*"
        out.append(block)
    MD.write_text("\n---\n".join(out), encoding="utf-8")
    after = MD.read_text(encoding="utf-8").count("Minu küsimus sulle:")
    print(f"Tagasipöörded: {after - before} added (total {after}).")


if __name__ == "__main__":
    main()
