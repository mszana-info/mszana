# Seminarium — „Muzeum bez ścian”

Materiały seminaryjne powstałe na podstawie wystąpienia „Muzeum bez ścian. Dziedzictwo mieszka
w ludziach”: o muzeum partycypacyjnym, Drodze Loslau, kamieniach pamięci, Ogrodzie
Sprawiedliwych, Archiwum Pamięci i tandemach pokoleń.

## Pliki

| Plik | Co to jest |
|---|---|
| `prezentacja-muzeum-bez-scian.pptx` | prezentacja 16:9 (24 slajdy) do edycji w PowerPoint / Keynote / Google Slides — **z notatkami prelegenta** |
| `prezentacja-muzeum-bez-scian.pdf` | ta sama prezentacja do wyświetlania (24 slajdy, 16:9) |
| `artykul-muzeum-bez-scian.md` | artykuł — wersja tekstowa (z przypisami) |
| `artykul-muzeum-bez-scian.pdf` | artykuł do druku (A4, z przypisami i listą rzeczy do potwierdzenia) |
| `generate_prezentacja.py` | generator prezentacji (PPTX + PDF) |
| `generate_artykul.py` | generator PDF artykułu z pliku `.md` |
| `generate_podstrona.py` | generator podstrony `../muzeum-bez-scian.html` na podstawie `../pamiec.html` |

Podstrona dla serwisu: **`../muzeum-bez-scian.html`** (dodana też karta w `../pamiec.html`
i wpis w `../sitemap.xml`).

## Jak generować ponownie

```bash
pip install reportlab python-pptx pypdfium2      # pypdfium2 opcjonalnie (numeracja stron)
python generate_artykul.py                       # → artykul-muzeum-bez-scian.pdf
python generate_prezentacja.py                   # → prezentacja .pptx + .pdf
python generate_podstrona.py                     # → ../muzeum-bez-scian.html
```

Treść prezentacji siedzi w liście `SLAJDY` (w `generate_prezentacja.py`), a artykułu —
w pliku `artykul-muzeum-bez-scian.md`; oba pliki można swobodnie edytować.

## Przed wygłoszeniem / publikacją — do potwierdzenia

Lista znajduje się na końcu artykułu (`artykul-muzeum-bez-scian.md`, rozdział
„Do sprawdzenia przed publikacją”) i w notatkach do slajdów (oznaczenia
„DO UZUPEŁNIENIA / DO POTWIERDZENIA”). Najważniejsze:

1. nazwa ulicy przy pomniku i krzyżu Drogi Loslau,
2. dokładna data pierwszego Marszu Pamięci przez Żory,
3. czy w Wodzisławiu nie ma jeszcze kamieni pamięci,
4. aktualne terminy konkursów (Sendlerowa / EUSTORY / „Historia Bliska”),
5. link do podcastu na Spotify — do materiałów towarzyszących.

## Uwagi wykonawcze wystąpienia

Tempo ok. 120 słów na minutę, całość ok. 14 minut. Po każdym zdaniu wyróżnionym na slajdzie —
pauza, oddech, kontakt wzrokowy. Awarunkowy plan skrócenia do 10 minut jest w notatkach
przy odpowiednich slajdach (sekcje 2, 6, 7, 10, 13, 16, 17).
