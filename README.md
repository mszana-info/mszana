# Mszana.info — instrukcja wgrania

Paczka zawiera kompletny, gotowy do publikacji serwis statyczny.
Wersja: 19.10.2026 r. (aktualizacja 11) · 7 stron · materiał „Szeptanie zamiast mówienia”

---

## Co jest w paczce

```
mszana.info/
├── index.html          strona główna (hero, mapa, O nas, Jak działamy)
├── pamiec.html         Pamięć i Historia
├── glos.html           ★ Głos i wartości — „Szeptanie zamiast mówienia"
├── dokumenty.html      Dokumenty i źródła
├── nadeslij.html       Prześlij materiał / zgłoś sprawę
├── kontakt.html        Kontakt
├── regulamin.html      Regulamin serwisu (rozdziały I–XI)
├── style.css           wspólny arkusz stylów
├── skrypt.js           licznik odsłon, czcionka, kontrast, menu, modal RODO
├── config.js           adres Google Apps Script (licznik odsłon)
├── sitemap.xml         mapa witryny (7 URL-i)
├── robots.txt          reguły dla robotów
├── CNAME               domena mszana.info
├── google65d22e3c799aa146.html   plik weryfikacyjny Google Search Console
├── README.md
└── grafiki/
    ├── mapa-serce-mszana-widok.png / .webp
    ├── artykul-glos-i-wartosci.png / .webp
    └── og-glos-i-wartosci.jpg     (1200×630, podgląd w social mediach)
```

`waliduj.py` to opcjonalne narzędzie deweloperskie — sprawdza poprawność
HTML na wszystkich stronach i wypisuje liczbę kotwic oraz obrazów. Nie jest
potrzebne do publikacji serwisu; uruchomienie: `python3 waliduj.py`.

**Brak zależności.** Serwis jest w pełni statyczny — nie wymaga PHP, bazy danych
ani procesu budowania. `config.js` i `skrypt.js` to jedyne pliki JS, oba działają
bez serwera.

---

## Wariant 1 — GitHub Pages (zalecany, obecna konfiguracja)

Repozytorium `mszana-info/mszana` już ma włączone GitHub Pages:
gałąź `main`, katalog `/`, domena `mszana.info`, HTTPS wymuszony, certyfikat ważny.

```bash
# 1. sprawdź, że jesteś w katalogu projektu
cd mszana

# 2. dodaj pliki
git add .

# 3. zatwierdź
git commit -m "Aktualizacja serwisu: materiał Głos i wartości, czytelna treść, sekcja O nas"

# 4. wypchnij na gałąź, z której czyta GitHub Pages
git push origin main
```

Po wypchnięciu GitHub Pages zbuduje witrynę automatycznie (1–3 minuty).
Sprawdź: **https://mszana.info/** → potem sekcja **Głos i wartości**.

> **Uwaga na gałąź.** GitHub Pages czyta z `main`. Jeśli pracujesz na gałęzi
> roboczej (np. `arena/...`), wypchnij najpierw na `main`:
> ```bash
> git checkout main
> git merge arena/twoa-galaz
> git push origin main
> ```

### Wariant 1a — bez terminala (przeciąganie plików)
1. Otwórz repozytorium na GitHubie → zakładka **Add file** → **Upload files**
2. Przeciągnij zawartość folderu `mszana.info/` (wraz z podfolderem `grafiki/`)
3. Zaznacz „Commit changes” → wpisz opis → **Commit changes**
4. Poczekaj na automatyczny build GitHub Pages

> Przy przeciąganiu **nie wchodź do** folderu `mszana.info/` — chcesz, by pliki
> trafiły do katalogu głównego repozytorium. Folder `grafiki/` przeciągnij razem
> z resztą, żeby zachować strukturę.

---

## Wariant 2 — własny hosting (FTP/SSH)

1. Rozpakuj paczkę.
2. Wyślij **całą zawartość** folderu `mszana.info/` do katalogu `public_html`,
   `www`, `htdocs` lub `docroot` — zależnie od hostingu.
3. Upewnij się, że `CNAME` znalazł się w katalogu głównym (serwery często go
   ignorują przy wgraniu przez FTP — wtedy ustaw domenę w panelu hostingu).
