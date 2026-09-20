"""Français : traduction de en.py."""

META = {"name": "Français", "locale": "fr_FR", "dir": "ltr"}

UI = {
    "nav": {"index": "Accueil", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Guide de flash", "screen": "Écran", "sensor": "Capteur filament", "slicer": "Slicer", "quiet": "Silence"},
    "language": "Langue",
    "model": "Modèle",
    "size": "Taille", "volume": "Volume d'impression", "file": "Firmware",
    "footer_src": "Sources et tickets sur GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware sous GNU GPL v3. Les manuels et firmwares Wanhao restent la propriété de Wanhao.",
}

# Libellés du schéma de branchement (img/d9-sensor-plug-<langue>.svg).
SVG = {
    "board": "Carte mère Wanhao D9 (vue de dessus)",
    "plug": "prise capteur",
    "switch": "fin de filament",
    "motion": "mouvement",
    "level": "niveau : filament présent / absent",
    "pulses": "impulsions quand le filament avance",
    "names": "les noms sur votre capteur peuvent varier",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
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
<li><strong>Capteurs de filament</strong> : un détecteur de fin de filament sur D8, actif par défaut sur tous les modèles (sans effet sans détecteur), et le BTT Smart Filament Sensor V2.0, qui détecte aussi les bourrages. Voir <a href="{p('sensor')}">Capteur filament</a>.</li>
<li><strong>La tête revient au centre après un nivellement</strong> : le plateau ne cache plus l'écran.</li>
<li><strong>Une nouvelle interface d'écran en 16 langues</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, avec une page pour régler le capteur de filament.</li>
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

    if page == "mk1u2":
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
<li><strong>À l'écran :</strong> <em>Réglages</em> → <em>Plus</em> → <em>Réinitialiser</em> → ✓.</li>
<li><strong>En USB :</strong> envoyez <code>M502</code> (charge les valeurs par défaut de ce firmware) puis <code>M500</code> (les enregistre).</li>
</ul>
<p>Réglez ensuite de nouveau l'offset Z du capteur (<code>M851 Z…</code> puis <code>M500</code>) et lancez un
nivellement. Vérifiez le résultat avec <code>M503</code>.</p>

<h2>Coupure de courant et capteur de filament</h2>
<ul>
<li>La reprise après coupure est active : l'avancement est enregistré à chaque couche. Pour la désactiver : <code>M413 S0</code> puis <code>M500</code>.</li>
<li>Une impression qui s'arrête dès la chauffe avec <em>power outage</em> : mettez à jour vers la v2.0.4 ou plus récente. Les versions précédentes surveillaient l'entrée de détection de coupure de la carte, qui passe à l'état bas dès que les chauffes démarrent.</li>
<li>La détection de fin de filament est active par défaut sur tous les modèles depuis la v2.0.8, et ne fait rien sans capteur. Après une mise à jour depuis une version précédente, activez-la avec <code>M412 S1</code> puis <code>M500</code>, ou à l'écran dans <em>Réglages</em> → <em>Filament</em> → <em>Capteur de filament</em>. Branchement et BTT Smart Filament Sensor : <a href="{p('sensor')}">Capteur filament</a>.</li>
</ul>

<h2>Dépannage</h2>
<div class="table"><table><thead><tr><th>Problème</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port déjà utilisé</td><td>Fermez tous les programmes qui utilisent le port de l'imprimante.</td></tr>
<tr><td>Périphérique introuvable</td><td>Installez le pilote USB CH340, essayez un autre câble ou port USB, vérifiez que l'imprimante est allumée.</td></tr>
<tr><td>Caractères illisibles après le flash</td><td>Utilisez 250000 bauds avec ces firmwares, 115200 avec ceux de Wanhao.</td></tr>
<tr><td>Températures ×10 à l'écran (236 pour 23,6 °C)</td><td>L'écran a encore d'anciens fichiers : flashez <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>L'écran revient à l'anglais à chaque démarrage, ou sa page <em>Capteur de filament</em> ne fait rien</td><td>Le firmware de la carte mère est plus ancien que la v2.0.9 : mettez-le à jour.</td></tr>
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
        return ("Firmware écran Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 en 16 langues",
                "Comment flasher l'écran tactile DWIN de la Wanhao D9 avec DGUS Reloaded 2.0 depuis une carte microSD : nouvelle "
                "interface en 16 langues, page capteur de filament, pour Marlin 2.1. Et revenir au firmware d'écran Wanhao.",
                f"""
<h1>Flasher l'écran tactile de la Duplicator 9</h1>
<p class="lead">Toutes les D9, de la MK1 à la MK3, ont le même écran tactile DWIN T5 (480 × 272). Avec ces firmwares,
il fonctionne avec DGUS Reloaded 2.0, notre nouvelle interface en 16 langues, flashée depuis une carte microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Télécharger DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Ce qu'apporte DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 langues</strong> : English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Touchez le drapeau à côté du nom de l'imprimante sur
l'accueil pour changer ; l'imprimante retient le choix.</li>
<li><strong>Une page capteur de filament</strong> : <em>Réglages</em> → <em>Filament</em> → <em>Capteur de filament</em>.
Voir <a href="{p('sensor')}#screen">Capteur filament</a>.</li>
<li><strong>Une ligne d'état qui reste</strong> : le dernier message, <em>Ready</em> par exemple, reste affiché au lieu
de disparaître au bout de 30 secondes.</li>
<li><strong>Des jauges de température</strong> pour la buse et le plateau, avec la consigne marquée.</li>
<li>Un nouveau look pour toutes les pages : thème sombre, boutons plus grands, pictogrammes dans les fenêtres.</li>
</ul>
</div><figure><img src="{img}screen/fr-home.png" width="480" height="272" alt="Accueil de DGUS Reloaded 2.0 sur une Wanhao D9 : températures de la buse et du plateau avec jauges, ligne d'état, boutons Imprimer, Température et Réglages">
<figcaption>L'écran d'accueil</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 demande la <strong>v2.0.9 ou plus récente</strong> sur la carte mère. Avec la v2.0.8 ou
avant, la langue revient à l'anglais à chaque démarrage et la page capteur de filament ne fonctionne pas :
<a href="{p('flash')}">flashez la carte mère</a> d'abord.</div>

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

<h2>D'où elle vient</h2>
<p>DGUS Reloaded 2.0 redessine page par page <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS
Reloaded 1.0.3</a> (de Desuuuu, puis Neo2003). Ses sources, le programme qui génère les fichiers de l'écran et les
traductions sont sur <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Un mot faux ou maladroit dans
votre langue ? Dites-le sur <a href="{DISCORD}">Discord</a> ou ouvrez un ticket là-bas.</p>
<p>Pour revenir à DGUS Reloaded 1.0.3, par exemple avec un firmware plus ancien que la v2.0.9, flashez
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> de la même façon.</p>

<h2>Revenir à l'écran Wanhao</h2>
<p>Le firmware d'écran Wanhao ne fonctionne qu'avec le firmware de carte mère Wanhao. MK1 : le fichier écran de
la version correspondante sur la <a href="{p('mk1')}">page MK1</a>. MK1 + kit, MK2 et MK3 :
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Même procédure.</p>
""")

    if page == "sensor":
        return ("Capteurs de filament de la Wanhao Duplicator 9 : fin de filament et branchement du BTT Smart Filament Sensor",
                "Où brancher un capteur de filament sur la carte mère Wanhao D9 (D8, D9, GND, 5V), comment câbler un BTT Smart "
                "Filament Sensor V2.0 et activer la détection de fin de filament et de bourrage avec M412.",
                f"""
<h1>Capteurs de filament</h1>
<p class="lead">Depuis la v2.0.5, ces firmwares lisent deux types de capteur : le détecteur de fin de filament Wanhao,
et le BTT Smart Filament Sensor V2.0, qui remarque aussi quand le filament n'avance plus (bobine emmêlée, bourrage,
filament rongé). <strong>La détection de fin de filament est active par défaut sur tous les modèles</strong>, et la
détection de bourrage est désactivée.</p>

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

<h2 id="screen">À l'écran</h2>
<div class="split"><div>
<p>Avec DGUS Reloaded 2.0 sur l'écran (firmware v2.0.9 ou plus récent) : <em>Réglages</em> → <em>Filament</em> →
<em>Capteur de filament</em>.</p>
<ul>
<li><strong>Fin de filament</strong> active ou désactive toute la détection, comme <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Détection de bourrage</strong> active la détection de bourrage avec la longueur réglée dessous, ou la désactive (<code>L0</code>).</li>
<li><strong>Longueur de bourrage</strong> : − et + la changent de 1 mm ; touchez le nombre pour la saisir.</li>
<li>Le point <strong>Filament</strong> est vert quand le détecteur voit du filament, rouge sinon.</li>
<li>Les changements s'appliquent tout de suite. <strong>Enregistrer</strong> les garde, comme <code>M500</code>. La flèche
de retour sort sans enregistrer : les réglages enregistrés reviennent au prochain démarrage.</li>
</ul>
</div><figure><img src="{img}screen/fr-sensor.png" width="480" height="272" alt="Page capteur de filament de DGUS Reloaded 2.0 : interrupteurs fin de filament et bourrage, longueur de bourrage avec boutons moins et plus, témoin de filament et bouton Enregistrer">
<figcaption>Réglages → Filament → Capteur de filament</figcaption></figure></div>

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
loin et l'écran lance un changement de filament.</p>
<p><strong>Il est actif par défaut sur tous les modèles, depuis la v2.0.8.</strong> Sans rien de branché sur D8, la
résistance de tirage de la carte maintient la broche à 5 V, ce qui se lit « filament présent » : la détection ne se
déclenche alors jamais, elle peut donc rester active avec ou sans capteur. Branchez un détecteur sur D8 et il
fonctionne tout de suite.</p>
<ul>
<li>La détection de bourrage reste désactivée (<code>L0</code>) : ce détecteur ne voit pas le filament avancer.</li>
<li>Pour le désactiver : <code>M412 S0</code> puis <code>M500</code>.</li>
<li>Les réglages enregistrés par une version précédente gardent leur état activé ou désactivé. Pour l'activer :
<code>M412 S1</code> puis <code>M500</code>, ou revenez aux réglages par défaut (<code>M502</code> puis
<code>M500</code>, ce qui efface aussi le décalage Z de la sonde et le maillage).</li>
</ul>

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

    if page == "slicer":
        return ("Profils Cura et OrcaSlicer pour la Wanhao Duplicator 9, et réglage du décalage Z",
                "Profils UltiMaker Cura et OrcaSlicer prêts à l'emploi pour toutes les Wanhao D9, PLA, PETG et ABS, "
                "comment régler le décalage Z de la sonde, lancer un palpage et imprimer un 3DBenchy de test.",
                f"""
<h1>Trancher pour la Duplicator 9</h1>
<p class="lead">Un profil pour chacune des douze imprimantes, pour <strong>UltiMaker Cura</strong> et
<strong>OrcaSlicer</strong>, tous deux gratuits et disponibles sous Windows, macOS et Linux. Chacun reprend le volume
d'impression, les accélérations et la température de plateau maximale de son propre firmware.</p>

<h2>Téléchargement</h2>
{h.slicer}
<p>Ils sont faits pour le firmware de ce site, <a href="{p('flash')}">v2.0.9 ou plus récent</a>.</p>

<h2>Les installer</h2>
<p><strong>OrcaSlicer</strong> : <em>Fichier</em> → <em>Importer</em> → <em>Importer des configurations…</em>, puis
choisissez le fichier <code>.orca_printer</code>. L'imprimante, ses trois qualités (0,12, 0,20 et 0,28 mm) et les
filaments PLA, PETG et ABS apparaissent dans vos préréglages.</p>
<p><strong>Cura</strong> : <em>Aide</em> → <em>Afficher le dossier de configuration</em>, fermez Cura, décompressez le
fichier dans ce dossier, relancez Cura, puis <em>Paramètres</em> → <em>Imprimante</em> → <em>Ajouter une imprimante…</em>
→ <em>Ajouter une imprimante hors réseau</em> → <em>Wanhao</em> → votre modèle. La <em>Wanhao Duplicator 9</em> fournie
avec Cura est un profil plus ancien : 300 uniquement, radeau et supports activés par défaut.</p>

<h2 id="first-print">Avant la première impression : le décalage Z, puis un palpage</h2>
<p>La sonde se déclenche un peu au-dessus du plateau, et le firmware doit savoir de combien. C'est le
<strong>décalage Z</strong>. Trop haut, la première couche n'accroche pas ; trop bas, la buse racle le plateau. Il se
règle une fois, et c'est le réglage qui décide si vos impressions tiennent ou non.</p>
<div class="note">Tout ce qui suit est conservé dans la mémoire de l'imprimante, pas dans le slicer. Cela survit à une
mise à jour du firmware (depuis la v2.0.3).</div>

<h3>1. Chauffez d'abord</h3>
<p>Une buse chaude est plus longue de quelques centièmes de millimètre. Chauffez comme pour une impression : à l'écran,
<em>Température</em> → <em>Préchauffe</em> → <em>PLA</em> (200 °C et 60 °C), et attendez deux minutes.</p>

<h3>2. Faites l'origine des axes</h3>
<p>À l'écran : <em>Réglages</em> → <em>Déplacer</em> → <em>Origine</em>. En USB : <code>G28</code>.</p>

<h3>3. Réglez le décalage Z</h3>
<p><strong>Le plus simple, en imprimant.</strong> Lancez une impression et, pendant la <strong>première couche</strong>,
allez dans <em>Ajuster</em> → <em>Décalage Z</em> à l'écran. Descendez par pas de 0,01 mm pendant que la ligne se trace,
jusqu'à ce qu'elle soit plate et touche sa voisine sans laisser de vide. Trop haut, les lignes restent rondes et
séparées ; trop bas, la surface devient rugueuse et on voit la buse creuser. La valeur est enregistrée toute seule.</p>
<p><strong>À la feuille de papier, sans imprimer.</strong> En USB, à température d'impression :</p>
<pre><code>M851 Z0     ; oublie le décalage actuel
M500
G28         ; refaire l'origine pour qu'il soit pris en compte
M420 S0     ; ignore le maillage pendant la mesure
M211 S0     ; autorise à descendre sous Z0 : les butées logicielles bloquent là
G1 Z0 F300  ; la buse descend au zéro que croit le firmware</code></pre>
<p>Glissez une feuille de papier sous la buse, puis descendez par petits pas avec <code>G91</code> puis
<code>G1 Z-0.05 F60</code>, encore et encore, jusqu'à ce que la feuille commence tout juste à frotter. Lisez la valeur
avec <code>M114</code> : elle est négative, par exemple −1,30. Ensuite :</p>
<pre><code>G90
M851 Z-1.30 ; votre valeur
M500
M211 S1     ; remet les butées logicielles, elles protègent le plateau</code></pre>
<p>À partir de la v2.1.0, les deux lignes <code>M211</code> sont inutiles : le firmware autorise déjà la buse à descendre 3 mm sous le zéro.</p>

<h3>4. Palpez le plateau</h3>
<p>À l'écran : <em>Réglages</em> → <em>Nivellement</em> → <em>Automatique</em> → <em>Palper</em>. L'imprimante mesure
25 points et <strong>enregistre le maillage toute seule</strong> (elle lance <code>G29</code> puis <code>M500</code>).
Comptez quelques minutes. En USB : <code>G29</code> puis <code>M500</code>.</p>
<p>Nos profils ne palpent pas avant chaque impression : ils réactivent le maillage enregistré avec <code>M420 S1</code>,
juste après l'origine. Refaites donc un palpage quand vous déplacez l'imprimante, changez de surface ou de buse, ou
quand la première couche est bonne d'un côté du plateau et pas de l'autre.</p>

<h3>5. Vérifiez</h3>
<p><code>M503</code> affiche ce qui est enregistré : la ligne <code>M851</code> est votre décalage Z, et
<code>M420 S1</code> indique que le maillage est actif. À l'écran, la page <em>Automatique</em> montre les 25 points
mesurés.</p>

<h2>Impressions de test</h2>
<p>Un 3DBenchy déjà tranché pour une <strong>D9 MK2 300</strong>, pour comparer les deux slicers ou vérifier un réglage
sans rien installer :</p>
<ul>
<li>Cura : <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer : <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Environ une heure et demie et 4 m de filament chacun. Pour un autre modèle ou une autre taille, tranchez le
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> vous-même avec votre profil.</p>
<h3>Le test tout-en-un</h3>
<p>Des barres en porte-à-faux, un pont, des tours de stringing, des trous de tolérance et une échelle de finesse dans
une pièce de 65 mm, environ 2 h 30. C'est le <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer
test</a> de <strong>majda107</strong> (CC BY 4.0), tranché pour <strong>toutes les imprimantes</strong> et les deux
slicers, dans les trois matériaux. Les fichiers de la <a href="{REPO}/releases/latest">dernière version</a> s'appellent
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, par exemple
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy imprimé avec le profil OrcaSlicer sur une Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy imprimé avec le profil Cura sur une Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="3DBenchy imprimé en PETG sur une Wanhao D9, par dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Par lequel commencer :</strong> sur une D9 MK2 300 en PLA, le même Benchy a pris <strong>1 h 14 avec
OrcaSlicer</strong> et <strong>1 h 22 avec Cura</strong>, et les parois d'OrcaSlicer sont ressorties un peu plus
nettes. Les deux sont bons ; OrcaSlicer est celui que nous conseillons pour commencer, et ses outils de calibration
(débit, pressure advance, tours de température) servent dès qu'on veut aller plus loin.</p>
<div class="note">La D9 est ouverte : l'ABS demande au minimum une pièce sans courant d'air, et sa température de
plateau est ramenée à ce qu'accepte votre modèle (80 °C sur une MK3 500).</div>

<h2>Ce que contiennent les profils</h2>
<ul>
<li><strong>Couches</strong> de 0,20 mm, <strong>3 parois</strong>, 4 couches pleines dessus et 3 dessous, remplissage
gyroïde à 15 %, une jupe de 2 tours, pas de supports.</li>
<li><strong>Vitesses</strong> : 40 mm/s sur la paroi extérieure, 60 à l'intérieur, 70 pour le remplissage, 20 sur la
première couche, 150 en déplacement. Wanhao donne 70 mm/s comme vitesse d'impression maximale de la D9.</li>
<li><strong>Rétraction</strong> de 1,5 mm à 25 mm/s : toutes les D9 ont un extrudeur MK10 en direct, et le firmware
limite l'extrudeur à 25 mm/s.</li>
<li><strong>Températures</strong> : PLA 210 °C puis 205, plateau 65 puis 60. PETG 240 / 80 puis 235 / 75. ABS
245 / 105 puis 245 / 100.</li>
<li><strong>Une ligne d'amorçage</strong> à 15 mm du bord gauche, au-delà des pinces du plateau : la buse arrive propre
sur la pièce.</li>
<li>À la fin, la buse monte et le plateau vient à l'avant.</li>
</ul>
<p>Tous les réglages et comment les modifier : <a href="{REPO}/tree/main/Slicer">dossier Slicer</a> sur GitHub.</p>
""")

    if page == "quiet":
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
