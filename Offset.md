# 🔧 G-Code XYZ Offset Configuration Guide

A comprehensive guide to adjust X, Y, and Z offsets on your 3D printer using G-code commands.

Un guide complet pour ajuster les offsets X, Y et Z sur votre imprimante 3D via des commandes G-code.

---

## 🌍 Language / Langue

- [English](#english)
- [Français](#français)

---

<a name="english"></a>
## 🇬🇧 English

### Overview

This guide explains how to adjust the X, Y, and Z axis offsets on your 3D printer using G-code commands. These adjustments are useful for fine-tuning your printer's positioning and ensuring perfect first layers.

### ⚠️ **CRITICAL: Save to EEPROM**

**After making any offset changes, you MUST save them to EEPROM using the `M500` command, otherwise your settings will be lost after reboot!**

```gcode
M500  ; Save settings to EEPROM
```

### Available Commands

#### 1. **M206 - Home Offset** ⭐ *Recommended*

Adjusts where the firmware considers the "zero" position after homing.

```gcode
M206 X10 Y5 Z0.2  ; Set home offset
M500              ; ⚠️ SAVE TO EEPROM!
M501              ; Load settings from EEPROM (optional, to verify)
```

**When to use:** Permanent offset adjustments for bed alignment or mechanical calibration.

---

#### 2. **M851 - Z-Probe Offset**

Configures the offset between your probe sensor and the nozzle.

```gcode
M851 X-40 Y-10 Z-2.5  ; Set probe offset
M500                   ; ⚠️ SAVE TO EEPROM!
```

**When to use:** When you have a BLTouch, CR-Touch, or other bed leveling sensor.

---

#### 3. **G92 - Set Current Position** ⚠️ *Temporary*

Defines the current position as a new reference point. **This is NOT saved to EEPROM.**

```gcode
G92 X0 Y0 Z0  ; Set current position as origin
```

**When to use:** Temporary adjustments during testing. Does not persist after reboot.

---

### 📋 Complete Workflow Example

```gcode
; 1. Check current settings
M503

; 2. Adjust offsets
M206 X5 Y-3 Z0.15

; 3. ⚠️ SAVE TO EEPROM (MANDATORY!)
M500

; 4. Verify settings were saved
M501

; 5. Display settings again to confirm
M503
```

---

### 🔍 Useful Commands

| Command | Description |
|---------|-------------|
| `M500` | **Save current settings to EEPROM** ⚠️ |
| `M501` | Load settings from EEPROM |
| `M502` | Reset to factory defaults |
| `M503` | Display current settings |

---

### ⚡ Quick Reference

```gcode
; Home offset adjustment (permanent)
M206 X10 Y5 Z0.2
M500  ; ⚠️ DON'T FORGET!

; Probe offset adjustment
M851 X-40 Y-10 Z-2.5
M500  ; ⚠️ DON'T FORGET!

; Temporary position adjustment (not saved)
G92 X0 Y0 Z0
```

---

### 🚨 Important Notes

1. **ALWAYS use M500 after changing offsets** - Without this, changes are lost on reboot
2. Test your changes with a small print before committing to larger projects
3. M206 offsets are additive to your homing position
4. Positive values move the nozzle in the positive direction, negative values in the negative direction

---

<a name="français"></a>
## 🇫🇷 Français

### Vue d'ensemble

Ce guide explique comment ajuster les offsets des axes X, Y et Z sur votre imprimante 3D en utilisant des commandes G-code. Ces ajustements sont utiles pour calibrer finement le positionnement de votre imprimante et garantir des premières couches parfaites.

### ⚠️ **CRITIQUE : Sauvegarder dans l'EEPROM**

**Après avoir effectué des modifications d'offset, vous DEVEZ les sauvegarder dans l'EEPROM avec la commande `M500`, sinon vos réglages seront perdus après redémarrage !**

```gcode
M500  ; Sauvegarder les paramètres dans l'EEPROM
```

### Commandes disponibles

#### 1. **M206 - Home Offset** ⭐ *Recommandé*

Ajuste où le firmware considère la position "zéro" après le homing.

```gcode
M206 X10 Y5 Z0.2  ; Définir l'offset d'origine
M500              ; ⚠️ SAUVEGARDER DANS L'EEPROM !
M501              ; Charger les paramètres depuis l'EEPROM (optionnel, pour vérifier)
```

**Quand l'utiliser :** Ajustements d'offset permanents pour l'alignement du plateau ou la calibration mécanique.

---

#### 2. **M851 - Z-Probe Offset**

Configure l'offset entre votre capteur de nivellement et la buse.

```gcode
M851 X-40 Y-10 Z-2.5  ; Définir l'offset du capteur
M500                   ; ⚠️ SAUVEGARDER DANS L'EEPROM !
```

**Quand l'utiliser :** Quand vous avez un BLTouch, CR-Touch ou autre capteur de nivellement.

---

#### 3. **G92 - Définir la position actuelle** ⚠️ *Temporaire*

Définit la position actuelle comme nouveau point de référence. **Ceci n'est PAS sauvegardé dans l'EEPROM.**

```gcode
G92 X0 Y0 Z0  ; Définir la position actuelle comme origine
```

**Quand l'utiliser :** Ajustements temporaires pendant les tests. Ne persiste pas après redémarrage.

---

### 📋 Exemple de workflow complet

```gcode
; 1. Vérifier les paramètres actuels
M503

; 2. Ajuster les offsets
M206 X5 Y-3 Z0.15

; 3. ⚠️ SAUVEGARDER DANS L'EEPROM (OBLIGATOIRE !)
M500

; 4. Vérifier que les paramètres ont été sauvegardés
M501

; 5. Afficher à nouveau les paramètres pour confirmer
M503
```

---

### 🔍 Commandes utiles

| Commande | Description |
|----------|-------------|
| `M500` | **Sauvegarder les paramètres actuels dans l'EEPROM** ⚠️ |
| `M501` | Charger les paramètres depuis l'EEPROM |
| `M502` | Réinitialiser aux paramètres d'usine |
| `M503` | Afficher les paramètres actuels |

---

### ⚡ Référence rapide

```gcode
; Ajustement de l'offset d'origine (permanent)
M206 X10 Y5 Z0.2
M500  ; ⚠️ NE PAS OUBLIER !

; Ajustement de l'offset du capteur
M851 X-40 Y-10 Z-2.5
M500  ; ⚠️ NE PAS OUBLIER !

; Ajustement temporaire de position (non sauvegardé)
G92 X0 Y0 Z0
```

---

### 🚨 Notes importantes

1. **TOUJOURS utiliser M500 après avoir changé les offsets** - Sans cela, les modifications sont perdues au redémarrage
2. Testez vos modifications avec une petite impression avant de vous lancer dans de gros projets
3. Les offsets M206 s'ajoutent à votre position de homing
4. Les valeurs positives déplacent la buse dans le sens positif, les valeurs négatives dans le sens négatif

---

## 📝 License

This guide is free to use and modify. Feel free to contribute!

Ce guide est libre d'utilisation et de modification. N'hésitez pas à contribuer !

---

## 🤝 Contributing / Contribuer

Contributions are welcome! Please feel free to submit a Pull Request.

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

