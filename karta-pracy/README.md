# Karta pracy — czasownik „to be” (klasa 4) · do druku

Materiał do wydruku dla uczniów: **język angielski, klasa 4** — czasownik *to be* w zdaniach
**twierdzących** i **przeczących** (*am / is / are*, przeczenie *not*, skróty *I’m not, isn’t, aren’t*).
6 zadań (40 pkt) + zadanie dodatkowe „Dla chętnych”, ramka gramatyczna, słowniczek, samoocena.

## Pliki do druku (A4, 100%)

| Plik | Strony | Do czego |
|---|---|---|
| `karta-pracy-to-be-klasa4-dla-ucznia.pdf` | 2 | dla uczniów — **bez klucza odpowiedzi**; tyle kopii, ilu uczniów |
| `karta-pracy-to-be-klasa4-dla-nauczyciela.pdf` | 3 | wersja z **kluczem odpowiedzi** i kryteriami oceny (s. 3) |
| `karta-pracy-to-be-klasa4-eko-do-druku.pdf` | 2 | wersja **bez teł kolorystycznych** — oszczędza toner, dobra w czerni i bieli |

**Ustawienia druku:** A4, skala 100% (bez „dopasuj do strony”), jednostronnie.
Wersję dla nauczyciela warto wydrukować 1×, uczniowie dostają 2 strony.

## Jak zmienić treść i wygenerować pliki ponownie

Treść zadań i odpowiedzi jest w skrypcie: listy `z1`–`z6` oraz `klucz` (i `slowka`, `wiersze_gram`).

```bash
pip install reportlab      # wymagane
pip install pypdfium2      # opcjonalne: numeracja „strona x z N” w stopce
python generate_karta_pracy.py
```

Skrypt tworzy na nowo wszystkie trzy pliki PDF w tym katalogu.

## Podlinkowanie na stronie (opcjonalnie)

```html
<a href="karta-pracy/karta-pracy-to-be-klasa4-dla-ucznia.pdf" download>
  Karta pracy „to be” (PDF, klasa 4) — do druku
</a>
```
