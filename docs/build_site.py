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
# Google Search Console ownership check for the URL-prefix property SITE.
GOOGLE_VERIFICATION = "TqbXre6qrm9jaoj6tFwRRiI2vuQilAZLm6kUJA-etmo"

PAGES = ["index", "mk1", "mk1u2", "mk2", "mk3", "flash", "screen", "sensor", "quiet"]
SIZES = [("300", "300 × 300 × 400 mm"), ("400", "400 × 400 × 400 mm"), ("500", "500 × 500 × 500 mm")]

UI = {
    "en": {
        "nav": {"index": "Home", "mk1": "MK1", "mk1u2": "MK1 + MK2 kit", "mk2": "MK2", "mk3": "MK3",
                "flash": "Flash guide", "screen": "Screen", "sensor": "Filament sensor", "quiet": "Quieter"},
        "other": ("fr", "Version française", "FR"),
        "size": "Size", "volume": "Build volume", "file": "Firmware",
        "footer_src": "Source and issues on GitHub", "footer_chat": "Discord",
        "footer_note": "Firmware under GNU GPL v3. Wanhao's manuals and firmwares remain Wanhao's.",
    },
    "fr": {
        "nav": {"index": "Accueil", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
                "flash": "Guide de flash", "screen": "Écran", "sensor": "Capteur filament", "quiet": "Silence"},
        "other": ("en", "English version", "GB"),
        "size": "Taille", "volume": "Volume d'impression", "file": "Firmware",
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
        rows.append(
            f'<tr><td><strong>D9/{size}</strong></td><td>{volume}</td>'
            f'<td><a class="btn" href="{DL}{std}">{std}</a></td></tr>')
    return (f'<div class="table"><table class="dl"><thead><tr><th>{u["size"]}</th><th>{u["volume"]}</th>'
            f'<th>{u["file"]}</th></tr></thead><tbody>'
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
with the changes proposed there: MK1 probe read the right way round, MK3 Y direction, power-loss recovery,
endstop noise filter.</li>
<li><strong>Wanhao's factory settings</strong>, taken from Wanhao's own firmware and source for each model: steps/mm,
speeds, accelerations, hotend PID, probe offsets and probing margins, homing, thermal limits, jerk and axis directions.</li>
<li><strong>Power-loss recovery</strong>: during an SD print the job is saved on each layer change, and after an outage the screen offers to resume from there.</li>
<li><strong>Filament sensors</strong>: Wanhao's runout switch, on by default on the MK3, and the BTT Smart Filament Sensor V2.0, which also catches jams. See <a href="{p('sensor')}">Filament sensor</a>.</li>
<li><strong>The head returns to the centre after a bed levelling</strong>, so the bed no longer hides the screen.</li>
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
avec les changements proposés là-bas : capteur MK1 lu dans le bon sens, sens Y de la MK3, reprise après coupure,
filtre anti-parasites des fins de course.</li>
<li><strong>Les réglages d'usine de Wanhao</strong>, tirés du firmware et des sources Wanhao de chaque modèle : pas/mm,
vitesses, accélérations, PID de la buse, décalages et marges de palpage, homing, limites thermiques, jerk et sens des axes.</li>
<li><strong>Reprise après coupure de courant</strong> : pendant une impression depuis la carte SD, l'avancement est enregistré à chaque couche, et après une coupure l'écran propose de reprendre à partir de là.</li>
<li><strong>Capteurs de filament</strong> : le détecteur de fin de filament Wanhao, actif par défaut sur la MK3, et le BTT Smart Filament Sensor V2.0, qui détecte aussi les bourrages. Voir <a href="{p('sensor')}">Capteur filament</a>.</li>
<li><strong>La tête revient au centre après un nivellement</strong> : le plateau ne cache plus l'écran.</li>
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
<p>These builds read the inductive probe the right way round (it triggers LOW) and take the settings of Wanhao's
last MK1 firmware, V0.164(B), probe offsets included (X 15, Y 0). The Y motor sits at the back, as Wanhao built it.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Inductive probe and ribbon cable on a Wanhao D9 MK1 print head">
<figcaption>MK1: inductive probe, ribbon cable</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Take the file for your size, then flash the screen with
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
<p>Ces builds lisent le capteur inductif dans le bon sens (il se déclenche à l'état bas) et reprennent les réglages
du dernier firmware MK1 de Wanhao, la V0.164(B), décalages du capteur compris (X 15, Y 0). Le moteur Y est à
l'arrière, comme Wanhao l'a monté.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Capteur inductif et nappe sur la tête d'une Wanhao D9 MK1">
<figcaption>MK1 : capteur inductif, nappe</figcaption></figure></div>

<h2>Téléchargement</h2>
{dl("MK1")}
<p>Prenez le fichier de votre taille, puis flashez l'écran avec
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
<p>Take the file for your size, then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">These builds use the kit firmware's probe offset, Y −10. It is the only line where Wanhao's kit
source differs from the factory MK2's (Y 0): the kit's BLTouch sits further back. If your bed mesh looks shifted front
to back, measure your own offset with the <a href="{REPO}/blob/main/Offset.md">offset guide</a>.</div>

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
<p>Prenez le fichier de votre taille, puis flashez l'écran avec
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Ces builds utilisent le décalage de capteur du firmware du kit, Y −10. C'est la seule ligne où
la source du kit Wanhao diffère de celle de la MK2 d'usine (Y 0) : le BLTouch du kit est placé plus en arrière. Si le
maillage du plateau semble décalé d'avant en arrière, mesurez votre propre décalage avec le
<a href="{REPO}/blob/main/Offset.md">guide des offsets</a>.</div>

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
<p>Take the file for your size. An MK2 whose head was also upgraded to the MK3 should
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
<p>Prenez le fichier de votre taille. Une MK2 dont la tête a aussi été passée en MK3 doit
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
<p>Take the file for your size, then flash the screen with
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
<p>Prenez le fichier de votre taille, puis flashez l'écran avec
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
                    "Step-by-step guide to flash Marlin on a Wanhao D9 over USB with AVRDUDESS or avrdude, fix homing "
                    "problems, and recover with Wanhao's firmware.",
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

<h2>Before flashing</h2>
<div class="note">Send <code>M503</code> and keep the answer. Since v2.0.3 an update keeps the settings stored in the
printer, but updating <strong>to</strong> v2.0.3 starts once from this firmware's defaults (the way settings are stored
changed), and so does coming from Wanhao's firmware. Set your probe Z offset again afterwards with <code>M851 Z…</code>
and <code>M500</code>.</div>
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

<h2 id="reset">Back to this firmware's default settings</h2>
<p>Since v2.0.3, a firmware update <strong>keeps</strong> the settings stored in the printer (probe Z offset, steps/mm,
PID, mesh…). New default values in a release therefore do not replace the ones already stored. Reset once when you
update from v2.0.2 or earlier while keeping values saved by hand, when the printer behaves oddly after trying other
firmwares, or whenever you want to start clean:</p>
<ul>
<li><strong>On the screen:</strong> <em>Settings</em> → <em>More</em> (…) → <em>Reset EEPROM</em> → <em>Yes</em>.</li>
<li><strong>Over USB:</strong> send <code>M502</code> (load this firmware's defaults) then <code>M500</code> (save them).</li>
</ul>
<p>Then set your probe Z offset again (<code>M851 Z…</code> then <code>M500</code>) and run a bed levelling. Check the
result with <code>M503</code>.</p>

<h2>Power loss and filament sensor</h2>
<ul>
<li>Power-loss recovery is on: the job is saved on each layer change. Turn it off with <code>M413 S0</code> then <code>M500</code>.</li>
<li>A print that stops at once with <em>power outage</em> as soon as it heats: update to v2.0.4 or later. Earlier builds watched the board's power-fail input, which reads low as soon as the heaters start.</li>
<li>The filament runout sensor is on by default on the MK3 only. Once a sensor is fitted on another model: <code>M412 S1</code> then <code>M500</code>. Wiring and the BTT Smart Filament Sensor: <a href="{p('sensor')}">Filament sensor</a>.</li>
</ul>

<h2>Troubleshooting</h2>
<div class="table"><table><thead><tr><th>Problem</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port in use</td><td>Close every program using the printer's port.</td></tr>
<tr><td>Device not found</td><td>Install the CH340 USB driver, try another cable or USB port, check the printer is switched on.</td></tr>
<tr><td>Unreadable characters after flashing</td><td>Use 250000 baud with these firmwares, 115200 with Wanhao's.</td></tr>
<tr><td>Temperatures shown ×10 on the screen (236 for 23.6 °C)</td><td>The screen still has old files: flash <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</td></tr>
<tr><td>Homing stops a few millimetres before the switch, then <em>Homing Failed</em></td><td>Electrical noise on the endstop line. These firmwares filter it since v2.0.1: update.</td></tr>
<tr><td>The nozzle hits a bed clip during levelling</td><td>Update to v2.0.2 or later: the first probing column is 10 mm in from the edge, as on Wanhao's firmware.</td></tr>
<tr><td>The bed moves away from the Y switch</td><td>Check you took your model's firmware: the Y motor is at the back on the MK1, MK1 + kit and MK2, at the front on the MK3.</td></tr>
</tbody></table></div>

<h2>Going back to Wanhao's firmware</h2>
<p>Each model page links Wanhao's original motherboard and screen firmwares. Flash them the same way; Wanhao's
motherboard firmware needs Wanhao's screen firmware of the same generation.</p>
<p>Questions: <a href="{DISCORD}">Discord</a> or <a href="{REPO}/issues">GitHub issues</a>.</p>
""")
        return ("Comment flasher le firmware d'une Wanhao Duplicator 9 (D9)",
                "Guide pas à pas pour flasher Marlin sur une Wanhao D9 en USB avec AVRDUDESS ou avrdude, régler les "
                "problèmes de homing, et revenir au firmware Wanhao.",
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

<h2>Avant de flasher</h2>
<div class="note">Envoyez <code>M503</code> et gardez la réponse. Depuis la v2.0.3, une mise à jour conserve les
réglages enregistrés dans l'imprimante, mais le passage <strong>à</strong> la v2.0.3 repart une fois des valeurs par
défaut de ce firmware (la façon de stocker les réglages a changé), tout comme le passage depuis le firmware Wanhao.
Réglez ensuite de nouveau l'offset Z du capteur avec <code>M851 Z…</code> puis <code>M500</code>.</div>
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

<h2 id="reset">Revenir aux réglages par défaut de ce firmware</h2>
<p>Depuis la v2.0.3, une mise à jour <strong>conserve</strong> les réglages enregistrés dans l'imprimante (offset Z du
capteur, pas/mm, PID, maillage…). Les nouvelles valeurs par défaut d'une version ne remplacent donc pas celles déjà
enregistrées. Faites une remise à zéro si vous mettez à jour depuis la v2.0.2 ou plus ancienne en gardant des valeurs
sauvegardées à la main, si l'imprimante se comporte bizarrement après avoir essayé d'autres firmwares, ou chaque fois
que vous voulez repartir de zéro :</p>
<ul>
<li><strong>À l'écran :</strong> <em>Settings</em> → <em>More</em> (…) → <em>Reset EEPROM</em> → <em>Yes</em>.</li>
<li><strong>En USB :</strong> envoyez <code>M502</code> (charge les valeurs par défaut de ce firmware) puis <code>M500</code> (les enregistre).</li>
</ul>
<p>Réglez ensuite de nouveau l'offset Z du capteur (<code>M851 Z…</code> puis <code>M500</code>) et lancez un
nivellement. Vérifiez le résultat avec <code>M503</code>.</p>

<h2>Coupure de courant et capteur de filament</h2>
<ul>
<li>La reprise après coupure est active : l'avancement est enregistré à chaque couche. Pour la désactiver : <code>M413 S0</code> puis <code>M500</code>.</li>
<li>Une impression qui s'arrête dès la chauffe avec <em>power outage</em> : mettez à jour vers la v2.0.4 ou plus récente. Les versions précédentes surveillaient l'entrée de détection de coupure de la carte, qui passe à l'état bas dès que les chauffes démarrent.</li>
<li>Le capteur de fin de filament n'est actif par défaut que sur la MK3. Une fois un capteur monté sur un autre modèle : <code>M412 S1</code> puis <code>M500</code>. Branchement et BTT Smart Filament Sensor : <a href="{p('sensor')}">Capteur filament</a>.</li>
</ul>

<h2>Dépannage</h2>
<div class="table"><table><thead><tr><th>Problème</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port déjà utilisé</td><td>Fermez tous les programmes qui utilisent le port de l'imprimante.</td></tr>
<tr><td>Périphérique introuvable</td><td>Installez le pilote USB CH340, essayez un autre câble ou port USB, vérifiez que l'imprimante est allumée.</td></tr>
<tr><td>Caractères illisibles après le flash</td><td>Utilisez 250000 bauds avec ces firmwares, 115200 avec ceux de Wanhao.</td></tr>
<tr><td>Températures ×10 à l'écran (236 pour 23,6 °C)</td><td>L'écran a encore d'anciens fichiers : flashez <a href="{p('screen')}">DGUS Reloaded 1.0.3</a>.</td></tr>
<tr><td>Le homing s'arrête quelques millimètres avant le fin de course, puis <em>Homing Failed</em></td><td>Parasite sur la ligne du fin de course. Ces firmwares le filtrent depuis la v2.0.1 : mettez à jour.</td></tr>
<tr><td>La buse touche une pince du plateau pendant le nivellement</td><td>Mettez à jour vers la v2.0.2 ou plus récente : la première colonne de palpage est à 10 mm du bord, comme dans le firmware Wanhao.</td></tr>
<tr><td>Le plateau s'éloigne du fin de course Y</td><td>Vérifiez que vous avez pris le firmware de votre modèle : le moteur Y est à l'arrière sur la MK1, la MK1 + kit et la MK2, à l'avant sur la MK3.</td></tr>
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
    if page == "sensor":
        if en:
            return ("Filament sensors on the Wanhao Duplicator 9: runout switch and BTT Smart Filament Sensor wiring",
                    "Where to plug a filament sensor on the Wanhao D9 main board (D8, D9, GND, 5V), how to wire a BTT Smart "
                    "Filament Sensor V2.0 and turn runout and jam detection on with M412.",
                    f"""
<h1>Filament sensors</h1>
<p class="lead">From v2.0.5 these firmwares read two kinds of sensor: Wanhao's runout switch, and the
BTT Smart Filament Sensor V2.0, which also notices when the filament stops moving (tangled spool, jam, stripped
filament). Detection is off until you turn it on, except for the runout switch on the MK3.</p>

<h2>The sensor plug</h2>
<figure><img src="{img}d9-sensor-plug-en.svg" width="760" height="440" alt="Wanhao D9 main board: the 4-pin sensor plug left of POWER-DET, pins D9, D8, GND and 5V, wired to a BTT Smart Filament Sensor V2.0"></figure>
<p>The 4-pin plug to the left of <strong>POWER-DET</strong>, below the endstop plugs, carries <strong>D9, D8, GND and 5V</strong>,
in that order. The pin names come from a wiring diagram by Wanhao that dustovich found and shared on the
<a href="{DISCORD}">Discord</a>; the back of the board prints the same four pins as CTRL, BTN, GND and VCC.</p>
<ul>
<li><strong>D8</strong> is the runout input Wanhao's own firmware reads.</li>
<li><strong>D9</strong> is not used by Wanhao's firmware: these builds read the BTT sensor's motion signal on it.</li>
</ul>
<div class="note">Printer <strong>switched off</strong> while you plug or unplug anything on the board.</div>

<h2>The M412 commands</h2>
<p>Everything is set over USB from a serial terminal (Pronterface, the terminal of your slicer or of OctoPrint,
250000 baud). Parameters can be combined in one command, for example <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Command</th><th>What it does</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Shows the state, for example <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Turns detection on</strong>: the runout switch, and jam detection too if the jam length is not 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Turns all detection off</strong>, switch and jam.</td></tr>
<tr><td><code>M412 D5</code></td><td>Once the switch sees no filament, keeps printing <strong>5 mm</strong> before pausing, to use the filament left between the sensor and the nozzle. Default 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Turns jam detection on</strong> (BTT sensor only): pauses when <strong>10 mm</strong> of filament go through the extruder without the sensor's wheel moving.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Turns jam detection off</strong> and leaves the runout switch as it is. This is the default.</td></tr>
<tr><td><code>M500</code></td><td>Saves the settings. Without it, a change is lost when the printer is switched off.</td></tr>
<tr><td><code>M119</code></td><td>The <em>filament</em> line reads <code>TRIGGERED</code> with filament loaded, <code>open</code> without.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, and <code>L</code> used on its own, come from our change to Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), built into these firmwares. In Marlin without it, <code>L</code>
alone is ignored and <code>L0</code> pauses the print as a jam at once.</p>

<h2>Wanhao's runout switch</h2>
<p>It tells the firmware whether filament is there. When it goes missing, the print pauses after 5 more mm of
filament and the screen starts a filament change. It is on by default on the MK3.</p>
<pre><code>M412 S1
M500</code></pre>
<p>Jam detection stays off (<code>L0</code>), since this switch cannot see filament move. To turn the switch off:
<code>M412 S0</code> then <code>M500</code>.</p>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>This sensor has two outputs, and the firmware reads them differently:</p>
<ul>
<li><strong>The runout switch</strong> (to D8) is a level: 5 V while filament is there, 0 V once it has gone.</li>
<li><strong>The motion output</strong> (to D9) comes from a small wheel the filament turns as it passes. Each few
millimetres of filament, the output flips between 0 V and 5 V. The firmware only watches for those changes: if the
extruder pushes the jam length of filament without a single one, the filament is not following (tangled spool, jam,
stripped filament), and the print pauses. The runout switch cannot see that: during a jam the filament is still there.</li>
</ul>
<h3>Wiring</h3>
<p><strong>5V</strong> to 5V, <strong>GND</strong> to GND, the <strong>runout switch</strong> signal to <strong>D8</strong>
and the <strong>motion</strong> signal to <strong>D9</strong>. The names printed on the sensor's cable may differ.</p>
<h3>Turning it on</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>If prints pause without a reason, raise the jam length: <code>M412 L15</code> then <code>M500</code>. To keep only
the runout switch: <code>M412 L0</code> then <code>M500</code>.</p>
<h3>Checking it</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> with filament loaded: <em>filament: TRIGGERED</em>. If that line changes while you push filament
through by hand instead of when you insert or remove it, the two signal wires are swapped: swap D8 and D9.</li>
</ul>
<div class="note">Jam detection was tested on an MK2 300 without the sensor (a 2 mm jam length triggers, <code>L0</code> never
does), but not yet with the BTT sensor itself. If the switch reads the wrong way round (<em>open</em> with filament
loaded), tell us on <a href="{DISCORD}">Discord</a>.</div>

<h2>Updating from v2.0.5 or v2.0.6</h2>
<p>Those releases had no way to turn jam detection off, so they used a jam length too long to ever be reached: 100 m in
v2.0.5 (too short in fact: about a third of a 1 kg spool, after which a printer left on could pause for nothing) and
10 km in v2.0.6. When the printer starts, v2.0.7 loads those two values as <code>L0</code>. A real length you set
for a BTT sensor, such as <code>L10</code>, is kept. From v2.0.4 or earlier, the 5 mm runout distance is loaded
instead of the 0 those versions saved.</p>
""")
        return ("Capteurs de filament de la Wanhao Duplicator 9 : fin de filament et branchement du BTT Smart Filament Sensor",
                "Où brancher un capteur de filament sur la carte mère Wanhao D9 (D8, D9, GND, 5V), comment câbler un BTT Smart "
                "Filament Sensor V2.0 et activer la détection de fin de filament et de bourrage avec M412.",
                f"""
<h1>Capteurs de filament</h1>
<p class="lead">Depuis la v2.0.5, ces firmwares lisent deux types de capteur : le détecteur de fin de filament Wanhao,
et le BTT Smart Filament Sensor V2.0, qui remarque aussi quand le filament n'avance plus (bobine emmêlée, bourrage,
filament rongé). La détection reste désactivée tant que vous ne l'activez pas, sauf le détecteur de fin de filament
de la MK3.</p>

<h2>La prise capteur</h2>
<figure><img src="{img}d9-sensor-plug-fr.svg" width="760" height="440" alt="Carte mère Wanhao D9 : la prise capteur 4 broches à gauche de POWER-DET, broches D9, D8, GND et 5V, câblée vers un BTT Smart Filament Sensor V2.0"></figure>
<p>La prise 4 broches à gauche de <strong>POWER-DET</strong>, sous les prises des fins de course, porte
<strong>D9, D8, GND et 5V</strong>, dans cet ordre. Les noms des broches viennent d'un schéma de câblage Wanhao que
dustovich a retrouvé et partagé sur le <a href="{DISCORD}">Discord</a> ; le dos de la carte marque les quatre mêmes
broches CTRL, BTN, GND et VCC.</p>
<ul>
<li><strong>D8</strong> est l'entrée de fin de filament que lit le firmware Wanhao.</li>
<li><strong>D9</strong> n'est pas utilisée par le firmware Wanhao : ces firmwares y lisent le signal de mouvement du capteur BTT.</li>
</ul>
<div class="note">Imprimante <strong>éteinte</strong> pour brancher ou débrancher quoi que ce soit sur la carte.</div>

<h2>Les commandes M412</h2>
<p>Tout se règle en USB depuis un terminal série (Pronterface, le terminal de votre slicer ou d'OctoPrint, 250000
bauds). Les paramètres se combinent dans une même commande, par exemple <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Commande</th><th>Ce qu'elle fait</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Affiche l'état, par exemple <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Active la détection</strong> : le détecteur de fin de filament, et aussi la détection de bourrage si la longueur de bourrage n'est pas 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Désactive toute la détection</strong>, fin de filament et bourrage.</td></tr>
<tr><td><code>M412 D5</code></td><td>Quand le détecteur ne voit plus de filament, continue d'imprimer <strong>5 mm</strong> avant la pause, pour utiliser le filament restant entre le capteur et la buse. 5 mm par défaut.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Active la détection de bourrage</strong> (capteur BTT uniquement) : pause quand <strong>10 mm</strong> de filament passent dans l'extrudeur sans que la roue du capteur bouge.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Désactive la détection de bourrage</strong> sans toucher au détecteur de fin de filament. C'est le réglage par défaut.</td></tr>
<tr><td><code>M500</code></td><td>Enregistre les réglages. Sans lui, un changement est perdu à l'extinction.</td></tr>
<tr><td><code>M119</code></td><td>La ligne <em>filament</em> affiche <code>TRIGGERED</code> avec du filament, <code>open</code> sans.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, et <code>L</code> utilisé seul, viennent de notre modification de Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), intégrée à ces firmwares. Dans Marlin sans elle, <code>L</code>
seul est ignoré et <code>L0</code> met tout de suite l'impression en pause pour bourrage.</p>

<h2>Le détecteur de fin de filament Wanhao</h2>
<p>Il indique au firmware si le filament est là. Quand il manque, l'impression se met en pause 5 mm de filament plus
loin et l'écran lance un changement de filament. Il est actif par défaut sur la MK3.</p>
<pre><code>M412 S1
M500</code></pre>
<p>La détection de bourrage reste désactivée (<code>L0</code>), puisque ce détecteur ne voit pas le filament avancer.
Pour le désactiver : <code>M412 S0</code> puis <code>M500</code>.</p>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Ce capteur a deux sorties, que le firmware lit différemment :</p>
<ul>
<li><strong>Le détecteur de fin de filament</strong> (vers D8) donne un niveau : 5 V tant que le filament est là, 0 V
quand il n'y en a plus.</li>
<li><strong>La sortie mouvement</strong> (vers D9) vient d'une petite roue que le filament fait tourner en passant.
Tous les quelques millimètres de filament, la sortie bascule entre 0 V et 5 V. Le firmware ne regarde que ces
changements : si l'extrudeur pousse la longueur de bourrage sans un seul changement, le filament ne suit pas (bobine
emmêlée, bourrage, filament rongé), et l'impression se met en pause. Le détecteur de fin de filament ne peut pas le
voir : pendant un bourrage, le filament est toujours là.</li>
</ul>
<h3>Branchement</h3>
<p><strong>5V</strong> sur 5V, <strong>GND</strong> sur GND, le signal de <strong>fin de filament</strong> sur
<strong>D8</strong> et le signal de <strong>mouvement</strong> sur <strong>D9</strong>. Les noms imprimés sur le câble
du capteur peuvent être différents.</p>
<h3>L'activer</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Si des impressions se mettent en pause sans raison, augmentez la longueur de bourrage : <code>M412 L15</code> puis
<code>M500</code>. Pour ne garder que le détecteur de fin de filament : <code>M412 L0</code> puis <code>M500</code>.</p>
<h3>Le vérifier</h3>
<ul>
<li><code>M412</code> : <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> avec du filament : <em>filament: TRIGGERED</em>. Si cette ligne change quand vous poussez le
filament à la main plutôt que quand vous l'insérez ou le retirez, les deux fils de signal sont inversés : échangez D8
et D9.</li>
</ul>
<div class="note">La détection de bourrage a été testée sur une MK2 300 sans le capteur (une longueur de 2 mm déclenche,
<code>L0</code> jamais), mais pas encore avec le capteur BTT lui-même. Si le détecteur est lu à l'envers
(<em>open</em> avec du filament), dites-le sur <a href="{DISCORD}">Discord</a>.</div>