4. Włącz HTTPS i przekierowanie `http://` → `https://`.

---

## Wariant 3 — Netlify / Cloudflare Pages (import z ZIP-a)

1. **Netlify:** nowy projekt → *Add new site* → *Import an existing project*,
   albo **Deploy manually** — przeciągnij ZIP.
2. **Cloudflare Pages:** *Create a project* → *Upload assets* → przeciągnij ZIP.
3. Po wgraniu ustaw custom domain na `mszana.info` i przekieruj DNS
   na dostawcę (CNAME).

---

## Po wgraniu — lista kontrolna

- [ ] `https://mszana.info/` otwiera się poprawnie, HTTPS bez ostrzeżeń
- [ ] `https://mszana.info/glos.html` — materiał „Szeptanie zamiast mówienia”
- [ ] `https://mszana.info/sitemap.xml` zawiera 7 adresów
- [ ] Menu główne zawiera pozycję **Głos i wartości** (wszystkie 7 stron)
- [ ] Stopka „Na skróty” zawiera **Głos i wartości**
- [ ] Na stronie głównej w sekcji **O nas** jest blok z materiałem i przyciskiem
      „Przeczytaj materiał →”
- [ ] Sekcja „Jak działamy” ma 3. kartę: **Głos i wartości**
- [ ] Grafiki się ładują (`/grafiki/*.png` i `*.webp` zwracają 200)
- [ ] Licznik odsłon w stopce się zlicza (wymaga działającego Apps Script)
- [ ] Modal RODO działa (przycisk w lewym górnym rogu) i ma wersję tekstową
      działającą bez JavaScriptu
- [ ] Pasek niezależności i stopka na wszystkich 7 stronach podają nowe
      brzmienie: „Mszana.info jest niezależną platformą informacyjno-społeczną.
      Nie jest oficjalną stroną Gminy Mszana ani jej jednostki organizacyjnej
      i nie jest prowadzony przez Urząd Gminy Mszana.”
- [ ] Przełącznik kontrastu (ikona w prawym górnym rogu) działa

### Google Search Console
Po wgraniu zaktualizuj `sitemap.xml` — adres jest już podany w `robots.txt`.
W Search Console: **Sitemaps** → wpisz `sitemap.xml` → zatwierdź.
Opcjonalnie zgłoś `https://mszana.info/glos.html` do indeksowania.

---

## Co zmieniło się w tej wersji

**Nowe:**
- `glos.html` — materiał „Szeptanie zamiast mówienia” (sekcja „Głos i wartości”)
- `grafiki/artykul-glos-i-wartosci.png` / `.webp` — ilustracja do materiału
- `grafiki/og-glos-i-wartosci.jpg` — podgląd 1200×630 dla social mediów
- Blok materiału w sekcji „O nas” na stronie głównej
- Pozycja „Głos i wartości” w menu, stopce, pagerze i `sitemap.xml`

**Czytelność materiału:**
- akapity rozbite na 2–3 zdania
- zestawienie sześciu zasad w formie tabeli „Zasada → Co to oznacza w praktyce”
- dwie listy zamiast ściany tekstu (koszt wypowiedzi, pętla umierającej debaty)
- (blok „W skrócie” i spis treści zostały usunięte w aktualizacji 6)

**Dostosowanie materiału do Regulaminu (aktualizacja 2):**
- oznaczenie niezależności — nowe brzmienie we wszystkich 7 stronach, w tym
  w cytowanym brzmieniu w rozdziale III § 1 Regulaminu
- metryka materiału — dodany kontakt do autora i zasięg terytorialny (rozdz. V § 4)
- scena w leadzie przedstawiona jako przykład, nie jako konkretne zdarzenie
  (rozdz. II § 3–4)
- podpis: zastrzeżenie, że tekst nie dotyczy konkretnej decyzji organu Gminy
  i nie zwracano się o stanowisko (rozdz. II § 1–2), oraz że cytaty osób
  trzecich nie są stanowiskiem Administracji portalu (rozdz. II § 5)
