CO ZMIENIONO — PACZKA PORTALU 17.11.2026
=============================================================

Paczka zawiera komplet plików, które przesłałeś, plus nowy materiał
"Opłaty za odpady — stanowisko radnego (tura II konsultacji)" wpięty
w strukturę serwisu. Wgraj ZAWARTOŚĆ folderu do katalogu głównego
serwisu (obok regulamin.html, kontakt.html itd.).


-------------------------------------------------------------
1. NOWY PLIK
-------------------------------------------------------------
  materialy-mieszkancow-odpady-tura-2.html   (51,0 KB)

  Nazwa zgodna z konwencją serwisu:
    materialy-mieszkancow.html                 <- przegląd zbioru
    materialy-mieszkancow-odpady.html          <- tura I
    materialy-mieszkancow-odpady-tura-2.html   <- tura II  (NOWY)

  Adres: https://mszana.info/materialy-mieszkancow-odpady-tura-2.html


-------------------------------------------------------------
2. NOWE GRAFIKI (folder grafiki/)
-------------------------------------------------------------
  protokol-konsultacje-odpady-2026-tura-2.png   1936x900   173 KB
  protokol-konsultacje-odpady-2026-tura-2.webp  1936x900   140 KB

  Zrzut protokołu z II tury (16.11.2026). Wstawiony w <picture>
  z <source type="image/webp"> — dokładnie tak, jak protokół I tury.
  UWAGA: nie podmieniaj plików protokol-konsultacje-odpady-2026.png/.webp —
  to protokół z I tury, używany na stronie materialy-mieszkancow-odpady.html.

  Wszystkie pozostałe grafiki (artykul-glos-i-wartosci, mapa-serce-mszana-widok,
  og-glos-i-wartosci) leżą w grafiki/ bez zmian.


-------------------------------------------------------------
3. ZMIENIONE PLIKI
-------------------------------------------------------------
  materialy-mieszkancow.html
    - lista "Dostępne materiały": dodana druga pozycja (tura II)
    - opis przy pierwszym materiale: "stanowiska radnych (konsultacje 2026)"
      -> "stanowiska radnych (tura I konsultacji, 2 listopada 2026)" dla odróżnienia tur
    - nowa karta w siatce: "Opłaty za odpady — stanowisko radnego
      (tura II konsultacji)" z linkiem i dwiema informacjami o turach

  materialy-mieszkancow-odpady.html
    - menu: dodana pozycja "Opłaty za odpady — stanowisko radnego (tura II)"
    - pager na dole: "Dokumenty i źródła →" zamienione na
      "Opłaty za odpady — tura II →" (naturalna kolejność czytania)

  index.html, nadeslij.html, glos.html
    - menu "Materiały mieszkańców": dodana pozycja tury II

  sitemap.xml
    - dodany adres materialy-mieszkancow-odpady-tura-2.html (lastmod 2026-11-17)
    - lastmod strony materialy-mieszkancow.html zmieniony na 2026-11-17

  PLIKI BEZ ZMIAN: config.js, skrypt.js, robots.txt,
  grafiki/artykul-glos-i-wartosci.*, grafiki/mapa-serce-mszana-widok.*,
  grafiki/og-glos-i-wartosci.jpg, grafiki/protokol-konsultacje-odpady-2026.*


-------------------------------------------------------------
4. CZEGO NIE MA W PACZCE (świadomie)
-------------------------------------------------------------
  Paczka zawiera tylko pliki, które przesłałeś. Brakuje stron, do których
  odwołują się linki menu: regulamin.html, kontakt.html, pamiec.html,
  dokumenty.html oraz style.css. To nie błąd — te pliki leżą już na serwerze.
  Przy wgrywaniu NIE usuwaj ich i nie nadpisuj style.css starszą wersją.


