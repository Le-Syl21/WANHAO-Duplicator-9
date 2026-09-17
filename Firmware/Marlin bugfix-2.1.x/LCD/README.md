# Wanhao Duplicator 9 - DGUS LCD Flash Guide (OS + Firm) / Guide de Flash de l'Écran LCD DGUS (OS + Firm)

<img src="../../../.github/flags/gb.svg" height="14" alt="GB"> [English Version](#english) | <img src="../../../.github/flags/fr.svg" height="14" alt="FR"> [Version Française](#français)

<a name="english"></a>
## <img src="../../../.github/flags/gb.svg" height="14" alt="GB"> English Version

### Prerequisites

**Required Items:**
- MicroSD card (minimum 1GB, maximum 32GB recommended)
- Computer with SD card reader
- DWIN_SET.zip file (provided) - **DGUS Reloaded 2.0**, in 16 languages. `DWIN_SET_1.0.3.zip` is the previous DGUS Reloaded 1.0.3, for firmwares v2.0.8 and earlier.
- Small screwdriver (for panel disassembly)

**⚠️ Important Note About This Firmware:**
This DGUS Reloaded firmware package is different from the original Wanhao firmware. It **forces a format of the LCD's internal memory** before flashing, which significantly reduces common flashing issues and improves reliability.

**Why version 2.0:**
DGUS Reloaded 2.0 is our redesign of DGUS Reloaded 1.0.3 ([source](https://github.com/Le-Syl21/DGUS-Reloaded-2)): 16 languages, chosen by tapping the flag on the home screen; a filament sensor page (*Settings* → *Filament* → *Filament sensor*) to turn runout and jam detection on or off and set the jam length; a status line that stays on screen; temperature gauges. It needs these firmwares from **v2.0.9**: with v2.0.8 or earlier, the language goes back to English at each start and the filament sensor page does not work. Like 1.0.3, it shows temperatures with their decimal, as Marlin sends them since 2023 ([Marlin#25490](https://github.com/MarlinFirmware/Marlin/pull/25490)); with the old 1.0.2 files, 23.6 °C appears as 236.

### Step 1: Format MicroSD Card

**⚠️ CRITICAL: The allocation unit size MUST be 4096 bytes (4K). This is essential for proper LCD firmware loading!**

#### Windows:

**⚠️ Note:** Windows 11's native format tool may not support FAT32 formatting. Use GUI Format instead.

**Method 1: GUI Format (Fat32Format) - RECOMMENDED**
1. **Download** GUI Format from: [http://ridgecrop.co.uk/index.htm?guiformat.htm](http://ridgecrop.co.uk/index.htm?guiformat.htm)
2. **Extract** and run `guiformat.exe` (no installation needed)
3. **Insert** MicroSD card into computer
4. **Select** your SD card drive from the dropdown
5. **Configure settings:**
   - **Allocation unit size:** **4096** ⚠️ **CRITICAL!**
   - **Volume label:** Optional (e.g., "DWIN")
   - ✅ **Quick Format** (recommended)
6. **Click** "Start" and confirm formatting

**Method 2: Native Windows Format Tool** (if FAT32 option available)
1. **Insert** MicroSD card into computer
2. **Right-click** on the SD card in File Explorer
3. **Select** "Format..."
4. **Configure settings:**
   - **File system:** FAT32
   - **Allocation unit size:** **4096 bytes** ⚠️ **CRITICAL!**
5. **Click** "Start" and confirm formatting

#### Linux:
```bash
# Replace /dev/sdX with your actual SD card device (check with 'lsblk')
# WARNING: Double-check device name to avoid data loss!

# Unmount if mounted
sudo umount /dev/sdX1

# Create MBR partition table
sudo parted /dev/sdX mklabel msdos

# Create FAT32 partition
sudo parted /dev/sdX mkpart primary fat32 1MiB 100%

# Format with 4K cluster size (CRITICAL!)
sudo mkfs.fat -F 32 -s 8 /dev/sdX1

# Verify formatting
sudo fsck.fat -v /dev/sdX1
```

#### macOS:
```bash
# Find your SD card device
diskutil list

# Format with 4K allocation unit size (replace disk2 with your device)
sudo newfs_msdos -F 32 -c 8 /dev/disk2
```

### Step 2: Prepare LCD Firmware

**About This DGUS Reloaded Firmware:**
This firmware package includes a pre-flash memory format routine that clears the LCD's internal storage before installing the new firmware. This significantly reduces corruption issues and failed updates that can occur with the standard firmware files.

1. **Extract** the DWIN_SET.zip file
2. **Copy** the entire `DWIN_SET` folder to the **root** of your MicroSD card
3. **Verify** the structure:
   ```
   MicroSD Card Root/
   └── DWIN_SET/
       ├── 13touch.bin
       ├── 14ShowEnglish.bin
       ├── Various other .bin files
       └── ...
   ```
4. **Safely eject** the MicroSD card

### Step 3: Access LCD Panel

**⚠️ IMPORTANT: Power OFF the printer completely before disassembly!**

1. **Power OFF** and unplug the printer
2. **Remove** the front panel screws (usually 4-6 screws around the LCD bezel)
3. **Carefully pull** the front panel forward
4. **Locate** the MicroSD card slot on the back of the LCD panel
   - It's usually a small slot near the ribbon cable connectors
   - May be labeled "TF" or "SD"

### Step 4: Flash LCD Firmware

1. **Insert** the prepared MicroSD card into the LCD panel slot
2. **Power ON** the printer (leave front panel accessible)
3. **Wait 10-30 seconds** - the LCD should show:
   - A progress bar, OR
   - "Firmware updating..." message, OR
   - Blue/blank screen during update
4. **Wait for completion** (1-3 minutes total)
   - LCD will automatically restart
   - Normal boot screen should appear
5. **Power OFF** the printer
6. **Remove** the MicroSD card from the LCD panel

### Step 5: Reassembly

1. **Verify** the LCD shows the new DGUS Reloaded interface
2. **Reassemble** the front panel
3. **Secure** all screws
4. **Power ON** and test LCD functionality

### Video Guide

📺 **Visual tutorial:** [Wanhao D9 LCD Firmware Update](https://www.youtube.com/watch?v=VGvtMmlBVj8&t=140s&pbjreload=10)

### Recovery Process

**If LCD becomes unresponsive or shows errors:**

1. **Take Wanhao's original LCD firmware** from `Wanhao_factory/`: [`MK1/Wanhao_factory/`](../MK1/Wanhao_factory/) for an MK1, [`MK2/Wanhao_factory/DWIN_SET_MK2.zip`](../MK2/Wanhao_factory/DWIN_SET_MK2.zip) for an MK1u2, MK2 or MK3 (Wanhao's download site no longer exists). It only works with Wanhao's original motherboard firmware, kept in the same folders.
2. **Follow same procedure** with original firmware files
3. **Once recovered**, retry with DGUS Reloaded firmware

---

<a name="français"></a>
## <img src="../../../.github/flags/fr.svg" height="14" alt="FR"> Version Française

### Prérequis

**Éléments requis :**
- Carte MicroSD (minimum 1GB, maximum 32GB recommandé)
- Ordinateur avec lecteur de carte SD
- Fichier DWIN_SET.zip (fourni) - **DGUS Reloaded 2.0**, en 16 langues. `DWIN_SET_1.0.3.zip` est l'ancienne DGUS Reloaded 1.0.3, pour les firmwares v2.0.8 et antérieurs.
- Petit tournevis (pour démontage du panneau)

**⚠️ Note importante concernant ce firmware :**
Ce package firmware DGUS Reloaded est différent du firmware Wanhao d'origine. Il **force un formatage de la mémoire interne du LCD** avant le flash, ce qui réduit considérablement les problèmes courants de flashage et améliore la fiabilité.

**Pourquoi la version 2.0 :**
DGUS Reloaded 2.0 est notre refonte de DGUS Reloaded 1.0.3 ([sources](https://github.com/Le-Syl21/DGUS-Reloaded-2)) : 16 langues, choisies en touchant le drapeau de l'accueil ; une page capteur de filament (*Réglages* → *Filament* → *Capteur de filament*) pour activer ou désactiver la détection de fin de filament et de bourrage et régler la longueur de bourrage ; une ligne d'état qui reste affichée ; des jauges de température. Elle demande ces firmwares à partir de la **v2.0.9** : avec la v2.0.8 ou avant, la langue revient à l'anglais à chaque démarrage et la page capteur de filament ne fonctionne pas. Comme la 1.0.3, elle affiche les températures avec leur décimale, telles que Marlin les envoie depuis 2023 ([Marlin#25490](https://github.com/MarlinFirmware/Marlin/pull/25490)) ; avec les anciens fichiers 1.0.2, 23,6 °C devient 236.

### Étape 1 : Formatage de la Carte MicroSD

**⚠️ CRITIQUE : La taille d'unité d'allocation DOIT être de 4096 octets (4K). C'est essentiel pour le chargement correct du firmware LCD !**

#### Windows :

**⚠️ Note :** L'outil de formatage natif de Windows 11 peut ne pas supporter le formatage FAT32. Utilisez GUI Format à la place.

**Méthode 1 : GUI Format (Fat32Format) - RECOMMANDÉ**
1. **Téléchargez** GUI Format depuis : [http://ridgecrop.co.uk/index.htm?guiformat.htm](http://ridgecrop.co.uk/index.htm?guiformat.htm)
2. **Extrayez** et exécutez `guiformat.exe` (aucune installation nécessaire)
3. **Insérez** la carte MicroSD dans l'ordinateur
4. **Sélectionnez** votre lecteur de carte SD dans le menu déroulant
5. **Configurez les paramètres :**
   - **Taille d'unité d'allocation :** **4096** ⚠️ **CRITIQUE !**
   - **Label du volume :** Optionnel (ex: "DWIN")
   - ✅ **Formatage rapide** (recommandé)
6. **Cliquez** "Start" et confirmez le formatage

**Méthode 2 : Outil de formatage natif Windows** (si option FAT32 disponible)
1. **Insérez** la carte MicroSD dans l'ordinateur
2. **Clic-droit** sur la carte SD dans l'Explorateur de fichiers
3. **Sélectionnez** "Formater..."
4. **Configurez les paramètres :**
   - **Système de fichiers :** FAT32
   - **Taille d'unité d'allocation :** **4096 octets** ⚠️ **CRITIQUE !**
5. **Cliquez** "Démarrer" et confirmez le formatage

#### Linux :
```bash
# Remplacez /dev/sdX par votre périphérique SD réel (vérifiez avec 'lsblk')
# ATTENTION : Vérifiez bien le nom du périphérique pour éviter la perte de données !

# Démontez si monté
sudo umount /dev/sdX1

# Créer table de partition MBR
sudo parted /dev/sdX mklabel msdos

# Créer partition FAT32
sudo parted /dev/sdX mkpart primary fat32 1MiB 100%

# Formater avec taille de cluster 4K (CRITIQUE !)
sudo mkfs.fat -F 32 -s 8 /dev/sdX1

# Vérifier le formatage
sudo fsck.fat -v /dev/sdX1
```

#### macOS :
```bash
# Trouver votre périphérique de carte SD
diskutil list

# Formater avec taille d'unité d'allocation 4K (remplacez disk2 par votre périphérique)
sudo newfs_msdos -F 32 -c 8 /dev/disk2
```

### Étape 2 : Préparation du Firmware LCD

**À propos de ce firmware DGUS Reloaded :**
Ce package firmware inclut une routine de formatage de la mémoire avant le flash qui efface le stockage interne du LCD avant d'installer le nouveau firmware. Cela réduit considérablement les problèmes de corruption et les échecs de mise à jour qui peuvent survenir avec les fichiers firmware standard.

1. **Extrayez** le fichier DWIN_SET.zip
2. **Copiez** l'intégralité du dossier `DWIN_SET` à la **racine** de votre carte MicroSD
3. **Vérifiez** la structure :
   ```
   Racine Carte MicroSD/
   └── DWIN_SET/
       ├── 13touch.bin
       ├── 14ShowEnglish.bin
       ├── Divers autres fichiers .bin
       └── ...
   ```
4. **Éjectez** proprement la carte MicroSD

### Étape 3 : Accès au Panneau LCD

**⚠️ IMPORTANT : Éteignez complètement l'imprimante avant le démontage !**

1. **Éteignez** et débranchez l'imprimante
2. **Retirez** les vis du panneau avant (généralement 4-6 vis autour du cadre LCD)
3. **Tirez** délicatement le panneau avant vers l'extérieur
4. **Localisez** la fente carte MicroSD à l'arrière du panneau LCD
   - C'est généralement une petite fente près des connecteurs de nappe
   - Peut être étiquetée "TF" ou "SD"

### Étape 4 : Flash du Firmware LCD

1. **Insérez** la carte MicroSD préparée dans la fente du panneau LCD
2. **Allumez** l'imprimante (laissez le panneau avant accessible)
3. **Attendez 10-30 secondes** - l'LCD devrait afficher :
   - Une barre de progression, OU
   - Message "Firmware updating...", OU
   - Écran bleu/vide pendant la mise à jour
4. **Attendez la fin** (1-3 minutes au total)
   - L'LCD redémarrera automatiquement
   - L'écran de démarrage normal devrait apparaître
5. **Éteignez** l'imprimante
6. **Retirez** la carte MicroSD du panneau LCD

### Étape 5 : Remontage

1. **Vérifiez** que l'LCD affiche la nouvelle interface DGUS Reloaded
2. **Remontez** le panneau avant
3. **Serrez** toutes les vis
4. **Allumez** et testez les fonctionnalités LCD

### Guide Vidéo

📺 **Tutoriel visuel :** [Mise à jour firmware LCD Wanhao D9](https://www.youtube.com/watch?v=VGvtMmlBVj8&t=140s&pbjreload=10)

### Procédure de Récupération

**Si l'LCD devient non-réactif ou affiche des erreurs :**

1. **Prenez le firmware LCD d'origine de Wanhao** dans `Wanhao_factory/` : [`MK1/Wanhao_factory/`](../MK1/Wanhao_factory/) pour une MK1, [`MK2/Wanhao_factory/DWIN_SET_MK2.zip`](../MK2/Wanhao_factory/DWIN_SET_MK2.zip) pour une MK1u2, MK2 ou MK3 (le site de téléchargement de Wanhao n'existe plus). Il ne fonctionne qu'avec le firmware carte d'origine de Wanhao, conservé dans les mêmes dossiers.
2. **Suivez la même procédure** avec les fichiers firmware d'origine
3. **Une fois récupéré**, réessayez avec le firmware DGUS Reloaded

---

## 📋 Troubleshooting / Dépannage

### Common Issues / Problèmes Courants

| Problem / Problème | Cause | Solution |
|---|---|---|
| LCD doesn't update / LCD ne se met pas à jour | Wrong cluster size / Mauvaise taille cluster | **Reformat with 4K clusters** / **Reformater avec clusters 4K** |
| "File error" / "Erreur fichier" | Corrupted files / Fichiers corrompus | Re-extract and copy DWIN_SET / Ré-extraire et copier DWIN_SET |
| Black screen after update / Écran noir après MAJ | Update failed / Mise à jour échouée | Use recovery firmware / Utiliser firmware de récupération |
| SD card not detected / Carte SD non détectée | Wrong format / Mauvais format | Use FAT32 with MBR / Utiliser FAT32 avec MBR |

### Important Notes / Notes Importantes

- **DGUS Reloaded firmware auto-formats LCD internal memory** / **Le firmware DGUS Reloaded formate automatiquement la mémoire interne du LCD** ✨
- **4K cluster size is mandatory** / **Taille cluster 4K obligatoire** ⚠️
- **MBR partition table required** / **Table partition MBR requise**
- **Maximum 32GB SD card** / **Carte SD maximum 32GB**
- **Power OFF during disassembly** / **Éteindre pendant démontage**

### Support

- **Original LCD firmware / Firmware LCD d'origine :** [`MK1/Wanhao_factory/`](../MK1/Wanhao_factory/) · [`MK2/Wanhao_factory/DWIN_SET_MK2.zip`](../MK2/Wanhao_factory/DWIN_SET_MK2.zip)
- **Video guide / Guide vidéo :** [YouTube Tutorial](https://www.youtube.com/watch?v=VGvtMmlBVj8&t=140s&pbjreload=10)
- **Issues / Problèmes :** Open an issue on this GitHub repository / Ouvrez un ticket sur ce dépôt GitHub
