# WANHAO Duplicator 9 Repository

🇬🇧 [English Version](#english) | 🇫🇷 [Version Française](#français)

---

## <a name="english"></a>🇬🇧 English Version

This repository is dedicated to the **WANHAO Duplicator 9** 3D printer and includes:
* 🔧 Custom **firmware** (Marlin)
* 🖥️ **LCD resources** and documentation (DGUS / DWIN_SET)
* ⚙️ **Configuration files** (Marlin) https://github.com/MarlinFirmware/Configurations/blob/import-2.1.x/config/examples/Wanhao/Duplicator%209

### 💬 Community & support

Questions, bug reports, beta testing, or just want to chat? Join the Discord:

[![Discord](https://img.shields.io/badge/Discord-Le--Syl21%20Tools-5865F2?logo=discord&logoColor=white)](https://discord.gg/T37DYHmt2j)

### 📂 Repository structure
```
WANHAO-Duplicator-9/
└── Firmware                 # First populated directory
    └── Marlin bugfix-2.1.x  # Marlin builds for D9
        ├── LCD
        │   ├── DWIN_SET.zip
        │   └── README.md    # Instructions for flashing the LCD (DGUS Reloaded)
        ├── MK1
        │   ├── D9_MK1_300.hex
        │   ├── D9_MK1_400.hex
        │   ├── D9_MK1_500.hex
        │   ├── D9_MK1_extruder.png
        │   └── D9_MK1.png
        ├── MK1u2
        │   ├── D9_MK1u2_300.hex
        │   ├── D9_MK1u2_400.hex
        │   └── D9_MK1u2_500.hex
        ├── MK2
        │   ├── D9_MK2_300.hex
        │   ├── D9_MK2_400.hex
        │   ├── D9_MK2_500.hex
        │   └── D9_MK2.png        
        └── MK3
            ├── D9_MK3_300.hex
            ├── D9_MK3_400.hex
            └── D9_MK3_500.hex
```
* **Firmware/** : Main directory for firmware and related files.
* **LCD/** : LCD firmware (`DWIN_SET`) + flashing instructions.
* **MK1 / MK1u2 / MK2 / MK3** : Marlin firmware builds (`.hex`) for each hardware revision and build size (300, 400, 500).

### 📜 License
This project is licensed under the **GNU GPL v3**.
You are free to use, modify, and redistribute this code under the terms of the license. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) for details.

---

## <a name="français"></a>🇫🇷 Version Française

Ce dépôt est dédié à l'imprimante 3D **WANHAO Duplicator 9** et comprend :
* 🔧 **Firmware** personnalisé (Marlin)
* 🖥️ **Ressources LCD** et documentation (DGUS / DWIN_SET)
* ⚙️ **Fichiers de configuration** (Marlin) https://github.com/MarlinFirmware/Configurations/blob/import-2.1.x/config/examples/Wanhao/Duplicator%209

### 💬 Communauté & support

Des questions, un bug à signaler, envie de tester en avant-première ou simplement de discuter ? Rejoignez le Discord :

[![Discord](https://img.shields.io/badge/Discord-Le--Syl21%20Tools-5865F2?logo=discord&logoColor=white)](https://discord.gg/T37DYHmt2j)

### 📂 Structure du dépôt
```
WANHAO-Duplicator-9/
└── Firmware                 # Premier répertoire principal
    └── Marlin bugfix-2.1.x  # Builds Marlin pour D9
        ├── LCD
        │   ├── DWIN_SET.zip
        │   └── README.md    # Instructions pour flasher l'écran LCD (DGUS Reloaded)
        ├── MK1
        │   ├── D9_MK1_300.hex
        │   ├── D9_MK1_400.hex
        │   ├── D9_MK1_500.hex
        │   ├── D9_MK1_extruder.png
        │   └── D9_MK1.png
        ├── MK1u2
        │   ├── D9_MK1u2_300.hex
        │   ├── D9_MK1u2_400.hex
        │   └── D9_MK1u2_500.hex
        ├── MK2
        │   ├── D9_MK2_300.hex
        │   ├── D9_MK2_400.hex
        │   ├── D9_MK2_500.hex
        │   └── D9_MK2.png        
        └── MK3
            ├── D9_MK3_300.hex
            ├── D9_MK3_400.hex
            └── D9_MK3_500.hex
```
* **Firmware/** : Répertoire principal pour le firmware et les fichiers associés.
* **LCD/** : Firmware LCD (`DWIN_SET`) + instructions de flashage.
* **MK1 / MK1u2 / MK2 / MK3** : Builds du firmware Marlin (`.hex`) pour chaque révision matérielle et taille de build (300, 400, 500).

### 📜 Licence
Ce projet est sous licence **GNU GPL v3**.
Vous êtes libre d'utiliser, modifier et redistribuer ce code selon les termes de la licence. Voir la [LICENCE](https://www.gnu.org/licenses/gpl-3.0.html) pour plus de détails.
