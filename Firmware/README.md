# Wanhao Duplicator 9 - Firmware Flash Guide / Guide de Flash du Firmware

## 🇬🇧 English Version

### Prerequisites

**Required Tools:**
- USB cable (printer to computer)
- **Serial Terminal** (choose one):
  - **PuTTY** (Windows) - [Download](https://www.putty.org/)
  - **CoolTerm** (Windows/macOS/Linux) - [Download](https://freeware.the-meiers.org/)
  - **Arduino IDE Serial Monitor** (all platforms)
- **Flash Tool** (choose one):
  - **AVRDUDESS** (GUI for Windows) - [Download](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommended for beginners**
  - **avrdude** (command line, all platforms) - [Download](https://github.com/avrdudes/avrdude)
- Firmware file (.hex) for your specific model

### Step 1: Serial Connection Test

**⚠️ CRITICAL:** Close ALL programs that might use the COM port (Cura, OctoPrint, Pronterface, etc.) before testing connection!

1. **Connect** your Wanhao D9 to your computer via USB
2. **Power on** the printer
3. **Open your serial terminal** (PuTTY, CoolTerm, or Arduino IDE)
4. **Configure connection:**
   - **Port:** Select your printer's COM port (usually highest number)
   - **Baud rate:** 
     - **Stock firmware:** 115200 baud
     - **Custom firmware:** May vary (try 57600, 115200, 250000)
     - **These firmware builds:** 250000 baud
5. **Connect** and test by sending `M115` command
6. You should receive printer information (firmware version, capabilities)

⚠️ **If connection fails:** 
- Try different baud rates
- Check Windows Device Manager for correct COM port
- Install/update CH340 or FTDI drivers
- Ensure no other software is using the port

### Step 2: Prepare for Flashing

1. **Choose the correct firmware** for your model:
   - `D9_MK1_xxx.hex` - For MK1 with inductive probe
   - `D9_MK2_xxx.hex` - For MK2 factory (BLTouch)
   - `D9_MK2u2_xxx.hex` - For MK1→MK2 upgrade kit
   - `D9_MK3_xxx.hex` - For MK3 with BLTouch + filament sensor

2. **⚠️ IMPORTANT:** Close ALL programs using the COM port (serial terminals, slicers, etc.)

### Step 3: Flash Firmware

#### Option A: AVRDUDESS (GUI - Recommended)

1. **Open AVRDUDESS**
2. **Configure settings:**
   - **Programmer:** `arduino`
   - **MCU:** `atmega2560`
   - **Port:** Select your COM port (e.g., `COM3`)
   - **Baud rate:** Use the **same baud rate that worked** in your serial connection test
   - **Flash file:** Browse and select your `.hex` file
3. **Click "Program!"**
4. **Wait** for completion (usually 30-60 seconds)

#### Option B: Command Line (avrdude)

Replace `COMX` with your actual COM port, `BAUDRATE` with the working baud rate from your connection test, and `firmware.hex` with your firmware file:

**Windows:**
```cmd
avrdude -v -p atmega2560 -c arduino -P COMX -b BAUDRATE -D -U flash:w:firmware.hex:i
```

**Linux/macOS:**
```bash
avrdude -v -p atmega2560 -c arduino -P /dev/ttyUSB0 -b BAUDRATE -D -U flash:w:firmware.hex:i
```

### Step 4: First Boot

1. **Disconnect** USB cable
2. **Power cycle** the printer (off/on)
3. **Reconnect** USB (optional)
4. **Test connection** at **250000 baud** (new firmware speed)
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
- **Terminal série** (choisir un) :
  - **PuTTY** (Windows) - [Télécharger](https://www.putty.org/)
  - **CoolTerm** (Windows/macOS/Linux) - [Télécharger](https://freeware.the-meiers.org/)
  - **Moniteur série Arduino IDE** (toutes plateformes)
- **Outil de flash** (choisir un) :
  - **AVRDUDESS** (GUI pour Windows) - [Télécharger](https://github.com/zkemble/AVRDUDESS) ⭐ **Recommandé pour débutants**
  - **avrdude** (ligne de commande, toutes plateformes) - [Télécharger](https://github.com/avrdudes/avrdude)
- Fichier firmware (.hex) pour votre modèle spécifique

### Étape 1 : Test de Connexion Série

**⚠️ CRITIQUE :** Fermez TOUS les programmes utilisant le port COM (Cura, OctoPrint, Pronterface, etc.) avant de tester !

1. **Connectez** votre Wanhao D9 à l'ordinateur via USB
2. **Allumez** l'imprimante
3. **Ouvrez votre terminal série** (PuTTY, CoolTerm, ou Arduino IDE)
4. **Configurez la connexion :**
   - **Port :** Sélectionnez le port COM de votre imprimante (généralement le plus haut numéro)
   - **Vitesse (baud rate) :**
     - **Firmware d'origine :** 115200 baud
     - **Firmware custom :** Variable (essayez 57600, 115200, 250000)
     - **Ces firmwares :** 250000 baud
5. **Connectez** et testez en envoyant la commande `M115`
6. Vous devriez recevoir les informations de l'imprimante (version firmware, capacités)

⚠️ **En cas d'échec de connexion :**
- Essayez différentes vitesses
- Vérifiez le Gestionnaire de périphériques Windows pour le bon port COM
- Installez/mettez à jour les pilotes CH340 ou FTDI
- Assurez-vous qu'aucun autre logiciel n'utilise le port

### Étape 2 : Préparation du Flash

1. **Choisissez le bon firmware** pour votre modèle :
   - `D9_MK1_xxx.hex` - Pour MK1 avec sonde inductive
   - `D9_MK2_xxx.hex` - Pour MK2 d'usine (BLTouch)
   - `D9_MK2u2_xxx.hex` - Pour kit d'upgrade MK1→MK2
   - `D9_MK3_xxx.hex` - Pour MK3 avec BLTouch + capteur filament

2. **⚠️ IMPORTANT :** Fermez TOUS les programmes utilisant le port COM !

### Étape 3 : Flash du Firmware

#### Option A : AVRDUDESS (GUI - Recommandé)

1. **Ouvrez AVRDUDESS**
2. **Configurez les paramètres :**
   - **Programmer :** `arduino`
   - **MCU :** `atmega2560`
   - **Port :** Sélectionnez votre port COM (ex: `COM3`)
   - **Baud rate :** Utilisez la **même vitesse qui a fonctionné** lors du test de connexion série
   - **Flash file :** Parcourez et sélectionnez votre fichier `.hex`
3. **Cliquez "Program!"**
4. **Attendez** la fin (généralement 30-60 secondes)

#### Option B : Ligne de Commande (avrdude)

Remplacez `COMX` par votre port COM réel, `BAUDRATE` par la vitesse qui a fonctionné lors du test de connexion, et `firmware.hex` par votre fichier :

**Windows :**
```cmd
avrdude -v -p atmega2560 -c arduino -P COMX -b BAUDRATE -D -U flash:w:firmware.hex:i
```

**Linux/macOS :**
```bash
avrdude -v -p atmega2560 -c arduino -P /dev/ttyUSB0 -b BAUDRATE -D -U flash:w:firmware.hex:i
```

### Étape 4 : Premier Démarrage

1. **Débranchez** le câble USB
2. **Redémarrez** l'imprimante (éteindre/rallumer)
3. **Reconnectez** l'USB (optionnel)
4. **Testez la connexion** à **250000 baud** (nouvelle vitesse du firmware)
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
| No response / Pas de réponse | Check baud rate, try 57600/115200/250000 / Vérifiez la vitesse |
| Permission denied / Accès refusé | Run as administrator / Exécutez en administrateur |
| Device not found / Périphérique introuvable | Install CH340/FTDI drivers / Installez pilotes CH340/FTDI |

### Support

- **Original firmware / Firmware d'origine :** [Wanhao Downloads](http://www.wanhao3dprinter.com/Down/ShowArticle.asp?ArticleID=190)
- **Issues / Problèmes :** Open an issue on this GitHub repository / Ouvrez un ticket sur ce dépôt GitHub
