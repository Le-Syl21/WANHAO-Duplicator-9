# Wanhao Duplicator 9 - Slicer profiles / Profils de slicer

<img src="../.github/flags/gb.svg" height="14" alt="GB"> [English Version](#english) | <img src="../.github/flags/fr.svg" height="14" alt="FR"> [Version Française](#français)

<a name="english"></a>
## <img src="../.github/flags/gb.svg" height="14" alt="GB"> English Version

Profiles for **UltiMaker Cura** and **OrcaSlicer**, one per printer: MK1, MK1 + MK2 kit (MK1u2), MK2 and MK3, in 300, 400 and 500. They are made for the firmwares in this repository (v2.0.9 and later).

| Folder | Contents |
|---|---|
| `Cura/D9_<model>_<size>/` | `definitions/` and `extruders/`: the printer, for Cura |
| `OrcaSlicer/D9_<model>_<size>/` | `printer/`, `process/`, `filament/` and `bundle_structure.json`: the files of a `.orca_printer` bundle |
| `build_profiles.py` | Generates all of the above |

### Settings

The same settings in both slicers:

- **Layers:** 0.20 mm by default, first layer 0.20 mm. OrcaSlicer also gets 0.12 mm Fine and 0.28 mm Draft; Cura uses its own quality levels.
- **Walls and infill:** 3 walls (1.2 mm), 4 top layers (0.8 mm), 3 bottom layers (0.6 mm), gyroid infill at 15 %, a 2-line skirt, no support.
- **Speeds:** outer wall 40 mm/s, inner walls 60, infill 70, top 40, first layer 20, travel 150. Wanhao gives 70 mm/s as the D9's top printing speed.
- **Retraction:** 1.5 mm at 25 mm/s. Every D9 has a direct-drive MK10 extruder, and the firmware limits the extruder to 25 mm/s. No Z hop: the Z axis is limited to 5 mm/s.
- **Acceleration:** the firmware's own (800 mm/s² printing and 1000 travel; 500 on the MK1). OrcaSlicer sends them with `M204`, Cura leaves them to the firmware.
- **Filaments (OrcaSlicer):** PLA 210 °C / bed 65 °C on the first layer, then 205 / 60; PETG 240 / 80, then 235 / 75; ABS 245 / 105, then 245 / 100. Wanhao gives the hotend for materials melting at up to 250 °C. A bed temperature above what a model allows is brought down to its limit, so the ABS bed is 80 °C on an MK3 500. ABS also wants an enclosure: the D9 is open. Cura uses its own material library.
- **Fan:** off on the first layer, then 100 % for PLA, 30 to 50 % for PETG and 10 to 30 % for ABS.
- **Priming line:** the start G-code draws two 120 mm lines of filament 15 mm from the left edge, clear of the bed clips (160 mm on a 400, 200 mm on a 500), wipes sideways and lifts. The nozzle arrives at the model clean, without the blob it collects while heating.

### Limits taken from each firmware

| | Build volume (mm) | Max acceleration (mm/s²) | Highest bed temperature |
|---|---|---|---|
| MK1 | 300 × 300 × 400 / 400 × 400 × 400 / 500 × 500 × 500 | 500 | 105 °C |
| MK1u2, MK2 | same | 3000 | 115 °C |
| MK3 300 and 400 | 300 × 300 × 400 / 400 × 400 × 400 | 3000 | 95 °C |
| MK3 500 | 500 × 500 × 500 | 3000 | 80 °C |

The highest bed temperature is the firmware's `BED_MAXTEMP` minus the 10 °C Marlin keeps as a margin; Cura refuses anything above it, and any nozzle temperature above 290 °C.

### Start and end G-code

```gcode
G91
G1 Z10 F300             ; raise, in case a stopped print left the nozzle down
G90
M280 P0 S160            ; BLTouch: clear an alarm and stow the pin (not on the MK1)
G28      ; home all axes (this turns bed levelling off)
M420 S1  ; turn the bed mesh saved from the screen back on
…
G1 X15 Y20 Z0.3 F3000   ; the priming line, clear of the bed clips
G1 Y140 E9.0 F1200
G1 X15.5 F3000
G1 Y20 E9.0 F1200
G1 X22 F6000            ; wipe sideways to snap the string
```

The nozzle is raised 10 mm before homing: a print stopped by hand can leave it resting on the bed, and the probe would then touch the bed and go into alarm (a BLTouch blinks red). The bed starts heating and the nozzle waits at 150 °C, so it does not ooze, while the printer homes; both reach their printing temperature afterwards. **Run a bed levelling from the screen first** (and save it): the profiles use the saved mesh, they do not probe before each print.

At the end the heaters and the fan turn off, the nozzle rises 10 mm and the bed comes to the front. The X, Y and extruder motors turn off; Z keeps its position.

### Installing

**OrcaSlicer:** *File* → *Import* → *Import Configs…*, then choose `D9_<model>_<size>.orca_printer` from the release. The printer, its three qualities and the PLA, PETG and ABS filaments appear under *User presets*. Bundles downloaded before 19 September 2026 only brought the printer into OrcaSlicer 2.4: delete it and import the current one. The D9 is also proposed to OrcaSlicer itself ([OrcaSlicer#15773](https://github.com/OrcaSlicer/OrcaSlicer/pull/15773)), so that it shows up in the printer wizard with nothing to import.

**UltiMaker Cura:**

1. *Help* → *Show Configuration Folder*, then close Cura.
2. Unzip `D9_<model>_<size>_Cura.zip` into that folder: its `definitions` and `extruders` folders merge with Cura's.
3. Start Cura, *Settings* → *Printer* → *Add Printer…* → *Add a non-networked printer* → *Wanhao* → *Wanhao D9 <model> <size>*.

Cura's built-in *Wanhao Duplicator 9* is a different, older profile: 300 only, raft and support on by default, 30 mm/s.

### How they were tested

- **UltiMaker Cura 5.13.0:** started without its window, with the definitions in its configuration folder. All 12 printers were added without a single setting in error, and a 3DBenchy was sliced with the MK2 300.
- **OrcaSlicer 2.4.2:** the 3DBenchy was sliced with all 12 printers, in the three qualities in PLA and in 0.20 mm with PETG, 48 slices without an error. A 3DBenchy was also sliced in PLA, PETG and ABS with both slicers on the MK2 300. For these command-line slices the presets were marked as system presets, because the command line only checks compatibility against system presets. The import through the menu was not tested this way.
- **Printed:** both, on a D9 MK2 300 in PLA. The same Benchy took **1 h 14 with OrcaSlicer** and **1 h 22 with Cura**, and OrcaSlicer's walls came out slightly cleaner, so that is the one the site recommends starting with.

### Changing them

Edit `build_profiles.py`, then:

```sh
python3 Slicer/build_profiles.py dist    # regenerates the folders, and the release files in dist/
```

<a name="français"></a>
## <img src="../.github/flags/fr.svg" height="14" alt="FR"> Version Française

Des profils pour **UltiMaker Cura** et **OrcaSlicer**, un par imprimante : MK1, MK1 + kit MK2 (MK1u2), MK2 et MK3, en 300, 400 et 500. Ils sont faits pour les firmwares de ce dépôt (v2.0.9 et suivantes).

| Dossier | Contenu |
|---|---|
| `Cura/D9_<modèle>_<taille>/` | `definitions/` et `extruders/` : l'imprimante, pour Cura |
| `OrcaSlicer/D9_<modèle>_<taille>/` | `printer/`, `process/`, `filament/` et `bundle_structure.json` : les fichiers d'un bundle `.orca_printer` |
| `build_profiles.py` | Génère tout ce qui précède |

### Réglages

Les mêmes réglages dans les deux slicers :

- **Couches :** 0,20 mm par défaut, première couche 0,20 mm. OrcaSlicer a aussi 0,12 mm Fine et 0,28 mm Draft ; Cura utilise ses propres niveaux de qualité.
- **Parois et remplissage :** 3 parois (1,2 mm), 4 couches pleines dessus (0,8 mm), 3 dessous (0,6 mm), remplissage gyroïde à 15 %, une jupe de 2 tours, pas de supports.
- **Vitesses :** paroi extérieure 40 mm/s, parois intérieures 60, remplissage 70, dessus 40, première couche 20, déplacements 150. Wanhao donne 70 mm/s comme vitesse d'impression maximale de la D9.
- **Rétraction :** 1,5 mm à 25 mm/s. Toutes les D9 ont un extrudeur MK10 en direct, et le firmware limite l'extrudeur à 25 mm/s. Pas de saut en Z : l'axe Z est limité à 5 mm/s.
- **Accélération :** celles du firmware (800 mm/s² en impression et 1000 en déplacement ; 500 sur la MK1). OrcaSlicer les envoie avec `M204`, Cura les laisse au firmware.
- **Filaments (OrcaSlicer) :** PLA 210 °C / plateau 65 °C sur la première couche, puis 205 / 60 ; PETG 240 / 80, puis 235 / 75 ; ABS 245 / 105, puis 245 / 100. Wanhao donne la buse pour des matériaux fondant jusqu'à 250 °C. Une température de plateau supérieure à ce qu'accepte un modèle est ramenée à sa limite : le plateau ABS est donc à 80 °C sur une MK3 500. L'ABS demande aussi un caisson : la D9 est ouverte. Cura utilise sa propre bibliothèque de matériaux.
- **Ventilateur :** coupé sur la première couche, puis 100 % pour le PLA, 30 à 50 % pour le PETG et 10 à 30 % pour l'ABS.
- **Ligne d'amorçage :** le G-code de début trace deux lignes de filament de 120 mm à 15 mm du bord gauche, au-delà des pinces du plateau (160 mm sur une 400, 200 mm sur une 500), essuie la buse sur le côté puis la lève. La buse arrive propre sur la pièce, sans la boule qu'elle accumule pendant la chauffe.

### Limites reprises de chaque firmware

| | Volume d'impression (mm) | Accélération max (mm/s²) | Température de plateau max |
|---|---|---|---|
| MK1 | 300 × 300 × 400 / 400 × 400 × 400 / 500 × 500 × 500 | 500 | 105 °C |
| MK1u2, MK2 | idem | 3000 | 115 °C |
| MK3 300 et 400 | 300 × 300 × 400 / 400 × 400 × 400 | 3000 | 95 °C |
| MK3 500 | 500 × 500 × 500 | 3000 | 80 °C |

La température de plateau max est le `BED_MAXTEMP` du firmware moins les 10 °C de marge que garde Marlin ; Cura refuse toute valeur au-dessus, et toute température de buse au-dessus de 290 °C.

### G-code de début et de fin

```gcode
G91
G1 Z10 F300             ; remonte, si une impression arrêtée a laissé la buse en bas
G90
M280 P0 S160            ; BLTouch : efface une alarme et range la tige (pas sur la MK1)
G28      ; homing de tous les axes (désactive le nivellement)
M420 S1  ; réactive le maillage du plateau enregistré depuis l'écran
…
G1 X15 Y20 Z0.3 F3000   ; ligne d'amorçage, au-delà des pinces du plateau
G1 Y140 E9.0 F1200
G1 X15.5 F3000
G1 Y20 E9.0 F1200
G1 X22 F6000            ; essuyage, casse le fil
```

La buse remonte de 10 mm avant le homing : une impression arrêtée à la main peut la laisser posée sur le plateau, et la sonde toucherait alors le plateau et partirait en alarme (un BLTouch clignote rouge). Le plateau commence à chauffer et la buse attend à 150 °C, pour ne pas couler, pendant le homing ; les deux montent ensuite à leur température d'impression. **Faites d'abord un nivellement depuis l'écran** (et enregistrez-le) : les profils utilisent le maillage enregistré, ils ne palpent pas avant chaque impression.

À la fin, les chauffes et le ventilateur s'arrêtent, la buse monte de 10 mm et le plateau vient à l'avant. Les moteurs X, Y et de l'extrudeur se coupent ; Z garde sa position.

### Installer

**OrcaSlicer :** *Fichier* → *Importer* → *Importer des configurations…*, puis choisissez `D9_<modèle>_<taille>.orca_printer` dans la release. L'imprimante, ses trois qualités et les filaments PLA, PETG et ABS apparaissent dans les *préréglages utilisateur*. Les bundles téléchargés avant le 19 septembre 2026 n'apportaient que l'imprimante dans OrcaSlicer 2.4 : supprimez-la et importez la version actuelle. La D9 est aussi proposée à OrcaSlicer lui-même ([OrcaSlicer#15773](https://github.com/OrcaSlicer/OrcaSlicer/pull/15773)), pour qu'elle apparaisse dans l'assistant de choix d'imprimante sans rien importer.

**UltiMaker Cura :**

1. *Aide* → *Afficher le dossier de configuration*, puis fermez Cura.
2. Décompressez `D9_<modèle>_<taille>_Cura.zip` dans ce dossier : ses dossiers `definitions` et `extruders` se fusionnent avec ceux de Cura.
3. Lancez Cura, *Paramètres* → *Imprimante* → *Ajouter une imprimante…* → *Ajouter une imprimante hors réseau* → *Wanhao* → *Wanhao D9 <modèle> <taille>*.

Le profil *Wanhao Duplicator 9* fourni avec Cura est un autre profil, plus ancien : 300 uniquement, radeau et supports activés par défaut, 30 mm/s.

### Comment ils ont été testés

- **UltiMaker Cura 5.13.0 :** lancé sans fenêtre, avec les définitions dans son dossier de configuration. Les 12 imprimantes ont été ajoutées sans aucun réglage en erreur, et un 3DBenchy a été tranché avec la MK2 300.
- **OrcaSlicer 2.4.2 :** le 3DBenchy a été tranché avec les 12 imprimantes, dans les trois qualités en PLA et en 0,20 mm en PETG, soit 48 tranchages sans erreur. Un 3DBenchy a aussi été tranché en PLA, PETG et ABS avec les deux slicers sur la MK2 300. Pour ces tranchages en ligne de commande, les préréglages ont été marqués comme préréglages système, car la ligne de commande ne vérifie la compatibilité qu'avec des préréglages système. L'import par le menu n'a pas été testé de cette façon.
- **Imprimés :** les deux, sur une D9 MK2 300 en PLA. Le même Benchy a pris **1 h 14 avec OrcaSlicer** et **1 h 22 avec Cura**, et les parois d'OrcaSlicer sont un peu plus nettes : c'est celui que le site conseille pour commencer.

### Les modifier

Modifiez `build_profiles.py`, puis :

```sh
python3 Slicer/build_profiles.py dist    # régénère les dossiers, et les fichiers de release dans dist/
```
