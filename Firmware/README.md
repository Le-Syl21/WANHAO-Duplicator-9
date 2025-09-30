# Wanhao Duplicator 9 - Firmware Flash Guide / Guide de Flash du Firmware

## 🇬🇧 English Version

### Prerequisites

**Required Tools:**
- USB cable (printer to computer)
- **Flash Tool** (choose one):
  - **AVRDUDESS** (GUI for Windows) - [Download](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommended for beginners**
  - **avrdude** (command line, all platforms) - [Download](https://github.com/avrdudes/avrdude)
- Firmware file (.hex) for your specific model

### Step 1: Prepare for Flashing

1. **Choose the correct firmware** for your model:
   - `D9_MK1_xxx.hex` - For MK1 with inductive probe
   - `D9_MK2_xxx.hex` - For MK2 factory (BLTouch)
   - `D9_MK2u2_xxx.hex` - For MK1→MK2 upgrade kit
   - `D9_MK3_xxx.hex` - For MK3 with BLTouch + filament sensor

2. **⚠️ IMPORTANT:** Close ALL programs using the COM port (serial terminals, slicers, Cura, OctoPrint, Pronterface, etc.)

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

1. **Download original firmware** from: [Wanhao Official Downloads](http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)
2. **Follow same flashing procedure** with original firmware
3. **Once recovered**, retry with custom firmware

---

## 🇫🇷 Version Française

### Prérequis

**Outils requis :**
- Câble USB (imprimante vers ordinateur)
- **Outil de flash** (choisir un) :
  - **AVRDUDESS** (GUI pour Windows) - [Télécharger](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommandé pour débutants**
  - **avrdude** (ligne de commande, toutes plateformes) - [Télécharger](https://github.com/avrdudes/avrdude)
- Fichier firmware (.hex) pour votre modèle spécifique

### Étape 1 : Préparation du Flash

1. **Choisissez le bon firmware** pour votre modèle :
   - `D9_MK1_xxx.hex` - Pour MK1 avec sonde inductive
   - `D9_MK2_xxx.hex` - Pour MK2 d'usine (BLTouch)
   - `D9_MK2u2_xxx.hex` - Pour kit d'upgrade MK1→MK2
   - `D9_MK3_xxx.hex` - Pour MK3 avec BLTouch + capteur filament

2. **⚠️ IMPORTANT :** Fermez TOUS les programmes utilisant le port COM (terminaux série, slicers, Cura, OctoPrint, Pronterface, etc.)

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

1. **Téléchargez le firmware d'origine** : [Téléchargements Officiels Wanhao](http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)
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

### Support

- **Original firmware / Firmware d'origine :** [Wanhao Downloads](http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)
- **Issues / Problèmes :** Open an issue on this GitHub repository / Ouvrez un ticket sur ce dépôt GitHub
