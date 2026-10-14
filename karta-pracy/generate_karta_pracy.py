# -*- coding: utf-8 -*-
"""
Karta pracy — język angielski, klasa 4
Czasownik "to be": zdania twierdzące i przeczące.

Generuje trzy pliki do druku (A4):
  1. karta-pracy-to-be-klasa4-dla-ucznia.pdf        (2 s., uczniowie, bez klucza)
  2. karta-pracy-to-be-klasa4-dla-nauczyciela.pdf   (3 s., karta + klucz odpowiedzi)
  3. karta-pracy-to-be-klasa4-eko-do-druku.pdf      (2 s., wersja bez teł — oszczędza toner)

Uruchomienie:
    pip install reportlab      # wymagane
    pip install pypdfium2      # opcjonalne (tylko do numeracji "strona x z N")
    python generate_karta_pracy.py
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

KATALOG = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- czcionki
pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("PL", normal="PL", bold="PL-Bold", italic="PL", boldItalic="PL-Bold")

PAGE_W, PAGE_H = A4
MARGIN = 15 * mm
TOP_M = 12 * mm
BOT_M = 16 * mm
PW = PAGE_W - 2 * MARGIN

# ---------------------------------------------------------------- motywy
MOTYW_KOLOR = {
    "nazwa": "kolor",
    "bar_bg": colors.HexColor("#0F5132"),   # paski nagłówków zadań
    "bar_fg": colors.white,
    "bar_line": None,
    "head_bg": colors.HexColor("#0F5132"),  # nagłówek tabeli gramatycznej
    "head_fg": colors.white,
    "zebra": colors.HexColor("#E7F1EB"),
    "grid": colors.HexColor("#C9DFD2"),
    "box_bg": colors.HexColor("#FFF6E6"),   # ramka z zasadami
    "box_border": colors.HexColor("#C9821A"),
    "box_grid": colors.HexColor("#EBD3A8"),
    "soft_bg": colors.HexColor("#E7F1EB"),  # pola: dane ucznia, samoocena
    "soft_border": colors.HexColor("#C9DFD2"),
    "line": colors.HexColor("#A9BAB1"),     # linie do pisania
    "title": colors.HexColor("#0F5132"),
    "accent": colors.HexColor("#C9821A"),   # nadtytuł (kicker)
    "grey": colors.HexColor("#5A5A5A"),
    "ink": colors.HexColor("#222222"),
    "footer_rule": colors.HexColor("#C9DFD2"),
}

MOTYW_EKO = {
    "nazwa": "eko",
    "bar_bg": colors.white,
    "bar_fg": colors.HexColor("#111111"),
    "bar_line": colors.HexColor("#111111"),
    "head_bg": colors.HexColor("#E4E4E4"),
    "head_fg": colors.HexColor("#111111"),
    "zebra": colors.white,
    "grid": colors.HexColor("#9A9A9A"),
    "box_bg": colors.white,
    "box_border": colors.HexColor("#444444"),
    "box_grid": colors.HexColor("#B5B5B5"),
    "soft_bg": colors.white,
    "soft_border": colors.HexColor("#444444"),
    "line": colors.HexColor("#6E6E6E"),
    "title": colors.HexColor("#111111"),
    "accent": colors.HexColor("#333333"),
    "grey": colors.HexColor("#444444"),
    "ink": colors.HexColor("#111111"),
    "footer_rule": colors.HexColor("#999999"),
}


class St:
    """Zestaw styli akapitów dla danego motywu."""


def zrob_style(th):
    s = St()
    s.title = ParagraphStyle("title", fontName="PL-Bold", fontSize=15.5, leading=19,
                             textColor=th["title"])
    s.sub = ParagraphStyle("sub", fontName="PL", fontSize=10, leading=13, textColor=th["grey"])
    s.kicker = ParagraphStyle("kicker", fontName="PL-Bold", fontSize=8.6, leading=11,
                              textColor=th["accent"], spaceAfter=1)
    s.body = ParagraphStyle("body", fontName="PL", fontSize=10, leading=13.6, textColor=th["ink"])
    s.item = ParagraphStyle("item", parent=s.body, fontSize=10, leading=13.8, spaceAfter=2.0)
    s.hlead = ParagraphStyle("hlead", parent=s.body, fontSize=9.8, leading=12.6,
                             textColor=th["grey"], spaceAfter=3.4)
    s.note = ParagraphStyle("note", parent=s.body, fontSize=9.2, leading=12.0,
                            textColor=th["grey"], spaceAfter=1.6)
    s.hzad = ParagraphStyle("hzad", fontName="PL-Bold", fontSize=10.6, leading=13.5,
                            textColor=th["bar_fg"])
    s.hzad_r = ParagraphStyle("hzad_r", parent=s.hzad, alignment=2)
    s.hsec = ParagraphStyle("hsec", parent=s.hzad, fontSize=10.2, leading=13)
    s.zap = ParagraphStyle("zap", parent=s.hzad, textColor=th["title"], fontSize=11.6, leading=14)
    s.hkey = ParagraphStyle("hkey", parent=s.hlead, fontName="PL-Bold", fontSize=10,
                            leading=12.8, textColor=th["title"], spaceAfter=2.5)
    s.cell = ParagraphStyle("cell", fontName="PL", fontSize=9.5, leading=12.2, textColor=th["ink"])
    s.cell_h = ParagraphStyle("cell_h", parent=s.cell, fontName="PL-Bold", fontSize=9.6,
                              textColor=th["head_fg"])
    s.cell_c = ParagraphStyle("cell_c", parent=s.cell, alignment=1)
    s.cell_hc = ParagraphStyle("cell_hc", parent=s.cell_h, alignment=1)
    s.kitem = ParagraphStyle("kitem", parent=s.body, fontSize=9.4, leading=12.2, spaceAfter=1.4)
    s.kitem_i = ParagraphStyle("kitem_i", parent=s.kitem, textColor=th["grey"])
    return s


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

slowka = [
    "I am (I\u2019m) \u2014 jestem", "years old \u2014 lat (o wieku)",
    "best friend \u2014 najlepszy przyjaciel", "pupil \u2014 ucze\u0144",
    "teacher \u2014 nauczyciel", "school \u2014 szko\u0142a",
    "heavy \u2014 ci\u0119\u017cki", "late \u2014 sp\u00f3\u017aniony",
    "tired \u2014 zm\u0119czony", "hungry \u2014 g\u0142odny",
    "at home \u2014 w domu", "dog \u2014 pies",
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
def zbuduj(sciezka, th, z_kluczem=True, total_stron="?"):
    st = zrob_style(th)
    line_kolor = th["line"]

    def P(txt, styl=None):
        return Paragraph(txt, styl or st.body)

    def bar(tekst, styl=None, prawy=None, tlo=None):
        komorki = [P(tekst, styl or st.hzad)]
        if prawy:
            komorki.append(P(prawy, st.hzad_r))
        tbl = Table([komorki], colWidths=[PW * 0.62, PW * 0.38] if prawy else [PW])
        styl_tbl = [
            ("BACKGROUND", (0, 0), (-1, -1), tlo or th["bar_bg"]),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 2.6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
        if th["bar_line"]:
            styl_tbl.append(("LINEBELOW", (0, 0), (-1, -1), 1.1, th["bar_line"]))
        tbl.setStyle(TableStyle(styl_tbl))
        return tbl

    def zadanie(nr, polecenie, punkty, wskazowka=None):
        out = [bar("Zadanie %s" % nr, st.hzad, prawy="%s pkt" % punkty), Spacer(1, 3.4),
               P(polecenie, st.hlead)]
        if wskazowka:
            out.append(P(wskazowka, st.note))
            out.append(Spacer(1, 1.6))
        return out

    def dwa_kolumny(elementy):
        polowa = (len(elementy) + 1) // 2
        lewa, prawa = elementy[:polowa], elementy[polowa:]
        while len(prawa) < len(lewa):
            prawa.append("")
        tbl = Table([[P(a, st.item), P(b, st.item)] for a, b in zip(lewa, prawa)],
                    colWidths=[PW * 0.5, PW * 0.5])
        tbl.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        return tbl

    def wiersz_linia(prefix, szer_linii=0.5, wysokosc=6.2 * mm):
        tbl = Table([[P(prefix, st.item), ""]],
                    colWidths=[PW * (1 - szer_linii), PW * szer_linii],
                    rowHeights=[wysokosc])
        tbl.setStyle(TableStyle([
            ("LINEBELOW", (1, 0), (1, 0), 0.6, line_kolor),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ]))
        return tbl

    def blok_wierszy(pozycje, szer_linii=0.5, wysokosc=6.2 * mm):
        return [wiersz_linia(t, szer_linii, wysokosc) for t in pozycje]

    def stopka(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(th["footer_rule"])
        canvas.setLineWidth(0.7)
        canvas.line(MARGIN, 12 * mm, PAGE_W - MARGIN, 12 * mm)
        canvas.setFont("PL", 7.8)
        canvas.setFillColor(th["grey"])
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
    S.append(P("J\u0118ZYK ANGIELSKI \u00b7 KLASA 4 \u00b7 KARTA PRACY", st.kicker))
    S.append(P("Czasownik \u201eto be\u201d \u2014 zdania twierdz\u0105ce i przecz\u0105ce", st.title))
    S.append(Spacer(1, 1.5))
    S.append(P("Oko\u0142o 20 minut \u00b7 40 punkt\u00f3w \u00b7 \u0107wiczymy: am / is / are, "
               "przeczenie not i skr\u00f3ty (I\u2019m not, isn\u2019t, aren\u2019t)", st.sub))
    S.append(Spacer(1, 5))

    info = Table([[
        P("<b>Imi\u0119 i nazwisko:</b> " + "_" * 30, st.cell),
        P("<b>Klasa:</b> " + "_" * 8, st.cell),
        P("<b>Data:</b> " + "_" * 10, st.cell),
    ]], colWidths=[PW * 0.5, PW * 0.21, PW * 0.29])
    info.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), th["soft_bg"]),
        ("BOX", (0, 0), (-1, -1), 0.8, th["soft_border"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(info)
    S.append(Spacer(1, 7))

    # ---------------------------------------------------- ramka gramatyczna
    S.append(P("Zapami\u0119taj!", st.zap))
    S.append(Spacer(1, 3))

    dane = [[P("Osoba", st.cell_hc), P("Twierdzenie \u2713", st.cell_hc), P("Skr\u00f3t", st.cell_hc),
             P("Przeczenie \u2717", st.cell_hc), P("Skr\u00f3t", st.cell_hc)]]
    for w in wiersze_gram:
        dane.append([P(w[0], st.cell_c)] + [P(x, st.cell_c) for x in w[1:]])

    gram = Table(dane, colWidths=[PW * 0.135, PW * 0.215, PW * 0.14, PW * 0.245, PW * 0.265],
                 rowHeights=[None] + [5.3 * mm] * len(wiersze_gram), repeatRows=1)
    gram.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), th["head_bg"]),
        ("BACKGROUND", (0, 1), (-1, 1), th["zebra"]),
        ("BACKGROUND", (0, 3), (-1, 3), th["zebra"]),
        ("BACKGROUND", (0, 5), (-1, 5), th["zebra"]),
        ("BACKGROUND", (0, 7), (-1, 7), th["zebra"]),
        ("GRID", (0, 0), (-1, -1), 0.4, th["grid"]),
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
          "She <b>is</b> my friend. We <b>are</b> at school.", st.cell),
        P("<b>2.</b> Przeczenie tworzymy, dodaj\u0105c <b>not</b> po am / is / are: "
          "I am <b>not</b> ten. She is <b>not</b> my friend.", st.cell),
        P("<b>3.</b> W mowie i w pisaniu cz\u0119sto u\u017cywamy skr\u00f3t\u00f3w: "
          "<b>I\u2019m not</b>, <b>isn\u2019t</b>, <b>aren\u2019t</b>.", st.cell),
    ]], colWidths=[PW / 3.0] * 3)
    zasady.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), th["box_bg"]),
        ("BOX", (0, 0), (-1, -1), 0.8, th["box_border"]),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, th["box_grid"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    S.append(zasady)
    S.append(Spacer(1, 6))

    # ---------------------------------------------------- słówka
    rzedy = [[P(slowka[i + j], st.cell) for j in (0, 4, 8)] for i in range(4)]
    voc = Table([[P("Przydatne s\u0142\u00f3wka / Vocabulary", st.zap)]] + rzedy,
                colWidths=[PW / 3.0] * 3)
    voc.setStyle(TableStyle([
        ("SPAN", (0, 0), (-1, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), th["soft_bg"]),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.8, th["soft_border"]),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, th["soft_border"]),
        ("INNERGRID", (0, 1), (-1, -1), 0.35, th["grid"]),
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

    S.append(PageBreak())

    # ---------------------------------------------------- Zadanie 4
    blok = zadanie(4, "Napisz te same zdania w formie przecz\u0105cej. U\u017cyj skr\u00f3t\u00f3w.",
                   6)
    blok += blok_wierszy(["%d. %s \u2192" % (i, t) for i, t in enumerate(z4, 1)],
                         szer_linii=0.60)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 7))

    # ---------------------------------------------------- Zadanie 5
    blok = zadanie(5, "U\u0142\u00f3\u017c zdania z podanych wyraz\u00f3w. Pami\u0119taj o "
                      "wielkiej literze i kropce.", 6)
    blok += blok_wierszy(["%d. %s \u2192" % (i, t) for i, t in enumerate(z5, 1)],
                         szer_linii=0.60)
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
    blok = [bar("\u2605 Dla ch\u0119tnych \u2014 bez punkt\u00f3w", st.hsec), Spacer(1, 3.4),
            P("Przepisz zdanie w formie przecz\u0105cej, a potem napisz zdanie "
              "prawdziwe o sobie (pe\u0142ne formy, bez skr\u00f3t\u00f3w).", st.hlead),
            P("Najpierw przepisz zdanie w formie przecz\u0105cej, potem napisz "
              "prawd\u0119 o sobie:", st.note)] + \
        blok_wierszy(["It is Monday today. \u2192", "Ja:", "I am at home now. \u2192", "Ja:"],
                     szer_linii=0.72, wysokosc=5.8 * mm)
    S.append(KeepTogether(blok))
    S.append(Spacer(1, 9))

    # ---------------------------------------------------- samoocena
    samo = Table([[
        P("<b>M\u00f3j wynik:</b> .......... / 40", st.cell),
        P("<b>Samoocena:</b> \u263a &nbsp;&nbsp; \u2639", st.cell),
        P("<b>Uwagi nauczyciela:</b> ..............................", st.cell),
    ]], colWidths=[PW * 0.28, PW * 0.26, PW * 0.46])
    samo.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), th["soft_bg"]),
        ("BOX", (0, 0), (-1, -1), 0.8, th["soft_border"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    S.append(samo)

    # ---------------------------------------------------- KLUCZ (opcjonalnie)
    if z_kluczem:
        S.append(PageBreak())
        S.append(P("KLUCZ ODPOWIEDZI \u00b7 STRONA DLA NAUCZYCIELA", st.kicker))
        S.append(P("Czasownik \u201eto be\u201d \u2014 zdania twierdz\u0105ce i przecz\u0105ce",
                   st.title))
        S.append(Spacer(1, 1.5))
        S.append(P("Klasa 4 \u00b7 razem 40 punkt\u00f3w \u00b7 zadania 1\u20136 "
                   "\u00b7 ocena: 40\u201336 pkt \u2014 bardzo dobrze \u00b7 35\u201330 pkt \u2014 dobrze "
                   "\u00b7 29\u201324 pkt \u2014 dostatecznie \u00b7 23\u201318 pkt \u2014 dopuszczaj\u0105co "
                   "\u00b7 poni\u017cej 18 pkt \u2014 wymaga \u0107wiczenia", st.sub))
        S.append(Spacer(1, 7))
        for tytul, pozycje in klucz:
            blok = [P(tytul, st.hkey)]
            for linia in pozycje:
                blok.append(P(linia, st.kitem_i if linia.startswith("<i>") else st.kitem))
            blok.append(Spacer(1, 5))
            S.append(KeepTogether(blok))
        S.append(Spacer(1, 2))
        S.append(P("<b>Wskaz\u00f3wka dla nauczyciela:</b> w zadaniach 4 i 5 uznajemy zar\u00f3wno "
                   "formy pe\u0142ne (is not, are not), jak i skr\u00f3cone (isn\u2019t, aren\u2019t). "
                   "W zadaniu 1 nie ma formy \u2019m \u2014 uczymy pe\u0142nego <b>I am</b>.",
                   st.note))

    doc.build(S)


def policz_strony(sciezka):
    """Liczba stron zbudowanego pliku (opcjonalnie, gdy jest pypdfium2)."""
    try:
        import pypdfium2 as pdfium
        return len(pdfium.PdfDocument(sciezka))
    except Exception:
        return "?"


def wypisz(nazwa_pliku, th, z_kluczem):
    """Dwuprzebiegowo: najpierw policz strony, potem wpisz 'strona x z N'."""
    docelowa = os.path.join(KATALOG, nazwa_pliku)
    tmp = os.path.join(KATALOG, ".tmp-probe.pdf")
    zbuduj(tmp, th, z_kluczem, total_stron="?")
    n = policz_strony(tmp)
    zbuduj(docelowa, th, z_kluczem, total_stron=n)
    os.remove(tmp)
    print("  %-46s stron: %s" % (nazwa_pliku, n))


PLIKI = [
    # (nazwa pliku, motyw, czy dołączyć klucz odpowiedzi)
    ("karta-pracy-to-be-klasa4-dla-ucznia.pdf", MOTYW_KOLOR, False),
    ("karta-pracy-to-be-klasa4-dla-nauczyciela.pdf", MOTYW_KOLOR, True),
    ("karta-pracy-to-be-klasa4-eko-do-druku.pdf", MOTYW_EKO, False),
]

if __name__ == "__main__":
    print("Generuję karty pracy (A4):")
    for nazwa, th, z_kluczem in PLIKI:
        wypisz(nazwa, th, z_kluczem)
    print("Gotowe.")
