# Wanhao factory firmware — Duplicator 9 MK1

🇬🇧 [English](#english) | 🇫🇷 [Français](#français)

---

<a name="english"></a>
## 🇬🇧 English

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

- **Directions match**: X inverted, Y, Z and the extruder not inverted, as in `D9_MK1_*.hex`.
- **Steps/mm**: Wanhao used 81 / 81 / 400.5 / 94.3 (80.3 on X and Y in V0.161); these builds use 80 / 80 / 400 / 100. The extruder difference is about 6 %; recalibrate with `M92 E…` if needed.
- **Maximum acceleration**: 500 mm/s² on X and Y from V0.161 on (1000 in V0.15), against 3000 here.
- **PID**: every Wanhao firmware ships 33.41 / 1.47 / 189.27; these builds use a PID tuned on a real machine (20.982 / 0.725 / 151.861). Run `M303` to tune yours.
- **Probe offset** (from Wanhao's source, not the binary): X 30, Y 0 in V0.15 and X 15, Y 0 in V0.164(B); these builds use Klipper's X 27, Y 3, measured on an MK1.
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

Not extractable this way: the probe offsets and maximum temperatures, which Marlin 1.1.4 compiles into code rather than into data. Where a value below comes from Wanhao's source instead, it says so.

---

<a name="français"></a>
## 🇫🇷 Français

Les firmwares de Wanhao pour la MK1 (sonde inductive, nappe grise), conservés ici pour pouvoir remettre une machine exactement dans son état d'usine. Chaque dossier de version contient le firmware de la carte mère (`.hex`, flashé en USB) et, quand Wanhao l'a publié, le firmware d'écran correspondant (flashé depuis une microSD, dans le socle).

Source : la page de téléchargement de Wanhao pour la D9 ([copie archivée](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)) ; chaque fichier renvoie à la copie Dropbox publiée par Wanhao.

### V0.15, V0.161, V0.164(B)

Tableaux identiques à la version anglaise ci-dessus.

### Comparaison avec les firmwares de ce dépôt (`../`)

- **Sens identiques** : X inversé, Y, Z et extrudeur non inversés, comme dans `D9_MK1_*.hex`.
- **Pas/mm** : Wanhao utilisait 81 / 81 / 400,5 / 94,3 (80,3 en X et Y dans la V0.161) ; ces firmwares utilisent 80 / 80 / 400 / 100. L'écart sur l'extrudeur est d'environ 6 % ; recalibrez avec `M92 E…` si besoin.
- **Accélération maximale** : 500 mm/s² en X et Y à partir de la V0.161 (1000 dans la V0.15), contre 3000 ici.
- **PID** : tous les firmwares Wanhao ont 33,41 / 1,47 / 189,27 ; ces firmwares utilisent un PID réglé sur une vraie machine (20,982 / 0,725 / 151,861). Lancez `M303` pour régler le vôtre.
- **Offset de sonde** (tiré des sources Wanhao, pas du binaire) : X 30, Y 0 dans la V0.15 et X 15, Y 0 dans la V0.164(B) ; ces firmwares utilisent les X 27, Y 3 de Klipper, mesurés sur une MK1.
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

Non extractible ainsi : les offsets de sonde et les températures maximales, que Marlin 1.1.4 compile dans le code et non dans les données. Quand une valeur ci-dessous vient plutôt des sources Wanhao, c'est précisé.