- sekcja „Granice” — art. 213 Kodeksu karnego i tryb ścigania z oskarżenia
  prywatnego; pełna lista aktów prawnych z artykułami
- sekcja „Forum publiczne” — rozróżnienie narzędzi mieszkańca i narzędzi
  radnego: interpelacje i zapytania składają radni (art. 24 ustawy o samorządzie
  gminnym), mieszkaniec ma wniosek o informację publiczną, skargę, wniosek,
  konsultacje, budżet obywatelski, młodzieżową radę i obywatelską inicjatywę
  uchwałodawczą
- wyjaśniono, że Serwis nie moderuje grupy na Facebooku — obowiązują odrębne
  reguły grupy (rozdz. VIII § 5)
- zastrzeżenie, że materiał nie jest usługą prawną ani poradą prawną
  (rozdz. VIII § 6)
- modal RODO: doprecyzowany punkt 10 o treściach w grupie (rozdz. VIII § 5)
- czas czytania skorygowany na 10 minut

**Usunięcie progów i odesłań (aktualizacja 11):**
- sesja rady — usunięty próg zgłoszenia do debaty nad raportem o stanie gminy
  (20 000 mieszkańców, 20 podpisów, 15 osób mówiących; art. 28aa ust. 6–8)
- wniosek o informację publiczną — usunięte zdanie o obowiązku odpowiedzi
  na piśmie (art. 13 u.d.i.p.); w tekście pozostało wskazanie art. 2 i 10
- zebranie wiejskie — usunięte odesłanie do statutu gminy i statutu sołectwa
- usunięty akapit o przysyłaniu materiałów (formularz, wymogi rozdziału V,
  zasady publikacji) — w sekcji „Trzy pytania” zostało samo zaproszenie
  „Masz własny temat… — napisz.”
- z listy źródeł usunięty art. 28aa ustawy o samorządzie gminnym — nie ma już
  do niego odwołania w treści
- czas czytania: 8 minut (1 833 słowa)

**Dostosowanie po skróceniu materiału (aktualizacja 10):**
- nagłówek „Czy potrafisz mówić głośno? Sześć zasad” zmieniony na „Sześć zasad
  obrony wartości” — pytanie nie miało już odpowiedzi w tekście po usunięciu
  podsekcji
- akapit wprowadzający do sekcji przepisany tak, żeby nie odwoływał się
  do pytania z nagłówka
- zapowiedź na stronie głównej skrócona z pięciu do trzech punktów — zgodna
  z obecną objętością materiału (8 minut)
- z `style.css` usunięte nieużywane reguły `.w-sprocie`, `.sprocie-tytul`,
  `.spis-trecci`, `.spis-tytul` oraz ich warianty w trybie wysokiego kontrastu
  i zapytaniu medialnym

**Poprawki spójności po cięciach (aktualizacja 9):**
- usunięte odwołania do tematów, których materiał już nie omawia: „spór o język
  i ideologię” oraz „pytanie o ideologię” (wątek słowa „woke” i etykiet zniknął
  razem z tabelą faktów)
- „Wracamy więc do pytania postawionego na początku: czy potrafisz mówić głośno?”
  zamienione na odwołanie do pytania, które faktycznie pada w pierwszym akapicie
  („czy warto powiedzieć swoje głośno?”)
- sprawdzone: brak innych odwołań do usuniętych treści, brak martwych kotwic,
  brak powtórzonych wyrazów, akapity w normie (poza cytowanymi dokumentami)
- czas czytania: 8 minut (1 926 słów)

**Usunięcie rozbudowanych opisów zasad (aktualizacja 8):**
- usunięto sześć podsekcji `h3` z rozbudowanym omówieniem każdej zasady
  (2 851 znaków)
- sekcja „Sześć zasad” zawiera teraz dwa akapity wprowadzenia i tabelę
  „Zasada → Co to oznacza w praktyce”
- razem z podsekcjami zniknęły dwa odnośniki: do rozdziału VII § 1 Regulaminu
  i do sekcji „Dokumenty i źródła” (w innym miejscu materiał nadal odsyła
  do Dokumentów i źródeł)
- czas czytania skorygowany na 8 minut (1 928 słów)

