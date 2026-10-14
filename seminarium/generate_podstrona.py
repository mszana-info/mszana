# -*- coding: utf-8 -*-
"""
Generuje podstronę muzeum-bez-scian.html na podstawie szablonu pamiec.html
(te same nagłówek, nawigacja, stopka, modale i skrypty — pełna spójność z serwisem).

Uruchomienie:  python generate_podstrona.py
"""

import os
import re

KATALOG = os.path.dirname(os.path.abspath(__file__))
KORZEN = os.path.dirname(KATALOG)          # katalog główny serwisu (z pamiec.html)
SZABLON = os.path.join(KORZEN, "pamiec.html")
WYJSCIE = os.path.join(KORZEN, "muzeum-bez-scian.html")

TYTUL = "Muzeum bez ścian — jak dziedzictwo staje się relacją | Mszana.info"
OPIS = ("Muzeum bez ścian: jak dziedzictwo przestaje być zbiorem, a staje się relacją. "
        "Muzeum partycypacyjne, Droga Loslau w Wodzisławiu Śląskim, kamienie pamięci, "
        "Ogród Sprawiedliwych i Archiwum Pamięci — artykuł o pamięci lokalnej.")

# ================================================================ TREŚĆ ARTYKUŁU
TRESC = """
<section id="artykul">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Pamięć i Historia · Artykuł</p>
      <h1>Muzeum bez ścian</h1>
      <p>Jak dziedzictwo przestaje być zbiorem, a staje się relacją.</p>
    </div>

    <article class="art">
      <p class="art-meta">
        Materiał seminaryjny · <span class="pytanie">Dziedzictwo i pamięć lokalna</span> ·
        na podstawie wystąpienia „Muzeum bez ścian. Dziedzictwo mieszka w ludziach”.
      </p>

      <p class="art-lead">
        W styczniu 1945 roku przez Wodzisław Śląski przeszła kolumna więźniów ewakuowanych
        z Auschwitz. Dziś upamiętniają ją w mieście trzy osobne punkty: tablica przy ulicy
        Michalskiego, miejsce pamięci na dworcu oraz pomnik i krzyż przy ulicy
        <em>[nazwa do uzupełnienia]</em>. Można z nich zrobić coś więcej niż zbiór miejsc
        pamięci — jedną trasę, którą się przechodzi, słuchając głosów mieszkańców.
      </p>

      <div class="spis" aria-label="Spis treści">
        <h2>W tym artykule</h2>
        <ol>
          <li><a href="#historia">Historia, którą widziała siedmioletnia dziewczynka</a></li>
          <li><a href="#gablota">Od gabloty do dialogu</a></li>
          <li><a href="#praktyka">Muzeum partycypacyjne w praktyce</a></li>
          <li><a href="#dostep">Dostęp jest prawem, nie przywilejem</a></li>
          <li><a href="#ekomuzeum">Eko-muzeum: muzeum rozproszone</a></li>
          <li><a href="#droga">Droga Loslau: trasa, którą się przechodzi</a></li>
          <li><a href="#kamienie">Kamienie pamięci i Ogród Sprawiedliwych</a></li>
          <li><a href="#archiwum">Archiwum Pamięci</a></li>
          <li><a href="#sztuka">Sztuka i technologie w przestrzeni miasta</a></li>
          <li><a href="#ludzie">Ludzie: tandemy pokoleń</a></li>
          <li><a href="#nauczyciel">Nauczyciel doceniony nie odpuszcza</a></li>
          <li><a href="#piec">Pięć kroków i brakujące podpisy</a></li>
          <li><a href="#palac">Ten pałac powstał z miłości</a></li>
          <li><a href="#zrodla">Źródła i materiały</a></li>
        </ol>
      </div>

      <h2 id="historia">1. Historia, którą widziała siedmioletnia dziewczynka</h2>
      <p>
        W lutym 2025 roku, podczas pierwszego Marszu Pamięci prowadzącego trasą przez Żory,
        przed jednym z domów w Świerklanach stanęła starsza kobieta. Powiedziała przez łzy:
        „Miałam siedem lat wtedy i wszystko widziałam — tych więźniów to było straszne,
        wszystko widziałam…”.
      </p>
      <p>
        Muzeum może mieć dokumenty. Ta pani miała historię. I właśnie dlatego cała ta opowieść
        jest w gruncie rzeczy o jednym zdaniu: <strong>dziedzictwo nie mieszka w gablotach.
        Dziedzictwo mieszka w ludziach.</strong> Zadaniem instytucji kultury — muzeum,
        biblioteki, szkoły, domu kultury — jest zrobić wszystko, żeby zdążyć je od nich usłyszeć.
      </p>
      <p>
        Za pięć, dziesięć lat te historie odejdą razem z ostatnimi świadkami.
        Nie mamy pięćdziesięciu lat. Mamy pięć. Może dziesięć.
      </p>

      <h2 id="gablota">2. Od gabloty do dialogu</h2>
      <p>
        Jeszcze pół wieku temu muzeum kojarzyło się z ciszą, dystansem i kontemplacją —
        przestrzenią, w której eksponat chroniony gablotą i czerwonym sznurem oddzielał widza
        od dzieła. Współcześnie ten model przechodzi głęboką przemianę.
      </p>
      <p>
        Sztuka przestaje być wyłącznie przedmiotem oglądu — staje się narzędziem dialogu
        społecznego. Dziedzictwo przestaje być statycznym zasobem, chronionym przed zmianą —
        staje się żywym procesem, który współtworzą mieszkańcy.
      </p>
      <blockquote>
        <p>Historia nie dzieje się w muzeach. Muzea tylko próbują ją dogonić.</p>
      </blockquote>
      <p>
        Punktem zwrotnym w myśleniu o instytucjach muzealnych był ruch nazywany
        <strong>nową muzeologią</strong>. Jego konsekwencją jest koncepcja
        <strong>muzeum partycypacyjnego</strong>: miejsca, w którym publiczność może tworzyć,
        dzielić się i łączyć wokół zbiorów.
      </p>
      <p>
        Nie chodzi już o to, by dodać kolejny eksponat czy kolejną salę. Chodzi o to,
        by muzeum przestało być miejscem, do którego się przychodzi, a stało się miejscem,
        które się współtworzy.
      </p>

      <h2 id="praktyka">3. Muzeum partycypacyjne w praktyce</h2>
      <p>
        Sztuka partycypacyjna i sztuka <em>site-specific</em> to dziś stała praktyka. Wystawy
        powstają wspólnie z mieszkańcami — przez konsultacje i wspólne wybieranie tematów.
        Dobrym przykładem jest doroczna wystawa budowana z przedmiotów i historii, które
        przynoszą sami mieszkańcy. Muzeum nie musi zgadywać, co interesuje ludzi z jego okolicy.
        Może ich po prostu zapytać.
      </p>
      <p>
        Efekt jest taki, że zmienia się rola publiczności: <strong>z odbiorców stają się
        współgospodarzami.</strong>
      </p>
      <p>
        Warto zobaczyć, jak to wygląda tam, gdzie działa to od lat. W wiedeńskim muzeum
        miejskim od 2023 roku działa tzw. Community Gallery — przestrzeń, w której o tym,
        co pokazać, decydują sami mieszkańcy; pierwsza wystawa powstała z grupą kobiet, które
        najpierw opowiadały swoje historie, a potem współtworzyły ekspozycję. Wcześniej muzeum
        zbierało przedmioty codzienne osób, które przyjechały do miasta w latach 60. i 70. —
        pytając ich samych, co i jak opowiedzieć.
      </p>
      <p>To nie są pojedyncze gesty. To metoda.</p>

      <h2 id="dostep">4. Dostęp jest prawem, nie przywilejem</h2>
      <p>
        Jest jeszcze poziom wojewódzki — bo do niezainteresowanych nie dotrzemy sami,
        jednym budynkiem. We Francji każdy młody człowiek dostaje w aplikacji bon na kulturę,
        podobnie we Włoszech i Hiszpanii. W Wielkiej Brytanii muzea narodowe są bezpłatne
        od 2001 roku — a efekty tego rozwiązania (znacznie szersza publiczność, nawyk
        odwiedzania muzeów kilka razy w roku) są dziś przywoływane w całej Europie.
        Wiedeńskie muzeum miejskie poszło tą drogą w grudniu 2023 r., otwierając bezpłatnie
        swoją wystawę stałą — z biletami wyłącznie na wystawy czasowe.
      </p>
      <p>
        Wyobraźmy to sobie u nas: każdy uczeń w województwie śląskim dostaje raz w roku
        sto złotych do wydania <strong>wyłącznie</strong> w muzeach regionu — plus comiesięczny
        dzień z wolnym wstępem dla wszystkich.
      </p>
      <blockquote>
        <p>Nie namawiamy. Nie przekonujemy. Otwieramy drzwi — i patrzymy, kto wejdzie.</p>
      </blockquote>

      <h2 id="ekomuzeum">5. Eko-muzeum: muzeum rozproszone</h2>
      <p>
        Kolejny model to <strong>eko-muzeum</strong>, czyli muzeum rozproszone. Ma potencjał
        terytorialny: zamiast jednego budynku obejmuje całe miasto i jego okolice. Punktami
        takiej sieci mogą być u nas miejsca, które już istnieją:
      </p>
      <ul>
        <li>wystawa o grodzie słowiańskim w Lubomi,</li>
        <li>dawny kopiec zamkowy w parku,</li>
        <li>wodzisławski browar,</li>
        <li>kościół Świętego Krzyża.</li>
      </ul>
      <p>
        To gotowe punkty, z których można zbudować prawdziwą sieć eko-muzealną.
        <strong>Sztuka może wyjść z sal na ulicę.</strong>
      </p>

      <h2 id="droga">6. Droga Loslau: trasa, którą się przechodzi</h2>
      <p>
        Przez Wodzisław Śląski przechodzi niewidzialna ścieżka. Prowadzi od granic miasta,
        przez konkretne ulice, aż do dworca. Jej przebieg odtworzył wodzisławski historyk
        Piotr Hojka, a od 2012 roku idzie nią co stycznia Marsz Pamięci. Dziś upamiętniają ją
        trzy osobne punkty: tablica przy ulicy Michalskiego, miejsce pamięci na dworcu,
        pomnik i krzyż.
      </p>
      <p>Te trzy punkty można połączyć. W jedną trasę. W jedno żywe eko-muzeum pod otwartym niebem:</p>
      <ul>
        <li>z audioprzewodnikiem w głosach mieszkańców,</li>
        <li>
          z kodami QR, które otwierają archiwalne zdjęcia dokładnie w tych miejscach,
          w których coś się wydarzyło,
        </li>
        <li>
          ze stacjami, przy których można zatrzymać się na dziesięć minut — i usłyszeć jedną
          historię. Nie z opracowania. Z pamięci.
        </li>
      </ul>
      <p>
        Ta droga ma już nawet nazwę: <strong>kierunek Loslau</strong>. Brakuje jednego —
        żeby istniała także wtedy, gdy nikt nią nie idzie.
      </p>
      <p>
        W Bawarii, wzdłuż trasy marszu z Dachau, w każdej gminie stanął taki sam pomnik:
        <strong>22 identyczne rzeźby</strong> autorstwa Huberta von Pilgrima, przedstawiające
        pochylone postacie. Jedna kopia znajduje się w Yad Vashem w Jerozolimie. Dzięki nim
        droga istnieje, nawet gdy zmieniają się ulice, właściciele i pokolenia.
      </p>
      <p>
        Tak samo może istnieć nasza: ten sam znak i ten sam symbol w Oświęcimiu, Pszczynie,
        Żorach, Świerklanach, Marklowicach i tutaj, na wodzisławskim dworcu — oraz wniosek
        o wpisanie trasy do Szlaku Wyzwolenia Europy, szlaku kulturowego Rady Europy.
      </p>
      <blockquote>
        <p>To byłoby muzeum, przez które się przechodzi. Dosłownie.</p>
      </blockquote>

      <h2 id="kamienie">7. Kamienie pamięci i Ogród Sprawiedliwych</h2>
      <p>
        W 1992 roku niemiecki artysta Gunter Demnig wmurował w bruk Kolonii pierwszą betonową
        kostkę z mosiężną tabliczką — z imieniem, datą i miejscem śmierci. Dziś takich kamieni
        jest ponad sto dwadzieścia tysięcy, w ponad trzydziestu krajach Europy. W Polsce leżą
        między innymi we Wrocławiu, Warszawie i Poznaniu. <strong>W Wodzisławiu — jeszcze
        żadnego.</strong>
      </p>
      <p>
        To format maksymalnie partycypacyjny: kamień fundują mieszkańcy, często klasy szkolne —
        jeden człowiek, jeden kamień.
      </p>
      <blockquote>
        <p>Pamięć nie stoi w gablocie. Leży na chodniku, po którym codziennie przechodzimy.</p>
      </blockquote>
      <p>
        Obok nich potrzebna jest druga pamięć. Pierwszy <strong>Ogród Sprawiedliwych</strong>
        powstał w 2003 roku w Mediolanie; warszawski rośnie od 2014 roku — drzewo dla każdego,
        kto ratował innych. U nas mógłby to być choćby skwer przy pałacu — z drzewami dla tych,
        którzy w styczniu 1945 roku otwierali drzwi.
      </p>
      <blockquote>
        <p>Kamienie — dla tych, którzy szli. Drzewa — dla tych, którzy nie odwrócili wzroku.</p>
      </blockquote>

      <h2 id="archiwum">8. Archiwum Pamięci: najcenniejsze eksponaty leżą w szufladach</h2>
      <p>
        Każdy mieszkaniec może przynieść coś, co ma znaczenie: nagrane wspomnienie, zeskanowaną
        fotografię albo przedmiot z historią. Wychodzi z poczuciem, że jego życie stało się
        częścią historii miasta.
      </p>
      <blockquote>
        <p>Najcenniejsze eksponaty często nie leżą w magazynach. Leżą w szufladach.</p>
      </blockquote>
      <p>
        Jeśli Archiwum Pamięci ma powstać — a powinno — to jego pierwszym zadaniem powinno być
        zebranie wszystkich notatek, listów, pocztówek i głosów, które jeszcze są.
        Bo za dziesięć lat już ich nie będzie.
      </p>
      <p>
        Że to nie marzenie, pokazuje przykład z Austrii. <strong>Topothek</strong> to
        ogólnokrajowa platforma na prywatne zdjęcia, dokumenty i nagrania lokalne: dziś działa
        w około 450 gminach, zawiera ponad dwa miliony wpisów i tworzy je ponad trzy tysiące
        wolontariuszy. Prawa do materiałów zostają u mieszkańców, gmina używa tylko kopii,
        a wartość zbioru rośnie z każdym opisem dodanym przez ludzi, którzy pamiętają szczegóły.
      </p>

      <h2 id="sztuka">9. Sztuka i technologie w przestrzeni miasta</h2>
      <p>
        Street art i sztuka publiczna mogą być przedłużeniem muzeum w tkance miasta. Sztuka nie
        musi czekać w salach. Może mieszkać tam, gdzie toczy się życie. Wyobraźmy sobie:
      </p>
      <ul>
        <li>mural złożony z archiwalnych zdjęć,</li>
        <li>ścieżkę pamięci, która łączy pałac z rynkiem,</li>
        <li>
          mural nie o Marszu Śmierci jako abstrakcyjnym fakcie historycznym, ale o jednym,
          konkretnym geście: o ręce, która podaje kromkę chleba; o otwartych drzwiach stodoły;
          o twarzach Sprawiedliwych wśród Narodów Świata z tego regionu.
        </li>
      </ul>
      <blockquote>
        <p>
          Pamięć o złu musi być. Ale pamięć o dobru — o tym, że w tym mieście byli ludzie,
          którzy ryzykowali życie, żeby ratować obcych — ta pamięć też musi być.
          I musi być widoczna.
        </p>
      </blockquote>
      <p>
        Obok sztuki — narzędzia cyfrowe. Aplikacja rozszerzonej rzeczywistości, która odtwarza
        wygląd pałacu z XVIII wieku albo rynek sprzed stu dwudziestu lat. Cyfrowa rekonstrukcja
        wnętrz zniszczonych przed wojną. Audioprzewodnik, w którym zamiast suchych dat słuchamy
        głosów mieszkańców. Kody QR otwierające wspomnienia. Cyfrowe zbiory dostępne dla każdego.
      </p>
      <p>
        Historia nie musi kończyć się na progu budynku. Może towarzyszyć każdemu, kto nosi ją
        w kieszeni. Wystarczy trzydzieści sekund głosu mieszkanki, której babcia widziała
        przechodzącą kolumnę — i ulica, którą dotąd mijaliśmy obojętnie, zaczyna mówić.
      </p>

      <h2 id="ludzie">10. Ludzie: tandemy pokoleń</h2>
      <p>
        W tym wszystkim najważniejsi są ludzie: wolontariusze dziedzictwa, seniorzy, którzy
        zostają przewodnikami po własnych wspomnieniach, i młodzi, którzy potrafią je zapisać
        i udostępnić.
      </p>
      <p>
        Bo ostatni świadkowie odchodzą. Jeśli nie posadzimy obok siebie dziewięćdziesięciolatka
        i siedemnastolatki — jednego, który pamięta, i drugiej, która potrafi nagrać
        i udostępnić — to pewne historie znikną na zawsze.
      </p>
      <p>
        Działają tu formy dobrze znane, wystarczy je wprowadzić: tandemy pokoleń przy warsztatach
        rzemiosła; żywa biblioteka, w której „książką” jest człowiek — także świadek Marszu
        Śmierci; nagrania wideo robione telefonami przez licealistów.
      </p>
      <blockquote>
        <p>Dziedzictwo przekazuje się między ludźmi albo nie przekazuje się wcale.</p>
      </blockquote>

      <h2 id="nauczyciel">11. Nauczyciel doceniony nie odpuszcza</h2>
      <p>
        Żadna młodzież nie pokocha historii, jeśli nie poprowadzi jej ktoś, kto sam czuje,
        że ta praca ma sens i prestiż. Dlatego potrzebne są konkursy, które nagradzają nie tylko
        uczniów — ale i nauczycieli. Takie konkursy już istnieją.
      </p>
      <p>
        Od 2006 roku <strong>Nagroda im. Ireny Sendlerowej „Za naprawianie świata”</strong>
        honoruje nauczycieli, którzy uczą tolerancji i szacunku. W Europie działa sieć
        <strong>EUSTORY</strong> — konkursy historyczne w ponad dwudziestu krajach, z ponad
        trzystoma tysiącami uczestników. W Polsce od 1996 r. organizowany jest konkurs
        „Historia Bliska”, a Fundacja Geremka prowadzi „Moje życie w PRL”, w którym nagrody
        otrzymują również nauczyciele-opiekunowie zwycięskich prac.
      </p>
      <p>
        Te konkursy już są. Wystarczy po nie sięgnąć — albo zgłosić do nich nauczyciela,
        który obok nas stoi. <strong>Bo nauczyciel doceniony to nauczyciel, który nie
        odpuszcza.</strong>
      </p>

      <h2 id="piec">12. Pięć kroków i brakujące podpisy</h2>
      <ol>
        <li><strong>Zapisać wspomnienia.</strong> Dopóki jeszcze są.</li>
        <li><strong>Współdecydować z mieszkańcami.</strong> Nie konsultować — współdecydować.</li>
        <li>
          <strong>Udostępnić zbiory cyfrowo.</strong> Dziedzictwo zamknięte w magazynie
          to dziedzictwo, które nie istnieje.
        </li>
        <li>
          <strong>Wyjść ze sztuką w miasto.</strong> Na ulicę Ofiar Oświęcimskich.
          Na dworzec. Na trasę marszu.
        </li>
        <li><strong>Włączyć wszystkie pokolenia.</strong></li>
      </ol>
      <p>
        Żeby to nie zależało od przypadku ani od jednego zapalonego nauczyciela, potrzebny jest
        plan współpracy: umowa szkoły z muzeum, koordynatorzy po obu stronach, klasy obejmujące
        patronat nad konkretnymi punktami Drogi Loslau i kalendarz w rytmie rocznic — nagrania
        jesienią, marsz w styczniu, wystawa w maju.
      </p>
      <p><strong>Taki plan jest już napisany. Brakuje podpisów.</strong></p>

      <h2 id="palac">13. Ten pałac powstał z miłości</h2>
      <p>
        Pałac przeszedł już pierwszy, kluczowy etap przemiany: z zaniedbanego budynku
        administracyjnego stał się nowoczesną, dostępną przestrzenią kultury. Teraz czas,
        by odzyskał to, co najważniejsze — głos ludzi.
      </p>
      <p>
        <strong>Ten pałac powstał z miłości.</strong> A w styczniu 1945 roku, tuż obok,
        przechodziła kolumna, w której każdy kolejny krok był przeciwieństwem miłości:
        pogardą, przemocą, odczłowieczeniem.
      </p>
      <p>Nie chodzi o to, żeby jedno zasłaniało drugie. Chodzi o to, żeby jedno drugie oświetlało.</p>
      <p class="wiersz">
        Nie każda historia mieści się w gablocie.<br>
        Czasem śpi w szufladzie — w liście, fotografii,<br>
        czasem budzi się w głosie starszej pani,<br>
        w jednym zdaniu, które drży od wspomnień.<br><br>
        Wtedy muzeum nie oddziela od życia.<br>
        Idzie obok, słucha, podaje głos.<br>
        Nie tylko przechowuje przeszłość —<br>
        pomaga nam spotkać się z nią na nowo.
      </p>
      <blockquote>
        <p>Niech ten pałac nadal będzie miejscem relacji.</p>
      </blockquote>

      <h2 id="zrodla">14. Źródła i materiały</h2>
      <div class="card soft">
        <ul class="zrodla">
          <li>
            <strong>Muzeum partycypacyjne:</strong> N. Simon, <em>The Participatory Museum</em>,
            2010; B. Fiedler / A. Harrer, teksty o partycypacji w kulturze („neues museum”).
          </li>
          <li>
            <strong>Droga Loslau:</strong> P. Hojka, <em>Kierunek Loslau</em>, Muzeum
            w Wodzisławiu Śląskim.
          </li>
          <li>
            <strong>Kamienie pamięci:</strong> projekt Guntera Demniga (stolpersteine.eu) —
            pierwsza kostka w Kolonii w 1992 r.; ponad 120 tys. kamieni w ponad 30 krajach.
          </li>
          <li>
            <strong>Pomniki na trasie z Dachau:</strong> 22 identyczne rzeźby Huberta von
            Pilgrima, jedna kopia w Yad Vashem w Jerozolimie (m.in. Süddeutsche Zeitung, 2025).
          </li>
          <li>
            <strong>Ogród Sprawiedliwych:</strong> Mediolan (od 2003 r.), Warszawa (od 2014 r.).
          </li>
          <li>
            <strong>Wiedeń:</strong> Community Gallery Wien Museum (od 2023 r.); wolny wstęp
            do wystawy stałej od grudnia 2023 r.; projekt <em>Migration sammeln</em> (2015–2016).
          </li>
          <li>
            <strong>Topothek:</strong> ogólnokrajowa platforma archiwów lokalnych (ICARUS) —
            ok. 450 gmin, ponad 2 mln wpisów, ponad 3 tys. wolontariuszy.
          </li>
          <li>
            <strong>Konkursy:</strong> Nagroda im. Ireny Sendlerowej (CEO, od 2006 r.);
            EUSTORY (Körber-Stiftung); „Historia Bliska” (Ośrodek KARTA); „Moje życie w PRL”.
          </li>
        </ul>
        <p class="zrodla" style="margin-bottom:0">
          <small>
            Uwaga redakcyjna: przed publikacją należy potwierdzić nazwę ulicy przy pomniku
            i krzyżu, dokładną datę pierwszego Marszu Pamięci przez Żory, aktualne terminy
            konkursów dla nauczycieli oraz wybrane dane liczbowe. Szczegółowa lista
            <a href="seminarium/artykul-muzeum-bez-scian.pdf">w wersji PDF artykułu</a>
            (rozdział „Do sprawdzenia przed publikacją”).
          </small>
        </p>
      </div>

      <p class="zrodla" style="margin-top:22px">
        <small>
          Tekst powstał na podstawie wystąpienia seminaryjnego „Muzeum bez ścian. Dziedzictwo
          mieszka w ludziach”. Wersje do pobrania:
          <a href="seminarium/artykul-muzeum-bez-scian.pdf">artykuł (PDF)</a> ·
          <a href="seminarium/prezentacja-muzeum-bez-scian.pdf">prezentacja (PDF)</a>.
        </small>
      </p>
    </article>
  </div>
</section>
"""


