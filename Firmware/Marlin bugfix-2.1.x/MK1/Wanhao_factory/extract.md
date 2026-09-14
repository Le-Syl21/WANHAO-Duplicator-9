# Wanhao factory firmware — Duplicator 9 MK1

<img src="../../../../.github/flags/gb.svg" height="14" alt="GB"> [English](#english) | <img src="../../../../.github/flags/fr.svg" height="14" alt="FR"> [Français](#français)

---

<a name="english"></a>
## <img src="../../../../.github/flags/gb.svg" height="14" alt="GB"> English

Wanhao's own firmwares for the MK1 (inductive probe, grey ribbon cable), kept here so a machine can be put back exactly as it left the factory. Each version folder holds the motherboard firmware (`.hex`, flashed over USB) and, where Wanhao published it, the matching screen firmware (flashed from a microSD card inside the base).

Source: Wanhao's own download page for the D9 ([archived copy](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)); every file links to the Dropbox copy Wanhao published.

### V0.15, V0.161, V0.164(B)

| File / Fichier | Model / Modèle | Compiled / Compilé | Marlin | SHA-256 |
|---|---|---|---|---|
| [`V0.15/D9-V0.15.hex`](https://www.dropbox.com/s/r2r6x5dv6y4iaj6/D9-V0.15.hex) | V0.15 · 300 | Apr 16 2018 | 1.1.4 | `222c0519eb873bd7…` |
| [`V0.161/D9-300-0.161.hex`](https://www.dropbox.com/s/rxv9gfh4tzitx6b/D9-300-0.161.hex) | V0.161 · 300 | Jun 12 2018 | 1.1.4 | `3a3091ffd5ac5f27…` |
| [`V0.164B/D9_300_V0.164(B).hex`](https://www.dropbox.com/s/fi5ctgbnmowylcr/D9%20300%20V0.164%28B%29.hex) | V0.164(B) · 300 | Jul 26 2018 | 1.1.4 | `6d4a425c55e66a4d…` |
| [`V0.164B/D9_400_V0.164(B).hex`](https://www.dropbox.com/s/l9433k8ls8b8bwr/D9%20400%20V0.164%28B%29.hex) | V0.164(B) · 400 | Jul 26 2018 | 1.1.4 | `7c3cbcbde8a7dfce…` |
| [`V0.164B/D9_500_V0.164(B).hex`](https://www.dropbox.com/s/0w6j2gyntm8gc5u/D9%20500%20V0.164%28B%29.hex) | V0.164(B) · 500 | Jul 26 2018 | 1.1.4 | `d47938009b33cf59…` |

| | V0.15 · 300 | V0.161 · 300 | V0.164(B) · 300 | V0.164(B) · 400 | V0.164(B) · 500 |
|---|---|---|---|---|---|
| Steps/mm X Y Z E | 81 / 81 / 400.5 / 94.3 | 80.3 / 80.3 / 400.5 / 94.3 | 81 / 81 / 400.5 / 94.3 | 81 / 81 / 400.5 / 94.3 | 81 / 81 / 400.5 / 94.3 |
| Max feedrate (mm/s) X Y Z E | 500 / 500 / 5 / 25 | 300 / 300 / 5 / 25 | 300 / 300 / 5 / 25 | 300 / 300 / 5 / 25 | 300 / 300 / 5 / 25 |
| Max acceleration (mm/s²) X Y Z E | 1000 / 1000 / 100 / 500 | 500 / 500 / 100 / 500 | 500 / 500 / 100 / 500 | 500 / 500 / 100 / 500 | 500 / 500 / 100 / 500 |
| Build volume / Volume (mm) | 300 × 300 × 400 | 300 × 300 × 400 | 300 × 300 × 400 | 400 × 400 × 400 | 500 × 500 × 500 |
| Hotend PID / PID buse (Kp Ki Kd) | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 | 33.41 / 1.47 / 189.27 |
| `INVERT_X_DIR` | true | true | true | true | true |
| `INVERT_Y_DIR` | **false** | **false** | **false** | **false** | **false** |
| `INVERT_Z_DIR` | false | false | false | false | false |
| `INVERT_E0_DIR` | false | false | false | false | false |
| Filament sensor reads / lectures capteur (pin 8) | none / aucune | none / aucune | none / aucune | none / aucune | none / aucune |
| Power-loss reads / lectures coupure (pin 63) | 1 (`sbrc`) | 1 (`sbrc`) | 1 (`sbrc`) | 1 (`sbrc`) | 1 (`sbrc`) |
| BLTouch code | no / non | no / non | no / non | no / non | no / non |

### Compared with this repository's builds (`../`)

- **These builds take V0.164(B)'s settings**, Wanhao's last MK1 firmware: steps/mm 81 / 81 / 400.5 / 94.3, maximum feedrate 300 / 300 / 5 / 25 mm/s, maximum acceleration 500 / 500 / 100 / 500 mm/s² (printing and travel acceleration 500, as in its source), hotend PID 33.41 / 1.47 / 189.27, and the same axis directions: X inverted, Y, Z and the extruder not.
- **Probe offset** (from Wanhao's source, not the binary): X 30, Y 0 in V0.15 and X 15, Y 0 in V0.164(B). These builds use V0.164(B)'s X 15, Y 0.
- **Z probe offset**: not stored in Wanhao's firmware (it is set on the screen). These builds start at −1.4; set yours with `M851 Z…` then `M500`.
- **Endstops**: these builds filter endstop noise (`ENDSTOP_NOISE_THRESHOLD 2`). Without it, a glitch on the Y endstop line ended homing a few millimetres short with *Homing Failed* on an MK2 300.
- **The rest of Wanhao's settings** are taken too: probing margins (the first column 10 mm in from the edge, clear of the bed clips), probe clearances and speeds, homing speeds, thermal protection periods, classic jerk, park position and preheat values. Three cannot follow: the hotend maximum stops at 305 °C instead of 315 (thermistor 1's table ends at 320 °C and Marlin 2 keeps a 15 °C margin), the mesh stays 5 × 5 because the DGUS Reloaded screen requires it, and the minimum temperatures stay at 5 °C instead of −5 so that a disconnected thermistor still stops the heaters.
- **Screen files**: Wanhao's MK1 screen firmware, not DGUS Reloaded; it only works with Wanhao's motherboard firmware.

### Notes from Wanhao

- **V0.15**: levelling increased from 6 to 24 points.
- **V0.161**: adds a calibration step restoring Z zero during levelling. [`How_to_flash_D9-300_V0.161.pdf`](V0.161/How_to_flash_D9-300_V0.161.pdf) is Wanhao's flashing procedure for it.
- **V0.162**: linear levelling replaced by bilinear mesh levelling, reference point moved from the centre to the top left (screen unchanged, V0.161).
- **V0.164(B)**: better Z offset after a paused print. For this version, D9/400 printers delivered until 3 August 2018 must have both Y gantry supports moved 1 cm to the right: 19 cm between the left support and the left side of the printer.
- Wanhao warned that a wrong firmware flash can brick the board or the screen.

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

Les firmwares de Wanhao pour la MK1 (sonde inductive, nappe grise), conservés ici pour pouvoir remettre une machine exactement dans son état d'usine. Chaque dossier de version contient le firmware de la carte mère (`.hex`, flashé en USB) et, quand Wanhao l'a publié, le firmware d'écran correspondant (flashé depuis une microSD, dans le socle).

Source : la page de téléchargement de Wanhao pour la D9 ([copie archivée](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)) ; chaque fichier renvoie à la copie Dropbox publiée par Wanhao.

### V0.15, V0.161, V0.164(B)

Tableaux identiques à la version anglaise ci-dessus.

### Comparaison avec les firmwares de ce dépôt (`../`)

- **Ces firmwares reprennent les réglages de la V0.164(B)**, le dernier firmware MK1 de Wanhao : pas/mm 81 / 81 / 400,5 / 94,3, vitesse maximale 300 / 300 / 5 / 25 mm/s, accélération maximale 500 / 500 / 100 / 500 mm/s² (accélération d'impression et de déplacement 500, comme dans sa source), PID de la buse 33,41 / 1,47 / 189,27, et les mêmes sens d'axes : X inversé, Y, Z et extrudeur non inversés.
- **Offset de sonde** (tiré des sources Wanhao, pas du binaire) : X 30, Y 0 dans la V0.15 et X 15, Y 0 dans la V0.164(B). Ces firmwares utilisent les X 15, Y 0 de la V0.164(B).
- **Offset Z de la sonde** : absent du firmware Wanhao (il se règle à l'écran). Ces firmwares partent de −1,4 ; réglez le vôtre avec `M851 Z…` puis `M500`.
- **Fins de course** : ces firmwares filtrent les parasites (`ENDSTOP_NOISE_THRESHOLD 2`). Sans ce filtre, un parasite sur la ligne du fin de course Y arrêtait le homing quelques millimètres trop tôt avec *Homing Failed* sur une MK2 300.
- **Le reste des réglages Wanhao** est repris aussi : marges de palpage (première colonne à 10 mm du bord, à l'écart des pinces du plateau), hauteurs et vitesses de palpage, vitesses de homing, délais de protection thermique, jerk classique, position de parking et préchauffes. Trois ne peuvent pas suivre : la température maximale de la buse s'arrête à 305 °C au lieu de 315 (le tableau de la thermistance 1 s'arrête à 320 °C et Marlin 2 garde 15 °C de marge), le maillage reste en 5 × 5 parce que l'écran DGUS Reloaded l'exige, et les températures minimales restent à 5 °C au lieu de −5 pour qu'une thermistance débranchée coupe toujours la chauffe.
- **Fichiers d'écran** : le firmware d'écran MK1 de Wanhao, pas DGUS Reloaded ; il ne fonctionne qu'avec le firmware carte de Wanhao.

### Notes de Wanhao

- **V0.15** : nivellement porté de 6 à 24 points.
- **V0.161** : ajoute une étape de calibration qui rétablit le zéro Z pendant le nivellement. [`How_to_flash_D9-300_V0.161.pdf`](V0.161/How_to_flash_D9-300_V0.161.pdf) est la procédure de flash de Wanhao pour cette version.
- **V0.162** : nivellement linéaire remplacé par un maillage bilinéaire, point de référence déplacé du centre vers le coin supérieur gauche (écran inchangé, V0.161).
- **V0.164(B)** : meilleur offset Z après une pause. Pour cette version, les D9/400 livrées jusqu'au 3 août 2018 doivent avoir les deux supports Y décalés de 1 cm vers la droite : 19 cm entre le support gauche et le côté gauche de l'imprimante.
- Wanhao prévenait qu'un mauvais flash peut rendre la carte ou l'écran inutilisable.

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
