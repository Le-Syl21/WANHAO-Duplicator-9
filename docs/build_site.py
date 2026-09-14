#!/usr/bin/env python3
"""Generate the GitHub Pages site (English at the root, French under fr/).

Run from anywhere: python3 docs/build_site.py
Pages are plain HTML so search engines index them without JavaScript.
"""
import html
import json
from pathlib import Path

DOCS = Path(__file__).resolve().parent
SITE = "https://le-syl21.github.io/WANHAO-Duplicator-9/"
REPO = "https://github.com/Le-Syl21/WANHAO-Duplicator-9"
FW = REPO + "/tree/main/Firmware/Marlin%20bugfix-2.1.x/"
RAW = REPO + "/raw/main/Firmware/Marlin%20bugfix-2.1.x/"
DL = REPO + "/releases/latest/download/"
DISCORD = "https://discord.gg/T37DYHmt2j"

PAGES = ["index", "mk1", "mk1u2", "mk2", "mk3", "flash", "screen"]
SIZES = [("300", "300 × 300 × 400 mm"), ("400", "400 × 400 × 400 mm"), ("500", "500 × 500 × 500 mm")]

UI = {
    "en": {
        "nav": {"index": "Home", "mk1": "MK1", "mk1u2": "MK1 + MK2 kit", "mk2": "MK2", "mk3": "MK3",
                "flash": "Flash guide", "screen": "Screen"},
        "other": ("fr", "Version française", "FR"),
        "size": "Size", "volume": "Build volume", "standard": "Standard", "inverted": "Y inverted",
        "footer_src": "Source and issues on GitHub", "footer_chat": "Discord",
        "footer_note": "Firmware under GNU GPL v3. Wanhao's manuals and firmwares remain Wanhao's.",
    },
    "fr": {
        "nav": {"index": "Accueil", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
                "flash": "Guide de flash", "screen": "Écran"},
        "other": ("en", "English version", "GB"),
        "size": "Taille", "volume": "Volume d'impression", "standard": "Standard", "inverted": "Y inversé",
        "footer_src": "Sources et tickets sur GitHub", "footer_chat": "Discord",
        "footer_note": "Firmware sous GNU GPL v3. Les manuels et firmwares Wanhao restent la propriété de Wanhao.",
    },
}


def href(page, lang, from_lang):
    """Relative link from a page in `from_lang` to `page` in `lang`."""
    up = "../" if from_lang == "fr" else ""
    base = up + ("fr/" if lang == "fr" else "")
    return (base + ("" if page == "index" else page + ".html")) or "./"


def url(page, lang):
    return SITE + ("fr/" if lang == "fr" else "") + ("" if page == "index" else page + ".html")


