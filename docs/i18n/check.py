#!/usr/bin/env python3
"""Check a translation against en.py: same pages, same links, images, commands and HTML structure.

Usage: python3 docs/i18n/check.py <code> [<code> ...]
Only the modules named are imported, so it is safe to run while other translations are being written.
"""
import collections
import importlib
import sys
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
PAGES = ["index", "mk1", "mk1u2", "mk2", "mk3", "flash", "screen", "sensor", "slicer", "quiet"]
BLOCKS = {"h1", "h2", "h3", "p", "ul", "ol", "li", "table", "thead", "tbody", "tr", "th", "td", "pre", "figure",
          "figcaption", "div", "img"}


class Shape(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks, self.links, self.code, self.tags, self._in = [], [], [], collections.Counter(), 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] += 1
        if tag in BLOCKS:
            self.blocks.append(tag + ("#" + a["id"] if "id" in a else "") + ("." + a["class"] if "class" in a else ""))
        for k in ("href", "src"):
            if k in a:
                self.links.append(a[k])
        if tag == "code":
            self._in += 1
            self.code.append("")

    def handle_endtag(self, tag):
        if tag == "code":
            self._in -= 1

    def handle_data(self, data):
        if self._in:
            self.code[-1] += data


def shape(body):
    s = Shape()
    s.feed(body)
    return s


def fixture(lang):
    return SimpleNamespace(p=lambda n: f"PAGE:{n}", img="IMG/", dl=lambda m: f"<div>DL:{m}</div>", rows="<tr><td>ROWS</td></tr>",
                           slicer="<div>SLICER</div>",
                           REPO="REPO", RAW="RAW/", FW="FW/", DL="DL/", DISCORD="DISCORD")


def check(code):
    en, tr = importlib.import_module("i18n.en"), importlib.import_module(f"i18n.{code}")
    errors = []
    for name in ("META", "UI", "SVG"):
        if set(getattr(en, name)) != set(getattr(tr, name)):
            errors.append(f"{name}: keys differ from en.py")
    if set(en.UI["nav"]) != set(tr.UI["nav"]):
        errors.append("UI['nav']: keys differ from en.py")
    if tr.META.get("dir") not in ("ltr", "rtl"):
        errors.append("META['dir'] must be ltr or rtl")
    for page in PAGES:
        e_title, e_desc, e_body = en.content(page, fixture("en"))
        t_title, t_desc, t_body = tr.content(page, fixture(code))
        if not t_title.strip() or not t_desc.strip() or t_title == e_title or t_desc == e_desc:
            errors.append(f"{page}: title or description missing or untranslated")
        e, t = shape(e_body), shape(t_body)
        if e.blocks != t.blocks:
            errors.append(f"{page}: block structure differs\n    en: {e.blocks}\n    {code}: {t.blocks}")
        want_links = collections.Counter(l.replace("-en.", f"-{code}.").replace("/en-", f"/{code}-") for l in e.links)
        if want_links != collections.Counter(t.links):
            errors.append(f"{page}: links/images differ: missing {sorted((want_links - collections.Counter(t.links)).elements())}, "
                          f"extra {sorted((collections.Counter(t.links) - want_links).elements())}")
        # One-line <code> is a command or a value and stays as is; a diagram in <pre> may translate its labels.
        e.code = [c for c in e.code if "\n" not in c]
        t.code = [c for c in t.code if "\n" not in c]
        if collections.Counter(e.code) != collections.Counter(t.code):
            errors.append(f"{page}: <code> contents differ: missing {sorted((collections.Counter(e.code) - collections.Counter(t.code)).elements())}, "
                          f"extra {sorted((collections.Counter(t.code) - collections.Counter(e.code)).elements())}")
        for tag in ("strong", "em", "a", "code", "br"):
            if abs(e.tags[tag] - t.tags[tag]) > (0 if tag in ("a", "code") else 3):
                errors.append(f"{page}: <{tag}> count {t.tags[tag]} vs {e.tags[tag]} in en.py")
    return errors


if __name__ == "__main__":
    bad = 0
    for code in sys.argv[1:]:
        errs = check(code)
        print(f"{code}: " + ("OK" if not errs else f"{len(errs)} problem(s)"))
        for err in errs:
            print("  - " + err)
        bad += bool(errs)
    sys.exit(bad)
