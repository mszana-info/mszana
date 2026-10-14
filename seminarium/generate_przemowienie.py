# -*- coding: utf-8 -*-
"""
Przemówienie do druku: „Muzeum bez ścian" (wersja seminaryjna).

Czyta przemowienie-muzeum-bez-scian.md i składa je do PDF A4 — z dużą czcionką,
z didaskaliami i podziałem na sekcje. Wersja do czytania z mównicy.

Uruchomienie:
    pip install reportlab
    python generate_przemowienie.py
Wynik: przemowienie-muzeum-bez-scian.pdf
"""

import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

KATALOG = os.path.dirname(os.path.abspath(__file__))
WEJSCIE = os.path.join(KATALOG, "przemowienie-muzeum-bez-scian.md")
WYJSCIE = os.path.join(KATALOG, "przemowienie-muzeum-bez-scian.pdf")

pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PL-It", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-BoldIt", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("PL", normal="PL", bold="PL-Bold",
                              italic="PL-It", boldItalic="PL-BoldIt")

GREEN = colors.HexColor("#0F5132")
GREEN_L = colors.HexColor("#E7F1EB")
AMBER = colors.HexColor("#C9821A")
AMBER_L = colors.HexColor("#FFF6E6")
INK = colors.HexColor("#111111")
GREY = colors.HexColor("#6A6A6A")
LINE = colors.HexColor("#C9DFD2")

PAGE_W, PAGE_H = A4
MARGIN = 22 * mm
BOT_M = 18 * mm
PW = PAGE_W - 2 * MARGIN

S_TITLE = ParagraphStyle("t", fontName="PL-Bold", fontSize=22, leading=27, textColor=GREEN)
S_SUB = ParagraphStyle("s", fontName="PL-It", fontSize=13, leading=18, textColor=GREY,
                       spaceBefore=3, spaceAfter=8)
S_HINT = ParagraphStyle("hint", fontName="PL", fontSize=11.5, leading=17.5, textColor=GREY,
                        leftIndent=10, spaceAfter=3)
S_SECTION = ParagraphStyle("sec", fontName="PL-Bold", fontSize=15.5, leading=20,
                           textColor=GREEN, spaceBefore=16, spaceAfter=3)
S_TALK = ParagraphStyle("talk", fontName="PL", fontSize=13, leading=21.5, textColor=INK,
                        alignment=TA_JUSTIFY, spaceAfter=9)
S_LEAD = ParagraphStyle("lead", parent=S_TALK, fontSize=13.5, leading=22)
S_DID = ParagraphStyle("did", fontName="PL-It", fontSize=10.8, leading=15, textColor=GREY,
                       leftIndent=16, spaceAfter=7)
S_VERSE = ParagraphStyle("verse", fontName="PL-It", fontSize=13, leading=21.5,
                         textColor=colors.HexColor("#2A2A2A"))
S_NUM = ParagraphStyle("num", fontName="PL", fontSize=13, leading=20.5, textColor=INK,
                       leftIndent=22, bulletIndent=6, spaceAfter=5)
S_TH = ParagraphStyle("th", fontName="PL-Bold", fontSize=10.5, leading=14, textColor=colors.white)
S_TD = ParagraphStyle("td", fontName="PL", fontSize=10.5, leading=14, textColor=INK)
S_NOTE = ParagraphStyle("note", fontName="PL", fontSize=9.6, leading=13.8, textColor=GREY,
                        alignment=TA_JUSTIFY, spaceAfter=4)


def inline(txt):
    t = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t