<h2>Mise à jour depuis la v2.0.5 ou la v2.0.6</h2>
<p>Ces versions ne pouvaient pas désactiver la détection de bourrage, elles utilisaient donc une longueur de bourrage
censée ne jamais être atteinte : 100 m en v2.0.5 (trop court en réalité : environ un tiers de bobine de 1 kg, au-delà
duquel une imprimante restée allumée pouvait se mettre en pause pour rien) et 10 km en v2.0.6. Au démarrage, la
v2.0.7 charge ces deux valeurs comme <code>L0</code>. Une vraie longueur réglée pour un capteur BTT, comme
<code>L10</code>, est conservée. Depuis la v2.0.4 ou avant, la distance de fin de filament de 5 mm est chargée à la
place du 0 enregistré par ces versions.</p>
""")
    if page == "quiet":
        if en:
            return ("Make a Wanhao Duplicator 9 quieter: which fans, and the board fan on NTC thermistors",
                    "Which of the Wanhao D9's fans can be quietened: the hotend fan must stay, the power supply fan already "
                    "regulates itself, and the board fan can be unplugged or run on NTC thermistors.",
                    f"""
<h1>Making the Duplicator 9 quieter</h1>
<p class="lead">At rest, the D9's noise comes from its fans. Here is which one can be quietened, and how.</p>
<div class="note">Work with the printer <strong>unplugged</strong>. Keep every wire away from the 230 V side.</div>

