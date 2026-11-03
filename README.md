# MicroPython HTX – øvelsesbank

Statisk undervisningsside til GitHub Pages, med 12 selvstændige emnesider, forside, CSS og søgning.

## Offentliggør på GitHub Pages

1. Opret et nyt public repository, fx `micropython-htx`.
2. Upload **indholdet** af denne mappe til roden af repositoryet (index.html skal ligge i roden).
3. Gå til **Settings → Pages → Build and deployment**.
4. Vælg **Deploy from a branch**, branch `main`, folder `/(root)` og gem.
5. Åbn den GitHub Pages-adresse, som GitHub viser.

## Redigering

- `index.html`: Forsidens tekst, kort og emner.
- `oevelse-01.html` … `oevelse-12.html`: Hvert emnes teori, opgaver og kode.
- `ressourcer.html`: Links og vejledning.
- `style.css`: Design og mobilvisning.
- `script.js`: Søgning, filtrering og kopiering af kode.

Den statiske side kræver hverken server eller build-proces. Den kan også åbnes lokalt med `index.html`.

**Bemærk:** Wokwi-links går til nye, tomme ESP32 MicroPython-projekter. For at få øvelsesspecifikke kredsløb skal du oprette og gemme Wokwi-projekter og udskifte links på relevante emnesider.

## Projektværksted

`projekter.html` samler otte selvstændige miniprojekter. Hvert `projekt-XX.html` er et projektbrief med minimumskrav, selvvalgte udvidelser, test og dokumentation. `projekt-skabelon.html` understøtter elevvalgte problemstillinger.
