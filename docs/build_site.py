#!/usr/bin/env python3
"""Generate the GitHub Pages site: English at the root, every other language under <code>/.

Run from anywhere: python3 docs/build_site.py
Pages are plain HTML so search engines index them without JavaScript. The text of each language is in
i18n/<code>.py; en.py is the reference the others translate.
"""
import html
import importlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

DOCS = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(DOCS))
SITE = "https://le-syl21.github.io/WANHAO-Duplicator-9/"
REPO = "https://github.com/Le-Syl21/WANHAO-Duplicator-9"
FW = REPO + "/tree/main/Firmware/Marlin%20bugfix-2.1.x/"
RAW = REPO + "/raw/main/Firmware/Marlin%20bugfix-2.1.x/"
DL = REPO + "/releases/latest/download/"
DISCORD = "https://discord.gg/T37DYHmt2j"
# Google Search Console ownership check for the URL-prefix property SITE.
GOOGLE_VERIFICATION = "TqbXre6qrm9jaoj6tFwRRiI2vuQilAZLm6kUJA-etmo"
# Bump when style.css changes, so browsers do not keep the old one.
STYLE_VERSION = 4

PAGES = ["index", "mk1", "mk1u2", "mk2", "mk3", "flash", "screen", "sensor", "slicer", "quiet"]
SIZES = [("300", "300 × 300 × 400 mm"), ("400", "400 × 400 × 400 mm"), ("500", "500 × 500 × 500 mm")]
# Same languages, same order as the touchscreen. hreflang uses the script for Chinese.
LANGS = ["en", "fr", "de", "es", "it", "pt", "nl", "pl", "tr", "ru", "ar", "hi", "zh", "ja", "ko", "id"]
HREFLANG = {"zh": "zh-Hans"}
LANG = {code: importlib.import_module(f"i18n.{code}") for code in LANGS
        if (DOCS / "i18n" / f"{code}.py").exists()}


def folder(lang):
    return "" if lang == "en" else lang + "/"


def href(page, lang, from_lang):
    """Relative link from a page in `from_lang` to `page` in `lang`."""
    up = "" if from_lang == "en" else "../"
    return (up + folder(lang) + ("" if page == "index" else page + ".html")) or "./"


def url(page, lang):
    return SITE + folder(lang) + ("" if page == "index" else page + ".html")


