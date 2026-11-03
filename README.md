# MicroPython HTX – ESP32-S3-udgave til brugerens print

Denne version er tilpasset det vedlagte **udsnit** af et skema for et specialfremstillet print med **ESP32-S3-WROOM-1 (N8R8)**. Hele kredsløbet er ikke til rådighed; især er temperatursensorens type og antallet af WS2812B-pixels ukendt.

## GPIO-signaler aflæst fra diagramudsnittet

- GPIO 5: `LED`
- GPIO 11: `Knap` (pulled up, aktiv lav)
- GPIO 12: `Buzzer` (aktiv/passiv type ikke fastslået)
- GPIO 10: `Din` til WS2812B-kæde (pixelantal ikke fastslået)
- GPIO 7: `trig`; GPIO 6: `echo`
- GPIO 8: `SDA`; GPIO 9: `SCL`
- GPIO 1: `temp` (sensortype ikke fastslået)
- GPIO 0: `BOOT`
- GPIO 19 / 20: USB D− / D+ (reserverede på printet)
- GPIO 4: `TIPbase`; GPIO 17/18: `TX`/`RX`

Bemærk: ESP32-S3 er en 3,3 V-mikrocontroller. HC-SR04 Echo kan være 5 V på gængse moduler; kontrollér niveaukonvertering ved fysisk tilslutning. GPIO 0/3/45/46 er strapping-pins. N8R8-modulets flash/PSRAM begrænser brug af interne reserverede pins.

## Hvad er opdateret?

- Alle 12 øvelser og 8 projekter har ESP32-S3-tilpasning og link til en ny board-/pinout-side.
- Øvelse 02 og 11: knap til GPIO 11 (i stedet for 14).
- Øvelse 06: NeoPixels fra GPIO 15 til GPIO 10. Antal pixels er en eksempelværdi på 3; skal kontrolleres på printet.
- Øvelse 07: ultralyd trig fra GPIO 5 til 7 og echo fra GPIO 18 til 6.
- Øvelse 08: I²C fra SDA 21/SCL 22 til SDA 8/SCL 9.
- Øvelse 09: fem bevidste kodefejl er bevaret som en fejlfindingsopgave.
- Wokwi-links starter et **ESP32-S3 MicroPython**-projekt i stedet for en almindelig ESP32. Wokwi-skabelonen simulerer et generisk ESP32-S3 DevKitC-1, IKKE hele specialprintet. Eleverne skal selv tilføje de komponenter, de bruger.
- Ny side: `board-esp32-s3.html`, med GPIO-tabel, skematikudsnit, sikkerhed og MicroPython-eksempler.
- Nye, selvstændige kodeeksempler i `eksempler/`.

## Start og udgiv på GitHub Pages

1. Åbn `index.html` lokalt for at se materialet.
2. Upload indholdet af denne mappe til roden af et GitHub-repository (inklusive `board-skematik-udsnit.png`, CSS og `eksempler/`).
3. Vælg Settings → Pages → Deploy from a branch → `main` → `/(root)`.
4. Se `board-esp32-s3.html` for pinoversigt, før eleverne tilslutter fysisk hardware.

## Kilder

- Wokwi ESP32-S3 MicroPython starter: https://wokwi.com/projects/new/micropython-esp32-s3
- Wokwi dokumentation: https://docs.wokwi.com/guides/esp32
- Espressif GPIO: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/gpio.html
