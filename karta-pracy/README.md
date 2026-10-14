# Karta pracy — czasownik „to be” (klasa 4)

Materiał do wydruku dla uczniów: **język angielski, klasa 4** — czasownik *to be* w zdaniach
**twierdzących** i **przeczących** (*am / is / are*, przeczenie *not*, skróty *I’m not, isn’t, aren’t*).

## Plik do rozdania

| Plik | Zawartość |
|---|---|
| `karta-pracy-to-be-klasa4.pdf` | A4, 3 strony: **s. 1–2 karta pracy dla ucznia**, **s. 3 klucz odpowiedzi** (do wydruku dla nauczyciela) |

Karta zawiera 6 zadań (razem 40 punktów) + zadanie dodatkowe „Dla chętnych”, ramkę
gramatyczną „Zapamiętaj!”, słowniczek i miejsce na samoocenę. Drukować w skali 100%
(A4, bez „dopasuj do strony”), najlepiej jednostronnie — strony 1–2 dla ucznia, strona 3 dla nauczyciela.

## Jak wygenerować plik ponownie / zmienić treść

Treść i układ są opisane w skrypcie — edytuj listy `z1`–`z6` (zadania) oraz `klucz` (odpowiedzi).

```bash
pip install reportlab      # wymagane
pip install pypdfium2      # opcjonalne: numeracja „strona x z N” w stopce
python generate_karta_pracy.py
```

Skrypt zapisuje plik `karta-pracy-to-be-klasa4.pdf` w tym samym katalogu.

## Podlinkowanie na stronie (opcjonalnie)

```html
<a href="karta-pracy/karta-pracy-to-be-klasa4.pdf" download>
  Karta pracy „to be” (PDF, klasa 4)
</a>
```