def main():
    with open(SZABLON, encoding="utf-8") as f:
        html = f.read()

    # --- 1. nagłówek dokumentu: tytuł, opis, canonical, OG
    html = html.replace(
        "<title>Pamięć i Historia — Mszana.info</title>",
        "<title>%s</title>" % TYTUL)
    html = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="%s">' % OPIS, html, count=1)
    html = html.replace('<link rel="canonical" href="https://mszana.info/pamiec.html">',
                        '<link rel="canonical" href="https://mszana.info/muzeum-bez-scian.html">')
    html = re.sub(r'<meta property="og:title" content="[^"]*">',
                  '<meta property="og:title" content="%s">' % TYTUL, html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*">',
                  '<meta property="og:description" content="%s">' % OPIS, html, count=1)
    html = html.replace('<meta property="og:url" content="https://mszana.info/pamiec.html">',
                        '<meta property="og:url" content="https://mszana.info/muzeum-bez-scian.html">')

    # --- 2. nawigacja: bieżąca strona to już nie „Pamięć i Historia”
    html = html.replace('<li><a href="pamiec.html" aria-current="page">Pamięć i Historia</a></li>',
                        '<li><a href="pamiec.html">Pamięć i Historia</a></li>')

    # --- 3. okruszki
    html = html.replace(
        '<a href="index.html">Mszana.info</a> <span aria-hidden="true">›</span> '
        '<span aria-current="page">Pamięć i Historia</span>',
        '<a href="index.html">Mszana.info</a> <span aria-hidden="true">›</span> '
        '<a href="pamiec.html">Pamięć i Historia</a> '
        '<span aria-hidden="true">›</span> <span aria-current="page">Muzeum bez ścian</span>')

    # --- 4. treść główna
    html = re.sub(r"<main id=\"tresc\">.*?</main>",
                  "<main id=\"tresc\">\n" + TRESC.strip() + "\n</main>",
                  html, flags=re.S)

    # --- 5. pager
    html = html.replace('<a class="prev" href="dokumenty.html" rel="prev">← Dokumenty i źródła</a>',
                        '<a class="prev" href="pamiec.html" rel="prev">← Pamięć i Historia</a>')
    html = html.replace('<a class="next" href="kontakt.html" rel="next">Kontakt →</a>',
                        '<a class="next" href="nadeslij.html" rel="next">Prześlij materiał →</a>')

    # --- 6. stopka: link do artykułu w „Na skróty”
    html = html.replace(
        '<li><a href="#pamiec">Pamięć i Historia</a></li>',
        '<li><a href="pamiec.html">Pamięć i Historia</a></li>\n'
        '          <li><a href="muzeum-bez-scian.html">Artykuł: Muzeum bez ścian</a></li>')

    with open(WYJSCIE, "w", encoding="utf-8") as f:
        f.write(html)
    print("Zapisano: %s (%d znaków)" % (WYJSCIE, len(html)))


if __name__ == "__main__":
    main()
