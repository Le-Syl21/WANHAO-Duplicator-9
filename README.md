# WANHAO Duplicator 9 Repository

This repository is dedicated to the **WANHAO Duplicator 9** 3D printer and will gradually include:

* 🔧 Official and custom **firmware** (Marlin, Klipper, etc.)
* 🖥️ **LCD resources** and documentation (DGUS / DWIN_SET)
* ⚙️ **Configuration files** (Marlin, Klipper)
* 🧪 **G-code test files** for calibration and troubleshooting
* 📖 Guides and tutorials for setup and upgrades

---

## 📂 Repository structure

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
        │   └── D9_MK1_500.hex
        ├── MK1u2
        │   ├── D9_MK1u2_300.hex
        │   ├── D9_MK1u2_400.hex
        │   └── D9_MK1u2_500.hex
        ├── MK2
        │   ├── D9_MK2_300.hex
        │   ├── D9_MK2_400.hex
        │   └── D9_MK2_500.hex
        └── MK3
            ├── D9_MK3_300.hex
            ├── D9_MK3_400.hex
            └── D9_MK3_500.hex
```

* **Firmware/** : Main directory for firmware and related files.
* **LCD/** : LCD firmware (`DWIN_SET`) + flashing instructions.
* **MK1 / MK1u2 / MK2 / MK3** : Marlin firmware builds (`.hex`) for each hardware revision and build size (300, 400, 500).

---

## 🚀 Roadmap / Planned additions

* **Klipper support**

  * Printer.cfg base files
  * Recommended macros
* **Calibration G-code**

  * Bed leveling tests
  * Flow / extrusion calibration
  * Acceleration and resonance tests
* **Extra documentation**

  * Tips for hardware upgrades
  * Known issues and fixes

---

## 📜 License

This project is licensed under the **GNU GPL v3**.
You are free to use, modify, and redistribute this code under the terms of the license. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) for details.
