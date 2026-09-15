# 🤫 Making the Duplicator 9 quieter / Rendre la Duplicator 9 plus silencieuse

<img src=".github/flags/gb.svg" height="14" alt="GB"> [English](#english) | <img src=".github/flags/fr.svg" height="14" alt="FR"> [Français](#français)

---

<a name="english"></a>
## <img src=".github/flags/gb.svg" height="14" alt="GB"> English

At rest, the D9's noise comes from its fans. This page lists them, says which one can be quietened, and how.

> [!WARNING]
> Work with the printer **unplugged**. Keep every wire away from the 230 V side.

### The fans

| Fan | Where | Controlled by | Can it be quietened? |
|---|---|---|---|
| **Hotend heatsink fan** | print head, cools the heatsink above the nozzle | nothing: 24 V always on | **no**. It is usually the loudest, but slowing it lets heat climb up the hotend and jams the filament (heat creep) |
| **Part cooling fan** | print head, blows on the print | firmware (pin D5, PWM) | already variable: set by the slicer and `M106` |
| **Power supply fan** | inside the power supply | the power supply itself | nothing to do: on the unit checked here (Chuanglian A-350FAK-24) it already follows the supply's temperature |
| **Board fan** | control box, cools the mainboard | nothing: 24 V always on | **yes**, see below |

Wanhao's firmware drives no board fan and no hotend fan (`CONTROLLER_FAN_PIN` and `E0_AUTO_FAN_PIN` are both `-1`), and the board has no spare switched output. That is why these two run from the always-on "24V OUT" connectors, and why no firmware can slow them down.

### Board fan

On the unit measured here: **HZ-D 4010MS, 40 × 10 mm, 24 V, 0.10 A max, sleeve bearing**.

**Many owners simply unplug it.** The board runs cool: it sits at the bottom of the control box, below the heated bed, and the bed's heat rises away from it. If you do, keep an eye on your first long prints: an overheating stepper driver cuts out briefly, which shows up as **shifted layers**, not as an error message.

**To keep it, but only when the drivers are warm:** two power NTC thermistors in series with the fan make it start around 45–50 °C and speed up as the drivers heat. **MF72-400D9** (400 Ω) + **MF72-200D9** (200 Ω), glued to a driver heatsink with thermal adhesive, leads insulated.

```
+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V
```

- This is a calculation, **not tested on a printer yet**: MF72 tolerance is ±20 %, and a small fan may start lower than expected. Check the start temperature on the bench (NTCs in a small bag in hot water, with a kitchen thermometer); add a second 200 Ω if it starts too early, drop the 200 Ω if too late.
- The NTCs must be glued to a heatsink: in free air, the fan current (up to about 0.6 W in the NTCs) heats them by tens of degrees.
- The fan never reaches full speed this way (about 75 % at 80 °C), and an NTC that fails goes open: the fan then stops for good.

---

<a name="français"></a>
## <img src=".github/flags/fr.svg" height="14" alt="FR"> Français

Au repos, le bruit de la D9 vient de ses ventilateurs. Cette page les liste, indique lequel peut être rendu silencieux, et comment.

> [!WARNING]
> Intervenez imprimante **débranchée**. Tenez tous les fils à l'écart de la partie 230 V.

### Les ventilateurs

| Ventilateur | Où | Commandé par | Peut-on le rendre silencieux ? |
|---|---|---|---|
| **Ventilateur du radiateur de buse** | tête, refroidit le radiateur au-dessus de la buse | rien : 24 V permanent | **non**. C'est en général le plus bruyant, mais le ralentir laisse la chaleur remonter dans la tête et bloque le filament (heat creep) |
| **Ventilateur de pièce** | tête, souffle sur l'impression | firmware (broche D5, PWM) | déjà variable : réglé par le slicer et `M106` |
| **Ventilateur d'alimentation** | dans l'alimentation | l'alimentation elle-même | rien à faire : sur l'exemplaire vérifié ici (Chuanglian A-350FAK-24), il suit déjà la température de l'alimentation |
| **Ventilateur de carte** | boîtier, refroidit la carte mère | rien : 24 V permanent | **oui**, voir plus bas |

Le firmware de Wanhao ne pilote ni ventilateur de carte ni ventilateur de buse (`CONTROLLER_FAN_PIN` et `E0_AUTO_FAN_PIN` valent `-1`), et la carte n'a aucune sortie commutée libre. C'est pour ça que ces deux-là sont branchés sur les connecteurs « 24V OUT » permanents, et qu'aucun firmware ne peut les ralentir.

### Ventilateur de carte

Sur l'exemplaire mesuré ici : **HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max, palier lisse**.

**Beaucoup de propriétaires le débranchent tout simplement.** La carte chauffe peu : elle est en bas du boîtier, sous le plateau chauffant, et la chaleur du plateau monte au lieu de descendre vers elle. Si vous le faites, surveillez vos premières longues impressions : un driver moteur en surchauffe coupe brièvement, ce qui se voit par des **décalages de couches**, pas par un message d'erreur.

**Pour le garder, mais seulement quand les drivers chauffent :** deux thermistances CTN de puissance en série avec le ventilateur le font démarrer vers 45-50 °C puis accélérer à mesure que les drivers chauffent. **MF72-400D9** (400 Ω) + **MF72-200D9** (200 Ω), collées sur un radiateur de driver avec de la colle thermique, pattes isolées.

```
+24V ── MF72-400D9 ── MF72-200D9 ── ventilateur (+)
                                    ventilateur (−) ── 0V
```

- C'est un calcul, **pas encore testé sur une imprimante** : les MF72 sont à ±20 %, et un petit ventilateur peut démarrer plus bas que prévu. Vérifiez la température de démarrage au banc (CTN dans un petit sachet plongé dans de l'eau chaude, avec un thermomètre de cuisine) ; ajoutez une deuxième 200 Ω s'il démarre trop tôt, retirez la 200 Ω s'il démarre trop tard.
- Les CTN doivent être collées sur un radiateur : à l'air libre, le courant du ventilateur (jusqu'à environ 0,6 W dans les CTN) les chauffe de plusieurs dizaines de degrés.
- Le ventilateur n'atteint jamais sa pleine vitesse de cette façon (environ 75 % à 80 °C), et une CTN qui claque s'ouvre : le ventilateur s'arrête alors définitivement.

---

Sources: [MF72 power NTC datasheet (Cantherm)](https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf) · [Wanhao's D9 firmware sources (garychen99)](https://github.com/garychen99/D9MK2)
