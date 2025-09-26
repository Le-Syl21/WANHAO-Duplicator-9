# Firmware LCD - DGUS Reloaded

This firmware comes from the [DGUS Reloaded project](https://github.com/Neo2003/DGUS-reloaded/).  
It is distributed under the **GPLv3** license.

---

## 🇫🇷 Procédure de flash (grand public)

### Avant de commencer
- Le flash de l’écran se fait **via la carte SD de l’écran** (pas celle de l’imprimante).  
- L’écran est **très sensible** à la carte SD utilisée : format, table de partition, taille de bloc.  
- Utiliser de préférence une carte SD de **8 Go ou moins**.

### Étapes pas à pas
1. **Éteindre l’imprimante et l’écran**.  
2. **Formater la carte SD** en FAT32, partition **MBR**, taille de bloc ≈ 4 kB.  
   - Sous Linux :
     ```bash
     sudo mkfs.fat -F 32 -s 8 /dev/sdd1
     ```
3. Télécharger et **décompresser** `DWIN_SET.zip`.  
4. Copier le dossier **`DWIN_SET`** à la **racine** de la carte SD (chemin = `/DWIN_SET/...`).  
5. Insérer la carte SD dans le **slot de l’écran** (pas celui de l’imprimante).  
6. **Allumer l’imprimante / écran**. Le flash démarre automatiquement.  
   - L’écran devient souvent **bleu** puis **orange** une fois terminé.  
7. **Éteindre**, retirer la carte SD, rallumer. Le nouvel écran est actif.

### Erreurs fréquentes
- Carte SD trop grande (> 8 Go) ou mal formatée.  
- Mauvais chemin (ex. `firmware/DWIN_SET/DWIN_SET/...`).  
- Partition en GPT au lieu de MBR.  
- L’écran n’est pas un DWIN mais un DACAI (firmware incompatible).

### Vidéo tutorielle
👉 [Guide vidéo YouTube](https://www.youtube.com/watch?v=VGvtMmlBVj8&t=140s&pbjreload=10)

---

## 🇬🇧 Flash procedure (for makers)

### Before you start
- The update is done **via the screen’s SD card slot** (not the printer’s).  
- The display is **very picky** about SD card format and block size.  
- Prefer **8 GB or smaller SD cards**.

### Step by step
1. **Power off** the printer and screen.  
2. **Format the SD card** to FAT32, **MBR partition**, ~4 kB block size.  
   - On Linux:
     ```bash
     sudo mkfs.fat -F 32 -s 8 /dev/sdd1
     ```
3. Download and **extract** `DWIN_SET.zip`.  
4. Copy the **`DWIN_SET`** folder to the **root** of the SD card (`/DWIN_SET/...`).  
5. Insert the SD card into the **screen’s slot** (not the printer’s).  
6. **Power on** the system. The update starts automatically.  
   - Screen usually turns **blue**, then **orange** when finished.  
7. **Power off**, remove SD, power back on. The new UI is now active.

### Common mistakes
- Wrong SD card size (> 8 GB) or bad formatting.  
- Nested folder structure (`firmware/DWIN_SET/DWIN_SET/...`).  
- GPT partition instead of MBR.  
- Using a DACAI screen instead of DWIN.

### Video tutorial
👉 [YouTube tutorial](https://www.youtube.com/watch?v=VGvtMmlBVj8&t=140s&pbjreload=10)

