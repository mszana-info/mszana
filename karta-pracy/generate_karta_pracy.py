# -*- coding: utf-8 -*-
"""
Karta pracy — język angielski, klasa 4
Czasownik "to be": zdania twierdzące i przeczące.

Uruchomienie:
    pip install reportlab          # wymagane
    pip install pypdfium2          # opcjonalne (tylko po to, by wpisać "strona x z N")
    python generate_karta_pracy.py

Wynik: karta-pracy-to-be-klasa4.pdf  (A4: s. 1-2 karta pracy, s. 3 klucz odpowiedzi)
"""

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "karta-pracy-to-be-klasa4.pdf")

# ---------------------------------------------------------------- czcionki
pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("PL", normal="PL", bold="PL-Bold", italic="PL", boldItalic="PL-Bold")

# ---------------------------------------------------------------- kolory
GREEN = colors.HexColor("#0F5132")
GREEN_L = colors.HexColor("#E7F1EB")
GREEN_M = colors.HexColor("#C9DFD2")
AMBER = colors.HexColor("#C9821A")
AMBER_L = colors.HexColor("#FFF6E6")
AMBER_M = colors.HexColor("#EBD3A8")
INK = colors.HexColor("#222222")
GREY = colors.HexColor("#5A5A5A")
LINE = colors.HexColor("#A9BAB1")

PAGE_W, PAGE_H = A4
MARGIN = 15 * mm
TOP_M = 12 * mm
BOT_M = 16 * mm
PW = PAGE_W - 2 * MARGIN

# ---------------------------------------------------------------- style
title = ParagraphStyle("title", fontName="PL-Bold", fontSize=15.5, leading=19, textColor=GREEN)
sub = ParagraphStyle("sub", fontName="PL", fontSize=10, leading=13, textColor=GREY)
kicker = ParagraphStyle("kicker", fontName="PL-Bold", fontSize=8.6, leading=11,
                        textColor=AMBER, spaceAfter=1)
body = ParagraphStyle("body", fontName="PL", fontSize=10, leading=13.6, textColor=INK)
item = ParagraphStyle("item", parent=body, fontSize=10, leading=13.8, spaceAfter=2.0)
hlead = ParagraphStyle("hlead", parent=body, fontSize=9.8, leading=12.6, textColor=GREY,
                       spaceAfter=3.4)
note = ParagraphStyle("note", parent=body, fontSize=9.2, leading=12.0, textColor=GREY,
                      spaceAfter=1.6)
hzad = ParagraphStyle("hzad", fontName="PL-Bold", fontSize=10.6, leading=13.5,
                      textColor=colors.white)
hzad_r = ParagraphStyle("hzad_r", parent=hzad, alignment=2)
hsec = ParagraphStyle("hsec", fontName="PL-Bold", fontSize=10.2, leading=13,
                      textColor=colors.white)
hkey = ParagraphStyle("hkey", parent=hlead, fontName="PL-Bold", fontSize=10,
                      leading=12.8, textColor=GREEN, spaceAfter=2.5)
cell = ParagraphStyle("cell", fontName="PL", fontSize=9.5, leading=12.2, textColor=INK)
cell_h = ParagraphStyle("cell_h", parent=cell, fontName="PL-Bold", fontSize=9.6,
                        textColor=colors.white)
cell_c = ParagraphStyle("cell_c", parent=cell, alignment=1)
cell_hc = ParagraphStyle("cell_hc", parent=cell_h, alignment=1)
kitem = ParagraphStyle("kitem", parent=body, fontSize=9.4, leading=12.2, spaceAfter=1.4)
kitem_i = ParagraphStyle("kitem_i", parent=kitem, textColor=GREY)


def P(txt, st=body):
    return Paragraph(txt, st)


def bar(tekst, styl=hzad, tlo=GREEN, prawy=None):
    """Kolorowy pasek nagłówka."""
    komorki = [P(tekst, styl)]
    if prawy:
        komorki.append(P(prawy, hzad_r))
    tbl = Table([komorki], colWidths=[PW * 0.62, PW * 0.38] if prawy else [PW])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tlo),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return tbl