**Usunięcie cytatu Hughesa (aktualizacja 7):**
- usunięty cytat „When we lose the right to be different, we lose the privilege
  to be free” wraz z podaniem źródła (Faneuil Hall, 17 VI 1925)
- usunięte dwa akapity, które go komentowały, w tym drugi cytat z tego samego
  wystąpienia („Our institutions were not devised to bring about uniformity
  of opinion…”)
- z listy źródeł usunięto pozycję Charles Evans Hughes — nie ma już do niej
  odwołania w tekście
- z podpisu usunięto zdanie o wypowiedzi Hughesa (rozdz. II § 5 Regulaminu);
  w materiale nie ma już cytatów osób trzecich
- czas czytania skorygowany na 9 minut (2 266 słów)

**Usunięcie spisu treści i bloku „W skrócie” (aktualizacja 6):**
- z materiału usunięty spis treści „W tym materiale” (7 pozycji z odnośnikami)
- usunięta ramka „W skrócie — pięć rzeczy, które warto zapamiętać”
- materiał otwiera się teraz od razu leadem, po nim trzy akapity wprowadzenia
  i sekcja „Szeptanie nie jest zgodą”
- czas czytania bez zmian: 10 minut

**Usunięcie terminów i progów (aktualizacja 5):**
- wniosek o udostępnienie informacji publicznej — usunięty termin odpowiedzi
  („14 dni”); pozostaje wskazanie, że urząd ma obowiązek odpowiedzieć na piśmie
  (art. 13 u.d.i.p.)
- interpelacja i zapytanie — usunięty termin odpowiedzi wójta („14 dni”);
  pozostaje wskazanie, że wójt musi odpowiedzieć, a pytanie i odpowiedź trafiają
  do BIP (art. 24 ust. 3 i 6–7 u.s.g.)
- obywatelska inicjatywa uchwałodawcza — usunięte dwa zdania o progu 200 podpisów
  i o rozpatrzeniu na najbliższej sesji w ciągu 3 miesięcy; zamiast tego odesłanie
  do statutu gminy, który określa liczbę podpisów i tryb rozpatrzenia
- ten sam termin usunięty z bloku „Przepisy, do których warto zajrzeć”
- bez zmian: terminy i progi dotyczące debaty nad raportem o stanie gminy
  (art. 28aa ust. 6–8), bo nie były objęte tą prośbą

**Usunięcie tabeli faktów (aktualizacja 4):**
- z materiału usunięto tabelę „Fakty — ze źródłem / Oceny i hipotezy — opinia autora”
- wraz z nią zniknęły wątki, które występowały tylko tam: słowniki Merriam-Webster
  i Oxford (data wejścia słowa „woke”), list do Komisji ds. Sądownictwa Izby
  Reprezentantów USA oraz zdanie sędziego Brandeisa z 1927 r.
- z listy źródeł usunięto pięć pozycji, do których nie ma już odwołań w tekście;
  w podpisie została tylko wypowiedź Charlesa Evansa Hughesa
- punkt 2 bloku „W skrócie” i blok na stronie głównej opisują teraz to, co faktycznie
  jest w tekście: milczenie jednostki jest rozsądne, milczenie wszystkich — nie
- czas czytania bez zmian: 10 minut

**Uproszczenie języka (aktualizacja 3):**
- cały materiał przepisany prostszym językiem — krótsze zdania, mniej pojęć
  specjalistycznych, trudne terminy wyjaśnione przy pierwszym użyciu
- słowo „artykuł” zastąpione słowem „materiał” w całym tekście, w spisie treści
  i w bloku na stronie głównej
- usunięty nagłówek „Co jest faktem, a co jest opinią” oraz dwa zdania
  wprowadzające do tabeli — tabela faktów i opinii zaczyna się od razu po leadzie
- poprawione literówki (m.in. „ruszyłała”, „rozdziałie”, „wypowiedzie”)
- czas czytania: 10 minut

**Bez zmian:** stopka pozostaje zgodna z resztą serwisu; modal RODO jest bajt
w bajt taki sam we wszystkich 7 plikach (różni się tylko odnośnik „Rozdział IX
Regulaminu” w samym regulaminie — trafia tam na własną stronę).
