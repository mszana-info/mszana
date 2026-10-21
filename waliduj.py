"""Walidator statyczny HTML dla serwisu Mszana.info.

Sprawdza:
  - zbilansowanie tagów (niedomknięte / nadmiarowe),
  - duplikaty id,
  - poprawność kotwic href="#..." w obrębie dokumentu,
  - obecność plików, do których odwołują się src/href,
  - obrazki bez atrybutu alt,
  - puste href/src.
"""
from html.parser import HTMLParser
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [
    "index.html", "glos.html", "regulamin.html", "pamiec.html",
    "dokumenty.html", "nadeslij.html", "kontakt.html",
]

VOID = {
    "meta", "link", "img", "br", "hr", "input", "source", "area",
    "base", "col", "embed", "param", "track", "wbr",
}


class Validator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = []
        self.hrefs = []
        self.imgs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.append(d["id"])
        if tag == "a" and "href" in d:
            self.hrefs.append(d["href"])
        if tag == "img":
            self.imgs.append((d.get("src", ""), d.get("alt")))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("nadmiarowy </%s> w linii %d" % (tag, self.getpos()[0]))
            return
        if self.stack[-1][0] != tag:
            self.errors.append(
                "niezbilansowane: otwarto <%s> (linia %d), zamknięto </%s> (linia %d)"
                % (self.stack[-1][0], self.stack[-1][1][0], tag, self.getpos()[0])
            )
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    return
            return
        self.stack.pop()


def main():
    total_errors = 0
    for name in FILES:
        path = os.path.join(BASE, name)
        if not os.path.exists(path):
            print("BRAK PLIKU: %s" % name)
            total_errors += 1
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        v = Validator()
        v.feed(text)
        v.close()
        errors = list(v.errors)
        for tag, pos in v.stack:
            errors.append("niezamkniety <%s> z linii %d" % (tag, pos[0]))

        seen = set()
        for i in v.ids:
            if i in seen:
                errors.append("duplikat id: %s" % i)
            seen.add(i)

        for href in v.hrefs:
            if not href.strip():
                errors.append("pusty href")
            elif href.startswith("#"):
                anchor = href[1:]
                if anchor and anchor not in seen:
                    errors.append("brak kotwicy w dokumencie: %s" % href)

        for src, alt in v.imgs:
            if not src.strip():
                errors.append("pusty src w <img>")
            elif not src.startswith(("http", "/cdn-cgi/", "data:")):
                target = os.path.join(BASE, src.split("?")[0])
                if not os.path.exists(target):
                    errors.append("brak pliku: %s" % src)
            if alt is None:
                errors.append("brak alt w <img src=%s>" % src)

        status = "OK" if not errors else "BŁĘDY"
        print("%-16s %-8s %3d B, %4d kotwic, %2d img" % (
            name, status, len(v.ids), len(v.hrefs), len(v.imgs)))
        for e in errors:
            print("    - %s" % e)
        total_errors += len(errors)

    print("\nRazem błędów: %d" % total_errors)
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
