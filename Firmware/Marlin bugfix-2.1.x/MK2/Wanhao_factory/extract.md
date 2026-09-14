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

- **Y direction**: every Wanhao MK2 firmware, including the 2019 rebuild of the 500, has Y **not inverted**. That is `D9_MK2_300.hex`, `D9_MK2_400.hex` and `D9_MK2_500.hex`. Some owners report an MK2 whose Y runs the other way, for instance a machine whose Y motor sits at the front, as on the MK3: `D9_MK2_*_Y-inverted.hex` covers them. See *Which firmware* in [`../../../README.md`](../../../README.md).
- **Other directions match**: X and the extruder inverted, Z not.
- **Steps/mm**: 80.2 / 80.2 / 400.3 / 94.3 at Wanhao, 80 / 80 / 400 / 100 here (extruder about 6 % apart).
- **PID**: 33.41 / 1.47 / 189.27 at Wanhao, a machine-tuned PID here.
- **Probe offset** (from Wanhao's source): X 25, Y 0. These builds use X 25, Y −5, validated on a real MK2 300.
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

Not extractable this way: the probe offsets and maximum temperatures, which Marlin 1.1.4 compiles into code rather than into data. Where a value below comes from Wanhao's source instead, it says so.

---

<a name="français"></a>
## <img src="../../../../.github/flags/fr.svg" height="14" alt="FR"> Français

Le firmware de Wanhao pour la MK2 d'usine (BLTouch), et le firmware d'écran MK2 ([`DWIN_SET_MK2.zip`](DWIN_SET_MK2.zip), l'interface de Wanhao, pas DGUS Reloaded). Wanhao a recompilé la 500 en juillet 2019 (V1.1.2.1).

Source : la page de téléchargement de Wanhao pour la D9 ([copie archivée](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)) ; chaque fichier renvoie à la copie Dropbox publiée par Wanhao.

### V1.1.2 / V1.1.2.1

Tableaux identiques à la version anglaise ci-dessus.

### Comparaison avec les firmwares de ce dépôt (`../`)

- **Sens de Y** : tous les firmwares MK2 de Wanhao, y compris la 500 recompilée en 2019, ont Y **non inversé**. Ce sont `D9_MK2_300.hex`, `D9_MK2_400.hex` et `D9_MK2_500.hex`. Des propriétaires signalent des MK2 dont Y tourne dans l'autre sens, par exemple une machine dont le moteur Y est à l'avant, comme sur la MK3 : `D9_MK2_*_Y-inverted.hex` les couvre. Voir *Quel firmware* dans [`../../../README.md`](../../../README.md).
- **Autres sens identiques** : X et extrudeur inversés, Z non.
- **Pas/mm** : 80,2 / 80,2 / 400,3 / 94,3 chez Wanhao, 80 / 80 / 400 / 100 ici (environ 6 % d'écart sur l'extrudeur).
- **PID** : 33,41 / 1,47 / 189,27 chez Wanhao, un PID réglé sur machine ici.
- **Offset de sonde** (tiré des sources Wanhao) : X 25, Y 0. Ces firmwares utilisent X 25, Y −5, validés sur une vraie MK2 300.
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

Non extractible ainsi : les offsets de sonde et les températures maximales, que Marlin 1.1.4 compile dans le code et non dans les données. Quand une valeur ci-dessous vient plutôt des sources Wanhao, c'est précisé.
