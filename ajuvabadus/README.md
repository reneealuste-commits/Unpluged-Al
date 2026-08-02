# Aju vabadus

Tasuta eestikeelne Android-rakendus mittevägivaldseks suhtluseks endaga (NVC).

Inspireeritud [NVC Guide](https://play.google.com/store/apps/details?id=com.thinkcolorful.nvcguide) rakendusest – sama samm-sammuline voog, aga eesti keeles, trauma-teadlik ja ilma reklaamideta.

## Voog

1. **Avaleht** – kalender, vestluste ajalugu, nupp „Uus vestlus“
2. **Tähelepanek** – „Kui ma näen/kuulen…“
3. **Energia** – vertikaalne liugur
4. **Ebameeldivus** – vertikaalne liugur
5. **Tunded** – valik sõnadest
6. **Vajadused** – universaalsed vajadused
7. **Palve** – kokkuvõte ja salvestus

Kõik andmed jäävad seadmesse (offline).

## Käivitamine

```bash
cd ajuvabadus
flutter pub get
flutter run -d chrome   # veebis testimiseks
flutter run             # Android seadmes
```

## Android APK ehitamine

```bash
flutter build apk --release
```

APK: `build/app/outputs/flutter-apk/app-release.apk`

## Tehnoloogia

- Flutter 3.x
- `shared_preferences` – kohalik salvestus
- `table_calendar` – kalendrivaade

## Seotud OPORD

Lisa P (takistused ja valideerimine) – kui kasutaja ei tunne midagi, alusta kehast/energiast, mitte sundimisest.
