# PLAANKONSPEKT DP1-G — Diplomaatia meistriklass (sõltlasega)

**Unpluged-Al** | Grupikoolitus | **Kestus: 90 min**

| | |
|---|---|
| **Kood** | DP1-G |
| **Teema** | Turvaline suhtlus · piirid · demo · de-eskalatsioon |
| **Versioon** | 1.0 · 16. august 2026 |
| **Koolitaja** | Juhendatud praktik (vt nõuded) |
| **Sihtgrupp** | Max 12 — pereliikmed, mentorid, malevapealikud, juhid |
| **Eeldused** | Lisa P / trauma-teadlikkus; **mitte** aktiivne füüsiline oht ruumis |
| **Seotud** | `diplomaatia-soltlasega-juhend.md` · `diplomaatia-soltlasega-koolituskaart.md` · `diplomaatia-soltlasega-demo-ohutusjuhend.md` |

---

## 1. Koolituse eesmärgid

Pärast 90 minutit osaleja:

| # | Õpiväljund |
|---|------------|
| 1 | Oskab **selgitada** diplomaatia vs enabling erinevust |
| 2 | Oskab nimetada **STOP** reeglid ja ohutuse piirid |
| 3 | Oskab teha **DP1-A kiirprotokolli** (15 min) enne vestlust |
| 4 | Oskab osaleda **demo soorituses** (DP1-D01–D04) ohutusjuhendi järgi |
| 5 | Teab, **millal** suunata ÕnneKlubi / ohvriabi / kriisiabi poole |
| 6 | Kirjutab **ühe debriefi lause** pärast rollimängu |

---

## 2. SWOT — koolituse tuum (30 sek pitch)

| | |
|---|---|
| **S** | Praktiline; vähendab perede konflikti; sobib juhtimise/debriefi konteksti |
| **W** | Ei asenda ravi; emotsionaalne koormus; vajab ohutut ruumi |
| **O** | Ühendus HY1, ohvriabi, ÕnneKlubi spetsialistidega |
| **T** | Enabling harjumus; füüsiline oht demo ajal; “diplomaatia asemel ravi” ootus |

---

## 3. Koolitaja nõuded

| # | Nõue |
|---|------|
| 1 | Lugeda läbi `diplomaatia-soltlasega-juhend.md` |
| 2 | Lugeda läbi `diplomaatia-soltlasega-demo-ohutusjuhend.md` |
| 3 | Käivitada `scripts/dp1_demo_koordinaator.py` enne tundi |
| 4 | Trauma-teadlikkus — STOP, mitte “ravida” rollis |
| 5 | Debrief oskus — 1 lause, mitte süüdistus |

---

## 4. Materjalid

| Materjal | Kogus |
|----------|-------|
| DP1 koolituskaart (prinditud) | 1 / osaleja |
| Demo ohutusjuhend (prinditud) | 1 / paar |
| Pliiats, paber | 1 / osaleja |
| STOP kontaktide leht (112, 116 123, palunabi.ee) | 1 / ruum |
| Valikuline: HY1 kiirjuhend | 1 / osaleja |

---

## 5. Tunnikava (90 min)

| Aeg | Faas | Koolitaja | Osaleja | Märkused |
|-----|------|-----------|---------|----------|
| **0–10** | **Avamine + ohutus** | Reeglid, STOP, füüsiline oht. SWOT 2 min. ÕnneKlubi kontekst 2 min. | Kuulab | Lisa P |
| **10–25** | **Mis on diplomaatia?** | DO/DON’T tabel. Enabling näited. | Märkmed | Ausus |
| **25–35** | **DP1-A protokoll** | Juhib grupi 5-min ankur + eesmärk | Teeb ise | HY1 link |
| **35–55** | **Demo sooritused** | Paarid: DP1-D01 või D02. Ohutusjuhend enne. | Rollimäng | vt koordinaator |
| **55–70** | **De-eskalatsioon D03** | Juhendatud stsenaarium; STOP harjutus | Osaleb | Mitte päris kriis |
| **70–85** | **Suunamine abile** | ÕnneKlubi, ohvriabi TTTVT, 116 006 | Küsimused | vt raport |
| **85–90** | **Debrief + lõpetus** | Ring: 1 lause “mis muutus?” | Jagab | Annex A stiil |

---

## 6. Demo soorituste koordinaator

Enne demot **kohustuslik**:

```bash
python3 scripts/dp1_demo_koordinaator.py --demo DP1-D01 --check
python3 scripts/dp1_demo_koordinaator.py --list
```

| Kood | Stsenaarium | Kestus | Rollid |
|------|-------------|--------|--------|
| DP1-D01 | Relaps — esimene kontakt | 8 min | Pereliige + sõltlane |
| DP1-D02 | Keeldumine raha ostmisest | 6 min | Pereliige + sõltlane |
| DP1-D03 | Kriis — nutab, ähvardab | 8 min | Pereliige + sõltlane + vaatleja |
| DP1-D04 | Suunamine ÕnneKlubi poole | 6 min | Pereliige + sõltlane |

**Ohutusjuhend:** `diplomaatia-soltlasega-demo-ohutusjuhend.md`

---

## 7. Hindamine

| Kriteerium | ☐ |
|------------|---|
| Osales 90 min | |
| Oskab 3 DON’T reeglit | |
| Oskab STOP reegli | |
| Teostas demo ohutusjuhendi järgi | |
| Kirjutas debriefi lause | |

---

## 8. Kodutöö (7 päeva)

| Päev | Ülesanne |
|------|----------|
| 1–2 | DP1-A enne üht vestlust; logi stress enne/pärast |
| 3 | Loe `hupnoteraapia-teenused-ohvriabi-raport.md` |
| 4 | 1× demo paaris (D01 või D02) |
| 5 | Debrief `debrief-kaart-malevapealik.pdf` stiilis |
| 6–7 | Kui kuriteoohvri kontekst — kontrolli palunabi.ee TTTVT |

---

*DP1-G v1.0 · Unpluged-Al · plaankonspekt 90 min grupikoolitusele*
