# Lisa BD — Riiklik peegel: hindamisvorm riigisektoris

> **Lugeja saab:** kuidas tuua Operatsioon „Peegel" riiklikule tasandile — ühtse hindamisvormi kaudu.  
> **Loe seda kui:** juhid asutust, osakonda, kooli, üksust või riiklikku võrgustikku.  
> **Ära loe kui:** oled esimene kord — alusta PEEGEL_TUUM.pdf; kriisis — Lisa H.

**Seotud:** Lisa AV (põhivorm), Lisa BE (iga päev), Lisa I (Steiger), Lisa P (trauma-teadlik tagasiside), Lisa Q (austav keel), riigisektori austusjuhendid (Techno TLN eeskuju)

**Prindi:**

| Fail | Kasutus |
|------|---------|
| [PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf](../PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf) | **A4** — juht, kolleeg, allüksuse juht (iga hindaja eraldi) |
| [PEEGEL_RIIK_PLANKETT.pdf](../PEEGEL_RIIK_PLANKETT.pdf) | **A3/A4 sein** — asutuse fuajee, personaliruum, õppejõudude tuba |
| [PEER_HINDAMINE_RAHAKOTT.pdf](../PEER_HINDAMINE_RAHAKOTT.pdf) | **85×55 mm** — igapäevane kaaslase hindamine (Lisa BE) |
| [PEEGEL_HINDAMISVORM_PRINT.pdf](../PEEGEL_HINDAMISVORM_PRINT.pdf) | **Suhte hindamise vorm** / pere (Lisa AV — AV-PERE) |

Genereeri: `python3 generate_hindamisvorm_pdf.py`

---

## Põhiidee

Riigis on vaja **ühtset peeglit** — mitte uut usu, vaid **sama küsimust igas asutuses**:

> **Kas ma usaldan seda inimest siis, kui keegi ei vaata?**

Riiklikul tasandil on peegel **hindamisvorm**. Vorm on plankett. Vestlus on protsess. **Üks tegu** on tulemus.

| Tase | Vorm | Sagedus |
|------|------|---------|
| **Iga päev** | **AV-PEER (Lisa BE)** | Iga olukord — alguses + sobival hetkel |
| **Kodu** | **Suhte hindamise vorm** (AV-PERE, Lisa AV) | 1× kuus |
| **Meeskond / SOK** | AV-MEESKOND / AV-SOK | 1× kvartal |
| **Asutus / riigisektor** | **AV-RIIK** (see lisa) | 1× kvartal (juhtkond), 2× aastas (ülejäänud) |

---

## AV-RIIK — kellele

| Roll | Hindamine | Kes hindab (min 2) |
|------|-----------|-------------------|
| **Asutuse juht** (direktor, sekretär) | Kvartalis | nõukogu esindaja + personalijuht või ülemus |
| **Osakonnajuht / õppejuht** | Kvartalis | juhtkond + 1 kolleeg |
| **Esiliin** (õpetaja, ametnik, meditsiin, sotsiaal) | 2× aastas | vahetu ülemus + 1 kolleeg |
| **Tugiteenused** (IT, hooldus, turva) | 2× aastas | vahetu ülemus + kasutaja/esindaja |
| **Demonstraator / instruktor** | Kvartalis | 2 kolleegi + üks alluv (kui on) |

**Reegel:** Iga hinnatav saab **vähemalt 2** täidetud vormi + **iserefleksiooni**. Üksi enda täidetud leht ei loe.

---

## Riiklikud kriteeriumid (Lisa AV + 2 rida)

Lisa AV kuus kriteeriumi **pluss** riigisektori read:

| # | Kriteerium | Küsimus |
|---|------------|---------|
| 1–6 | Initsiatiiv … Vastupidavus | (vt Lisa AV) |
| 7 | **Austus ja lugupidamine** | Kas ta suhtleb nii, et teine tunneb end väärtustatuna? (ei solva, ei häbista, ei ignoreeri) |
| 8 | **Turvalisus ja selgus** | Kas ta teatab ohtudest, järgib protsessi, ei jäta pöördumist vastuseta? |

