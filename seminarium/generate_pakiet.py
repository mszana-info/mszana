# -*- coding: utf-8 -*-
"""
Pakiet do pobrania: prezentacja + przemówienie (+ artykuł).

Tworzy w katalogu seminarium/:
  1. pobierz/prezentacja-i-przemowienie-muzeum-bez-scian.pdf
     — jeden dokument: najpierw slajdy prezentacji (16:9), potem przemówienie (A4)
  2. pobierz/prezentacja-i-przemowienie-muzeum-bez-scian.zip
     — paczka ZIP ze wszystkimi plikami źródłowymi i gotowymi do druku

Uruchomienie:
    pip install pypdfium2 reportlab
    python generate_pakiet.py
"""

import os
import zipfile

KATALOG = os.path.dirname(os.path.abspath(__file__))
POBRAC = os.path.join(KATALOG, "pobierz")

PDFY = [
    ("prezentacja-muzeum-bez-scian.pdf", "Prezentacja — slajdy (16:9, 25 slajdów)"),
    ("przemowienie-muzeum-bez-scian.pdf", "Przemówienie — wersja do czytania z mównicy (A4)"),
    ("artykul-muzeum-bez-scian.pdf", "Artykuł — wersja do druku (A4, z przypisami)"),
]

DO_ZIP = [
    ("prezentacja-muzeum-bez-scian.pptx", "Prezentacja do edycji (PowerPoint / Keynote / Google Slides)"),
    ("prezentacja-muzeum-bez-scian.pdf", "Prezentacja do wyświetlania (PDF, 25 slajdów)"),
    ("przemowienie-muzeum-bez-scian.pdf", "Przemówienie do wydruku (A4, 13 stron)"),
    ("przemowienie-muzeum-bez-scian.md", "Przemówienie — wersja edytowalna (Markdown)"),
    ("artykul-muzeum-bez-scian.pdf", "Artykuł do druku (A4, z przypisami)"),
    ("artykul-muzeum-bez-scian.md", "Artykuł — wersja edytowalna (Markdown)"),
    ("README.md", "Opis plików i instrukcja generowania"),
]


def scal_pdf(wyjscie):
    """Slajdy + przemówienie + artykuł w jednym PDF, z okładką."""
    import pypdfium2 as pdfium

    # okładka
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas as pdfcanvas

    pdfmetrics.registerFont(TTFont("PL", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("PL-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

    okladka = os.path.join(POBRAC, "_okladka.pdf")
    c = pdfcanvas.Canvas(okladka, pagesize=A4)
    W, H = A4
    ziel = HexColor("#0F5132")
    amber = HexColor("#C9821A")
    szary = HexColor("#5A5A5A")
    c.setFillColor(ziel)
    c.rect(0, H - 4 * mm, W, 4 * mm, stroke=0, fill=1)
    c.setFillColor(amber)
    c.setFont("PL-Bold", 11)
    c.drawString(22 * mm, H - 45 * mm, "MATERIAŁY SEMINARYJNE")
    c.setFillColor(ziel)
    c.setFont("PL-Bold", 26)
    c.drawString(22 * mm, H - 62 * mm, "Muzeum bez ścian")
    c.setFillColor(szary)
    c.setFont("PL", 14)
    c.drawString(22 * mm, H - 75 * mm, "Dziedzictwo mieszka w ludziach")
    c.setFont("PL", 11.5)
    linie = [
        "W tym dokumencie:",
        "",
        "1.  Prezentacja — 25 slajdów (16:9) do wyświetlania",
        "2.  Przemówienie — wersja do czytania z mównicy (13 stron)",
        "3.  Artykuł — wersja do druku z przypisami (8 stron)",
        "",
        "Pliki edytowalne (.pptx, .md) znajdują się w paczce ZIP:",
        "prezentacja-i-przemowienie-muzeum-bez-scian.zip",
    ]
    y = H - 105 * mm
    for linia in linie:
        c.drawString(22 * mm, y, linia)
        y -= 7 * mm
    c.setFont("PL", 9.5)
    c.setFillColor(szary)
    c.drawString(22 * mm, 25 * mm,
                 "Przed wygłoszeniem uzupełnij: imię i nazwisko, instytucja, data oraz link do podcastu.")
    c.showPage()
    c.save()

    doc = pdfium.PdfDocument.new()
    zrodla = [okladka] + [os.path.join(KATALOG, nazwa) for nazwa, _ in PDFY]
    for sciezka in zrodla:
        doc.import_pages(pdfium.PdfDocument(sciezka))
    doc.save(wyjscie)
    os.remove(okladka)
    return len(doc)


def zrob_zip(wyjscie):
    with zipfile.ZipFile(wyjscie, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("JAK-KORZYSTAĆ.txt", (
            "PREZENTACJA I PRZEMÓWIENIE — „Muzeum bez ścian”\n"
            "================================================\n\n"
            "1) prezentacja-muzeum-bez-scian.pptx\n"
            "   Do edycji w PowerPoint / Keynote / Google Slides.\n"
            "   Każdy slajd ma NOTATKI PRELEGENTA (tempo, pauzy, plan skrócenia do 10 minut).\n\n"
            "2) prezentacja-muzeum-bez-scian.pdf\n"
            "   Ta sama prezentacja do wyświetlania na rzutniku (25 slajdów, 16:9).\n\n"
            "3) przemowienie-muzeum-bez-scian.pdf\n"
            "   Przemówienie do wydruku (A4, duża czcionka — do czytania z mównicy),\n"
            "   z didaskaliami i tabelą źródeł.\n\n"
            "4) przemowienie-muzeum-bez-scian.md\n"
            "   Wersja edytowalna przemówienia (do własnych poprawek).\n\n"
            "5) artykul-muzeum-bez-scian.pdf / .md\n"
            "   Artykuł z przypisami — wersja do druku i do edycji.\n\n"
            "PRZED WYSTĄPIENIEM UZUPEŁNIJ:\n"
            "  - imię i nazwisko, instytucja, data (slajd tytułowy),\n"
            "  - link do podcastu na Spotify (materiały towarzyszące),\n"
            "  - aktualne terminy konkursów dla nauczycieli.\n"
        ))
        for nazwa, opis in DO_ZIP:
            sciezka = os.path.join(KATALOG, nazwa)
            if os.path.exists(sciezka):
                z.write(sciezka, nazwa)
            else:
                print("  (pominięto, brak pliku: %s)" % nazwa)
    return len(DO_ZIP)


if __name__ == "__main__":
    os.makedirs(POBRAC, exist_ok=True)
    pdf_out = os.path.join(POBRAC, "prezentacja-i-przemowienie-muzeum-bez-scian.pdf")
    zip_out = os.path.join(POBRAC, "prezentacja-i-przemowienie-muzeum-bez-scian.zip")

    n = scal_pdf(pdf_out)
    print("PDF (wszystko w jednym): %s — stron: %d" % (pdf_out, n))
    zrob_zip(zip_out)
    print("ZIP (pliki osobno):      %s — %.0f kB" % (zip_out, os.path.getsize(zip_out) / 1024))
