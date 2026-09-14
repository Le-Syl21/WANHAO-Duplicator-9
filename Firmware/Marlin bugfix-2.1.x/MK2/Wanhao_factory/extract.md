# Wanhao factory firmware — Duplicator 9 MK2

<img src="../../../../.github/flags/gb.svg" height="14" alt="GB"> [English](#english) | <img src="../../../../.github/flags/fr.svg" height="14" alt="FR"> [Français](#français)

---

<a name="english"></a>
## <img src="../../../../.github/flags/gb.svg" height="14" alt="GB"> English

Wanhao's firmware for the factory MK2 (BLTouch), and the MK2 screen firmware ([`DWIN_SET_MK2.zip`](DWIN_SET_MK2.zip), Wanhao's own interface, not DGUS Reloaded). The 500 was rebuilt by Wanhao in July 2019 (V1.1.2.1).

Source: Wanhao's own download page for the D9 ([archived copy](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)); every file links to the Dropbox copy Wanhao published.

### V1.1.2 / V1.1.2.1

| File / Fichier | Model / Modèle | Compiled / Compilé | Marlin | SHA-256 |
|---|---|---|---|---|
| [`D9-300-BLTOUCH-FD_V1.1.2.hex`](https://www.dropbox.com/s/80tje7xi93p5rt5/D9-300-BLTOUCH-FD_V1.1.2.hex) | 300 | Oct 31 2018 | 1.1.4 | `b7cc0276385cb673…` |
| [`D9-400-BLTOUCH-FD_V1.1.2.hex`](https://www.dropbox.com/s/5w0tvfwis8of5iq/D9-400-BLTOUCH-FD_V1.1.2.hex) | 400 | Oct 31 2018 | 1.1.4 | `616a87931cdf335a…` |
| [`D9-500-BLTOUCH-FD_V1.1.2.1.hex`](https://www.dropbox.com/s/gch96z4fcjytyhr/D9-500-BLTOUCH-FD_V1.1.2.1.hex) | 500 | Jul  9 2019 | 1.1.4 | `4f444c7ca65cdbca…` |

| | 300 | 400 | 500 |
|---|---|---|---|
| Steps/mm X Y Z E | 80.2 / 80.2 / 400.3 / 94.3 | 80.2 / 80.2 / 400.3 / 94.3 | 80.2 / 80.2 / 400.3 / 94.3 |
| Max feedrate (mm/s) X Y Z E | 300 / 300 / 5 / 25 | 300 / 300 / 5 / 25 | 300 / 300 / 5 / 25 |
| Max acceleration (mm/s²) X Y Z E | 3000 / 3000 / 100 / 3000 | 3000 / 3000 / 100 / 3000 | 3000 / 3000 / 100 / 3000 |
| Build volume / Volume (mm) | 300 × 300 × 400 | 400 × 400 × 400 | 500 × 500 × 500 |
| Hotend PID / PID buse (Kp Ki Kd) | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 |
| `INVERT_X_DIR` | true | true | true |
| `INVERT_Y_DIR` | **false** | **false** | **false** |
| `INVERT_Z_DIR` | false | false | false |
| `INVERT_E0_DIR` | true | true | true |
| Filament sensor reads / lectures capteur (pin 8) | 3 (`sbrc`) | 3 (`sbrc`) | 3 (`sbrc`) |
| Power-loss reads / lectures coupure (pin 63) | 1 (`sbrc`) | 1 (`sbrc`) | 1 (`sbrc`) |
| BLTouch code | yes / oui | yes / oui | yes / oui |

### Compared with this repository's builds (`../`)

- **These builds take Wanhao's MK2 settings**: steps/mm, maximum feedrate and acceleration, hotend PID and axis directions are the values in the table above. Every Wanhao MK2 firmware, including the 2019 rebuild of the 500, has Y **not inverted**: X and the extruder inverted, Y and Z not.
- **Probe offset** (from Wanhao's source): X 25, Y 0, used as is.
- **Z probe offset**: not stored in Wanhao's firmware (it is set on the screen). These builds start at −1.3; set yours with `M851 Z…` then `M500`.
- **Endstops**: these builds filter endstop noise (`ENDSTOP_NOISE_THRESHOLD 2`). Without it, a glitch on the Y endstop line ended homing a few millimetres short with *Homing Failed* on an MK2 300.
- **The rest of Wanhao's settings** are taken too: probing margins (the first column 10 mm in from the edge, clear of the bed clips), probe clearances and speeds, homing speeds, thermal protection periods, classic jerk, park position and preheat values. Three cannot follow: the hotend maximum stops at 305 °C instead of 315 (thermistor 1's table ends at 320 °C and Marlin 2 keeps a 15 °C margin), the mesh stays 5 × 5 because the DGUS Reloaded screen requires it, and the minimum temperatures stay at 5 °C instead of −5 so that a disconnected thermistor still stops the heaters.
- **Filament sensor**: Wanhao's MK2 firmware reads it (3 tests of pin 8), which is why these builds keep it compiled in, off by default.

## How the values were extracted

These firmwares come without source code, so the values above were read out of the `.hex` files themselves. The script that does it is [`extract_wanhao.py`](../../extract_wanhao.py) (`python3 extract_wanhao.py MK*/Wanhao_factory/**/*.hex`); it needs `avr-objdump`, which PlatformIO installs with the AVR toolchain.

1. **Flash image and strings.** The Intel HEX records are decoded into the flash image. The build date, Marlin version and machine type are plain strings in it (`Compiled: …`, `FIRMWARE_NAME:Marlin 1.1.4`, `MACHINE_TYPE:I3PLUS`).
2. **Motion tables.** Marlin 1.1.4's `MarlinSettings::reset()` declares `DEFAULT_MAX_ACCELERATION` (4 × `uint32`), `DEFAULT_MAX_FEEDRATE` (4 × `float`) and `DEFAULT_AXIS_STEPS_PER_UNIT` (4 × `float`) as constant arrays that the compiler stores side by side. The script looks for four plausible floats (X and Y between 70 and 90, Z between 300 and 1700, E between 80 and 200) and reads the 32 bytes in front of them.
3. **Build volume.** The soft endstop maxima `X_MAX_POS`, `Y_MAX_POS`, `Z_MAX_POS` are three consecutive floats in the initialised data.
4. **Hotend PID.** `Temperature` keeps `Kd ÷ dT`, `Ki × dT` and `Kp` as three consecutive floats, with dT = 0.16384 s for a 16 MHz ATmega2560; multiplying and dividing back gives the configured values.
5. **Axis directions.** The firmware is disassembled (`avr-objdump -D -m avr6 -b ihex`). In `Stepper::set_directions()` every axis writes its DIR pin twice: first `INVERT_x_DIR` for a move towards min, then `!INVERT_x_DIR`. On this board X, Y and Z DIR are PK0, PK3 and PK7, all on PORTK (data address `0x0108`), so the writes are `ori 0x01 / 0x08 / 0x80` (set) and `andi 0xFE / 0xF7 / 0x7F` (clear). Set-then-clear means `INVERT` is `true`, clear-then-set means `false`. E0 DIR is PF5, written with `sbi` / `cbi 0x11,5`.
6. **Filament sensor and power loss.** Pin 8 is PH5 and pin 63 is PK1. The script counts the tests of bit 5 of `PINH` (`0x0100`) and bit 1 of `PINK` (`0x0106`) and records the skip instruction used. In every firmware the pin-63 test sits in an interrupt routine that returns straight away when the pin is high and starts the power-loss handling when it is low.
7. **Validation.** Before being trusted on the firmwares published without source, every one of these extractions was checked against the `Configuration.h` of the four source packages Wanhao did publish (MK1 V0.15, MK1 V0.164(B), MK2 V1.1.2 and the MK2 kit V1.1.31). All of them matched.

8. **Everything else.** For the four packages published with source, every option active in Wanhao's `Configuration.h` and `Configuration_adv.h` was run through the compiler's preprocessor and compared with the effective value in these builds: probing margins, probe and homing speeds, thermal limits and protection periods, jerk, park position, preheat values. For the MK3, published without source, the floating-point constants loaded by its code were compared with those of the MK2 firmwares of the same size: the only setting that differs is the bed's maximum temperature.

Not extractable from the binary tables above: the probe offsets, which Marlin 1.1.4 compiles into code rather than into data. Where a value below comes from Wanhao's source instead, it says so.

---

<a name="français"></a>
## <img src="../../../../.github/flags/fr.svg" height="14" alt="FR"> Français

Le firmware de Wanhao pour la MK2 d'usine (BLTouch), et le firmware d'écran MK2 ([`DWIN_SET_MK2.zip`](DWIN_SET_MK2.zip), l'interface de Wanhao, pas DGUS Reloaded). Wanhao a recompilé la 500 en juillet 2019 (V1.1.2.1).

Source : la page de téléchargement de Wanhao pour la D9 ([copie archivée](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)) ; chaque fichier renvoie à la copie Dropbox publiée par Wanhao.

### V1.1.2 / V1.1.2.1

Tableaux identiques à la version anglaise ci-dessus.

### Comparaison avec les firmwares de ce dépôt (`../`)

- **Ces firmwares reprennent les réglages MK2 de Wanhao** : pas/mm, vitesse et accélération maximales, PID de la buse et sens des axes sont les valeurs du tableau ci-dessus. Tous les firmwares MK2 de Wanhao, y compris la 500 recompilée en 2019, ont Y **non inversé** : X et extrudeur inversés, Y et Z non.
- **Offset de sonde** (tiré des sources Wanhao) : X 25, Y 0, repris tel quel.
- **Offset Z de la sonde** : absent du firmware Wanhao (il se règle à l'écran). Ces firmwares partent de −1,3 ; réglez le vôtre avec `M851 Z…` puis `M500`.
- **Fins de course** : ces firmwares filtrent les parasites (`ENDSTOP_NOISE_THRESHOLD 2`). Sans ce filtre, un parasite sur la ligne du fin de course Y arrêtait le homing quelques millimètres trop tôt avec *Homing Failed* sur une MK2 300.
- **Le reste des réglages Wanhao** est repris aussi : marges de palpage (première colonne à 10 mm du bord, à l'écart des pinces du plateau), hauteurs et vitesses de palpage, vitesses de homing, délais de protection thermique, jerk classique, position de parking et préchauffes. Trois ne peuvent pas suivre : la température maximale de la buse s'arrête à 305 °C au lieu de 315 (le tableau de la thermistance 1 s'arrête à 320 °C et Marlin 2 garde 15 °C de marge), le maillage reste en 5 × 5 parce que l'écran DGUS Reloaded l'exige, et les températures minimales restent à 5 °C au lieu de −5 pour qu'une thermistance débranchée coupe toujours la chauffe.
- **Capteur de filament** : le firmware MK2 de Wanhao le lit (3 tests de la broche 8), c'est pourquoi ces firmwares le gardent compilé, désactivé par défaut.

## Comment ces valeurs ont été extraites

Ces firmwares sont publiés sans code source : les valeurs ci-dessus ont été lues directement dans les fichiers `.hex`. Le script qui le fait est [`extract_wanhao.py`](../../extract_wanhao.py) (`python3 extract_wanhao.py MK*/Wanhao_factory/**/*.hex`) ; il a besoin d'`avr-objdump`, que PlatformIO installe avec la chaîne AVR.

1. **Image flash et chaînes.** Les enregistrements Intel HEX sont décodés en image de la flash. La date de compilation, la version de Marlin et le type de machine y sont en clair (`Compiled: …`, `FIRMWARE_NAME:Marlin 1.1.4`, `MACHINE_TYPE:I3PLUS`).
2. **Tables de mouvement.** Dans Marlin 1.1.4, `MarlinSettings::reset()` déclare `DEFAULT_MAX_ACCELERATION` (4 × `uint32`), `DEFAULT_MAX_FEEDRATE` (4 × `float`) et `DEFAULT_AXIS_STEPS_PER_UNIT` (4 × `float`) comme tableaux constants, rangés côte à côte par le compilateur. Le script cherche quatre flottants plausibles (X et Y entre 70 et 90, Z entre 300 et 1700, E entre 80 et 200) et lit les 32 octets qui les précèdent.
3. **Volume d'impression.** Les butées logicielles `X_MAX_POS`, `Y_MAX_POS`, `Z_MAX_POS` sont trois flottants consécutifs dans les données initialisées.
4. **PID de la buse.** `Temperature` conserve `Kd ÷ dT`, `Ki × dT` et `Kp` en trois flottants consécutifs, avec dT = 0,16384 s pour un ATmega2560 à 16 MHz ; en multipliant et divisant à l'inverse, on retrouve les valeurs configurées.
5. **Sens des axes.** Le firmware est désassemblé (`avr-objdump -D -m avr6 -b ihex`). Dans `Stepper::set_directions()`, chaque axe écrit sa broche DIR deux fois : d'abord `INVERT_x_DIR` pour un déplacement vers le minimum, puis `!INVERT_x_DIR`. Sur cette carte, les DIR de X, Y et Z sont PK0, PK3 et PK7, toutes sur PORTK (adresse `0x0108`) : les écritures sont `ori 0x01 / 0x08 / 0x80` (mise à 1) et `andi 0xFE / 0xF7 / 0x7F` (mise à 0). Mise à 1 puis à 0 signifie `INVERT` à `true`, l'inverse `false`. La DIR de E0 est PF5, écrite par `sbi` / `cbi 0x11,5`.
6. **Capteur de filament et coupure.** La broche 8 est PH5 et la broche 63 est PK1. Le script compte les tests du bit 5 de `PINH` (`0x0100`) et du bit 1 de `PINK` (`0x0106`) et relève l'instruction de saut utilisée. Dans tous les firmwares, le test de la broche 63 se trouve dans une routine d'interruption qui ressort aussitôt quand la broche est à l'état haut, et lance la gestion de coupure quand elle est à l'état bas.
7. **Validation.** Avant de s'y fier sur les firmwares publiés sans source, chacune de ces extractions a été vérifiée contre le `Configuration.h` des quatre paquets de sources que Wanhao a publiés (MK1 V0.15, MK1 V0.164(B), MK2 V1.1.2 et le kit MK2 V1.1.31). Toutes concordaient.

8. **Tout le reste.** Pour les quatre paquets publiés avec leurs sources, chaque option active du `Configuration.h` et du `Configuration_adv.h` de Wanhao est passée au préprocesseur du compilateur et comparée à la valeur effective de ces firmwares : marges de palpage, vitesses de palpage et de homing, limites et délais de protection thermique, jerk, position de parking, préchauffes. Pour la MK3, publiée sans source, les constantes à virgule flottante chargées par son code sont comparées à celles des firmwares MK2 de même taille : le seul réglage qui diffère est la température maximale du plateau.

Non extractibles des tables ci-dessus : les offsets de sonde, que Marlin 1.1.4 compile dans le code et non dans les données. Quand une valeur ci-dessous vient plutôt des sources Wanhao, c'est précisé.