def zadanie(nr, polecenie, punkty, wskazowka=None):
    """Nagłówek zadania + polecenie (+ wskazówka)."""
    out = [bar("Zadanie %s" % nr, hzad, prawy="%s pkt" % punkty), Spacer(1, 3.4),
           P(polecenie, hlead)]
    if wskazowka:
        out.append(P(wskazowka, note))
        out.append(Spacer(1, 1.6))
    return out


def dwa_kolumny(elementy):
    """Rozkłada pozycje w dwóch kolumnach (oszczędza miejsce)."""
    polowa = (len(elementy) + 1) // 2
    lewa, prawa = elementy[:polowa], elementy[polowa:]
    while len(prawa) < len(lewa):
        prawa.append("")
    tbl = Table([[P(a, item), P(b, item)] for a, b in zip(lewa, prawa)],
                colWidths=[PW * 0.5, PW * 0.5])
    tbl.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return tbl


def wiersz_linia(prefix, szer_linii=0.5, styl_pred=item, wysokosc=6.0 * mm):
    """Wiersz zadania: tekst polecenia + pusta linia do pisania (pełna szerokość)."""
    tbl = Table([[P(prefix, styl_pred), ""]],
                colWidths=[PW * (1 - szer_linii), PW * szer_linii],
                rowHeights=[wysokosc])
    tbl.setStyle(TableStyle([
        ("LINEBELOW", (1, 0), (1, 0), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
    ]))
    return tbl


def blok_wierszy(pozycje, szer_linii=0.5, styl_pred=item, wysokosc=6.0 * mm):
    """Lista wierszy z liniami do pisania."""
    return [wiersz_linia(t, szer_linii, styl_pred, wysokosc) for t in pozycje]


# ================================================================ TREŚĆ
wiersze_gram = [
    ("I", "I am", "I\u2019m", "I am not", "I\u2019m not"),
    ("you", "you are", "you\u2019re", "you are not", "you aren\u2019t"),
    ("he", "he is", "he\u2019s", "he is not", "he isn\u2019t"),
    ("she", "she is", "she\u2019s", "she is not", "she isn\u2019t"),
    ("it", "it is", "it\u2019s", "it is not", "it isn\u2019t"),
    ("we", "we are", "we\u2019re", "we are not", "we aren\u2019t"),
    ("you", "you are", "you\u2019re", "you are not", "you aren\u2019t"),
    ("they", "they are", "they\u2019re", "they are not", "they aren\u2019t"),
]

z1 = ["I ________ nine years old.",
      "Maja ________ my best friend.",
      "We ________ in the same class.",
      "Our school ________ in Mszana.",
      "You ________ a good pupil.",
      "It ________ a yellow pencil.",
      "They ________ my friends.",
      "My dog ________ small and funny."]

z2 = ["I ______________________ a teacher. I am a pupil.",
      "My bag ______________________ heavy.",
      "We ______________________ at school today. It is Saturday!",
      "Kate ______________________ from Poland.",
      "These pencils ______________________ new.",
      "It ______________________ my dog.",
      "You ______________________ late.",
      "My brothers ______________________ at home."]

z3 = ["I ( am / are ) ten years old.",
      "She ( isn\u2019t / aren\u2019t ) at school today.",
      "My parents ( is / are ) at work.",
      "It ( isn\u2019t / aren\u2019t ) my pen.",
      "We ( \u2019m not / aren\u2019t ) tired.",
      "Tom and Kate ( is / are ) my friends."]

z4 = ["I am from Mszana.", "My sister is a doctor.", "They are at the cinema.",
      "It is cold today.", "We are hungry.", "You are in class five."]

z5 = ["She / my / is / teacher", "are / not / at / They / school",
      "We / happy / are / today", "This / my / is / not / pencil",
      "nine / Tom / old / is / years", "dogs / The / small / are"]

z6 = ["\u2713", "\u2713", "\u2713", "\u2713", "\u2717", "\u2717"]

klucz = [
    ("Zadanie 1 (8 pkt)", [
        "1. I <b>am</b> nine years old.",
        "2. Maja <b>is</b> my best friend.",
        "3. We <b>are</b> in the same class.",
        "4. Our school <b>is</b> in Mszana.",
        "5. You <b>are</b> a good pupil.",
        "6. It <b>is</b> a yellow pencil.",
        "7. They <b>are</b> my friends.",
        "8. My dog <b>is</b> small and funny.",
    ]),
    ("Zadanie 2 (8 pkt)", [
        "1. I <b>\u2019m not</b> a teacher.",
        "2. My bag <b>isn\u2019t</b> heavy.",
        "3. We <b>aren\u2019t</b> at school today.",
        "4. Kate <b>isn\u2019t</b> from Poland.",
        "5. These pencils <b>aren\u2019t</b> new.",
        "6. It <b>isn\u2019t</b> my dog.",
        "7. You <b>aren\u2019t</b> late.",
        "8. My brothers <b>aren\u2019t</b> at home.",
    ]),
    ("Zadanie 3 (6 pkt)", [
        "1. I <b>am</b> ten years old.",
        "2. She <b>isn\u2019t</b> at school today.",
        "3. My parents <b>are</b> at work.",
        "4. It <b>isn\u2019t</b> my pen.",
        "5. We <b>aren\u2019t</b> tired.",
        "6. Tom and Kate <b>are</b> my friends.",
    ]),
    ("Zadanie 4 (6 pkt)", [
        "1. I\u2019m not from Mszana.",
        "2. My sister isn\u2019t a doctor.",
        "3. They aren\u2019t at the cinema.",
        "4. It isn\u2019t cold today.",
        "5. We aren\u2019t hungry.",
        "6. You aren\u2019t in class five.",
        "<i>Uwaga: pe\u0142ne formy (is not, are not) s\u0105 r\u00f3wnie\u017c poprawne.</i>",
    ]),
    ("Zadanie 5 (6 pkt)", [
        "1. She is my teacher.",
        "2. They are not at school.",
        "3. We are happy today.",
        "4. This is not my pencil.",
        "5. Tom is nine years old.",
        "6. The dogs are small.",
        "<i>Uwaga: dopuszczamy skr\u00f3ty (aren\u2019t, isn\u2019t).</i>",
    ]),
    ("Zadanie 6 (6 pkt)", [
        "<i>Odpowiedzi indywidualne \u2014 1 pkt za ka\u017cde poprawne zdanie.</i>",
        "Przyk\u0142ady \u2713: I\u2019m a pupil. / I\u2019m ten. / We\u2019re from Mszana. / It\u2019s a cat.",
        "Przyk\u0142ady \u2717: I\u2019m not tall. / My hair isn\u2019t long. / We aren\u2019t at school.",
        "<i>Punkt przyznajemy, gdy w zdaniu jest poprawna forma am / is / are "
        "(lub isn\u2019t / aren\u2019t / \u2019m not).</i>",
    ]),
]


# ================================================================ BUDOWA
def zbuduj(sciezka, total_stron="?"):
    def stopka(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(GREEN_M)
        canvas.setLineWidth(0.7)
        canvas.line(MARGIN, 12 * mm, PAGE_W - MARGIN, 12 * mm)
        canvas.setFont("PL", 7.8)
        canvas.setFillColor(GREY)
        canvas.drawString(MARGIN, 8.4 * mm,
                          "Karta pracy \u00b7 J\u0119zyk angielski \u00b7 Klasa 4 \u00b7 "
                          "czasownik \u201eto be\u201d (zdania twierdz\u0105ce i przecz\u0105ce)")
        canvas.drawRightString(PAGE_W - MARGIN, 8.4 * mm,
                               "strona %d z %s" % (doc.page, total_stron))
        canvas.restoreState()

    doc = BaseDocTemplate(
        sciezka, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN, topMargin=TOP_M, bottomMargin=BOT_M,
        title="Karta pracy - czasownik to be (zdania twierdzace i przeczace), klasa 4",
        author="Mszana.info", subject="Jezyk angielski, klasa 4 - czasownik to be",
    )
    doc.addPageTemplates([PageTemplate(
        id="all",
        frames=[Frame(MARGIN, BOT_M, PW, PAGE_H - TOP_M - BOT_M, id="gl",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)],
        onPage=stopka)])

    S = []

    # ---------------------------------------------------- nagłówek karty
    S.append(P("J\u0118ZYK ANGIELSKI \u00b7 KLASA 4 \u00b7 KARTA PRACY", kicker))
    S.append(P("Czasownik \u201eto be\u201d \u2014 zdania twierdz\u0105ce i przecz\u0105ce", title))
    S.append(Spacer(1, 1.5))
    S.append(P("Oko\u0142o 20 minut \u00b7 40 punkt\u00f3w \u00b7 \u0107wiczymy: "
               "am / is / are, przeczenie not i skr\u00f3ty (I\u2019m not, isn\u2019t, "
               "aren\u2019t)", sub))
    S.append(Spacer(1, 5))

    info = Table([[
        P("<b>Imi\u0119 i nazwisko:</b> " + "_" * 30, cell),
        P("<b>Klasa:</b> " + "_" * 8, cell),
        P("<b>Data:</b> " + "_" * 10, cell),
    ]], colWidths=[PW * 0.5, PW * 0.21, PW * 0.29])
    info.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_L),
        ("BOX", (0, 0), (-1, -1), 0.8, GREEN_M),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(info)
    S.append(Spacer(1, 7))

    # ---------------------------------------------------- ramka gramatyczna
    S.append(P("Zapami\u0119taj!", ParagraphStyle("zap", parent=hzad, textColor=GREEN,
                                                  fontSize=11.6, leading=14)))
    S.append(Spacer(1, 3))

    dane = [[P("Osoba", cell_hc), P("Twierdzenie \u2713", cell_hc), P("Skr\u00f3t", cell_hc),
             P("Przeczenie \u2717", cell_hc), P("Skr\u00f3t", cell_hc)]]
    for w in wiersze_gram:
        dane.append([P(w[0], cell_c)] + [P(x, cell_c) for x in w[1:]])

    gram = Table(dane, colWidths=[PW * 0.135, PW * 0.215, PW * 0.14, PW * 0.245, PW * 0.265],
                 rowHeights=[None] + [5.3 * mm] * len(wiersze_gram), repeatRows=1)
    gram.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("BACKGROUND", (0, 1), (-1, 1), GREEN_L),
        ("BACKGROUND", (0, 3), (-1, 3), GREEN_L),
        ("BACKGROUND", (0, 5), (-1, 5), GREEN_L),
        ("BACKGROUND", (0, 7), (-1, 7), GREEN_L),
        ("GRID", (0, 0), (-1, -1), 0.4, GREEN_M),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(gram)
    S.append(Spacer(1, 4))

    zasady = Table([[
        P("<b>1.</b> Twierdzenie to <b>osoba + am / is / are</b>: I <b>am</b> ten. "
          "She <b>is</b> my friend. We <b>are</b> at school.", cell),
        P("<b>2.</b> Przeczenie tworzymy, dodaj\u0105c <b>not</b> po am / is / are: "
          "I am <b>not</b> ten. She is <b>not</b> my friend.", cell),
        P("<b>3.</b> W mowie i w pisaniu cz\u0119sto u\u017cywamy skr\u00f3t\u00f3w: "
          "<b>I\u2019m not</b>, <b>isn\u2019t</b>, <b>aren\u2019t</b>.", cell),
    ]], colWidths=[PW / 3.0] * 3)
    zasady.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AMBER_L),
        ("BOX", (0, 0), (-1, -1), 0.8, AMBER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, AMBER_M),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    S.append(zasady)
    S.append(Spacer(1, 6))

    # ---------------------------------------------------- słówka
    slowka = [
        "I am (I\u2019m) \u2014 jestem", "years old \u2014 lat (o wieku)",
        "best friend \u2014 najlepszy przyjaciel", "pupil \u2014 ucze\u0144",
        "teacher \u2014 nauczyciel", "school \u2014 szko\u0142a",
        "heavy \u2014 ci\u0119\u017cki", "late \u2014 sp\u00f3\u017aniony",
        "tired \u2014 zm\u0119czony", "hungry \u2014 g\u0142odny",
        "at home \u2014 w domu", "dog \u2014 pies",
    ]
    rzedy = [[P(slowka[i + j], cell) for j in (0, 4, 8)] for i in range(4)]
    voc = Table([[P("Przydatne s\u0142\u00f3wka / Vocabulary", ParagraphStyle(
        "voc", parent=hzad, fontSize=10.2, textColor=GREEN))]] + rzedy,
        colWidths=[PW / 3.0] * 3)
    voc.setStyle(TableStyle([
        ("SPAN", (0, 0), (-1, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_L),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.8, GREEN_M),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, GREEN_M),
        ("INNERGRID", (0, 1), (-1, -1), 0.35, GREEN_M),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(voc)
    S.append(Spacer(1, 9))

    # ---------------------------------------------------- Zadanie 1
    blok = zadanie(1, "Uzupe\u0142nij zdania. Wpisz <b>am</b>, <b>is</b> lub <b>are</b>.",
                   8, "Ramka: <b>am \u00b7 is \u00b7 are</b> \u2014 ka\u017cdego wyrazu mo\u017cesz "
                      "u\u017cy\u0107 wi\u0119cej ni\u017c raz.")
    blok.append(dwa_kolumny(["%d. %s" % (i, t) for i, t in enumerate(z1, 1)]))
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 6))

    # ---------------------------------------------------- Zadanie 2
    blok = zadanie(2, "Uzupe\u0142nij zdania przecz\u0105ce. U\u017cyj skr\u00f3t\u00f3w: "
                      "<b>\u2019m not</b>, <b>isn\u2019t</b>, <b>aren\u2019t</b>.",
                   8, "Pami\u0119taj: <b>not</b> stoi zawsze po czasowniku <b>am / is / are</b>.")
    blok.append(dwa_kolumny(["%d. %s" % (i, t) for i, t in enumerate(z2, 1)]))
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 6))

    # ---------------------------------------------------- Zadanie 3
    blok = zadanie(3, "Zakre\u015bl poprawn\u0105 form\u0119.", 6)
    blok.append(dwa_kolumny(["%d. %s" % (i, t) for i, t in enumerate(z3, 1)]))
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 7))

    S.append(PageBreak())

    # ---------------------------------------------------- Zadanie 4
    blok = zadanie(4, "Napisz te same zdania w formie przecz\u0105cej. U\u017cyj skr\u00f3t\u00f3w.",
                   6)
    blok += blok_wierszy(["%d. %s \u2192" % (i, t) for i, t in enumerate(z4, 1)],
                         szer_linii=0.60, wysokosc=6.2 * mm)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 7))

    # ---------------------------------------------------- Zadanie 5
    blok = zadanie(5, "U\u0142\u00f3\u017c zdania z podanych wyraz\u00f3w. Pami\u0119taj o "
                      "wielkiej literze i kropce.", 6)
    blok += blok_wierszy(["%d. %s \u2192" % (i, t) for i, t in enumerate(z5, 1)],
                         szer_linii=0.60, wysokosc=6.2 * mm)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 7))

    # ---------------------------------------------------- Zadanie 6
    blok = zadanie(6, "Napisz o sobie: <b>cztery zdania twierdz\u0105ce</b> (\u2713) "
                      "i <b>dwa przecz\u0105ce</b> (\u2717).", 6,
                   "Przyk\u0142ad: <b>I\u2019m</b> ten. \u00b7 <b>I\u2019m not</b> tall. "
                   "\u00b7 <b>We aren\u2019t</b> at school today.")
    blok += blok_wierszy(["%d. %s" % (i, znak) for i, znak in enumerate(z6, 1)],
                         szer_linii=0.93, wysokosc=6.4 * mm)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 8))

    # ---------------------------------------------------- Dla chętnych
    blok = [bar("\u2605 Dla ch\u0119tnych \u2014 bez punkt\u00f3w", hsec), Spacer(1, 3.4),
            P("Przepisz zdanie w formie przecz\u0105cej, a potem napisz zdanie "
              "prawdziwe o sobie (pe\u0142ne formy, bez skr\u00f3t\u00f3w).", hlead),
            P("Najpierw przepisz zdanie w formie przecz\u0105cej, potem napisz "
              "prawd\u0119 o sobie:", note)] + \
        blok_wierszy(["It is Monday today. \u2192", "Ja:", "I am at home now. \u2192", "Ja:"],
                     szer_linii=0.72, wysokosc=5.8 * mm)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 9))

    # ---------------------------------------------------- samoocena
    samo = Table([[
        P("<b>M\u00f3j wynik:</b> .......... / 40", cell),
        P("<b>Samoocena:</b> \u263a &nbsp;&nbsp; \u2639", cell),
        P("<b>Uwagi nauczyciela:</b> ..............................", cell),
    ]], colWidths=[PW * 0.28, PW * 0.26, PW * 0.46])
    samo.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_L),
        ("BOX", (0, 0), (-1, -1), 0.8, GREEN_M),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(samo)

    S.append(PageBreak())

    # ---------------------------------------------------- KLUCZ
    S.append(P("KLUCZ ODPOWIEDZI \u00b7 STRONA DLA NAUCZYCIELA", kicker))
    S.append(P("Czasownik \u201eto be\u201d \u2014 zdania twierdz\u0105ce i przecz\u0105ce", title))
    S.append(Spacer(1, 1.5))
    S.append(P("Klasa 4 \u00b7 razem 40 punkt\u00f3w \u00b7 zadania 1\u20136 "
               "\u00b7 ocena: 40\u201336 pkt \u2014 bardzo dobrze \u00b7 35\u201330 pkt \u2014 dobrze "
               "\u00b7 29\u201324 pkt \u2014 dostatecznie \u00b7 23\u201318 pkt \u2014 dopuszczaj\u0105co "
               "\u00b7 poni\u017cej 18 pkt \u2014 wymaga \u0107wiczenia", sub))
    S.append(Spacer(1, 7))

    for tytul, pozycje in klucz:
        blok = [P(tytul, hkey)]
        for linia in pozycje:
            blok.append(P(linia, kitem_i if linia.startswith("<i>") else kitem))
        blok.append(Spacer(1, 5))
        S.append(KeepTogether(blok))

    S.append(Spacer(1, 2))
    S.append(P("<b>Wskaz\u00f3wka dla nauczyciela:</b> w zadaniach 4 i 5 uznajemy zar\u00f3wno "
               "formy pe\u0142ne (is not, are not), jak i skr\u00f3cone (isn\u2019t, aren\u2019t). "
               "W zadaniu 1 nie ma formy \u2019m \u2014 uczymy pe\u0142nego <b>I am</b>.",
               note))

    doc.build(S)


# dwuprzebiegowo: najpierw policz strony, potem wpisz "z N"
tmp = "/tmp/_karta_probe.pdf"
zbuduj(tmp, total_stron="?")
try:  # opcjonalnie: policzenie stron do stopki "strona x z N"
    import pypdfium2 as pdfium
    n = len(pdfium.PdfDocument(tmp))
except Exception:
    n = "?"
zbuduj(OUT, total_stron=n)
print("OK: %s (stron: %s)" % (OUT, n))
