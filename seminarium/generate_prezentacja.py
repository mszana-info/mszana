# -*- coding: utf-8 -*-
"""
Prezentacja na seminarium: „Muzeum bez ścian. Dziedzictwo mieszka w ludziach"
na podstawie wystąpienia o muzeum partycypacyjnym, Drodze Loslau i pamięci lokalnej.

Generuje:
  - prezentacja-muzeum-bez-scian.pptx   (16:9, do edycji, z notatkami prelegenta)
  - prezentacja-muzeum-bez-scian.pdf    (16:9, do wyświetlania)

Uruchomienie:
    pip install python-pptx reportlab
    python generate_prezentacja.py
"""

import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

KATALOG = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- styl
GREEN = RGBColor(0x0F, 0x51, 0x32)
GREEN_L = RGBColor(0xE7, 0xF1, 0xEB)
AMBER = RGBColor(0xC9, 0x82, 0x1A)
INK = RGBColor(0x22, 0x22, 0x22)
GREY = RGBColor(0x5A, 0x5A, 0x5A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Arial"

W_IN, H_IN = 13.333, 7.5  # 16:9

# ================================================================ TREŚĆ SLAJDÓW
SLAJDY = [
    {
        "layout": "title",
        "eyebrow": "SEMINARIUM · DZIEDZICTWO I PAMIĘĆ LOKALNA",
        "title": "Muzeum bez ścian",
        "subtitle": "Dziedzictwo mieszka w ludziach.\nO muzeum partycypacyjnym, Drodze Loslau\ni o pamięci, którą trzeba zdążyć zapisać",
        "footer": "Prelegentka: [imię i nazwisko]  ·  [instytucja]  ·  [data]",
        "notes": (
            "Uwagi wykonawcze: tempo spokojne, ok. 120 słów na minutę, całość ~14 minut.\n"
            "Nie spieszyć się. Po każdym zdaniu wyróżnionym na slajdzie — pełna pauza, oddech, "
            "kontakt wzrokowy z salą.\n"
            "Ostatnie zdanie („Dziękuję.”) powiedzieć wolniej i zostać chwilę w ciszy.\n"
            "UZUPEŁNIĆ przed wygłoszeniem: imię i nazwisko, instytucja, data, miejsce seminarium."
        ),
    },
    {
        "layout": "poem",
        "eyebrow": "",
        "title": "Zamknijmy na chwilę oczy…",
        "poem": [
            "W styczniu czterdziestego piątego",
            "mróz zaciskał dłonie na drodze.",
            "Tysiące kroków szło ku stacji,",
            "a miasto patrzyło zza okien.",
        ],
        "notes": (
            "Wiersz czytamy spokojnie, wolniej niż resztę wystąpienia. Didaskalia w nawiasach "
            "(„zamknijmy oczy”) mówimy, nie czytamy z kartki.\n"
            "Po ostatniej linijce — pauza 2–3 sekundy, dopiero potem przejście dalej."
        ),
    },
    {
        "layout": "poem",
        "eyebrow": "…i posłuchajmy, o co pyta ta droga",
        "title": "",
        "poem": [
            "Jedni odwracali wzrok.",
            "Inni otwierali drzwi.",
            "Czasem jeden gest wystarcza,",
            "by ocalić w człowieku człowieka.",
            "",
            "Ślady dawno przykrył czas,",
            "lecz droga wciąż o coś pyta:",
            "kiedy cudze cierpienie puka,",
            "czy umiesz otworzyć?",
        ],
        "notes": "Po wierszu od razu teza całego wystąpienia (slajd następny).",
    },
    {
        "layout": "big",
        "eyebrow": "TEZA",
        "title": "Dziedzictwo nie mieszka w gablotach.\nDziedzictwo mieszka w ludziach.",
        "subtitle": "Zadaniem instytucji kultury jest zrobić wszystko,\nżeby zdążyć je od nich usłyszeć.",
        "notes": (
            "To zdanie jest osią całego wystąpienia — wracamy do niego w zakończeniu.\n"
            "Po wypowiedzeniu: pauza."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "1. ZMIANA MODELU",
        "title": "Od gabloty do dialogu",
        "bullets": [
            "Jeszcze 50 lat temu: cisza, dystans, kontemplacja — eksponat chroniony gablotą i czerwonym sznurem oddzielał widza od dzieła.",
            "Dziś: sztuka przestaje być wyłącznie przedmiotem oglądu — staje się narzędziem dialogu społecznego.",
            "Dziedzictwo przestaje być statycznym zasobem, chronionym przed zmianą — staje się żywym procesem współtworzonym przez mieszkańców.",
        ],
        "quote": "Historia nie dzieje się w muzeach. Muzea tylko próbują ją dogonić.",
        "notes": "Slajd wprowadzający w teorię — mówimy spokojnie, bez pośpiechu.",
    },
    {
        "layout": "content",
        "eyebrow": "2. NOWA MUZEOLOGIA",
        "title": "Nowa muzeologia → muzeum partycypacyjne",
        "bullets": [
            "Punkt zwrotny: ruch „nowej muzeologii” i wyrastająca z niego koncepcja muzeum partycypacyjnego.",
            "Publiczność może tworzyć, dzielić się i łączyć wokół zbiorów.",
            "Nie chodzi o kolejny eksponat ani kolejną salę — chodzi o to, by muzeum stało się miejscem, które się współtworzy, a nie tylko odwiedza.",
        ],
        "notes": (
            "Gdy trzeba skrócić do 10 minut: zostaw z tego slajdu trzy zdania zamiast całego "
            "akapitu — oszczędność ok. 40 s."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "3. DOWÓD Z BLISKA",
        "title": "Świerklany: historia, która może odejść",
        "bullets": [
            "25–26 stycznia 2025 r., pierwszy Marsz Pamięci trasą Pszczyna – Żory – Wodzisław (inicjatywa Tomasza Przybylskiego). Podczas przejścia przez Świerklany wyszła przed dom starsza pani.",
            "Ze łzami w oczach: „Miałam siedem lat wtedy i wszystko widziałam — tych więźniów to było straszne, wszystko widziałam…”.",
            "W Świerklanach przy cmentarzu parafialnym leży 13 więźniów zamordowanych 18 stycznia 1945 r.; mieszkańcy pochowali ich i w 1948 r. ufundowali pomnik."
            ,
            "Muzeum może mieć dokumenty. Ta pani miała historię.",
        ],
        "quote": "Muzeum partycypacyjne nie jest modą. Jest obowiązkiem.",
        "notes": (
            "Moment emocjonalny — nie przyspieszać. Cytat starszej pani przytoczyć z pamięci, "
            "nie czytać z kartki.\n"
            "Data i trasa potwierdzone: 25–26 stycznia 2025 r. (Pszczyna – Żory – Wodzisław), "
            "inicjatywa Tomasza Przybylskiego."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "5. MIEJSCE, KTÓRE JEST NASZE",
        "title": "Mszana — nasza mogiła, nasza pamięć",
        "bullets": [
            "Na cmentarzu parafialnym przy kościele św. Jerzego: Grób Ofiar Marszu Śmierci — 33 ofiary, ciała złożyli mieszkańcy Mszany.",
            "1965 r.: społeczeństwo z własnych funduszy ufundowało pomnik nad bezimienną mogiłą.",
            "2011 r.: archiwiści Yad Vashem i Muzeum Auschwitz-Birkenau ustalili po numerach obozowych nazwiska czworga ofiar; odsłonięto nowe tablice, przyjechała 30-osobowa delegacja z Izraela.",
            "W przedsionku kościoła tablica wdzięczności dla mieszkańców Mszany, którzy w styczniu 1945 r. ratowali innych. Od 2011 r. grób jest stałym punktem wycieczek z Izraela.",
        ],
        "quote": "Pamięć nie jest abstrakcją. Pamięć ma adres: cmentarz przy św. Jerzym w Mszanie.",
        "notes": (
            "Najmocniejszy akcent lokalny całego wystąpienia — mówimy spokojnie, z pauzami. "
            "Po ostatnim zdaniu (na slajdzie) zostawić ciszę."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "5. PRAKTYKA",
        "title": "Z odbiorców — we współgospodarzy",
        "bullets": [
            "Sztuka partycypacyjna i site-specific to dziś stała praktyka wystawiennicza.",
            "Wystawy powstają wspólnie z mieszkańcami — przez konsultacje i wspólne wybieranie tematów.",
            "Przykład: doroczna wystawa budowana z przedmiotów i historii przynoszonych przez mieszkańców.",
            "Muzeum nie musi zgadywać, co interesuje mieszkańców — może ich po prostu zapytać.",
        ],
        "notes": "Tu warto podać przykład z własnego podwórka (wystawa z przedmiotów przyniesionych).",
    },
    {
        "layout": "content",
        "eyebrow": "6. DOSTĘP",
        "title": "Kultura jako prawo, nie przywilej",
        "bullets": [
            "Francja, Włochy, Hiszpania: bon kulturowy w aplikacji dla każdego młodego człowieka.",
            "Wielka Brytania: muzea narodowe bezpłatne od 2001 roku.",
            "Propozycja dla województwa: 100 zł raz w roku dla każdego ucznia — do wydania wyłącznie w muzeach regionu.",
            "Plus comiesięczny dzień z wolnym wstępem dla wszystkich.",
        ],
        "quote": "Nie namawiamy. Nie przekonujemy. Otwieramy drzwi — i patrzymy, kto wejdzie.",
        "notes": (
            "DO POTWIERZENIA: czy województwo nie prowadzi już bonu kultury / dnia z wolnym "
            "wstępem. Jeśli tak — podać nazwę programu i budżet."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "7. MUZEUM BEZ ŚCIAN (1)",
        "title": "Eko-muzeum, czyli muzeum rozproszone",
        "bullets": [
            "Zamiast jednego budynku — całe miasto i jego okolice jako sieć punktów.",
            "Wystawa o grodzie słowiańskim w Lubomi.",
            "Dawny kopiec zamkowy w parku.",
            "Wodzisławski browar.",
            "Kościół Świętego Krzyża.",
        ],
        "quote": "Sztuka może wyjść z sal na ulicę.",
        "notes": (
            "Gdy skracamy do 10 minut: wymień tylko dwa z czterech punktów sieci — "
            "oszczędność ok. 15 s."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "8. MUZEUM BEZ ŚCIAN (2)",
        "title": "Droga Loslau: trasa, którą się przechodzi",
        "bullets": [
            "Niewidzialna ścieżka przez Wodzisław: od granic miasta, przez konkretne ulice, aż do dworca.",
            "Dziś trzy punkty: tablica przy ul. Michalskiego 4a, tablica na dworcu kolejowym (ul. Rybnicka 2A), pomnik ofiar i krzyż przy ul. Ofiar Oświęcimskich.",
            "Do zbudowania: jedna trasa — audioprzewodnik w głosach mieszkańców, kody QR otwierające archiwalne zdjęcia w miejscu zdarzenia, stacje na 10 minut.",
            "Przebieg trasy odtworzył wodzisławski historyk Piotr Hojka; od 2012 roku idzie nią co stycznia Marsz Pamięci.",
        ],
        "quote": "Brakuje jednego — żeby ta droga istniała także wtedy, gdy nikt nią nie idzie.",
        "notes": (
            "Adresy potwierdzone: ul. Michalskiego 4a (tablica), dworzec kolejowy ul. Rybnicka 2A, "
            "pomnik i krzyż przy ul. Ofiar Oświęcimskich.\n"
            "Mieć pod ręką link do podcastu na Spotify na wypadek pytania z sali.\n"
            "Egzemplarz książki „Kierunek Loslau” do wglądu przy ustalaniu przebiegu ulic."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "9. WZORZEC",
        "title": "Bawaria: droga, która istnieje zawsze",
        "bullets": [
            "Wzdłuż trasy marszu z Dachau stanęły 22 identyczne pomniki autorstwa Huberta von Pilgrima (jedna kopia w Yad Vashem w Jerozolimie).",
            "Dzięki nim droga istnieje, nawet gdy zmieniają się ulice, właściciele i pokolenia.",
            "U nas: ten sam znak w Oświęcimiu, Pszczynie, Żorach, Świerklanach, Marklowicach i na wodzisławskim dworcu.",
            "Wniosek: wpisanie trasy do Szlaku Wyzwolenia Europy — szlaku kulturowego Rady Europy.",
        ],
        "notes": (
            "Gdy skracamy do 10 minut: pomiń akapit o Bawarii, zostaw nazwę i wniosek do "
            "Rady Europy — oszczędność ok. 25 s."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "10. FORMAT MAKSYMALNIE PARTYCYPACYJNY",
        "title": "Kamienie pamięci",
        "bullets": [
            "1992 r., Kolonia: Gunter Demnig wmurowuje pierwszą kostkę z mosiężną tabliczką — imię, data, miejsce śmierci.",
            "Dziś: ponad 120 000 kamieni w ponad 30 krajach Europy. W Polsce m.in. we Wrocławiu, Warszawie i Poznaniu.",
            "W Wodzisławiu — jeszcze żadnego.",
            "Kamień fundują mieszkańcy, często klasy szkolne. Jeden człowiek, jeden kamień.",
        ],
        "quote": "Pamięć nie stoi w gablocie. Leży na chodniku, po którym codziennie przechodzimy.",
        "notes": (
            "DO POTWIERDZENIA: czy w Wodzisławiu na pewno nie ma jeszcze kamieni pamięci — "
            "zapytać lokalnych historyków lub w urzędzie miasta.\n"
            "Mieć kontakt do fundacji Guntera Demniga (koszt kamienia ok. 120 euro) na wypadek "
            "pytania „kto to robi?”.\n"
            "Pytanie o kontrowersje wokół kamieni: pamięć, o którą się dyskutuje, żyje."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "11. DRUGA STRONA PAMIĘCI",
        "title": "Ogród Sprawiedliwych",
        "bullets": [
            "Pierwszy ogród: Mediolan, 2003 r. Warszawski rośnie od 2014 r. — drzewo dla każdego, kto ratował innych.",
            "U nas: choćby skwer przy pałacu — drzewa dla tych, którzy w styczniu 1945 roku otwierali drzwi.",
        ],
        "quote": "Kamienie — dla tych, którzy szli. Drzewa — dla tych, którzy nie odwrócili wzroku.",
        "notes": (
            "Gdy skracamy do 10 minut: jedno zdanie o kamieniach, jedno o drzewach — "
            "oszczędność ok. 50 s."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "12. INSTYTUCJA",
        "title": "Archiwum Pamięci Wodzisławia",
        "bullets": [
            "Każdy mieszkaniec przynosi coś, co ma znaczenie: nagrane wspomnienie, zeskanowaną fotografię, przedmiot z historią.",
            "Wychodzi z poczuciem, że jego życie stało się częścią historii miasta.",
            "Pierwsze zadanie: zebrać notatki, listy, pocztówki i głosy, które jeszcze są.",
        ],
        "quote": "Najcenniejsze eksponaty często nie leżą w magazynach. Leżą w szufladach.",
        "notes": "„Bo za dziesięć lat już ich nie będzie” — to zdanie zostawić w ciszy.",
    },
    {
        "layout": "content",
        "eyebrow": "13. SZTUKA",
        "title": "Sztuka w przestrzeni miasta",
        "bullets": [
            "Mural złożony z archiwalnych zdjęć; ścieżka pamięci łącząca pałac z rynkiem.",
            "Mural nie o Marszu Śmierci jako abstrakcyjnym fakcie — o jednym konkretnym geście:",
            "• ręka podająca kromkę chleba,",
            "• otwarte drzwi stodoły,",
            "• twarze Sprawiedliwych wśród Narodów Świata z tego regionu.",
        ],
        "quote": "Pamięć o złu musi być. Pamięć o dobru — też. I musi być widoczna.",
        "notes": "Slajd „wizualny” — dobrze, jeśli w wersji na rzutnik pojawi się tu zdjęcie lub szkic muralu.",
    },
    {
        "layout": "content",
        "eyebrow": "14. TECHNOLOGIE",
        "title": "Historia w kieszeni",
        "bullets": [
            "Aplikacja AR odtwarzająca wygląd pałacu z XVIII wieku i rynek sprzed stu dwudziestu lat.",
            "Cyfrowa rekonstrukcja wnętrz zniszczonych przed wojną.",
            "Audioprzewodnik z głosami mieszkańców — nie lektora.",
            "Kody QR otwierające wspomnienia; cyfrowe zbiory dostępne dla każdego.",
        ],
        "quote": "Ulica, którą dotąd mijaliśmy obojętnie, zaczyna mówić.",
        "notes": (
            "Przykład do opowiedzenia: 30 sekund głosu mieszkanki, której babcia widziała "
            "przechodzącą kolumnę.\n"
            "Gdy skracamy do 10 minut: lista do trzech najważniejszych pozycji — "
            "oszczędność ok. 30 s."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "15. LUDZIE",
        "title": "Tandemy pokoleń",
        "bullets": [
            "Wolontariusze dziedzictwa; seniorzy jako przewodnicy po własnych wspomnieniach.",
            "Młodzi, którzy potrafią je zapisać i udostępnić.",
            "Żywa biblioteka, w której książką jest człowiek — w tym świadkowie Marszu Śmierci.",
            "Tandemy przy warsztatach rzemiosła; nagrania wideo robione telefonami przez licealistów.",
        ],
        "quote": "Mamy pięć lat. Może dziesięć.",
        "notes": (
            "Kluczowe zdanie do wypowiedzenia w ciszy: „Jeśli nie posadzimy obok siebie "
            "dziewięćdziesięciolatka i siedemnastolatki — jednego, który pamięta, i drugiej, "
            "która potrafi nagrać i udostępnić — to pewne historie znikną na zawsze.”"
        ),
    },
    {
        "layout": "big",
        "eyebrow": "16. POWRÓT DO PUNKTU WYJŚCIA",
        "title": "Ten pałac powstał z miłości.",
        "subtitle": (
            "A w styczniu 1945 roku, tuż obok, przechodziła kolumna,\n"
            "w której każdy kolejny krok był przeciwieństwem miłości.\n"
            "Nie żeby jedno zasłaniało drugie — żeby jedno drugie oświetlało."
        ),
        "notes": (
            "Zatrzymać się nad tym zdaniem. Pauza. Potem wiersz zamykający (slajd następny)."
        ),
    },
    {
        "layout": "poem",
        "eyebrow": "",
        "title": "",
        "poem": [
            "Nie każda historia mieści się w gablocie.",
            "Czasem śpi w szufladzie — w liście, fotografii,",
            "czasem budzi się w głosie starszej pani,",
            "w jednym zdaniu, które drży od wspomnień.",
            "",
            "Miasto może stać się salą muzealną,",
            "ulica — ścieżką, dworzec — opowieścią.",
            "Mieszkańcy przyniosą swoje historie,",
            "a młodzi pomogą im nie zamilknąć.",
            "",
            "Wtedy muzeum nie oddziela od życia.",
            "Idzie obok, słucha, podaje głos.",
        ],
        "notes": "Czytamy wolno, z pauzami między strofami.",
    },
    {
        "layout": "content",
        "eyebrow": "17. NAUCZYCIELE",
        "title": "Nauczyciel doceniony nie odpuszcza",
        "bullets": [
            "Nagroda im. Ireny Sendlerowej „Za naprawianie świata” (od 2006 r.) — dla nauczycieli uczących tolerancji i szacunku; nagroda pieniężna dla laureata.",
            "EUSTORY — sieć konkursów historycznych (Körber-Stiftung, ponad 20 krajów, ponad 300 tys. uczestników).",
            "Polskie ogniwa: „Historia Bliska” (KARTA, od 1996 r.) i „Moje życie w PRL” (Fundacja Geremka) — wywiad wideo 7–8 min z bliską osobą, wsparcie mentora, nagrody także dla nauczycieli-opiekunów.",
            "W kalendarzu szkoły: Nauczyciel Roku oraz Nauczyciel Jutr@ (z Fundacją Orange).",
        ],
        "notes": (
            "Gdy skracamy do 10 minut: zostaw dwa zdania — oszczędność ok. 40 s.\n"
            "DO SPRAWDZENIA: aktualne terminy naboru (Sendlerowa/CEO, EUSTORY, Geremek) — "
            "zmieniają się co rok.\n"
            "Przygotować krótkie uzasadnienie: kto z nauczycieli w powiecie zasługuje na nominację."
        ),
    },
    {
        "layout": "content",
        "eyebrow": "18. PLAN",
        "title": "Pięć kroków",
        "bullets": [
            "1. Zapisać wspomnienia. Dopóki jeszcze są.",
            "2. Współdecydować z mieszkańcami. Nie konsultować — współdecydować.",
            "3. Udostępnić zbiory cyfrowo. Dziedzictwo zamknięte w magazynie nie istnieje.",
            "4. Wyjść ze sztuką w miasto. Na ulicę Ofiar Oświęcimskich. Na dworzec. Na trasę marszu.",
            "5. Włączyć wszystkie pokolenia.",
        ],
        "quote": "Umowa szkoła–muzeum i kalendarz w rytmie rocznic: nagrania jesienią, marsz w styczniu, wystawa w maju.",
        "notes": (
            "Kluczowa pointa: „Taki plan jest już napisany — leży w dokumentach tego projektu. "
            "Brakuje podpisów.”\n"
            "Gdy skracamy do 10 minut: pomiń akapit o planie współpracy — oszczędność ok. 30 s.\n"
            "DO USTALENIA: kto podpisuje umowę szkoła–muzeum i kiedy (pierwszy krok planu)."
        ),
    },
    {
        "layout": "big",
        "eyebrow": "ZAKOŃCZENIE",
        "title": "Niech ten pałac nadal będzie\nmiejscem relacji.",
        "subtitle": "Dziękuję.",
        "notes": "Ostatnie zdanie powiedzieć wolniej i zostać chwilę w ciszy.",
    },
    {
        "layout": "sources",
        "eyebrow": "",
        "title": "Źródła i materiały",
        "bullets": [
            "T. Behrens i in., nowa muzeologia i muzeum partycypacyjne — literatura przedmiotu.",
            "P. Hojka, „Kierunek Loslau” (Muzeum w Wodzisławiu Śląskim) — przebieg trasy Marszu Śmierci.",
            "Gunter Demnig / Stolpersteine: stolpersteine.eu — liczba kamieni, koszt, procedura.",
            "Hubertus von Pilgrim — 22 identyczne pomniki wzdłuż trasy marszu z Dachau (jedna kopia w Yad Vashem).",
            "Ogród Sprawiedliwych: Mediolan (2003), Warszawa (2014) — m.in. ogrodsprawiedliwych.pl.",
            "Nagroda im. Ireny Sendlerowej „Za naprawianie świata” — Centrum Edukacji Obywatelskiej.",
            "EUSTORY (Körber-Stiftung); „Historia Bliska” (KARTA); „Moje życie w PRL” (Fundacja Geremka).",
            "Wzorce dostępu: bon kulturowy (Francja, Włochy, Hiszpania); wolny wstęp do muzeów narodowych w Wielkiej Brytanii od 2001 r.",
        ],
        "notes": (
            "Slajd na wypadek pytań z sali — można go zostawić na końcu prezentacji jako "
            "zaplecze źródłowe."
        ),
    },
]


# ================================================================ PPTX
def zbuduj_pptx(sciezka):
    prs = Presentation()
    prs.slide_width = Inches(W_IN)
    prs.slide_height = Inches(H_IN)
    puste = prs.slide_layouts[6]

    def pole(slide, l, t, w, h):
        tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
        tf = tb.text_frame
        tf.word_wrap = True
        return tf

    def akapit(tf, tekst, rozmiar=18, pogrubienie=False, kolor=INK, pierwszy=False,
               odstep=8, wyrownanie=PP_ALIGN.LEFT, kursywa=False):
        p = tf.paragraphs[0] if pierwszy else tf.add_paragraph()
        p.text = tekst
        p.alignment = wyrownanie
        p.space_after = Pt(odstep)
        for r in p.runs:
            r.font.size = Pt(rozmiar)
            r.font.bold = pogrubienie
            r.font.italic = kursywa
            r.font.color.rgb = kolor
            r.font.name = FONT
        return p

    def pasek(slide, tekst, kolor_tla=GREEN, kolor_tekstu=WHITE, rozmiar=13, wys=0.55, gora=0.55):
        if not tekst:
            return
        # szerokość plakietki zależna od długości tekstu (max 6,2 cala)
        szer = min(6.2, max(2.0, 0.096 * len(tekst) + 0.55))
        ksztalt = slide.shapes.add_shape(1, Inches(0.7), Inches(gora), Inches(szer), Inches(wys))
        ksztalt.fill.solid()
        ksztalt.fill.fore_color.rgb = kolor_tla
        ksztalt.line.fill.background()
        tf = ksztalt.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.text = tekst
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = Pt(rozmiar)
            r.font.bold = True
            r.font.color.rgb = kolor_tekstu
            r.font.name = FONT

    for s in SLAJDY:
        slide = prs.slides.add_slide(puste)
        layout = s.get("layout", "content")

        if layout == "title":
            tf = pole(slide, 0.9, 2.2, 11.5, 3.2)
            akapit(tf, s["eyebrow"], 14, True, AMBER, pierwszy=True, odstep=14)
            akapit(tf, s["title"], 54, True, GREEN, odstep=10)
            akapit(tf, s["subtitle"], 20, False, GREY, odstep=18)
            akapit(tf, s.get("footer", ""), 13, False, GREY)

        elif layout == "big":
            pasek(slide, s["eyebrow"])
            tf = pole(slide, 1.0, 2.5, 11.3, 3.0)
            akapit(tf, s["title"], 40, True, GREEN, pierwszy=True, odstep=18)
            if s.get("subtitle"):
                akapit(tf, s["subtitle"], 20, False, GREY)

        elif layout == "poem":
            if s.get("eyebrow"):
                pasek(slide, s["eyebrow"], GREEN_L, GREEN, 13)
            if s.get("title"):
                tf = pole(slide, 1.0, 1.35, 11.3, 0.8)
                akapit(tf, s["title"], 24, True, GREEN, pierwszy=True)
            tf = pole(slide, 1.6, 2.3, 10.1, 4.2)
            pierwszy = True
            for linia in s["poem"]:
                akapit(tf, linia, 22, False, INK, pierwszy=pierwszy, odstep=6)
                pierwszy = False

        elif layout == "sources":
            tf = pole(slide, 0.9, 0.55, 11.5, 0.8)
            akapit(tf, s["title"], 28, True, GREEN, pierwszy=True)
            tf = pole(slide, 0.9, 1.6, 11.5, 5.2)
            pierwszy = True
            for b in s["bullets"]:
                akapit(tf, "•  " + b, 13, False, GREY, pierwszy=pierwszy, odstep=6)
                pierwszy = False

        else:  # content
            pasek(slide, s.get("eyebrow", ""))
            tf = pole(slide, 0.9, 1.35, 11.5, 0.9)
            akapit(tf, s["title"], 30, True, GREEN, pierwszy=True)
            tf = pole(slide, 0.9, 2.45, 11.5, 3.3)
            pierwszy = True
            for b in s.get("bullets", []):
                wciecie = b.startswith("•")
                akapit(tf, ("      " + b) if wciecie else ("•  " + b),
                       16 if not wciecie else 15,
                       False, INK if not wciecie else GREY,
                       pierwszy=pierwszy, odstep=9)
                pierwszy = False
            if s.get("quote"):
                tf2 = pole(slide, 0.9, 5.9, 11.5, 1.1)
                akapit(tf2, s["quote"], 19, True, AMBER, pierwszy=True)

        if s.get("notes"):
            slide.notes_slide.notes_text_frame.text = s["notes"]

    prs.save(sciezka)
    return len(SLAJDY)


# ================================================================ PDF (16:9)
def zbuduj_pdf(sciezka):
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph

    pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

    from reportlab.pdfgen import canvas as pdfcanvas

    SW, SH = W_IN * inch, H_IN * inch
    ziel = HexColor("#0F5132")
    ziel_l = HexColor("#E7F1EB")
    amber = HexColor("#C9821A")
    atrament = HexColor("#222222")
    szary = HexColor("#5A5A5A")

    st_title = ParagraphStyle("t", fontName="PL-Bold", fontSize=40, leading=46, textColor=ziel)
    st_big = ParagraphStyle("b", fontName="PL-Bold", fontSize=32, leading=39, textColor=ziel)
    st_sub = ParagraphStyle("s", fontName="PL", fontSize=20, leading=27, textColor=szary)
    st_eye = ParagraphStyle("e", fontName="PL-Bold", fontSize=13, leading=17, textColor=amber)
    st_h = ParagraphStyle("h", fontName="PL-Bold", fontSize=27, leading=33, textColor=ziel)
    st_b = ParagraphStyle("bb", fontName="PL", fontSize=16, leading=21.5, textColor=atrament)
    st_sub_b = ParagraphStyle("sb", fontName="PL", fontSize=15, leading=20.5, textColor=szary)
    st_quote = ParagraphStyle("q", fontName="PL-Bold", fontSize=17, leading=22, textColor=amber)
    st_poem = ParagraphStyle("p", fontName="PL", fontSize=21, leading=29, textColor=atrament)
    st_src = ParagraphStyle("src", fontName="PL", fontSize=12, leading=16.5, textColor=szary)
    st_stopka = ParagraphStyle("st", fontName="PL", fontSize=10, leading=13, textColor=szary)

    c = pdfcanvas.Canvas(sciezka, pagesize=(SW, SH))
    c.setTitle("Muzeum bez scian - prezentacja na seminarium")

    def tekst(par, x, y, szerokosc):
        """Rysuje akapit od góry; zwraca nowe y (pod akapitem)."""
        w, h = par.wrap(szerokosc, SH)
        par.drawOn(c, x, y - h)
        return y - h

    for i, s in enumerate(SLAJDY, 1):
        layout = s.get("layout", "content")
        c.setFillColor(white)
        c.rect(0, 0, SW, SH, stroke=0, fill=1)

        # pasek nagłówka
        if s.get("eyebrow") and layout != "title":
            etykieta = s["eyebrow"]
            szer_txt = pdfmetrics.stringWidth(etykieta, "PL-Bold", 11)
            szer = min(6.2 * inch, szer_txt + 22)
            c.setFillColor(ziel_l if layout == "poem" else ziel)
            c.rect(0.7 * inch, SH - 1.15 * inch, szer, 0.42 * inch, stroke=0, fill=1)
            c.setFillColor(ziel if layout == "poem" else white)
            c.setFont("PL-Bold", 11)
            c.drawCentredString(0.7 * inch + szer / 2.0, SH - 1.03 * inch, etykieta)

        if layout == "title":
            y = SH - 2.4 * inch
            y = tekst(Paragraph(s["eyebrow"], st_eye), 0.9 * inch, y, SW - 1.8 * inch) - 16
            y = tekst(Paragraph(s["title"], st_title), 0.9 * inch, y, SW - 1.8 * inch) - 14
            y = tekst(Paragraph(s["subtitle"].replace("\n", "<br/>"), st_sub),
                      0.9 * inch, y, SW - 1.8 * inch) - 22
            tekst(Paragraph(s.get("footer", ""), st_stopka), 0.9 * inch, y, SW - 1.8 * inch)

        elif layout == "big":
            y = SH - 2.7 * inch
            y = tekst(Paragraph(s["title"].replace("\n", "<br/>"), st_big),
                      1.0 * inch, y, SW - 2.0 * inch) - 20
            if s.get("subtitle"):
                tekst(Paragraph(s["subtitle"].replace("\n", "<br/>"), st_sub),
                      1.0 * inch, y, SW - 2.0 * inch)

        elif layout == "poem":
            y = SH - 1.85 * inch
            if s.get("title"):
                y = tekst(Paragraph(s["title"], st_h), 1.0 * inch, y, SW - 2.0 * inch) - 18
            for linia in s["poem"]:
                y = tekst(Paragraph(linia if linia else "&nbsp;", st_poem),
                          1.6 * inch, y, SW - 3.2 * inch) - 2

        elif layout == "sources":
            y = SH - 1.35 * inch
            y = tekst(Paragraph(s["title"], st_h), 0.9 * inch, y, SW - 1.8 * inch) - 18
            for b in s["bullets"]:
                y = tekst(Paragraph("•  " + b, st_src), 0.9 * inch, y, SW - 1.8 * inch) - 7

        else:
            y = SH - 1.5 * inch
            y = tekst(Paragraph(s["title"], st_h), 0.9 * inch, y, SW - 1.8 * inch) - 20
            for b in s.get("bullets", []):
                wciecie = b.startswith("•")
                y = tekst(Paragraph(("&nbsp;&nbsp;&nbsp;&nbsp;" + b) if wciecie else ("•  " + b),
                                    st_sub_b if wciecie else st_b),
                          0.9 * inch, y, SW - 1.8 * inch) - 10
            if s.get("quote"):
                # cytat zakotwiczony u dołu slajdu
                tekst(Paragraph(s["quote"], st_quote), 0.9 * inch, 1.75 * inch,
                      SW - 1.8 * inch)

        c.setFillColor(szary)
        c.setFont("PL", 9)
        c.drawRightString(SW - 0.7 * inch, 0.45 * inch, "%d / %d" % (i, len(SLAJDY)))
        c.showPage()

    c.save()
    return len(SLAJDY)


if __name__ == "__main__":
    pptx_path = os.path.join(KATALOG, "prezentacja-muzeum-bez-scian.pptx")
    pdf_path = os.path.join(KATALOG, "prezentacja-muzeum-bez-scian.pdf")
    n1 = zbuduj_pptx(pptx_path)
    n2 = zbuduj_pdf(pdf_path)
    print("PPTX: %s (slajdów: %d)" % (pptx_path, n1))
    print("PDF:  %s (slajdów: %d)" % (pdf_path, n2))