<h2>The fans</h2>
<div class="table"><table class="stack"><thead><tr><th>Fan</th><th>Controlled by</th><th>Can it be quietened?</th></tr></thead><tbody>
<tr><td><strong>Hotend heatsink fan</strong> (print head)</td><td>nothing: 24 V always on</td><td><strong>no</strong>: usually the loudest, but slowing it lets heat climb up the hotend and jams the filament (heat creep)</td></tr>
<tr><td><strong>Part cooling fan</strong> (print head)</td><td>firmware, pin D5 (PWM)</td><td>already variable: set by the slicer and <code>M106</code></td></tr>
<tr><td><strong>Power supply fan</strong></td><td>the power supply itself</td><td>nothing to do: on the unit checked here (Chuanglian A-350FAK-24) it already follows the supply's temperature</td></tr>
<tr><td><strong>Board fan</strong> (control box)</td><td>nothing: 24 V always on</td><td><strong>yes</strong>, see below</td></tr>
</tbody></table></div>
<p>Wanhao's firmware drives no board fan and no hotend fan (<code>CONTROLLER_FAN_PIN</code> and
<code>E0_AUTO_FAN_PIN</code> are both <code>-1</code>), and the board has no spare switched output. That is why these
two run from the always-on "24V OUT" connectors, and why no firmware can slow them down.</p>

