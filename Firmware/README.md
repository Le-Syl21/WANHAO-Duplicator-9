# Wanhao Duplicator 9 - Firmware Flash Guide / Guide de Flash du Firmware

<img src="../.github/flags/gb.svg" height="14" alt="GB"> [English Version](#english) | <img src="../.github/flags/fr.svg" height="14" alt="FR"> [Version Française](#français)

<a name="english"></a>
## <img src="../.github/flags/gb.svg" height="14" alt="GB"> English Version

### Prerequisites

**Required Tools:**
- USB cable (printer to computer)
- **Flash Tool** (choose one):
  - **AVRDUDESS** (GUI for Windows) - [Download](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommended for beginners**
  - **avrdude** (command line, all platforms) - [Download](https://github.com/avrdudes/avrdude)
- Firmware file (.hex) for your specific model

### What's in these builds

Built from Marlin `bugfix-2.1.x` (September 2026) with the Duplicator 9 configurations published in [Marlin Configurations](https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209). The first five points are changes not merged there yet.

- **Wanhao's factory settings**, taken from Wanhao's firmware and source for each model: steps/mm, speeds and accelerations, hotend PID, probe offsets and probing margins, homing speeds, thermal limits and protection, jerk, park position, preheat values and axis directions. Each model's `Wanhao_factory/extract.md` lists them, with the three that Marlin 2 cannot follow.
- **MK1:** the inductive probe is now read the right way round (it triggers LOW).
- **MK3:** the Y axis is inverted, as in Wanhao's own MK3 firmware: the MK3 has its Y motor on the touchscreen side.
- **Endstop noise filter** (`ENDSTOP_NOISE_THRESHOLD 2`): without it, a glitch on the endstop line could stop homing a few millimetres short with *Homing Failed*.
- **Power-loss recovery** is on: after an outage during an SD print, the screen offers to resume. Turn it off with `M413 S0` then `M500`.
- **Filament runout sensor** support is built in, off by default except on the MK3. Without a sensor nothing happens; once you fit one, enable it with `M412 S1` then `M500`.
- **Wanhao's factory firmwares** are kept in `Wanhao_factory/` inside each model folder, so a machine can be put back as it left the factory. Each has an `extract.md` listing the settings read out of Wanhao's binaries and how they were read.
- **`M503`** is available to print every setting.
- **The screen needs DGUS Reloaded 1.0.3** (`LCD/DWIN_SET.zip`). With the older 1.0.2 files, temperatures show without their decimal point (23.6 °C appears as 236).

### Step 1: Prepare for Flashing

1. **Choose the correct firmware** for your model:
   - `D9_MK1_xxx.hex` - For MK1 with inductive probe
   - `D9_MK2_xxx.hex` - For MK2 factory (BLTouch)
   - `D9_MK1u2_xxx.hex` - For MK1→MK2 upgrade kit
   - `D9_MK3_xxx.hex` - For MK3 with BLTouch + filament sensor

2. **⚠️ IMPORTANT:** Close ALL programs using the COM port (serial terminals, slicers, Cura, OctoPrint, Pronterface, etc.)

3. **⚠️ Note your settings first:** the first boot of a new build resets the EEPROM. Send `M851` (probe Z offset), `M92` (steps/mm) and `M301` (hotend PID) and keep the answers, so you can set them back and save them with `M500`.

### Step 2: Flash Firmware

#### Option A: AVRDUDESS (GUI - Recommended)

1. **Open AVRDUDESS**
2. **Configure settings:**
   - **Programmer:** `wiring`
   - **MCU:** `atmega2560`
   - **Port:** Select your COM port (e.g., `COM3`)
   - **Baud rate:** Leave default (auto-configured)
   - **Flash file:** Browse and select your `.hex` file
3. **Click "Program!"**
4. **Wait** for completion (usually 30-60 seconds)

#### Option B: Command Line (avrdude)

Replace `COMX` with your actual COM port and `firmware.hex` with your firmware file:

**Windows:**
```cmd
avrdude -v -p atmega2560 -c wiring -P COMX -D -U flash:w:firmware.hex:i
```

**Linux/macOS:**
```bash
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:firmware.hex:i
```

**Note:** The `-c wiring` protocol automatically configures the correct baud rate for the bootloader.

### Step 3: First Boot & Serial Connection

1. **Disconnect** USB cable
2. **Power cycle** the printer (off/on)
3. **Reconnect** USB
4. **Test connection** with a serial terminal (PuTTY, CoolTerm, Arduino IDE):
   - **Port:** Select your printer's COM port
   - **⚠️ IMPORTANT - Baud rate:**
     - **Factory firmware:** 115200 baud
     - **These custom firmwares:** 250000 baud
5. **Send `M115`** to verify new firmware version

### Video Guide

📺 **Visual tutorial:** [Wanhao D9 LCD Firmware Update](https://www.youtube.com/watch?v=VGvtMmlBVj8)

### Recovery Process

**If flashing fails or printer becomes unresponsive:**

1. **Take Wanhao's original firmware** from the `Wanhao_factory/` folder of your model (Wanhao's download site no longer exists)
2. **Follow same flashing procedure** with original firmware
3. **Once recovered**, retry with custom firmware

---

<a name="français"></a>
## <img src="../.github/flags/fr.svg" height="14" alt="FR"> Version Française

### Prérequis

**Outils requis :**
- Câble USB (imprimante vers ordinateur)
- **Outil de flash** (choisir un) :
  - **AVRDUDESS** (GUI pour Windows) - [Télécharger](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommandé pour débutants**
  - **avrdude** (ligne de commande, toutes plateformes) - [Télécharger](https://github.com/avrdudes/avrdude)
- Fichier firmware (.hex) pour votre modèle spécifique

### Contenu de ces firmwares

Compilés depuis Marlin `bugfix-2.1.x` (septembre 2026) avec les configurations Duplicator 9 publiées dans [Marlin Configurations](https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209). Les cinq premiers points sont des changements pas encore intégrés là-bas.

- **Les réglages d'usine de Wanhao**, tirés du firmware et des sources Wanhao de chaque modèle : pas/mm, vitesses et accélérations, PID de la buse, offsets et marges de palpage, vitesses de homing, limites et protections thermiques, jerk, position de parking, préchauffes et sens des axes. Le `Wanhao_factory/extract.md` de chaque modèle les liste, avec les trois que Marlin 2 ne peut pas suivre.
- **MK1 :** la sonde inductive est maintenant lue dans le bon sens (elle se déclenche à l'état bas).
- **MK3 :** l'axe Y est inversé, comme dans le firmware MK3 de Wanhao : la MK3 a son moteur Y du côté de l'écran tactile.
- **Filtre anti-parasites des fins de course** (`ENDSTOP_NOISE_THRESHOLD 2`) : sans lui, un parasite sur la ligne d'un fin de course pouvait arrêter le homing quelques millimètres trop tôt avec *Homing Failed*.
- **Reprise après coupure** active : après une coupure de courant pendant une impression depuis la carte SD, l'écran propose de reprendre. Pour la désactiver : `M413 S0` puis `M500`.
- **Capteur de fin de filament** pris en charge, désactivé par défaut sauf sur la MK3. Sans capteur, rien ne se passe ; une fois un capteur installé, activez-le avec `M412 S1` puis `M500`.
- **Les firmwares d'usine de Wanhao** sont conservés dans `Wanhao_factory/`, dans le dossier de chaque modèle, pour pouvoir remettre une machine dans son état d'origine. Chacun a un `extract.md` qui liste les réglages lus dans les binaires de Wanhao et explique comment ils ont été lus.
- **`M503`** est disponible pour afficher tous les réglages.
- **L'écran doit être en DGUS Reloaded 1.0.3** (`LCD/DWIN_SET.zip`). Avec les anciens fichiers 1.0.2, les températures s'affichent sans la virgule (23,6 °C devient 236).

### Étape 1 : Préparation du Flash

1. **Choisissez le bon firmware** pour votre modèle :
   - `D9_MK1_xxx.hex` - Pour MK1 avec sonde inductive
   - `D9_MK2_xxx.hex` - Pour MK2 d'usine (BLTouch)
   - `D9_MK1u2_xxx.hex` - Pour kit d'upgrade MK1→MK2
   - `D9_MK3_xxx.hex` - Pour MK3 avec BLTouch + capteur filament

2. **⚠️ IMPORTANT :** Fermez TOUS les programmes utilisant le port COM (terminaux série, slicers, Cura, OctoPrint, Pronterface, etc.)

3. **⚠️ Notez d'abord vos réglages :** le premier démarrage d'un nouveau firmware réinitialise l'EEPROM. Envoyez `M851` (offset Z de la sonde), `M92` (pas/mm) et `M301` (PID de la buse) et gardez les réponses, pour les remettre puis les sauvegarder avec `M500`.

### Étape 2 : Flash du Firmware

#### Option A : AVRDUDESS (GUI - Recommandé)

1. **Ouvrez AVRDUDESS**
2. **Configurez les paramètres :**
   - **Programmer :** `wiring`
   - **MCU :** `atmega2560`
   - **Port :** Sélectionnez votre port COM (ex: `COM3`)
   - **Baud rate :** Laissez par défaut (auto-configuré)
   - **Flash file :** Parcourez et sélectionnez votre fichier `.hex`
3. **Cliquez "Program!"**
4. **Attendez** la fin (généralement 30-60 secondes)

#### Option B : Ligne de Commande (avrdude)

Remplacez `COMX` par votre port COM réel et `firmware.hex` par votre fichier :

**Windows :**
```cmd
avrdude -v -p atmega2560 -c wiring -P COMX -D -U flash:w:firmware.hex:i
```

**Linux/macOS :**
```bash
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:firmware.hex:i
```

**Note :** Le protocole `-c wiring` configure automatiquement la bonne vitesse pour le bootloader.

### Étape 3 : Premier Démarrage & Connexion Série

1. **Débranchez** le câble USB
2. **Redémarrez** l'imprimante (éteindre/rallumer)
3. **Reconnectez** l'USB
4. **Testez la connexion** avec un terminal série (PuTTY, CoolTerm, Arduino IDE) :
   - **Port :** Sélectionnez le port COM de votre imprimante
   - **⚠️ IMPORTANT - Vitesse (baud rate) :**
     - **Firmware d'usine :** 115200 baud
     - **Ces firmwares custom :** 250000 baud
5. **Envoyez `M115`** pour vérifier la nouvelle version

### Guide Vidéo

📺 **Tutoriel visuel :** [Mise à jour firmware LCD Wanhao D9](https://www.youtube.com/watch?v=VGvtMmlBVj8)

### Procédure de Récupération

**Si le flash échoue ou l'imprimante ne répond plus :**

1. **Prenez le firmware d'origine de Wanhao** dans le dossier `Wanhao_factory/` de votre modèle (le site de téléchargement de Wanhao n'existe plus)
2. **Suivez la même procédure** avec le firmware d'origine
3. **Une fois récupérée**, réessayez avec le firmware custom

---

## 📋 Troubleshooting / Dépannage

### Common Issues / Problèmes Courants

| Problem / Problème | Solution |
|---|---|
| "Port in use" / "Port utilisé" | Close all COM port software / Fermez tous logiciels utilisant le port COM |
| Permission denied / Accès refusé | Run as administrator / Exécutez en administrateur |
| Device not found / Périphérique introuvable | Install CH340/FTDI drivers / Installez pilotes CH340/FTDI |
| Wrong baud rate after flash / Mauvaise vitesse après flash | Use 250000 baud for custom firmware, 115200 for stock / Utilisez 250000 pour firmware custom, 115200 pour d'usine |
| Homing stops a few mm before the switch, *Homing Failed* / Le homing s'arrête quelques mm avant le fin de course, *Homing Failed* | Electrical noise on the endstop line: use v2.0.1 or later, which filters it / Parasite sur la ligne du fin de course : utilisez la v2.0.1 ou plus récente, qui le filtre |
| Nozzle hits a bed clip during levelling / La buse touche une pince du plateau pendant le nivellement | Use v2.0.2 or later: the first probing column is 10 mm in from the edge, as on Wanhao's firmware / Utilisez la v2.0.2 ou plus récente : la première colonne de palpage est à 10 mm du bord, comme dans le firmware Wanhao |
| Bed moves away from the Y switch / Le plateau s'éloigne du fin de course Y | Check the model: the Y motor is at the back on MK1, MK1u2 and MK2, at the front on MK3 / Vérifiez le modèle : le moteur Y est à l'arrière sur MK1, MK1u2 et MK2, à l'avant sur MK3 |

### Support

- **Original firmware / Firmware d'origine :** `Wanhao_factory/` in each model folder / dans le dossier de chaque modèle ([archived Wanhao page / page Wanhao archivée](https://web.archive.org/web/20260516085023/http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190))
- **Issues / Problèmes :** Open an issue on this GitHub repository / Ouvrez un ticket sur ce dépôt GitHub