def zbuduj(sciezka, total="?"):
    def stopka(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN, 13 * mm, PAGE_W - MARGIN, 13 * mm)
        canvas.setFont("PL", 8.4)
        canvas.setFillColor(GREY)
        canvas.drawString(MARGIN, 9.4 * mm, "Muzeum bez ścian · przemówienie seminaryjne")
        canvas.drawRightString(PAGE_W - MARGIN, 9.4 * mm, "strona %d z %s" % (doc.page, total))
        canvas.restoreState()

    doc = BaseDocTemplate(
        sciezka, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=18 * mm, bottomMargin=BOT_M,
        title="Muzeum bez scian - przemowienie seminaryjne (wersja uzupelniona)",
        author="[autorka]", subject="Dziedzictwo, pamiec lokalna, muzeum partycypacyjne",
    )
    doc.addPageTemplates([PageTemplate(
        id="all",
        frames=[Frame(MARGIN, BOT_M, PW, PAGE_H - 18 * mm - BOT_M, id="gl",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)],
        onPage=stopka)])

    with open(WEJSCIE, encoding="utf-8") as f:
        linie = f.read().split("\n")

    S_ = []
    bufor_versu, bufor_tabeli, bufor_did = [], [], []

    def oproznij_vers():
        if not bufor_versu:
            return
        tresc = "<br/>".join(inline(x) for x in bufor_versu)
        tbl = Table([[Paragraph(tresc, S_VERSE)]], colWidths=[PW - 14 * mm])
        tbl.setStyle(TableStyle([
            ("LINEBEFORE", (0, 0), (0, -1), 2.6, AMBER),
            ("BACKGROUND", (0, 0), (-1, -1), AMBER_L),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        S_.append(tbl)
        S_.append(Spacer(1, 10))
        bufor_versu.clear()

    def oproznij_tabele():
        if not bufor_tabeli:
            return
        dane = []
        for i, wiersz in enumerate(bufor_tabeli):
            komorki = [c.strip() for c in wiersz.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in komorki):
                continue
            styl = S_TH if not dane else S_TD
            dane.append([Paragraph(inline(c), styl) for c in komorki])
        if dane:
            kol = [PW * 0.34, PW * 0.5, PW * 0.16]
            tbl = Table(dane, colWidths=kol, repeatRows=1)
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            S_.append(tbl)
            S_.append(Spacer(1, 10))
        bufor_tabeli.clear()

    for i, linia in enumerate(linie):
        goly = linia.strip()

        if goly.startswith("|"):
            oproznij_vers()
            bufor_tabeli.append(goly)
            continue
        oproznij_tabele()

        if goly == ">":
            bufor_versu.append("")          # przerwa między strofami
            continue
        if goly.startswith("> "):
            bufor_versu.append(goly[2:])
            continue
        oproznij_vers()

        if not goly:
            continue
        if goly == "---":
            S_.append(Spacer(1, 6))
            continue
        if goly.startswith("# "):
            S_.append(Paragraph(inline(goly[2:]), S_TITLE))
            continue
        if goly.startswith("### "):
            S_.append(Paragraph(inline(goly[4:]), S_SUB))
            continue
        if goly.startswith("## "):
            tytul = goly[3:]
            kreska = Table([[""]], colWidths=[PW], rowHeights=[0.6])
            kreska.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.8, GREEN)]))
            S_.append(KeepTogether([Spacer(1, 4), kreska, Paragraph(inline(tytul), S_SECTION)]))
            continue

        # didaskalia: *( ... )*
        if re.match(r"^\*\(.*\)\*$", goly):
            S_.append(Paragraph("<i>%s</i>" % goly[1:-1].strip(), S_DID))
            continue
        # kursywa techniczna w nawiasie
        if goly.startswith("*(") and goly.endswith(")*"):
            S_.append(Paragraph("<i>%s</i>" % goly[1:-1].strip(), S_DID))
            continue

        dopasowanie = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)$", goly)
        if dopasowanie:
            S_.append(Paragraph("<b>%s. %s</b> %s" % (dopasowanie.group(1),
                                                      dopasowanie.group(2),
                                                      inline(dopasowanie.group(3))),
                                S_NUM, bulletText=""))
            continue
        if re.match(r"^[-–•]\s", goly):
            S_.append(Paragraph(inline(goly[2:]), S_NUM, bulletText="\u2022"))
            continue
        if goly.startswith("###"):
            continue

        styl = S_LEAD if (i < 30) else S_TALK
        S_.append(Paragraph(inline(goly), styl))

    oproznij_vers()
    oproznij_tabele()
    doc.build(S_)


if __name__ == "__main__":
    zbuduj("/tmp/_probe_przem.pdf")
    try:
        import pypdfium2 as pdfium
        n = len(pdfium.PdfDocument("/tmp/_probe_przem.pdf"))
    except Exception:
        n = "?"
    zbuduj(WYJSCIE, total=n)
    print("PDF: %s (stron: %s)" % (WYJSCIE, n))