-------------------------------------------------------------
5. SPRAWDZENIE PRZED WGRANIEM
-------------------------------------------------------------
  - parser HTML: 0 błędów na wszystkich 5 stronach
  - brak martwych kotwic (#...): 0
  - wszystkie obrazy: istnieją w grafiki/
  - różnica względem wersji "github-pages": linki są RELATYWNE
    (materialy-mieszkancow.html, regulamin.html), bo paczka idzie
    na mszana.info, a nie na github.io


-------------------------------------------------------------
6. TREŚĆ MATERIAŁU Z TURY II
-------------------------------------------------------------
  - zdanie wiążące ze zbiorem "Materiały mieszkańców"
  - pytanie administracji portalu + informacja o odpowiedzi radnego
    i zgodzie autora na publikację
  - blok "Aktualizacja": III tura konsultacji 17-23.11.2026
    (zarządzenie AEI.0050.196.2026, uwagi do 23.11 godz. 16:00)
  - "W skrócie" — ustalenia po II turze
  - cztery dokumenty w rozwijanych blokach:
      01 stanowisko radnego z 9.11.2026 (materiał nadesłany, pełna treść)
      02 protokół z II tury 16.11.2026 (treść + zrzut + webp)
      03 protokół z I tury 28.10.2026
      04 projekt uchwały z 16.11.2026 z kalkulacją kosztów
  - "Czego nie wiadomo", źródła (8 pozycji), korekty i sprostowania
  - ramka "Pozostałe materiały w tym zbiorze"


-------------------------------------------------------------
7. WYSZUKIWARKI, IKONY, PODGLĄD LINKU (dodane 18.11.2026)
-------------------------------------------------------------
  NOWE PLIKI:
    favicon.ico                       (16/32/48/64 px)
    site.webmanifest                  (manifest PWA, theme #0f5132)
    grafiki/favicon-32.png
    grafiki/favicon-192.png
    grafiki/favicon-512.png
    grafiki/apple-touch-icon.png      (180 px)
    grafiki/logo-mszana-info.png      (512 px, przezroczyste tło)
    grafiki/og-mszana-info.jpg        (1200x630, podgląd linku)

  ZMIENIONE:
    wszystkie 6 stron HTML:
      - <link rel="icon"> (ico + 32 + 192 + apple-touch) i <link rel="manifest">
      - og:image + og:image:width/height/alt + twitter:card (summary_large_image)
      - index.html: JSON-LD WebSite + Organization + FAQPage
      - materialy-mieszkancow.html: CollectionPage + ItemList (2 materiały)
      - materialy-mieszkancow-odpady.html: Article (data 2026-11-02)
      - materialy-mieszkancow-odpady-tura-2.html: Article (data 2026-11-17)
    robots.txt: blokady dla Googlebot, Googlebot-Image, Bingbot, DuckDuckBot
                + Sitemap + Host

  DODANA SEKCJA na index.html (przed </main>):
    "Uchwała o herbie Gminy Mszana — dokument nadesłany przez Urząd Gminy"
    z linkiem do PDF w dokumenty/uchwala-XXIII-38-2000-w-sprawie-herbu-gminy-mszana.pdf

  UWAGA: PDF uchwały jest skanem bez warstwy tekstowej (6 stron).
    Google nie odczyta z niego treści — dlatego opis i tytuł uchwały
    są w HTML (sekcja + FAQPage), a nie tylko w PDF.

  CO ZROBIĆ W GOOGLE SEARCH CONSOLE (bez tego ikona i wyniki
  pojawią się później niż mogłyby):
    1. https://search.google.com/search-console → dodaj usługę
       (właściwość typu "Prefiks URL"): https://mszana.info/
    2. Zweryfikuj przez plik HTML w katalogu głównym albo przez DNS.
    3. Indeksowanie → Mapy witryn → dodaj https://mszana.info/sitemap.xml
    4. Kontrola adresu URL → wklej https://mszana.info/ → "Poproś o zindeksowanie"
    5. To samo dla adresu materialy-mieszkancow-odpady-tura-2.html
    6. Test wyników z elementami rozszerzonymi → sprawdź FAQPage i Article
    7. Favicona Google odświeża osobno i potrafi to trwać od kilku dni
       do kilku tygodni — nie da się tego przyspieszyć.

  KLUCZOWA UWAGA O FAVICONIE:
    Google wymaga, aby ikona była kwadratowa, miała przezroczyste tło
    lub tło w kolorze marki i była dostępna pod stałym adresem.
    Podpięte: /favicon.ico oraz /grafiki/favicon-32.png i 192.png.
    Jeśli po dwóch tygodniach w wynikach nadal widać domyślną kulkę,
    sprawdź w Search Console raport "Indeksowanie stron" — favicona
    pobierana jest z Googlebot-Image, dlatego w robots.txt jest osobny
    wpis dla Googlebot-Image.

  CZEGO NIE DA SIĘ ZAGWARANTOWAĆ:
    Pozycja strony w Google nie zależy od meta tagów, tylko od treści,
    linków i czasu. Meta tagi i JSON-LD zwiększają szansę na tzw. rich
    results (podgląd z ikoną, tytułem i opisem), ale nie dają gwarancji
    wyświetlenia pod jakimkolwiek hasłem.


-------------------------------------------------------------
8. LICZNIK ODSŁON — DIAGNOZA I NAPRAWA (18.11.2026)
-------------------------------------------------------------
  OBJAW:  w stopce zamiast liczby pokazywała się kreska "—"
          z podpisem "Nie udało się pobrać licznika".

  PRZYCZYNA (zmierzona, nie zgadywana):
          Adres z config.js zwracał HTTP 404 "Page Not Found":
          https://script.google.com/macros/s/AKfycbz4.../exec
          404 = wdrożenie Apps Script nie istnieje. Najczęstsze powody:
            - wdrożenie zostało usunięte (Wdróż → Zarządzaj wdrożeniami → Usuń),
            - projekt Apps Script skasowano albo wyczyszczono,
            - wdrożenie zastąpiono nowym, a config.js nie został zaktualizowany.
          Kod strony był sprawny — licznik nie miał do czego się odezwać.

  CO ZMIENIONO:
    config.js
      - APPS_SCRIPT_URL wyczyszczony (""). Stary adres był martwy.
    skrypt.js
      - gdy licznik nie odpowie w 9 s, próbuje raz ponownie po 2,5 s,
      - po drugiej nieudanej próbie CAŁY blok "Odsłony serwisu" jest
        ukrywany (hidden) — zamiast kreski i komunikatu o błędzie,
      - podobnie po powrocie do karty: jeśli nadal nie ma liczby, próbuje ponownie.

  NOWY PLIK: apps-script-licznik.gs
      Gotowy skrypt licznika. Wklej do nowego projektu Apps Script,
      wdróż jako aplikację internetową (wykonaj jako JA, dostęp: KAŻDY),
      skopiuj adres /exec i wklej do config.js.

  JAK PRZYWRÓCIĆ LICZNIK W 5 KROKACH:
    1. script.google.com → Nowy projekt → wklej apps-script-licznik.gs
    2. Wdróż → Nowe wdrożenie → Aplikacja internetowa
       • Wykonaj jako: JA
       • Kto ma dostęp: KAŻDY
    3. Skopiuj adres kończący się na /exec
    4. Wklej do config.js:  APPS_SCRIPT_URL: "https://script.google.com/macros/s/.../exec"
    5. Test w przeglądarce:
       <adres>/exec?action=peek        -> powinno zwrócić {"views":0,...}
       <adres>/exec?action=count       -> zwiększa licznik o 1

  UWAGA O STAREJ LICZBIE:
      Licznik trzymał jedną liczbę we Właściwościach skryptu. Jeśli
      projekt został usunięty, liczby nie da się odzyskać — nowy
      projekt startuje od zera. Jeśli chcesz zachować ciągłość,
      w nowym projekcie uruchom raz funkcję ustawLicznik(liczba)
      i wpisz ostatnią znaną wartość (np. z kopii zapasowej arkusza).


-------------------------------------------------------------
9. LICZNIK — PRZYWRÓCONY (20.11.2026)
-------------------------------------------------------------
  Nowy adres wdrożenia wpisany do config.js:
    .../macros/s/AKfycbyWdTvfuUIjLPm_ClR2vgulMdOTdEXjvpv4FpCuY6b11dINcypXl1OLUbImtEidojpW/exec

  TESTY WYKONANE (curl, 20.11.2026):
    ?action=peek   -> HTTP 200, {"views":0,"updated":"..."}
    ?action=count&callback=cbTest
                   -> HTTP 200, text/javascript, cbTest({"views":1,...});
                      czyli JSONP działa i licznik się zwiększa

  UWAGA: test "count" podniósł licznik o 1 (z 0 na 1). Jeśli chcesz
  zacząć od zera, uruchom w edytorze Apps Script funkcję wyzerujLicznik().
  Jeśli chcesz przenieść starą liczbę, uruchom ustawLicznik(N).

  CO ZADZIAŁA AUTOMATYCZNIE PO WGRANIU:
    - liczba odsłon pokaże się w stopce wszystkich stron
    - jeśli endpoint znowu przestanie odpowiadać, blok "Odsłony serwisu"
      schowa się sam po dwóch próbach (ok. 12 s) — bez kreski i błędu