<h2>Board fan</h2>
<p>On the unit measured here: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0.10 A max, sleeve bearing</strong>.</p>
<p><strong>Many owners simply unplug it.</strong> The board runs cool: it sits at the bottom of the control box, below
the heated bed, and the bed's heat rises away from it. If you do, keep an eye on your first long prints: an overheating
stepper driver cuts out briefly, which shows up as <strong>shifted layers</strong>, not as an error message.</p>
<h3>Keeping it, but only when the drivers are warm</h3>
<p>Two power NTC thermistors in series make the fan start around 45–50 °C and speed up as the drivers heat:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), glued to a driver heatsink with thermal
adhesive, leads insulated.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V</code></pre>
<ul>
<li>This is a calculation, <strong>not tested on a printer yet</strong>: MF72 tolerance is ±20 %, and a small fan may
start lower than expected. Check the start temperature on the bench (NTCs in a small bag in hot water, with a kitchen
thermometer); add a second 200 Ω if it starts too early, drop the 200 Ω if too late.</li>
<li>The NTCs must be glued to a heatsink: in free air, the fan current (up to about 0.6 W in the NTCs) heats them by
tens of degrees.</li>
<li>The fan never reaches full speed this way (about 75 % at 80 °C), and an NTC that fails goes open: the fan then stops
for good.</li>
</ul>
<p>Sources: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 datasheet</a>.</p>
""")
        return ("Rendre une Wanhao Duplicator 9 plus silencieuse : quels ventilateurs, et le ventilateur de carte sur CTN",
                "Quels ventilateurs de la Wanhao D9 rendre silencieux : celui de la buse doit rester, celui de l'alimentation "
                "se régule déjà, et celui de la carte peut être débranché ou piloté par des thermistances CTN.",
                f"""