**Usaldusküsimus (muutumatu):** Kas sa selle inimesega **luurele** läheksid?

**Areng:** **K** Kasv | **H** Hoia | **P** Paus — mitte E/T/V, mitte avalik häbistamine.

---

## Riiklik protsess (5 sammu)

| Samm | Tegevus | Vastutaja |
|------|---------|-----------|
| 1 | **Prindi** vorm — iga hindaja oma eksemplar | Personal / sekretariaat |
| 2 | **Täida kirjalikult** enne vestlust — konkreetsed näited | Hindajad (eraldi) |
| 3 | **Vestle** 20–30 min (Lisa P — spordikommentaator) | Juht + hinnatav |
| 4 | **Üks tegu** järgmiseks kvartaliks | Mõlemad kinnitavad |
| 5 | **Hoia konfidentsiaalselt** — mitte Slacki, mitte koridoris | Juhtkond |

**Seinale:** `PEEGEL_RIIK_PLANKETT.pdf` — fuajees või personaliruumis.  
**Koos:** riigisektori austusjuhend (Techno TLN sisekorra eeskirja loogika).

---

## Kus alustada (piloot)

| Prioriteet | Asutus | Miks |
|------------|--------|------|
| 1 | **Techno TLN** (üks linnak) | ~6000 õppijat, ühendamine, Y-põlvkond, austusjuhend olemas |
| 2 | **Kaitseliit / KV koolitusüksus** | Demonstraatorid, instruktorid, distsipliin + inimesekeskus |
| 3 | **Üks vallamaja või sotsiaalosakond** | Kodaniku kontakt, läbipõlemine |
| 4 | **Aluste_kool (SOK)** | Demomehed juba checklisti peal — üleminek AV-SOK ? AV-RIIK |

**Mõõdik 90 päeva:** Kas iga pilootüksuses on 100% juhtkonnast läbinud 1 peegelvestluse (2 vormi + 1 tegu)?

---

## Faasid — riiklik levitamine

### Faas 0 — Standard (valmis)
- Lisa AV + Lisa BD
- PDF-id: `PEEGEL_RIIK_HINDAMISVORM_PRINT.pdf`, `PEEGEL_RIIK_PLANKETT.pdf`
- Üks lause: *Ennast keegi ise ei hinda. Peegel on hindamisvorm.*

### Faas 1 — Piloot (3 asutust, 6 kuud)
- Techno TLN + KV/Kaitseliit + üks omavalitsus
- Igakuine raport: mis töötab, mis triggerdas, üks parandus

### Faas 2 — Sektorid (12 kuud)
- Haridus, tervis, sisejulgeolek, kohalikud omavalitsused
- Koolitaja-koolitajad (demonstraatorid) juhivad vormi, mitte loengut

### Faas 3 — Riiklik raamistik (24 kuud)
- Hindamisvorm osa arenguvestluse standardist avalikus teenistuses
- Seotud: austus ja turvalisus (sisekord), mitte eraldi „pehme projekt"

---

## Mida MITTE teha

| Ära tee | Miks |
|---------|------|
| Avalik pingerida | Trauma, kiusamine (Lisa S) |
| Vorm karistusena | Peegel ? kohtunik |
| Ainult HR-is | Peegel peab olema juhi tööriist |
| Ilma kirjata | Vestlus ununeb, moonutatakse |
| Ilma järgmise sammuta | Kriitika ilma teota |

---

## Üks lause riigile

> **Iga avaliku teenistuse juht ja esiliin teeb kvartalis kirjaliku peegli — ja vastab ausalt: kas ma usaldan seda inimest siis, kui keegi ei vaata?**

---

*Lisa BD — Riiklik peegel. Täiendab Lisa AV. Viimati uuendatud: 2026-07-30.*
