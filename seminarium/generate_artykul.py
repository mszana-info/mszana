# -*- coding: utf-8 -*-
"""
Artykuł do druku: „Muzeum bez ścian. Jak dziedzictwo przestaje być zbiorem, a staje się relacją"

Czyta artykul-muzeum-bez-scian.md i składa go do PDF A4 (z przypisami i numeracją stron).

Uruchomienie:
    pip install reportlab
    python generate_artykul.py
Wynik: artykul-muzeum-bez-scian.pdf
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
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)

KATALOG = os.path.dirname(os.path.abspath(__file__))
WEJSCIE = os.path.join(KATALOG, "artykul-muzeum-bez-scian.md")
WYJSCIE = os.path.join(KATALOG, "artykul-muzeum-bez-scian.pdf")

# ---------------------------------------------------------------- czcionki
pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PL-It", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PL-BoldIt", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("PL", normal="PL", bold="PL-Bold",
                              italic="PL-It", boldItalic="PL-BoldIt")

GREEN = colors.HexColor("#0F5132")
GREEN_L = colors.HexColor("#E7F1EB")
AMBER = colors.HexColor("#C9821A")
INK = colors.HexColor("#1F1F1F")
GREY = colors.HexColor("#5A5A5A")
LINE = colors.HexColor("#C9DFD2")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm
BOT_M = 18 * mm
PW = PAGE_W - 2 * MARGIN

S_TITLE = ParagraphStyle("t", fontName="PL-Bold", fontSize=21, leading=25.5, textColor=GREEN)
S_SUB = ParagraphStyle("s", fontName="PL-It", fontSize=13.5, leading=18, textColor=GREY,
                       spaceBefore=4, spaceAfter=10)
S_H2 = ParagraphStyle("h2", fontName="PL-Bold", fontSize=14, leading=18, textColor=GREEN,
                      spaceBefore=14, spaceAfter=5)
S_H3 = ParagraphStyle("h3", fontName="PL-Bold", fontSize=11.5, leading=15.5, textColor=GREEN,
                      spaceBefore=10, spaceAfter=4)
S_BODY = ParagraphStyle("b", fontName="PL", fontSize=10.5, leading=15.6, textColor=INK,
                        alignment=TA_JUSTIFY, spaceAfter=7)
S_LEAD = ParagraphStyle("lead", parent=S_BODY, fontSize=11.3, leading=16.6, textColor=colors.HexColor("#333333"))
S_QUOTE = ParagraphStyle("q", fontName="PL-It", fontSize=10.8, leading=16, textColor=colors.HexColor("#3A3A3A"))
S_BUL = ParagraphStyle("bu", fontName="PL", fontSize=10.5, leading=15.2, textColor=INK,
                       alignment=TA_LEFT, leftIndent=16, bulletIndent=2, spaceAfter=3.5)
S_FN = ParagraphStyle("fn", fontName="PL", fontSize=8.7, leading=12.4, textColor=GREY,
                      alignment=TA_LEFT, spaceAfter=4)
S_NOTE = ParagraphStyle("no", fontName="PL-It", fontSize=9.3, leading=13.4, textColor=GREY,
                        alignment=TA_JUSTIFY)


def inline(txt):
    """Zamiana znaczników Markdown na znaczniki ReportLab."""
    t = (txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"\[\^(\d+)\](?!:)", r"<super>\1</super>", t)
    return t


def wczytaj(sciezka):
    """Zwraca (elementy_tresci, definicje_przypisow)."""
    with open(sciezka, encoding="utf-8") as f:
        linie = f.read().split("\n")

    tresc, przypisy = [], []
    tryb_przypisy = False
    bufor_cytat, bufor_lista = [], []

    def oproznij_cytat():
        if bufor_cytat:
            tekst = "<br/>".join(inline(x) for x in bufor_cytat)
            tabela = Table([[Paragraph(tekst, S_QUOTE)]], colWidths=[PW - 12 * mm])
            tabela.setStyle(TableStyle([
                ("LINEBEFORE", (0, 0), (0, -1), 2.4, AMBER),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            tresc.append(Spacer(1, 2))
            tresc.append(tabela)
            tresc.append(Spacer(1, 9))
            bufor_cytat.clear()

    def oproznij_liste(uporzadkowana):
        if not bufor_lista:
            return
        for punkt, tekst in bufor_lista:
            znacznik = (punkt + ".") if punkt else "\u2022"
            tresc.append(Paragraph(inline(tekst), S_BUL, bulletText=znacznik))
        tresc.append(Spacer(1, 5))
        bufor_lista.clear()

    for linia in linie:
        goly = linia.strip()

        if goly.startswith("[^") and "]:" in goly:
            tryb_przypisy = True
            oproznij_cytat()
            oproznij_liste(False)
            numer, tresc_przypisu = goly[2:].split("]:", 1)
            przypisy.append((numer.strip(), inline(tresc_przypisu.strip())))
            continue

        if tryb_przypisy:
            if goly.startswith("## ") or goly.startswith("#"):
                tryb_przypisy = False
            else:
                # kontynuacja ostatniego przypisu
                if przypisy and goly:
                    numer, poprzedni = przypisy[-1]
                    przypisy[-1] = (numer, poprzedni + " " + inline(goly))
                continue

        if not goly:
            oproznij_cytat()
            oproznij_liste(False)
            continue

        if goly.startswith("> "):
            oproznij_liste(False)
            bufor_cytat.append(goly[2:])
            continue
        oproznij_cytat()

        if re.match(r"^[-–] ", goly):
            oproznij_liste(False)
            bufor_lista.append((None, goly[2:]))
            continue
        dopasowanie = re.match(r"^(\d+)\. (.*)$", goly)
        if dopasowanie:
            oproznij_liste(False)
            bufor_lista.append((dopasowanie.group(1), dopasowanie.group(2)))
            continue
        oproznij_liste(False)

        if goly == "---":
            tresc.append(Spacer(1, 8))
            kreska = Table([[""]], colWidths=[PW], rowHeights=[0.5])
            kreska.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.7, LINE)]))
            tresc.append(kreska)
            tresc.append(Spacer(1, 10))
            continue

        if goly.startswith("# "):
            tresc.append(Paragraph(inline(goly[2:]), S_TITLE))
            continue
        if goly.startswith("### "):
            tresc.append(Paragraph(inline(goly[4:]), S_SUB))
            continue
        if goly.startswith("## "):
            tytul = goly[3:]
            if tytul.lower().startswith("przypis"):
                continue  # przypisy drukujemy osobno, na końcu
            tresc.append(Paragraph(inline(tytul), S_H2))
            continue
        if goly.startswith("*") and goly.endswith("*") and goly.count("*") == 2:
            tresc.append(Paragraph(inline(goly), S_NOTE))
            tresc.append(Spacer(1, 6))
            continue

        tresc.append(Paragraph(inline(goly), S_BODY))

    oproznij_cytat()
    oproznij_liste(False)
    return tresc, przypisy


def zbuduj(sciezka, przypisy, total="?"):
    def stopka(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN, 13 * mm, PAGE_W - MARGIN, 13 * mm)
        canvas.setFont("PL", 8)
        canvas.setFillColor(GREY)
        canvas.drawString(MARGIN, 9.4 * mm, "Muzeum bez ścian · materiał seminaryjny")
        canvas.drawRightString(PAGE_W - MARGIN, 9.4 * mm, "strona %d z %s" % (doc.page, total))
        canvas.restoreState()

    doc = BaseDocTemplate(
        sciezka, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=18 * mm, bottomMargin=BOT_M,
        title="Muzeum bez scian - artykul seminaryjny",
        author="[autorka]", subject="Dziedzictwo, muzeum partycypacyjne, pamiec lokalna",
    )
    doc.addPageTemplates([PageTemplate(
        id="all",
        frames=[Frame(MARGIN, BOT_M, PW, PAGE_H - 18 * mm - BOT_M, id="gl",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)],
        onPage=stopka)])

    tresc, _ = wczytaj(WEJSCIE)
    if przypisy:
        tresc.append(Spacer(1, 12))
        ramka = Table([[Paragraph("Przypisy", ParagraphStyle(
            "ph", parent=S_H2, spaceBefore=0, spaceAfter=6))]], colWidths=[PW])
        ramka.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GREEN_L),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        tresc.append(ramka)
        tresc.append(Spacer(1, 6))
        for numer, tekst in przypisy:
            tresc.append(Paragraph("<b>[%s]</b> %s" % (numer, tekst), S_FN))

    doc.build(tresc)


if __name__ == "__main__":
    tresc, przypisy = wczytaj(WEJSCIE)
    zbuduj("/tmp/_probe.pdf", przypisy)
    try:
        import pypdfium2 as pdfium
        n = len(pdfium.PdfDocument("/tmp/_probe.pdf"))
    except Exception:
        n = "?"
    zbuduj(WYJSCIE, przypisy, total=n)
    print("PDF: %s (stron: %s, przypisów: %d)" % (WYJSCIE, n, len(przypisy)))