def downloads(model, lang):
    u = UI[lang]
    rows = []
    for size, volume in SIZES:
        std = f"D9_{model}_{size}.hex"
        inv = f"D9_{model}_{size}_Y-inverted.hex"
        rows.append(
            f'<tr><td><strong>D9/{size}</strong></td><td>{volume}</td>'
            f'<td><a class="btn" href="{DL}{std}">{std}</a></td>'
            f'<td><a class="btn ghost" href="{DL}{inv}">{inv}</a></td></tr>')
    return (f'<div class="table"><table class="dl"><thead><tr><th>{u["size"]}</th><th>{u["volume"]}</th>'
            f'<th>{u["standard"]}</th><th>{u["inverted"]}</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


# ---------------------------------------------------------------- content

def content(page, lang):
    p = lambda name: href(name, lang, lang)  # noqa: E731
    img = ("../" if lang == "fr" else "") + "img/"
    dl = lambda m: downloads(m, lang)  # noqa: E731
    en = lang == "en"

    if page == "index":
        if en:
            return ("Wanhao Duplicator 9 firmware (D9 MK1, MK2, MK3) – Marlin 2.1",
                    "Up-to-date Marlin firmware for every Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                    "screen files, Wanhao's original firmwares and manuals, and how to flash them.",
                    f"""
<h1>Wanhao Duplicator 9 firmware</h1>
<p class="lead">Wanhao's download site for the Duplicator 9 is gone. Everything a D9 owner needs is here instead:
current Marlin 2.1 firmware for every model and size, the matching touchscreen files, Wanhao's original
firmwares, Wanhao's manuals, and step-by-step flashing guides.</p>
<p><a class="btn" href="{REPO}/releases/latest">All downloads</a> <a class="btn ghost" href="{DISCORD}">Ask on Discord</a></p>

<h2>Which D9 do I have?</h2>
<div class="split"><div>
<ol>
<li><strong>Grey flat ribbon cable</strong> running to the print head, and a <strong>metal cylinder probe</strong>
next to the nozzle, no side reinforcements on the frame: <a href="{p('mk1')}">MK1</a>.</li>
<li>The same first-generation machine with a <strong>white BLTouch probe</strong> instead of the metal one:
an MK1 fitted with Wanhao's upgrade kit, <a href="{p('mk1u2')}">MK1 + MK2 kit</a>.</li>
<li><strong>Angled reinforcement ribs</strong> on both sides of the frame, a <strong>round black cable</strong>
to the head and a BLTouch: an MK2 or an MK3. Look under the bed at the <strong>Y motor</strong>, the one that
moves the bed: at the back, it is an <a href="{p('mk2')}">MK2</a>; at the front, on the touchscreen side, an
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>The number after D9 is the size: D9/300, D9/400 or D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 with its side reinforcement ribs">
<figcaption>D9 MK2: side ribs, round cable</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Inductive probe, ribbon cable. Firmware, Wanhao V0.15 to V0.164(B), manual.</p><a class="more" href="{p('mk1')}">MK1 firmware →</a></div>
<div class="card"><h3>D9 MK1 + MK2 kit</h3><p>MK1 upgraded with the BLTouch kit. Firmware and Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Kit firmware →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, side ribs. Firmware, Wanhao V1.1.2, guides.</p><a class="more" href="{p('mk2')}">MK2 firmware →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y motor at the front, filament sensor. Firmware and Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3 firmware →</a></div>
</div>

<h2>What these firmwares bring</h2>
<ul>
<li><strong>Marlin 2.1</strong> built from the Duplicator 9 configurations published in
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
with the fixes proposed there: MK1 probe read the right way round, MK3 Y direction, power-loss recovery.</li>
<li><strong>Axis directions checked against Wanhao's own firmwares</strong>, read out of Wanhao's binaries.
Each file also exists with the Y axis inverted, for machines whose Y motor was moved.</li>
<li><strong>Power-loss recovery</strong>: after an outage during an SD print, the screen offers to resume.</li>
<li><strong>Filament runout sensor</strong> support, on by default on the MK3, one command away on the others.</li>
<li><strong>A modern touchscreen interface</strong>, <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</li>
</ul>

<h2>Flashing in three steps</h2>
<ol>
<li>Download the <strong>.hex</strong> for your model and size from its page.</li>
<li>Flash it over USB with AVRDUDESS or avrdude: <a href="{p('flash')}">flash guide</a>.</li>
<li>Flash the touchscreen from a microSD card: <a href="{p('screen')}">screen guide</a>.</li>
</ol>
<p>Wanhao's original firmwares stay available on each model page, so a machine can always go back to how it left the factory.</p>
""")
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Firmware Marlin à jour pour toutes les Wanhao Duplicator 9 (D9/300, D9/400, D9/500 ; MK1, MK2, MK3), "
                "fichiers écran, firmwares d'origine Wanhao, manuels et guides de flash.",
                f"""
<h1>Firmware Wanhao Duplicator 9</h1>
<p class="lead">Le site de téléchargement de Wanhao pour la Duplicator 9 a disparu. Tout ce qu'il faut à un
propriétaire de D9 est ici : firmware Marlin 2.1 à jour pour chaque modèle et chaque taille, les fichiers de
l'écran tactile, les firmwares d'origine Wanhao, les manuels Wanhao et des guides de flash pas à pas.</p>
<p><a class="btn" href="{REPO}/releases/latest">Tous les téléchargements</a> <a class="btn ghost" href="{DISCORD}">Poser une question sur Discord</a></p>

<h2>Quelle D9 ai-je ?</h2>
<div class="split"><div>
<ol>
<li><strong>Nappe grise plate</strong> jusqu'à la tête d'impression, <strong>capteur cylindrique en métal</strong>
à côté de la buse, pas de renforts sur les côtés du cadre : <a href="{p('mk1')}">MK1</a>.</li>
<li>La même machine de première génération avec un <strong>capteur BLTouch blanc</strong> à la place du capteur
métallique : une MK1 équipée du kit Wanhao, <a href="{p('mk1u2')}">MK1 + kit MK2</a>.</li>
<li><strong>Renforts inclinés</strong> des deux côtés du cadre, <strong>câble noir rond</strong> jusqu'à la tête
et BLTouch : une MK2 ou une MK3. Regardez sous le plateau le <strong>moteur Y</strong>, celui qui déplace le
plateau : à l'arrière, c'est une <a href="{p('mk2')}">MK2</a> ; à l'avant, du côté de l'écran tactile, une
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Le nombre après D9 est la taille : D9/300, D9/400 ou D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 avec ses renforts latéraux">
<figcaption>D9 MK2 : renforts latéraux, câble rond</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Capteur inductif, nappe. Firmware, Wanhao V0.15 à V0.164(B), manuel.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + kit MK2</h3><p>MK1 passée au kit BLTouch. Firmware et Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware du kit →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, renforts latéraux. Firmware, Wanhao V1.1.2, guides.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Moteur Y à l'avant, capteur de filament. Firmware et Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>Ce qu'apportent ces firmwares</h2>
<ul>
<li><strong>Marlin 2.1</strong> compilé depuis les configurations Duplicator 9 publiées dans
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
avec les corrections proposées là-bas : capteur MK1 lu dans le bon sens, sens Y de la MK3, reprise après coupure.</li>
<li><strong>Sens des axes vérifiés contre les firmwares Wanhao</strong>, lus dans les binaires de Wanhao.
Chaque fichier existe aussi avec l'axe Y inversé, pour les machines dont le moteur Y a été déplacé.</li>
<li><strong>Reprise après coupure de courant</strong> : après une coupure pendant une impression depuis la carte SD, l'écran propose de reprendre.</li>
<li><strong>Capteur de fin de filament</strong> géré, actif par défaut sur la MK3, activable d'une commande sur les autres.</li>
<li><strong>Une interface d'écran moderne</strong>, <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</li>
</ul>

<h2>Flasher en trois étapes</h2>
<ol>
<li>Téléchargez le <strong>.hex</strong> de votre modèle et de votre taille depuis sa page.</li>
<li>Flashez-le en USB avec AVRDUDESS ou avrdude : <a href="{p('flash')}">guide de flash</a>.</li>
<li>Flashez l'écran tactile depuis une carte microSD : <a href="{p('screen')}">guide de l'écran</a>.</li>
</ol>
<p>Les firmwares d'origine Wanhao restent disponibles sur chaque page modèle : une machine peut toujours revenir à son état d'usine.</p>
""")

    if page == "mk1":
        factory = [("V0.15", "V0.15/D9-V0.15.hex", "D9/300", "V0.15/D9-LCD-firmware-V0.15.rar"),
                   ("V0.161", "V0.161/D9-300-0.161.hex", "D9/300", "V0.161/DWIN_SET_V0.161.zip"),
                   ("V0.164(B)", "V0.164B/D9_300_V0.164(B).hex", "D9/300", "V0.164B/D9-LCD-firmware_v0.164(B).zip"),
                   ("V0.164(B)", "V0.164B/D9_400_V0.164(B).hex", "D9/400", "V0.164B/D9-LCD-firmware_v0.164(B).zip"),
                   ("V0.164(B)", "V0.164B/D9_500_V0.164(B).hex", "D9/500", "V0.164B/D9-LCD-firmware_v0.164(B).zip")]
        rows = "".join(
            f'<tr><td>{v}</td><td>{s}</td><td><a href="{RAW}MK1/Wanhao_factory/{html.escape(h)}">{html.escape(h.split("/")[1])}</a></td>'
            f'<td><a href="{RAW}MK1/Wanhao_factory/{html.escape(z)}">{html.escape(z.split("/")[1])}</a></td></tr>'
            for v, h, s, z in factory)
        if en:
            return ("Wanhao Duplicator 9 MK1 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                    "Marlin 2.1 firmware for the Wanhao D9 MK1 with inductive probe, Wanhao's original V0.15 to V0.164(B) firmwares, "
                    "screen files and the MK1 user manual.",
                    f"""
<h1>Wanhao Duplicator 9 MK1 firmware</h1>
<div class="split"><div>
<p class="lead">The first Duplicator 9: a metal inductive probe next to the nozzle, a grey ribbon cable to the
print head, and a frame without side ribs.</p>
<p>These builds read the inductive probe the right way round (it triggers LOW) and use probe offsets measured on
a real MK1 (X 27, Y 3). The Y motor sits at the back, as Wanhao built it.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Inductive probe and ribbon cable on a Wanhao D9 MK1 print head">
<figcaption>MK1: inductive probe, ribbon cable</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Take the <strong>Standard</strong> file unless your Y motor was moved to the front: see
<a href="{p('flash')}#y-direction">standard or Y inverted</a>. Then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Wanhao's documents</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 user manual</a> (June 2018): assembly, wiring, menus, levelling, troubleshooting.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 getting started guide</a>.</li>
</ul>

<h2>Wanhao's original firmwares</h2>
<p>To put a machine back as it left the factory. Each motherboard firmware only works with the screen firmware
of the same version.</p>
<div class="table"><table><thead><tr><th>Version</th><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>The settings of each version (steps/mm, speeds, PID, axis directions) are listed in
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, read out of Wanhao's binaries.</p>
""")
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 pour la Wanhao D9 MK1 à capteur inductif, firmwares d'origine Wanhao V0.15 à V0.164(B), "
                "fichiers écran et manuel MK1.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">La première Duplicator 9 : un capteur inductif en métal à côté de la buse, une nappe grise jusqu'à