def downloads(model, lang):
    u = LANG[lang].UI
    rows = []
    for size, volume in SIZES:
        std = f"D9_{model}_{size}.hex"
        rows.append(
            f'<tr><td><strong>D9/{size}</strong></td><td class="volume">{volume}</td>'
            f'<td><a class="btn" href="{DL}{std}">{std}</a></td></tr>')
    return (f'<div class="table"><table class="dl"><thead><tr><th>{u["size"]}</th><th class="volume">{u["volume"]}</th>'
            f'<th>{u["file"]}</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


MODELS = ["MK1", "MK1u2", "MK2", "MK3"]


def slicer_table(lang):
    """One row per printer: the Cura profile and the OrcaSlicer bundle of the latest release."""
    u = LANG[lang].UI
    rows = []
    for model in MODELS:
        for size, _volume in SIZES:
            rows.append(
                f'<tr><td><strong>{u["nav"][model.lower()]}</strong> D9/{size}</td>'
                f'<td><a class="btn" href="{DL}D9_{model}_{size}_Cura.zip">Cura</a></td>'
                f'<td><a class="btn" href="{DL}D9_{model}_{size}.orca_printer">OrcaSlicer</a></td></tr>')
    # One column for the printer: the phone layout drops the second column of a download table.
    return (f'<div class="table"><table class="dl slicer"><thead><tr><th>{u["model"]}</th>'
            f'<th>Cura</th><th>OrcaSlicer</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")


def factory_rows(model, files):
    return "".join(
        f'<tr><td>D9/{s}</td><td><a href="{RAW}{model}/Wanhao_factory/{f}">{f}</a></td>'
        f'<td><a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a></td></tr>'
        for s, f in files)


MK1_FACTORY = [("V0.15", "V0.15/D9-V0.15.hex", "D9/300", "V0.15/D9-LCD-firmware-V0.15.rar"),
               ("V0.161", "V0.161/D9-300-0.161.hex", "D9/300", "V0.161/DWIN_SET_V0.161.zip"),
               ("V0.164(B)", "V0.164B/D9_300_V0.164(B).hex", "D9/300", "V0.164B/D9-LCD-firmware_v0.164(B).zip"),
               ("V0.164(B)", "V0.164B/D9_400_V0.164(B).hex", "D9/400", "V0.164B/D9-LCD-firmware_v0.164(B).zip"),
               ("V0.164(B)", "V0.164B/D9_500_V0.164(B).hex", "D9/500", "V0.164B/D9-LCD-firmware_v0.164(B).zip")]
# Tables of Wanhao's original firmwares, the same in every language.
ROWS = {
    "mk1": "".join(
        f'<tr><td>{v}</td><td>{s}</td><td><a href="{RAW}MK1/Wanhao_factory/{html.escape(h)}">{html.escape(h.split("/")[1])}</a></td>'
        f'<td><a href="{RAW}MK1/Wanhao_factory/{html.escape(z)}">{html.escape(z.split("/")[1])}</a></td></tr>'
        for v, h, s, z in MK1_FACTORY),
    "mk1u2": factory_rows("MK1u2", [(s, f"D9-{s}-BLTOUCH-FD_V1.1.31.hex") for s in ("300", "400", "500")]),
    "mk2": factory_rows("MK2", [("300", "D9-300-BLTOUCH-FD_V1.1.2.hex"), ("400", "D9-400-BLTOUCH-FD_V1.1.2.hex"),
                                ("500", "D9-500-BLTOUCH-FD_V1.1.2.1.hex")]),
    "mk3": factory_rows("MK3", [(s, f"D9-{s}-BLTOUCH-FD_V1.1.3.hex") for s in ("300", "400", "500")]),
}


def content(page, lang):
    h = SimpleNamespace(p=lambda name: href(name, lang, lang), img=("" if lang == "en" else "../") + "img/",
                        dl=lambda m: downloads(m, lang), rows=ROWS.get(page, ""), slicer=slicer_table(lang),
                        REPO=REPO, RAW=RAW, FW=FW, DL=DL, DISCORD=DISCORD)
    return LANG[lang].content(page, h)


# ---------------------------------------------------------------- wiring diagram

def sensor_svg(lang):
    """Top view of the board's sensor plug, wired to a BTT Smart Filament Sensor V2.0.

    Pin names come from Wanhao's own wiring diagram (the 4-pin plug left of POWER-DET:
    D9, D8, GND, 5V; the back of the board prints CTRL, BTN, GND, VCC in the same order).
    """
    t = dict(LANG[lang].SVG, sfs="BTT Smart Filament Sensor V2.0")
    font = "font-family=\"system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif\""
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 440" role="img" '
           f'aria-label="{html.escape(t["board"])}: D9, D8, GND, 5V → {t["sfs"]}" {font}>',
           '<rect width="760" height="440" rx="16" fill="#1d1d21"/>',
           '<rect x="20" y="20" width="380" height="400" rx="12" fill="#0e0e10" stroke="#34343a"/>',
           f'<text x="36" y="46" font-size="14" fill="#a3a3ab">{html.escape(t["board"])}</text>']

    def jst(x, y, pins, fill="#f2f2ee", w=None):
        w = w or 20 + pins * 30
        o = [f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="4" fill="{fill}" stroke="#bdbdb6"/>']
        for i in range(pins):
            cx = x + 10 + 15 + i * 30
            o.append(f'<rect x="{cx - 5}" y="{y + 17}" width="10" height="10" fill="#8a8a84"/>')
        return o

    # Row of endstop plugs, as on the board.
    for x, name, pins, fill in ((40, "Z-min", 2, "#f2f2ee"), (140, "Y-min", 2, "#d9352b"), (240, "X-min", 2, "#f2f2ee")):
        out.append(f'<text x="{x + 40}" y="84" font-size="13" fill="#ececef" text-anchor="middle">{name}</text>')
        out += jst(x, 92, pins, fill)
    # The sensor plug, highlighted, and POWER-DET next to it.
    out.append('<rect x="30" y="158" width="160" height="78" rx="8" fill="none" stroke="#ff5a6e" stroke-width="3"/>')
    out += jst(40, 181, 4)
    out += jst(222, 181, 3)
    out.append('<text x="267" y="252" font-size="13" fill="#a3a3ab" text-anchor="middle">POWER-DET</text>')
    out.append(f'<text x="32" y="153" font-size="14" font-weight="700" fill="#ff5a6e">{html.escape(t["plug"])}</text>')

    # Pin x centres of the 4-pin plug, left to right: D9, D8, GND, 5V.
    pins = [(65, "D9", "#4cc47f", 378, t["motion"], t["pulses"]),
            (95, "D8", "#f0b429", 332, t["switch"], t["level"]),
            (125, "GND", "#c8c8d0", 296, "GND", ""),
            (155, "5V", "#ff5a6e", 262, "5V", "")]
    for x, name, colour, y, _, _ in pins:
        out.append(f'<text x="{x}" y="176" font-size="12" font-weight="700" fill="{colour}" text-anchor="middle">{name}</text>')
    # Wires: the rightmost pin turns first, so no two wires cross.
    for x, _, colour, y, _, _ in pins:
        out.append(f'<path d="M{x} 226 V{y} H470" fill="none" stroke="{colour}" stroke-width="4" stroke-linejoin="round"/>')
        out.append(f'<circle cx="{x}" cy="226" r="4" fill="{colour}"/>')

    # The sensor.
    out.append('<rect x="470" y="244" width="36" height="152" rx="4" fill="#f2f2ee" stroke="#bdbdb6"/>')
    out.append('<rect x="506" y="204" width="236" height="210" rx="10" fill="#26262b" stroke="#5b5b62"/>')
    out.append(f'<text x="624" y="228" font-size="14" font-weight="700" fill="#ececef" text-anchor="middle">{t["sfs"]}</text>')
    for x, name, colour, y, label, hint in pins:
        out.append(f'<text x="518" y="{y + 5}" font-size="13" font-weight="700" fill="{colour}">{html.escape(label)}</text>')
        if hint:
            out.append(f'<text x="518" y="{y + 20}" font-size="11" fill="#a3a3ab">{html.escape(hint)}</text>')
    out.append(f'<text x="742" y="432" font-size="11" fill="#a3a3ab" text-anchor="end">{html.escape(t["names"])}</text>')
    out.append('</svg>')
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- layout

GLOBE = ('<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" '
         'stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9'
         'M12 3c-2.5 2.7-3.8 5.7-3.8 9s1.3 6.3 3.8 9"/></svg>')


def render(page, lang):
    title, description, body = content(page, lang)
    m = LANG[lang]
    u = m.UI
    up = "" if lang == "en" else "../"
    nav = "".join(
        f'<a href="{href(n, lang, lang)}"{" aria-current=\"page\"" if n == page else ""}>{u["nav"][n]}</a>'
        for n in PAGES)
    choices = "".join(
        f'<li><a href="{href(page, code, lang)}" hreflang="{HREFLANG.get(code, code)}" lang="{HREFLANG.get(code, code)}"'
        f'{" aria-current=\"true\"" if code == lang else ""}>{LANG[code].META["name"]}</a></li>'
        for code in LANG)
    alternates = "".join(
        f'<link rel="alternate" hreflang="{HREFLANG.get(code, code)}" href="{url(page, code)}">\n' for code in LANG)
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": description,
          "url": url(page, lang), "inLanguage": HREFLANG.get(lang, lang),
          "about": {"@type": "Product", "name": "Wanhao Duplicator 9", "brand": "Wanhao"}}
    if page == "index":
        ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "Wanhao Duplicator 9 firmware",
              "url": SITE, "inLanguage": HREFLANG.get(lang, lang), "description": description}
    verification = (f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION}">\n'
                    if page == "index" else "")
    return f"""<!doctype html>
<html lang="{HREFLANG.get(lang, lang)}" dir="{m.META['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
{verification}<link rel="canonical" href="{url(page, lang)}">
{alternates}<link rel="alternate" hreflang="x-default" href="{url(page, 'en')}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url(page, lang)}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta property="og:locale" content="{m.META['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🖨️</text></svg>">
<link rel="stylesheet" href="{up}style.css?v={STYLE_VERSION}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{href('index', lang, lang)}">Wanhao <span>D9</span> firmware</a>
<nav class="main">{nav}</nav>
<details class="lang"><summary aria-label="{html.escape(u['language'])}">{GLOBE}<span>{m.META['name']}</span></summary><ul>{choices}</ul></details>
</div></header>
<main><div class="wrap">
{body.strip()}
</div></main>
<footer class="site"><div class="wrap">
<a href="{REPO}">{u["footer_src"]}</a>
<a href="{DISCORD}">{u["footer_chat"]}</a>
<span>{u["footer_note"]}</span>
</div></footer>
</body>
</html>
"""


def main():
    for lang in LANG:
        (DOCS / "img" / f"d9-sensor-plug-{lang}.svg").write_text(sensor_svg(lang), encoding="utf-8")
        out = DOCS / folder(lang)
        out.mkdir(exist_ok=True)
        for page in PAGES:
            (out / ("index.html" if page == "index" else page + ".html")).write_text(render(page, lang), encoding="utf-8")
    urls = []
    for page in PAGES:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HREFLANG.get(l, l)}" href="{url(page, l)}"/>' for l in LANG)
        for lang in LANG:
            urls.append(f"<url><loc>{url(page, lang)}</loc>{alts}</url>")
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
