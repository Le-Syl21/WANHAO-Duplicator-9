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

Built from Marlin `bugfix-2.1.x` (September 2026) with the Duplicator 9 configurations published in [Marlin Configurations](https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209). The first six points are changes proposed there and not merged yet; the BTT sensor support and DGUS Reloaded 2.0 exist only in these builds.

- **Wanhao's factory settings**, taken from Wanhao's firmware and source for each model: steps/mm, speeds and accelerations, hotend PID, probe offsets and probing margins, homing speeds, thermal limits and protection, jerk, park position, preheat values and axis directions. Each model's `Wanhao_factory/extract.md` lists them, with the three that Marlin 2 cannot follow.
- **MK1:** the inductive probe is now read the right way round (it triggers LOW).
- **MK3:** the Y axis is inverted, as in Wanhao's own MK3 firmware: the MK3 has its Y motor on the touchscreen side.
- **Endstop noise filter** (`ENDSTOP_NOISE_THRESHOLD 2`): without it, a glitch on the endstop line could stop homing a few millimetres short with *Homing Failed*.
- **Power-loss recovery** is on: during an SD print the job is saved on each layer change, and after an outage the screen offers to resume from the last saved layer. Turn it off with `M413 S0` then `M500`. (v2.0.0 to v2.0.3 also watched the board's power-fail input, which stopped every print at once with a false *power outage*; v2.0.4 no longer does.)
- **After a bed levelling the head returns to the centre** (Z up 10 mm), so the bed no longer hides the screen.
- **Bed levelling is a switch** (since v2.1.2, made to work in v2.1.3): the *Automatic levelling* page shows an on/off switch once a mesh has been probed, and nothing at all before. Stock DGUS Reloaded switched levelling back on every time that page was opened, which undid the switch; these builds report the state instead of forcing it.
- **Long file names on the screen** (since v2.1.3): `SCROLL_LONG_FILENAMES` is on, so Marlin keeps 65 characters instead of 26 and the screen shows the 32 the DGUS field carries. Without it a name was cut at 26 whatever the screen did.
- **Filament runout detection is on by default on every model** (since v2.0.8). Without a sensor on D8 nothing happens: the pin's pull-up reads as filament present. Settings saved by an earlier release keep their state: turn it on with `M412 S1` then `M500`, off with `M412 S0` then `M500`.
- **BTT Smart Filament Sensor V2.0** (runout switch + motion, catches jams): its motion signal is read on D9, next to the runout input D8 on the board's sensor plug. Wire it, then `M412 S1 L10` and `M500`. `M412 S1` / `S0` turns detection on or off, `M412 L<mm>` sets the jam length and `M412 L0` turns jam detection off (the default), leaving the runout switch alone. Wiring diagram and every command: [Filament sensor](https://le-syl21.github.io/WANHAO-Duplicator-9/sensor.html). For this, these release builds turn on `FILAMENT_SWITCH_AND_MOTION` with `FIL_MOTION1_PIN 9`, runout detection on by default and a jam length of 0, and carry our Marlin change [MarlinFirmware/Marlin#28585](https://github.com/MarlinFirmware/Marlin/pull/28585) (`marlin-m412-l0.patch` in this folder: `L0` turns jam detection off, `L` works on its own). When settings are loaded, the 0 runout distance saved by v2.0.4 or earlier becomes 5 mm, and the 100 m / 10 km jam lengths saved by v2.0.5 / v2.0.6 become 0.
- **Wanhao's factory firmwares** are kept in `Wanhao_factory/` inside each model folder, so a machine can be put back as it left the factory. Each has an `extract.md` listing the settings read out of Wanhao's binaries and how they were read.
- **`M503`** is available to print every setting.
- **The screen's *Information* page shows your model, size and release**, for example *Wanhao D9 MK2 300* and *2.1.x (v2.0.9)*. `M115` reports the same.
- **Updates keep your settings** (since v2.0.3). See *Back to this firmware's default settings* below to start from the defaults.
- **DGUS Reloaded 2.0 on the screen** (since v2.0.9, `LCD/DWIN_SET.zip`): a new interface in 16 languages, chosen by tapping the flag on the home screen and saved in the printer; a filament sensor page (*Settings* → *Filament* → *Filament sensor*: runout on/off, jam on/off, jam length, *Save*); a status line that stays on screen; temperature gauges. The firmware side is our change `marlin-dgus-reloaded-2.patch` in this folder; the screen is built from [DGUS-Reloaded-2](https://github.com/Le-Syl21/DGUS-Reloaded-2). These firmwares need it: with the older DGUS Reloaded 1.0.3 (`LCD/DWIN_SET_1.0.3.zip`) the new pages are missing, and with 1.0.2, temperatures show without their decimal point (23.6 °C appears as 236).

### Step 1: Prepare for Flashing

1. **Choose the correct firmware** for your model:
   - `D9_MK1_xxx.hex` - For MK1 with inductive probe
   - `D9_MK2_xxx.hex` - For MK2 factory (BLTouch)
   - `D9_MK1u2_xxx.hex` - For MK1→MK2 upgrade kit
   - `D9_MK3_xxx.hex` - For MK3 with BLTouch + filament sensor

2. **⚠️ IMPORTANT:** Close ALL programs using the COM port (serial terminals, slicers, Cura, OctoPrint, Pronterface, etc.)

3. **⚠️ Note your settings first:** send `M503` and keep the answer. Since v2.0.3 an update keeps the stored settings, but updating **to** v2.0.3 starts once from this firmware's defaults (the way settings are stored changed), and so does coming from Wanhao's firmware. You then set your probe Z offset again with `M851 Z…` and `M500`.

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

### Back to this firmware's default settings

Since v2.0.3, a firmware update **keeps** the settings stored in the printer (probe Z offset, steps/mm, PID, mesh…). That is what you want most of the time, but it also means new default values in a release do not replace the ones already stored. Reset once:

- **when you update from v2.0.2 or earlier while keeping values saved by hand**, and the release notes change a default you want (v2.0.2 brought Wanhao's settings);
- **when the printer behaves oddly** after trying other firmwares;
- **whenever you want to start clean.**

How, either way:

- **On the screen:** *Settings* → *More* → *Reset settings* → ✓.
- **Over USB:** send `M502` (load this firmware's defaults) then `M500` (save them).

Then set your probe Z offset again (`M851 Z…` then `M500`) and run a bed levelling. Check the result with `M503`.

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

Compilés depuis Marlin `bugfix-2.1.x` (septembre 2026) avec les configurations Duplicator 9 publiées dans [Marlin Configurations](https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209). Les six premiers points sont des changements proposés là-bas et pas encore intégrés ; la prise en charge du capteur BTT et DGUS Reloaded 2.0 n'existent que dans ces firmwares.

- **Les réglages d'usine de Wanhao**, tirés du firmware et des sources Wanhao de chaque modèle : pas/mm, vitesses et accélérations, PID de la buse, offsets et marges de palpage, vitesses de homing, limites et protections thermiques, jerk, position de parking, préchauffes et sens des axes. Le `Wanhao_factory/extract.md` de chaque modèle les liste, avec les trois que Marlin 2 ne peut pas suivre.
- **MK1 :** la sonde inductive est maintenant lue dans le bon sens (elle se déclenche à l'état bas).
- **MK3 :** l'axe Y est inversé, comme dans le firmware MK3 de Wanhao : la MK3 a son moteur Y du côté de l'écran tactile.
- **Filtre anti-parasites des fins de course** (`ENDSTOP_NOISE_THRESHOLD 2`) : sans lui, un parasite sur la ligne d'un fin de course pouvait arrêter le homing quelques millimètres trop tôt avec *Homing Failed*.
- **Reprise après coupure** active : pendant une impression depuis la carte SD, l'avancement est enregistré à chaque changement de couche, et après une coupure l'écran propose de reprendre depuis la dernière couche enregistrée. Pour la désactiver : `M413 S0` puis `M500`. (Les v2.0.0 à v2.0.3 surveillaient aussi l'entrée de détection de coupure de la carte, qui arrêtait toute impression dès le départ avec une fausse *power outage* ; la v2.0.4 ne le fait plus.)
- **Après un nivellement, la tête revient au centre** (Z monte de 10 mm) : le plateau ne cache plus l'écran.
- **Le nivellement est un interrupteur** (depuis la v2.1.2, fonctionnel en v2.1.3) : la page *Nivellement automatique* affiche un interrupteur une fois le maillage palpé, et rien du tout avant. DGUS Reloaded d'origine réactivait le nivellement à chaque ouverture de cette page, ce qui annulait l'interrupteur ; ces firmwares affichent l'état au lieu de l'imposer.
- **Noms de fichiers longs à l'écran** (depuis la v2.1.3) : `SCROLL_LONG_FILENAMES` est activé, donc Marlin conserve 65 caractères au lieu de 26 et l'écran affiche les 32 que transporte le champ DGUS. Sans cela, un nom était coupé à 26 caractères quoi que fasse l'écran.
- **La détection de fin de filament est active par défaut sur tous les modèles** (depuis la v2.0.8). Sans capteur sur D8, rien ne se passe : la résistance de tirage de la broche se lit « filament présent ». Les réglages enregistrés par une version précédente gardent leur état : activez-la avec `M412 S1` puis `M500`, désactivez-la avec `M412 S0` puis `M500`.
- **BTT Smart Filament Sensor V2.0** (fin de filament + mouvement, détecte les bourrages) : son signal de mouvement est lu sur D9, à côté de l'entrée de fin de filament D8 sur la prise capteur de la carte. Branchez-le, puis `M412 S1 L10` et `M500`. `M412 S1` / `S0` active ou désactive la détection, `M412 L<mm>` règle la longueur de bourrage et `M412 L0` désactive la détection de bourrage (réglage par défaut) sans toucher au détecteur de fin de filament. Schéma de branchement et toutes les commandes : [Capteur filament](https://le-syl21.github.io/WANHAO-Duplicator-9/fr/sensor.html). Pour cela, ces firmwares activent `FILAMENT_SWITCH_AND_MOTION` avec `FIL_MOTION1_PIN 9`, la détection de fin de filament active par défaut et une longueur de bourrage de 0, et intègrent notre modification de Marlin [MarlinFirmware/Marlin#28585](https://github.com/MarlinFirmware/Marlin/pull/28585) (`marlin-m412-l0.patch` dans ce dossier : `L0` désactive la détection de bourrage, `L` fonctionne seul). Au chargement des réglages, la distance de fin de filament à 0 enregistrée par la v2.0.4 ou avant devient 5 mm, et les longueurs de bourrage de 100 m / 10 km enregistrées par la v2.0.5 / v2.0.6 deviennent 0.
- **Les firmwares d'usine de Wanhao** sont conservés dans `Wanhao_factory/`, dans le dossier de chaque modèle, pour pouvoir remettre une machine dans son état d'origine. Chacun a un `extract.md` qui liste les réglages lus dans les binaires de Wanhao et explique comment ils ont été lus.
- **`M503`** est disponible pour afficher tous les réglages.
- **La page *Informations* de l'écran affiche votre modèle, votre taille et la version**, par exemple *Wanhao D9 MK2 300* et *2.1.x (v2.0.9)*. `M115` indique la même chose.
- **Les mises à jour conservent vos réglages** (depuis la v2.0.3). Voir *Revenir aux réglages par défaut de ce firmware* plus bas pour repartir des valeurs par défaut.
- **DGUS Reloaded 2.0 sur l'écran** (depuis la v2.0.9, `LCD/DWIN_SET.zip`) : une nouvelle interface en 16 langues, choisie en touchant le drapeau de l'accueil et enregistrée dans l'imprimante ; une page capteur de filament (*Réglages* → *Filament* → *Capteur de filament* : fin de filament, bourrage, longueur de bourrage, *Enregistrer*) ; une ligne d'état qui reste affichée ; des jauges de température. Côté firmware, c'est notre modification `marlin-dgus-reloaded-2.patch` dans ce dossier ; l'écran est généré par [DGUS-Reloaded-2](https://github.com/Le-Syl21/DGUS-Reloaded-2). Ces firmwares en ont besoin : avec l'ancienne DGUS Reloaded 1.0.3 (`LCD/DWIN_SET_1.0.3.zip`) les nouvelles pages manquent, et avec la 1.0.2 les températures s'affichent sans la virgule (23,6 °C devient 236).

### Étape 1 : Préparation du Flash

1. **Choisissez le bon firmware** pour votre modèle :
   - `D9_MK1_xxx.hex` - Pour MK1 avec sonde inductive
   - `D9_MK2_xxx.hex` - Pour MK2 d'usine (BLTouch)
   - `D9_MK1u2_xxx.hex` - Pour kit d'upgrade MK1→MK2
   - `D9_MK3_xxx.hex` - Pour MK3 avec BLTouch + capteur filament

2. **⚠️ IMPORTANT :** Fermez TOUS les programmes utilisant le port COM (terminaux série, slicers, Cura, OctoPrint, Pronterface, etc.)

3. **⚠️ Notez d'abord vos réglages :** envoyez `M503` et gardez la réponse. Depuis la v2.0.3, une mise à jour conserve les réglages enregistrés, mais le passage **à** la v2.0.3 repart une fois des valeurs par défaut de ce firmware (la façon de stocker les réglages a changé), tout comme le passage depuis le firmware Wanhao. Réglez alors de nouveau l'offset Z de la sonde avec `M851 Z…` puis `M500`.

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

### Revenir aux réglages par défaut de ce firmware

Depuis la v2.0.3, une mise à jour **conserve** les réglages enregistrés dans l'imprimante (offset Z de la sonde, pas/mm, PID, maillage…). C'est ce qu'on veut la plupart du temps, mais les nouvelles valeurs par défaut d'une version ne remplacent donc pas celles déjà enregistrées. Faites une remise à zéro :

- **si vous mettez à jour depuis la v2.0.2 ou une version plus ancienne en gardant des valeurs sauvegardées à la main**, et que les notes de version changent un réglage par défaut qui vous intéresse (la v2.0.2 a apporté les réglages Wanhao) ;
- **si l'imprimante se comporte bizarrement** après avoir essayé d'autres firmwares ;
- **chaque fois que vous voulez repartir de zéro.**

Au choix :

- **À l'écran :** *Réglages* → *Plus* → *Réinitialiser* → ✓.
- **En USB :** envoyez `M502` (charge les valeurs par défaut de ce firmware) puis `M500` (les enregistre).

Réglez ensuite de nouveau l'offset Z de la sonde (`M851 Z…` puis `M500`) et lancez un nivellement. Vérifiez le résultat avec `M503`.

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