<h1>Rendre la Duplicator 9 plus silencieuse</h1>
<p class="lead">Au repos, le bruit de la D9 vient de ses ventilateurs. Voici lequel peut être rendu silencieux, et comment.</p>
<div class="note">Intervenez imprimante <strong>débranchée</strong>. Tenez tous les fils à l'écart de la partie 230 V.</div>

<h2>Les ventilateurs</h2>
<div class="table"><table class="stack"><thead><tr><th>Ventilateur</th><th>Commandé par</th><th>Peut-on le rendre silencieux ?</th></tr></thead><tbody>
<tr><td><strong>Ventilateur du radiateur de buse</strong> (tête)</td><td>rien : 24 V permanent</td><td><strong>non</strong> : c'est en général le plus bruyant, mais le ralentir laisse la chaleur remonter dans la tête et bloque le filament (heat creep)</td></tr>
<tr><td><strong>Ventilateur de pièce</strong> (tête)</td><td>firmware, broche D5 (PWM)</td><td>déjà variable : réglé par le slicer et <code>M106</code></td></tr>
<tr><td><strong>Ventilateur d'alimentation</strong></td><td>l'alimentation elle-même</td><td>rien à faire : sur l'exemplaire vérifié ici (Chuanglian A-350FAK-24), il suit déjà la température de l'alimentation</td></tr>
<tr><td><strong>Ventilateur de carte</strong> (boîtier)</td><td>rien : 24 V permanent</td><td><strong>oui</strong>, voir plus bas</td></tr>
</tbody></table></div>
<p>Le firmware de Wanhao ne pilote ni ventilateur de carte ni ventilateur de buse (<code>CONTROLLER_FAN_PIN</code> et
<code>E0_AUTO_FAN_PIN</code> valent <code>-1</code>), et la carte n'a aucune sortie commutée libre. C'est pour ça que
ces deux-là sont sur les connecteurs « 24V OUT » permanents, et qu'aucun firmware ne peut les ralentir.</p>