la tête d'impression et un cadre sans renforts latéraux.</p>
<p>Ces builds lisent le capteur inductif dans le bon sens (il se déclenche à l'état bas) et utilisent des décalages
de capteur mesurés sur une vraie MK1 (X 27, Y 3). Le moteur Y est à l'arrière, comme Wanhao l'a monté.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Capteur inductif et nappe sur la tête d'une Wanhao D9 MK1">
<figcaption>MK1 : capteur inductif, nappe</figcaption></figure></div>

<h2>Téléchargement</h2>
{dl("MK1")}
<p>Prenez le fichier <strong>Standard</strong>, sauf si votre moteur Y a été déplacé à l'avant : voir
<a href="{p('flash')}#y-direction">standard ou Y inversé</a>. Flashez ensuite l'écran avec
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documents Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Manuel utilisateur D9 MK1</a> (juin 2018, en anglais) : montage, câblage, menus, nivellement, dépannage.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Guide de démarrage D9 MK1</a>.</li>
</ul>

<h2>Firmwares d'origine Wanhao</h2>
<p>Pour remettre une machine dans son état d'usine. Chaque firmware de carte mère ne fonctionne qu'avec le firmware
d'écran de la même version.</p>
<div class="table"><table><thead><tr><th>Version</th><th>Taille</th><th>Carte mère</th><th>Écran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Les réglages de chaque version (pas/mm, vitesses, PID, sens des axes) sont listés dans
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, lus dans les binaires de Wanhao.</p>
""")

    def factory_rows(model, files):
        return "".join(
            f'<tr><td>D9/{s}</td><td><a href="{RAW}{model}/Wanhao_factory/{f}">{f}</a></td>'
            f'<td><a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a></td></tr>'
            for s, f in files)

    if page == "mk1u2":
        files = [(s, f"D9-{s}-BLTOUCH-FD_V1.1.31.hex") for s in ("300", "400", "500")]
        rows = factory_rows("MK1u2", files)
        if en:
            return ("Wanhao Duplicator 9 MK1 with MK2 upgrade kit (BLTouch) firmware – Marlin 2.1",
                    "Marlin 2.1 firmware for a Wanhao D9 MK1 upgraded with Wanhao's MK2 BLTouch kit, and Wanhao's original V1.1.31 kit firmware.",
                    f"""
<h1>Wanhao D9 MK1 with the MK2 upgrade kit</h1>
<div class="split"><div>
<p class="lead">A first-generation D9 fitted with Wanhao's MK2 upgrade kit: the MK1 frame, with a BLTouch probe
instead of the metal inductive one.</p>
<p>Wanhao shipped a separate firmware for this combination, because the kit's BLTouch does not sit where the
factory MK2's does: the probe's Y offset differs. These builds use the kit's geometry. The Y motor sits at the
back.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="BLTouch probe on a Wanhao D9 print head">
<figcaption>BLTouch probe</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Take the <strong>Standard</strong> file unless your Y motor was moved: see
<a href="{p('flash')}#y-direction">standard or Y inverted</a>. Then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">If the bed mesh looks shifted front to back, check the probe offset first: Wanhao's kit source
says Y −10, these builds use Y −20. Set yours with <code>M851 Y-10</code> then <code>M500</code>.</div>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.31 kit firmware (December 2018), used with the MK2 screen firmware.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")
        return ("Firmware Wanhao Duplicator 9 MK1 avec kit MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 pour une Wanhao D9 MK1 équipée du kit BLTouch MK2 de Wanhao, et firmware d'origine Wanhao V1.1.31 du kit.",
                f"""
<h1>Wanhao D9 MK1 avec le kit MK2</h1>
<div class="split"><div>
<p class="lead">Une D9 de première génération équipée du kit MK2 de Wanhao : le cadre de la MK1, avec un capteur
BLTouch à la place du capteur inductif en métal.</p>
<p>Wanhao a publié un firmware à part pour cette combinaison, car le BLTouch du kit n'est pas placé comme celui
d'une MK2 d'usine : le décalage Y du capteur diffère. Ces builds utilisent la géométrie du kit. Le moteur Y est à
l'arrière.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Capteur BLTouch sur la tête d'une Wanhao D9">
<figcaption>Capteur BLTouch</figcaption></figure></div>

<h2>Téléchargement</h2>
{dl("MK1u2")}
<p>Prenez le fichier <strong>Standard</strong>, sauf si votre moteur Y a été déplacé : voir
<a href="{p('flash')}#y-direction">standard ou Y inversé</a>. Flashez ensuite l'écran avec
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Si le maillage du plateau semble décalé d'avant en arrière, vérifiez d'abord le décalage du
capteur : la source du kit Wanhao indique Y −10, ces builds utilisent Y −20. Réglez le vôtre avec
<code>M851 Y-10</code> puis <code>M500</code>.</div>

<h2>Firmwares d'origine Wanhao</h2>
<p>Le firmware V1.1.31 du kit Wanhao (décembre 2018), utilisé avec le firmware d'écran de la MK2.</p>
<div class="table"><table><thead><tr><th>Taille</th><th>Carte mère</th><th>Écran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Réglages lus dans les binaires de Wanhao : <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        files = [("300", "D9-300-BLTOUCH-FD_V1.1.2.hex"), ("400", "D9-400-BLTOUCH-FD_V1.1.2.hex"),
                 ("500", "D9-500-BLTOUCH-FD_V1.1.2.1.hex")]
        rows = factory_rows("MK2", files)
        if en:
            return ("Wanhao Duplicator 9 MK2 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                    "Marlin 2.1 firmware for the Wanhao D9 MK2 with BLTouch, Wanhao's original V1.1.2 firmware and screen files, and Wanhao's MK2 guides.",
                    f"""
<h1>Wanhao Duplicator 9 MK2 firmware</h1>
<div class="split"><div>
<p class="lead">The second Duplicator 9: angled reinforcement ribs on both sides, a round black data cable to the
print head, a BLTouch probe and a spool holder on top.</p>
<p>Wanhao also changed the carriages to four rollers, fitted a double-rail Y axis and a thicker belt on the 400
and 500, and a double-sided bed on the 300 and 400. The Y motor sits at the back; these builds turn the Y axis the
way Wanhao's V1.1.2 firmware does.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Take the <strong>Standard</strong> file unless your Y motor sits at the front: see
<a href="{p('flash')}#y-direction">standard or Y inverted</a>. An MK2 whose head was also upgraded to the MK3 should
use the <a href="{p('mk3')}">MK3 firmware</a>. Then flash the screen with <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Wanhao's documents</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 getting started guide</a>.</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">The 12 improvements from MK1 to MK2</a>, by Wanhao.</li>
</ul>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.2 (October 2018; the 500 was rebuilt as V1.1.2.1 in July 2019), with Wanhao's MK2 screen firmware.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 pour la Wanhao D9 MK2 à BLTouch, firmware et fichiers écran d'origine Wanhao V1.1.2, guides Wanhao de la MK2.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">La deuxième Duplicator 9 : des renforts inclinés des deux côtés, un câble de données noir et rond
jusqu'à la tête, un capteur BLTouch et un porte-bobine sur le dessus.</p>
<p>Wanhao a aussi passé les chariots à quatre roulettes, monté un axe Y à double rail et une courroie plus épaisse
sur les 400 et 500, et un plateau double face sur les 300 et 400. Le moteur Y est à l'arrière ; ces builds font
tourner Y comme le firmware V1.1.2 de Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Téléchargement</h2>
{dl("MK2")}
<p>Prenez le fichier <strong>Standard</strong>, sauf si votre moteur Y est à l'avant : voir
<a href="{p('flash')}#y-direction">standard ou Y inversé</a>. Une MK2 dont la tête a aussi été passée en MK3 doit
prendre le <a href="{p('mk3')}">firmware MK3</a>. Flashez ensuite l'écran avec <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documents Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Guide de démarrage D9 MK2</a> (en anglais).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">Les 12 améliorations de la MK1 à la MK2</a>, par Wanhao.</li>
</ul>

<h2>Firmwares d'origine Wanhao</h2>
<p>La V1.1.2 de Wanhao (octobre 2018 ; la 500 a été recompilée en V1.1.2.1 en juillet 2019), avec le firmware d'écran MK2 de Wanhao.</p>
<div class="table"><table><thead><tr><th>Taille</th><th>Carte mère</th><th>Écran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Réglages lus dans les binaires de Wanhao : <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        files = [(s, f"D9-{s}-BLTOUCH-FD_V1.1.3.hex") for s in ("300", "400", "500")]
        rows = factory_rows("MK3", files)
        if en:
            return ("Wanhao Duplicator 9 MK3 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                    "Marlin 2.1 firmware for the Wanhao D9 MK3 (Y motor at the front, filament sensor) and Wanhao's original V1.1.3 firmware.",
                    f"""
<h1>Wanhao Duplicator 9 MK3 firmware</h1>
<p class="lead">The last Duplicator 9 keeps the MK2's frame and BLTouch, adds a filament runout sensor and moves
the Y motor to the front, on the touchscreen side.</p>
<p>Moving the motor reverses the Y axis: Wanhao's own V1.1.3 firmware inverts Y, and so do these builds. The
filament runout sensor is on by default. Wanhao published no probe offsets for the MK3, so these builds use the
MK2's.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Take the <strong>Standard</strong> file unless your Y motor sits at the back: see
<a href="{p('flash')}#y-direction">standard or Y inverted</a>. Then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">If the filament sensor stops prints at random, turn it off with <code>M412 S0</code> then
<code>M500</code>. Wanhao Europe had published a "ReverseMode" MK3 firmware for that problem; it has since been
deleted and could not be found.</div>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.3 (August 2019). Wanhao published no MK3 screen firmware: its MK3 downloads relied on the MK2 one.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 pour la Wanhao D9 MK3 (moteur Y à l'avant, capteur de filament) et firmware d'origine Wanhao V1.1.3.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK3</h1>
<p class="lead">La dernière Duplicator 9 garde le cadre et le BLTouch de la MK2, ajoute un capteur de fin de
filament et déplace le moteur Y à l'avant, du côté de l'écran tactile.</p>
<p>Déplacer le moteur inverse l'axe Y : le firmware V1.1.3 de Wanhao inverse Y, ces builds aussi. Le capteur de
fin de filament est actif par défaut. Wanhao n'a publié aucun décalage de capteur pour la MK3, ces builds
reprennent donc ceux de la MK2.</p>

<h2>Téléchargement</h2>
{dl("MK3")}
<p>Prenez le fichier <strong>Standard</strong>, sauf si votre moteur Y est à l'arrière : voir
<a href="{p('flash')}#y-direction">standard ou Y inversé</a>. Flashez ensuite l'écran avec
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Si le capteur de filament interrompt les impressions au hasard, désactivez-le avec
<code>M412 S0</code> puis <code>M500</code>. Wanhao Europe avait publié un firmware MK3 « ReverseMode » pour ce
problème ; il a été supprimé depuis et reste introuvable.</div>

<h2>Firmwares d'origine Wanhao</h2>
<p>La V1.1.3 de Wanhao (août 2019). Wanhao n'a publié aucun firmware d'écran MK3 : ses téléchargements MK3 renvoyaient à celui de la MK2.</p>
<div class="table"><table><thead><tr><th>Taille</th><th>Carte mère</th><th>Écran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Réglages lus dans les binaires de Wanhao : <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        if en:
            return ("How to flash a Wanhao Duplicator 9 (D9) motherboard firmware",
                    "Step-by-step guide to flash Marlin on a Wanhao D9 over USB with AVRDUDESS or avrdude, choose between the "
                    "standard and Y-inverted builds, and recover with Wanhao's firmware.",
                    f"""
<h1>Flashing the Duplicator 9 motherboard</h1>
<p class="lead">The D9's motherboard is an ATmega2560 with a USB bootloader: no programmer, no opening the base,
just a USB cable.</p>

<h2>What you need</h2>
<ul>
<li>A USB cable between the printer and the computer, and the printer <strong>switched on</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, graphical, easiest) or
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (command line, every system).</li>
<li>The <strong>.hex</strong> for your model and size: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2 id="y-direction">Standard or Y inverted?</h2>
<p>Every model comes in two builds. The <strong>standard</strong> file turns the Y axis the way Wanhao's own
firmware for that model does. The <strong>Y-inverted</strong> file turns it the other way, for machines whose Y motor
is not where Wanhao put it: moved motor, partial upgrade, replaced part.</p>
<ol>
<li><strong>Look at the Y motor</strong>, under the bed. Wanhao put it at the <strong>back</strong> on the MK1, the
MK1 + kit and the MK2, and at the <strong>front</strong>, on the touchscreen side, on the MK3. Where Wanhao put it
for your model: standard. At the other end: Y inverted.</li>
<li><strong>If you can't tell</strong>, flash the standard file and home Y alone (<code>G28 Y</code>, or Home on the
screen) with a hand on the power switch. The bed must move towards the Y endstop and stop on it. If it moves away,
or homing ends with <em>Homing Failed</em>, switch off and flash the Y-inverted file.</li>
</ol>

<h2>Before flashing</h2>
<div class="note">The first boot of a new build resets the settings stored in the printer. Send <code>M851</code>
(probe Z offset), <code>M92</code> (steps/mm) and <code>M301</code> (hotend PID) and keep the answers, to set them back
afterwards and save them with <code>M500</code>.</div>
<p>Close every program that may hold the printer's port: Cura, PrusaSlicer, OctoPrint, Pronterface, serial terminals.</p>

<h2>Flash with AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: your printer's COM port (for instance <code>COM3</code>). Leave the baud rate at its default.</li>
<li>Flash: choose the .hex file, then click <strong>Program!</strong>. It takes 30 to 60 seconds.</li>
</ol>

<h2>Flash with avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Replace the port and the file name with yours. The <code>wiring</code> protocol picks the bootloader's speed by itself.</p>

<h2>First boot</h2>
<ol>
<li>Unplug the USB cable, switch the printer off and on, plug the cable back.</li>
<li>Connect at <strong>250000 baud</strong> (Wanhao's firmwares used 115200) and send <code>M115</code>: the answer shows the new firmware.</li>
<li>Home all axes, then run a bed levelling from the screen or with <code>G29</code>, and save with <code>M500</code>.</li>
</ol>

<h2>Power loss and filament sensor</h2>
<ul>
<li>Power-loss recovery is on. Turn it off with <code>M413 S0</code> then <code>M500</code>.</li>
<li>The filament runout sensor is on by default on the MK3 only. Once a sensor is fitted on another model: <code>M412 S1</code> then <code>M500</code>.</li>
</ul>

<h2>Troubleshooting</h2>
<div class="table"><table><thead><tr><th>Problem</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port in use</td><td>Close every program using the printer's port.</td></tr>
<tr><td>Device not found</td><td>Install the CH340 USB driver, try another cable or USB port, check the printer is switched on.</td></tr>
<tr><td>Unreadable characters after flashing</td><td>Use 250000 baud with these firmwares, 115200 with Wanhao's.</td></tr>
<tr><td>Temperatures shown ×10 on the screen (236 for 23.6 °C)</td><td>The screen still has old files: flash <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</td></tr>
<tr><td>Homing Failed on Y</td><td>See <a href="#y-direction">standard or Y inverted</a>.</td></tr>
</tbody></table></div>

<h2>Going back to Wanhao's firmware</h2>
<p>Each model page links Wanhao's original motherboard and screen firmwares. Flash them the same way; Wanhao's
motherboard firmware needs Wanhao's screen firmware of the same generation.</p>
<p>Questions: <a href="{DISCORD}">Discord</a> or <a href="{REPO}/issues">GitHub issues</a>.</p>
""")
        return ("Comment flasher le firmware d'une Wanhao Duplicator 9 (D9)",
                "Guide pas à pas pour flasher Marlin sur une Wanhao D9 en USB avec AVRDUDESS ou avrdude, choisir entre les "
                "builds standard et Y inversé, et revenir au firmware Wanhao.",
                f"""
<h1>Flasher la carte mère de la Duplicator 9</h1>
<p class="lead">La carte mère de la D9 est un ATmega2560 avec bootloader USB : pas de programmateur, pas besoin
d'ouvrir le socle, juste un câble USB.</p>

<h2>Ce qu'il faut</h2>
<ul>
<li>Un câble USB entre l'imprimante et l'ordinateur, et l'imprimante <strong>allumée</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, graphique, le plus simple) ou
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (ligne de commande, tous systèmes).</li>
<li>Le <strong>.hex</strong> de votre modèle et de votre taille : <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2 id="y-direction">Standard ou Y inversé ?</h2>
<p>Chaque modèle existe en deux versions. Le fichier <strong>standard</strong> fait tourner l'axe Y comme le
firmware de Wanhao pour ce modèle. Le fichier <strong>Y inversé</strong> le fait tourner dans l'autre sens, pour les
machines dont le moteur Y n'est pas là où Wanhao l'a mis : moteur déplacé, upgrade partiel, pièce remplacée.</p>
<ol>
<li><strong>Regardez le moteur Y</strong>, sous le plateau. Wanhao l'a placé à l'<strong>arrière</strong> sur la MK1,
la MK1 + kit et la MK2, et à l'<strong>avant</strong>, du côté de l'écran tactile, sur la MK3. À l'endroit prévu par
Wanhao pour votre modèle : standard. À l'autre bout : Y inversé.</li>
<li><strong>Si vous ne savez pas</strong>, flashez le fichier standard et faites le homing de Y seul
(<code>G28 Y</code>, ou Home à l'écran), la main sur l'interrupteur. Le plateau doit aller vers le fin de course Y et
s'arrêter dessus. S'il s'en éloigne, ou si le homing finit en <em>Homing Failed</em>, éteignez et flashez le fichier Y inversé.</li>
</ol>

<h2>Avant de flasher</h2>
<div class="note">Le premier démarrage d'un nouveau build remet à zéro les réglages enregistrés dans l'imprimante.
Envoyez <code>M851</code> (décalage Z du capteur), <code>M92</code> (pas/mm) et <code>M301</code> (PID de la buse) et
gardez les réponses, pour les remettre ensuite et les enregistrer avec <code>M500</code>.</div>
<p>Fermez tous les programmes qui peuvent occuper le port de l'imprimante : Cura, PrusaSlicer, OctoPrint, Pronterface, terminaux série.</p>

<h2>Flasher avec AVRDUDESS</h2>
<ol>
<li>Programmer : <code>wiring</code>. MCU : <code>ATmega2560</code>.</li>
<li>Port : le port COM de l'imprimante (par exemple <code>COM3</code>). Laissez la vitesse par défaut.</li>
<li>Flash : choisissez le fichier .hex, puis cliquez sur <strong>Program!</strong>. Comptez 30 à 60 secondes.</li>
</ol>

<h2>Flasher avec avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Remplacez le port et le nom du fichier par les vôtres. Le protocole <code>wiring</code> choisit tout seul la vitesse du bootloader.</p>

<h2>Premier démarrage</h2>
<ol>
<li>Débranchez le câble USB, éteignez puis rallumez l'imprimante, rebranchez le câble.</li>
<li>Connectez-vous à <strong>250000 bauds</strong> (les firmwares Wanhao utilisaient 115200) et envoyez <code>M115</code> : la réponse indique le nouveau firmware.</li>
<li>Faites le homing de tous les axes, puis un nivellement depuis l'écran ou avec <code>G29</code>, et enregistrez avec <code>M500</code>.</li>
</ol>

<h2>Coupure de courant et capteur de filament</h2>
<ul>
<li>La reprise après coupure est active. Pour la désactiver : <code>M413 S0</code> puis <code>M500</code>.</li>
<li>Le capteur de fin de filament n'est actif par défaut que sur la MK3. Une fois un capteur monté sur un autre modèle : <code>M412 S1</code> puis <code>M500</code>.</li>
</ul>

<h2>Dépannage</h2>
<div class="table"><table><thead><tr><th>Problème</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port déjà utilisé</td><td>Fermez tous les programmes qui utilisent le port de l'imprimante.</td></tr>
<tr><td>Périphérique introuvable</td><td>Installez le pilote USB CH340, essayez un autre câble ou port USB, vérifiez que l'imprimante est allumée.</td></tr>
<tr><td>Caractères illisibles après le flash</td><td>Utilisez 250000 bauds avec ces firmwares, 115200 avec ceux de Wanhao.</td></tr>
<tr><td>Températures ×10 à l'écran (236 pour 23,6 °C)</td><td>L'écran a encore d'anciens fichiers : flashez <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</td></tr>
<tr><td>Homing Failed sur Y</td><td>Voir <a href="#y-direction">standard ou Y inversé</a>.</td></tr>
</tbody></table></div>

<h2>Revenir au firmware Wanhao</h2>
<p>Chaque page modèle donne les firmwares d'origine Wanhao de la carte mère et de l'écran. Ils se flashent de la
même façon ; le firmware de carte mère Wanhao a besoin du firmware d'écran Wanhao de la même génération.</p>
<p>Questions : <a href="{DISCORD}">Discord</a> ou <a href="{REPO}/issues">tickets GitHub</a>.</p>
""")

    if page == "screen":
        if en:
            return ("Wanhao Duplicator 9 touchscreen firmware (DWIN DGUS) – DGUS Reloaded 1.0.3",
                    "How to flash the Wanhao D9 DWIN touchscreen with DGUS Reloaded 1.0.3 from a microSD card, for Marlin 2.1, "
                    "and how to go back to Wanhao's screen firmware.",
                    f"""
<h1>Flashing the Duplicator 9 touchscreen</h1>
<p class="lead">Every D9, MK1 to MK3, has the same DWIN T5 touchscreen (480 × 272). With Marlin 2.1 it runs
DGUS Reloaded, flashed from a microSD card.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Download DWIN_SET.zip (DGUS Reloaded 1.0.3)</a></p>

<h2>Why version 1.0.3</h2>
<p>Since 2023 (<a href="https://github.com/MarlinFirmware/Marlin/pull/25490">Marlin#25490</a>) Marlin sends
temperatures with one decimal and the Z position with two. The screen files must match: with the older 1.0.2,
23.6 °C shows as 236. The original DGUS Reloaded project stopped at 1.0.2; 1.0.3 is published by
<a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">Neo2003</a>, the author of that Marlin change.
This package is that 1.0.3, unchanged, plus the two T5 system files.</p>

<h2>1. Format the microSD card</h2>
<div class="note">FAT32 with an allocation unit of <strong>4096 bytes</strong>. With any other size the screen ignores the card.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 often won't format FAT32; use <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
and set the allocation unit size to 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (check the device with <code>lsblk</code> first).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (check with <code>diskutil list</code>).</li>
</ul>

<h2>2. Copy the files</h2>
<p>Unzip <code>DWIN_SET.zip</code> and copy the whole <code>DWIN_SET</code> folder to the root of the card.</p>

<h2>3. Flash</h2>
<ol>
<li>Switch the printer off and unplug it.</li>
<li>Open the front of the base to reach the back of the screen, where its microSD slot is.</li>
<li>Insert the card and switch on. The screen shows the update within 10 to 30 seconds; wait until it restarts
normally, 1 to 3 minutes in all.</li>
<li>Switch off, remove the card, close the base.</li>
</ol>
<p>Wanhao's <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">video of a D9 screen update</a> shows where the slot is.</p>

<h2>Going back to Wanhao's screen</h2>
<p>Wanhao's screen firmware only works with Wanhao's motherboard firmware. MK1: the screen file of the matching
version on the <a href="{p('mk1')}">MK1 page</a>. MK1 + kit, MK2 and MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Same procedure.</p>
""")
        return ("Firmware écran Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 1.0.3",
                "Comment flasher l'écran tactile DWIN de la Wanhao D9 avec DGUS Reloaded 1.0.3 depuis une carte microSD, pour Marlin 2.1, "
                "et revenir au firmware d'écran Wanhao.",
                f"""
<h1>Flasher l'écran tactile de la Duplicator 9</h1>
<p class="lead">Toutes les D9, de la MK1 à la MK3, ont le même écran tactile DWIN T5 (480 × 272). Avec Marlin 2.1,
il fonctionne avec DGUS Reloaded, flashé depuis une carte microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Télécharger DWIN_SET.zip (DGUS Reloaded 1.0.3)</a></p>

<h2>Pourquoi la version 1.0.3</h2>
<p>Depuis 2023 (<a href="https://github.com/MarlinFirmware/Marlin/pull/25490">Marlin#25490</a>), Marlin envoie les
températures avec une décimale et la position Z avec deux. Les fichiers de l'écran doivent suivre : avec l'ancienne
1.0.2, 23,6 °C s'affiche 236. Le projet DGUS Reloaded d'origine s'est arrêté à la 1.0.2 ; la 1.0.3 est publiée par
<a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">Neo2003</a>, l'auteur de ce changement dans
Marlin. Ce paquet est cette 1.0.3, sans modification, plus les deux fichiers système T5.</p>

<h2>1. Formater la carte microSD</h2>
<div class="note">FAT32 avec une taille d'unité d'allocation de <strong>4096 octets</strong>. Avec toute autre taille, l'écran ignore la carte.</div>
<ul>
<li><strong>Windows</strong> : Windows 11 refuse souvent le FAT32 ; utilisez <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
avec une taille d'unité d'allocation de 4096.</li>
<li><strong>Linux</strong> : <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (vérifiez d'abord le périphérique avec <code>lsblk</code>).</li>
<li><strong>macOS</strong> : <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (vérifiez avec <code>diskutil list</code>).</li>
</ul>

<h2>2. Copier les fichiers</h2>
<p>Décompressez <code>DWIN_SET.zip</code> et copiez tout le dossier <code>DWIN_SET</code> à la racine de la carte.</p>

<h2>3. Flasher</h2>
<ol>
<li>Éteignez l'imprimante et débranchez-la.</li>
<li>Ouvrez l'avant du socle pour accéder à l'arrière de l'écran, où se trouve son lecteur microSD.</li>
<li>Insérez la carte et allumez. L'écran affiche la mise à jour sous 10 à 30 secondes ; attendez qu'il redémarre
normalement, 1 à 3 minutes en tout.</li>
<li>Éteignez, retirez la carte, refermez le socle.</li>
</ol>
<p>La <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">vidéo de mise à jour de l'écran D9</a> montre où se trouve le lecteur.</p>

<h2>Revenir à l'écran Wanhao</h2>
<p>Le firmware d'écran Wanhao ne fonctionne qu'avec le firmware de carte mère Wanhao. MK1 : le fichier écran de
la version correspondante sur la <a href="{p('mk1')}">page MK1</a>. MK1 + kit, MK2 et MK3 :
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Même procédure.</p>
""")
    raise KeyError(page)


# ---------------------------------------------------------------- layout

def render(page, lang):
    title, description, body = content(page, lang)
    u = UI[lang]
    up = "../" if lang == "fr" else ""
    other, other_label, other_code = u["other"]
    nav = "".join(
        f'<a href="{href(n, lang, lang)}"{" aria-current=\"page\"" if n == page else ""}>{u["nav"][n]}</a>'
        for n in PAGES)
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": description,
          "url": url(page, lang), "inLanguage": lang,
          "about": {"@type": "Product", "name": "Wanhao Duplicator 9", "brand": "Wanhao"}}
    if page == "index":
        ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "Wanhao Duplicator 9 firmware",
              "url": SITE, "inLanguage": lang, "description": description}
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{url(page, lang)}">
<link rel="alternate" hreflang="en" href="{url(page, 'en')}">
<link rel="alternate" hreflang="fr" href="{url(page, 'fr')}">
<link rel="alternate" hreflang="x-default" href="{url(page, 'en')}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url(page, lang)}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_GB'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🖨️</text></svg>">
<link rel="stylesheet" href="{up}style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{href('index', lang, lang)}">Wanhao <span>D9</span> firmware</a>
<nav class="main">{nav}</nav>
<a class="lang" href="{href(page, other, lang)}" hreflang="{other}"><img src="{up}img/{other_code.lower()}.svg" alt="{other_code}" width="21" height="14">{other_label}</a>
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
    (DOCS / "fr").mkdir(exist_ok=True)
    for lang in ("en", "fr"):
        out = DOCS / ("fr" if lang == "fr" else "")
        for page in PAGES:
            (out / ("index.html" if page == "index" else page + ".html")).write_text(render(page, lang), encoding="utf-8")
    urls = []
    for page in PAGES:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(page, l)}"/>' for l in ("en", "fr"))
        for lang in ("en", "fr"):
            urls.append(f"<url><loc>{url(page, lang)}</loc>{alts}</url>")
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
