# Seminarium — „Muzeum bez ścian”

Materiały seminaryjne powstałe na podstawie wystąpienia „Muzeum bez ścian. Dziedzictwo mieszka
w ludziach”: o muzeum partycypacyjnym, Drodze Loslau, kamieniach pamięci, Ogrodzie
Sprawiedliwych, Archiwum Pamięci i tandemach pokoleń.

## Najszybszy sposób — jeden plik do pobrania

| Plik | Zawartość |
|---|---|
| `pobierz/prezentacja-i-przemowienie-muzeum-bez-scian.zip` | **wszystko**: prezentacja .pptx (z notatkami) + prezentacja PDF + przemówienie PDF i .md + artykuł PDF i .md + instrukcja JAK-KORZYSTAĆ.txt |
| `pobierz/prezentacja-i-przemowienie-muzeum-bez-scian.pdf` | **jeden dokument**: okładka + 25 slajdów + przemówienie + artykuł (47 stron) |

Do odtworzenia pakietu: `python generate_pakiet.py`

## Pliki źródłowe

| Plik | Co to jest |
|---|---|
| `prezentacja-muzeum-bez-scian.pptx` | prezentacja 16:9 (24 slajdy) do edycji w PowerPoint / Keynote / Google Slides — **z notatkami prelegenta** |
| `prezentacja-muzeum-bez-scian.pdf` | ta sama prezentacja do wyświetlania (24 slajdy, 16:9) |
| `przemowienie-muzeum-bez-scian.md` | **przemówienie — wersja uzupełniona, gotowa do wygłoszenia** (z didaskaliami i planem cięć) |
| `przemowienie-muzeum-bez-scian.pdf` | przemówienie do wydruku A4 (duża czcionka, do czytania z mównicy) |
| `artykul-muzeum-bez-scian.md` | artykuł — wersja tekstowa (z przypisami) |
| `artykul-muzeum-bez-scian.pdf` | artykuł do druku (A4, z przypisami i listą rzeczy do potwierdzenia) |
| `generate_prezentacja.py` | generator prezentacji (PPTX + PDF) |
| `generate_artykul.py` | generator PDF artykułu z pliku `.md` |
| `generate_przemowienie.py` | generator PDF przemówienia z pliku `.md` |
| `generate_podstrona.py` | generator podstrony `../muzeum-bez-scian.html` na podstawie `../pamiec.html` |

Podstrona dla serwisu: **`../muzeum-bez-scian.html`** (dodana też karta w `../pamiec.html`
i wpis w `../sitemap.xml`).

## Jak generować ponownie

```bash
pip install reportlab python-pptx pypdfium2      # pypdfium2 opcjonalnie (numeracja stron)
python generate_artykul.py                       # → artykul-muzeum-bez-scian.pdf
python generate_przemowienie.py                  # → przemowienie-muzeum-bez-scian.pdf
python generate_prezentacja.py                   # → prezentacja .pptx + .pdf
python generate_podstrona.py                     # → ../muzeum-bez-scian.html
```

Treść prezentacji siedzi w liście `SLAJDY` (w `generate_prezentacja.py`), a artykułu —
w pliku `artykul-muzeum-bez-scian.md`; oba pliki można swobodnie edytować.

## Przed wygłoszeniem / publikacją — do potwierdzenia

Lista znajduje się na końcu artykułu (`artykul-muzeum-bez-scian.md`, rozdział
„Do sprawdzenia przed publikacją”) i w notatkach do slajdów (oznaczenia
„DO UZUPEŁNIENIA / DO POTWIERDZENIA”). Najważniejsze:

1. ~~nazwa ulicy przy pomniku i krzyżu Drogi Loslau~~ — **uzupełnione:** ul. Ofiar Oświęcimskich
   (pomnik i krzyż), dworzec ul. Rybnicka 2A, tablica ul. Michalskiego 4a,
2. ~~data pierwszego Marszu Pamięci przez Żory~~ — **uzupełnione:** 25–26 stycznia 2025 r.
3. czy w Wodzisławiu nie ma jeszcze kamieni pamięci (potwierdzić w Muzeum w Wodzisławiu),
4. aktualne terminy konkursów (Sendlerowa / EUSTORY / „Historia Bliska”),
5. link do podcastu na Spotify — do materiałów towarzyszących,
6. [imię i nazwisko], instytucja, data — na slajdzie tytułowym i w pierwszych słowach.

**Uzupełnione w tej wersji (fakty potwierdzone źródłowo):** adresy trzech punktów pamięci
w Wodzisławiu; data i trasa pierwszego Marszu Pamięci przez Żory (25–26.01.2025, inicjatywa
Tomasza Przybylskiego); grób 13 więźniów w Świerklanach (pomnik 1948); początek Marszu Pamięci
(5–6.01.2012, 15 osób, inicjatywa śp. Jana Stolarza); **Grób Ofiar Marszu Śmierci w Mszanie**
(33 ofiary, pomnik 1965, tablice z nazwiskami czworga ofiar — 2011, tablica wdzięczności
w przedsionku kościoła św. Jerzego).

## Uwagi wykonawcze wystąpienia

Tempo ok. 120 słów na minutę, całość ok. 14 minut. Po każdym zdaniu wyróżnionym na slajdzie —
pauza, oddech, kontakt wzrokowy. Awarunkowy plan skrócenia do 10 minut jest w notatkach
przy odpowiednich slajdach (sekcje 2, 6, 7, 10, 13, 16, 17).