<h2>Ventilateur de carte</h2>
<p>Sur l'exemplaire mesuré ici : <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max, palier lisse</strong>.</p>
<p><strong>Beaucoup de propriétaires le débranchent tout simplement.</strong> La carte chauffe peu : elle est en bas du
boîtier, sous le plateau chauffant, et la chaleur du plateau monte au lieu de descendre vers elle. Si vous le faites,
surveillez vos premières longues impressions : un driver moteur en surchauffe coupe brièvement, ce qui se voit par des
<strong>décalages de couches</strong>, pas par un message d'erreur.</p>
<h3>Le garder, mais seulement quand les drivers chauffent</h3>
<p>Deux thermistances CTN de puissance en série font démarrer le ventilateur vers 45-50 °C, puis accélérer à mesure
que les drivers chauffent : <strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), collées sur un
radiateur de driver avec de la colle thermique, pattes isolées.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ventilateur (+)
                                    ventilateur (−) ── 0V</code></pre>
<ul>
<li>C'est un calcul, <strong>pas encore testé sur une imprimante</strong> : les MF72 sont à ±20 %, et un petit
ventilateur peut démarrer plus bas que prévu. Vérifiez la température de démarrage au banc (CTN dans un petit sachet
plongé dans de l'eau chaude, avec un thermomètre de cuisine) ; ajoutez une deuxième 200 Ω s'il démarre trop tôt,
retirez la 200 Ω s'il démarre trop tard.</li>
<li>Les CTN doivent être collées sur un radiateur : à l'air libre, le courant du ventilateur (jusqu'à environ 0,6 W
dans les CTN) les chauffe de plusieurs dizaines de degrés.</li>
<li>Le ventilateur n'atteint jamais sa pleine vitesse de cette façon (environ 75 % à 80 °C), et une CTN qui claque
s'ouvre : le ventilateur s'arrête alors définitivement.</li>
</ul>
<p>Sources : <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">fiche MF72</a>.</p>
""")
    raise KeyError(page)


# ---------------------------------------------------------------- wiring diagram

def sensor_svg(lang):
    """Top view of the board's sensor plug, wired to a BTT Smart Filament Sensor V2.0.

    Pin names come from Wanhao's own wiring diagram (the 4-pin plug left of POWER-DET:
    D9, D8, GND, 5V; the back of the board prints CTRL, BTN, GND, VCC in the same order).
    """
    en = lang == "en"
    t = {
        "board": "Wanhao D9 main board (top view)" if en else "Carte mère Wanhao D9 (vue de dessus)",
        "plug": "sensor plug" if en else "prise capteur",
        "sfs": "BTT Smart Filament Sensor V2.0",
        "switch": "runout switch" if en else "fin de filament",
        "motion": "motion" if en else "mouvement",
        "level": "level: filament in / out" if en else "niveau : filament présent / absent",
        "pulses": "pulses while filament moves" if en else "impulsions quand le filament avance",
        "names": "names on your sensor may differ" if en else "les noms sur votre capteur peuvent varier",
    }
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
    verification = (f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION}">\n'
                    if page == "index" else "")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
{verification}<link rel="canonical" href="{url(page, lang)}">
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
        (DOCS / "img" / f"d9-sensor-plug-{lang}.svg").write_text(sensor_svg(lang), encoding="utf-8")
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
