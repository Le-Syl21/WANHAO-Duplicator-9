# 🤫 Making the Duplicator 9 quieter / Rendre la Duplicator 9 plus silencieuse

<img src=".github/flags/gb.svg" height="14" alt="GB"> [English](#english) | <img src=".github/flags/fr.svg" height="14" alt="FR"> [Français](#français)

---

<a name="english"></a>
## <img src=".github/flags/gb.svg" height="14" alt="GB"> English

Most of the D9's noise at rest comes from its fans, and three of the four run at full speed from power-on, whatever the temperature. This page lists them, says which ones can be slowed down safely, and how.

> [!WARNING]
> Work with the printer **unplugged**, and wait a few minutes before opening the power supply: its capacitors stay charged. Keep every wire away from the 230 V side.

### The fans

| Fan | Where | Controlled by | Can it be quietened? |
|---|---|---|---|
| **Part cooling fan** | print head, blows on the print | firmware (pin D5, PWM) | already variable: set by the slicer and `M106` |
| **Hotend heatsink fan** | print head, cools the heatsink above the nozzle | nothing: 24 V always on | **no**, leave it running. Slowing it lets heat climb up the hotend and jams the filament (heat creep) |
| **Board fan** | control box, cools the mainboard | nothing: 24 V always on | yes, see below |
| **Power supply fan** | inside the power supply | the power supply itself | yes, with care, see below |

Wanhao's firmware drives no board fan and no hotend fan (`CONTROLLER_FAN_PIN` and `E0_AUTO_FAN_PIN` are both `-1`), and the board has no spare switched output. That is why these two run from the always-on "24V OUT" connectors, and why the firmware cannot slow them down.

### Board fan

On the unit measured here: **HZ-D 4010MS, 40 × 10 mm, 24 V, 0.10 A max, sleeve bearing**.

The board itself runs cool at rest, but its stepper drivers heat up during long prints. An overheating driver cuts out briefly, which shows up as **shifted layers**, not as an error message. Removing the fan entirely is therefore a risk; making it run only when the drivers are warm is not.

Two ways to do it, both without firmware changes:

**1. Bimetal thermostat (simplest).** A KSD9700 **normally open (NO)** thermal switch, 45 °C or 50 °C, in series with the fan's + wire, glued or screwed onto a driver heatsink. Below its temperature it is open and the fan is off; above, it closes and the fan runs at full speed. It resets by itself about 10–15 °C lower. Rated 250 V / 5 A, far more than the fan needs.

```
+24V ── KSD9700 NO 50 °C ── fan (+)
                            fan (−) ── 0V
```

To keep the fan turning slowly when cold instead of stopping, add a 150–220 Ω, 2 W resistor across the thermostat.

**2. NTC thermistors in series (progressive).** Two power NTC discs in series with the fan make it start around 45–50 °C and speed up as the drivers heat: **MF72-400D9** (400 Ω) + **MF72-200D9** (200 Ω), glued to a driver heatsink with thermal adhesive, leads insulated.

```
+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V
```

- This is a calculation, **not tested on a printer yet**: MF72 tolerance is ±20 %, and a small fan may start lower than expected. Check the start temperature on the bench (NTCs in a small bag in hot water, with a kitchen thermometer); add a second 200 Ω if it starts too early, drop the 200 Ω if too late.
- The NTCs must be glued to a heatsink: in free air, the fan current (up to about 0.6 W in the NTCs) heats them by tens of degrees.
- The fan never reaches full speed this way (about 75 % at 80 °C), and if an NTC fails, it fails open and the fan stops for good. Check from time to time that it spins up when the drivers are warm.

### Power supply fan

The D9 used for this page has a **Chuanglian (CZCL) A-350FAK-24**: 350 W, 24 V, 14.6 A, 30 mm slim case. Its terminal block carries only mains and the 24 V outputs: there is **no external fan control**, so any change happens inside, on the fan's own connector. Its datasheet mentions a built-in DC fan and an over-temperature protection in hiccup mode, but nothing about how the fan is driven; on this unit it runs at a fixed speed.

Before touching it, keep in mind that the heated bed draws a large share of those 14.6 A, and a slim 350 W supply heats up quickly under load. If it overheats, **it cuts out and restarts, which stops the print**. So:

- let the fan start early (around 40 °C) and never limit its maximum speed;
- after any change, run the bed at full power for 30 minutes and check that the supply never cuts out.

The fan model inside has not been identified yet; this section will be completed once it is.

---

<a name="français"></a>
## <img src=".github/flags/fr.svg" height="14" alt="FR"> Français

L'essentiel du bruit de la D9 au repos vient de ses ventilateurs, et trois des quatre tournent à fond dès la mise sous tension, quelle que soit la température. Cette page les liste, indique lesquels peuvent être ralentis sans risque, et comment.

> [!WARNING]
> Intervenez imprimante **débranchée**, et attendez quelques minutes avant d'ouvrir l'alimentation : ses condensateurs restent chargés. Tenez tous les fils à l'écart de la partie 230 V.

### Les ventilateurs

| Ventilateur | Où | Commandé par | Peut-on le rendre silencieux ? |
|---|---|---|---|
| **Ventilateur de pièce** | tête, souffle sur l'impression | firmware (broche D5, PWM) | déjà variable : réglé par le slicer et `M106` |
| **Ventilateur du radiateur de buse** | tête, refroidit le radiateur au-dessus de la buse | rien : 24 V permanent | **non**, laissez-le tourner. Le ralentir laisse la chaleur remonter dans la tête et bloque le filament (heat creep) |
| **Ventilateur de carte** | boîtier, refroidit la carte mère | rien : 24 V permanent | oui, voir plus bas |
| **Ventilateur d'alimentation** | dans l'alimentation | l'alimentation elle-même | oui, avec précaution, voir plus bas |

Le firmware de Wanhao ne pilote ni ventilateur de carte ni ventilateur de buse (`CONTROLLER_FAN_PIN` et `E0_AUTO_FAN_PIN` valent `-1`), et la carte n'a aucune sortie commutée libre. C'est pour ça que ces deux-là sont branchés sur les connecteurs « 24V OUT » permanents, et que le firmware ne peut pas les ralentir.

### Ventilateur de carte

Sur l'exemplaire mesuré ici : **HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max, palier lisse**.

La carte chauffe peu au repos, mais ses drivers moteurs chauffent pendant les longues impressions. Un driver en surchauffe coupe brièvement, ce qui se voit par des **décalages de couches**, pas par un message d'erreur. Retirer complètement le ventilateur est donc un risque ; le faire tourner seulement quand les drivers sont chauds ne l'est pas.

Deux solutions, sans toucher au firmware :

**1. Thermostat bimétallique (le plus simple).** Un interrupteur thermique KSD9700 **normalement ouvert (NO)**, 45 °C ou 50 °C, en série sur le fil + du ventilateur, collé ou vissé sur un radiateur de driver. Sous sa température il est ouvert et le ventilateur est arrêté ; au-dessus il se ferme et le ventilateur tourne à fond. Il se réarme tout seul environ 10 à 15 °C plus bas. Donné pour 250 V / 5 A, bien au-delà de ce que demande le ventilateur.

```
+24V ── KSD9700 NO 50 °C ── ventilateur (+)
                            ventilateur (−) ── 0V
```

Pour que le ventilateur tourne lentement à froid au lieu de s'arrêter, ajoutez une résistance de 150 à 220 Ω, 2 W, en parallèle sur le thermostat.

**2. Thermistances CTN en série (progressif).** Deux disques CTN de puissance en série avec le ventilateur le font démarrer vers 45-50 °C puis accélérer à mesure que les drivers chauffent : **MF72-400D9** (400 Ω) + **MF72-200D9** (200 Ω), collés sur un radiateur de driver avec de la colle thermique, pattes isolées.

```
+24V ── MF72-400D9 ── MF72-200D9 ── ventilateur (+)
                                    ventilateur (−) ── 0V
```

- C'est un calcul, **pas encore testé sur une imprimante** : les MF72 sont à ±20 %, et un petit ventilateur peut démarrer plus bas que prévu. Vérifiez la température de démarrage au banc (CTN dans un petit sachet plongé dans de l'eau chaude, avec un thermomètre de cuisine) ; ajoutez une deuxième 200 Ω s'il démarre trop tôt, retirez la 200 Ω s'il démarre trop tard.
- Les CTN doivent être collées sur un radiateur : à l'air libre, le courant du ventilateur (jusqu'à environ 0,6 W dans les CTN) les chauffe de plusieurs dizaines de degrés.
- Le ventilateur n'atteint jamais sa pleine vitesse de cette façon (environ 75 % à 80 °C), et si une CTN claque, elle s'ouvre et le ventilateur s'arrête définitivement. Vérifiez de temps en temps qu'il se lance quand les drivers sont chauds.

### Ventilateur d'alimentation

La D9 utilisée pour cette page a une **Chuanglian (CZCL) A-350FAK-24** : 350 W, 24 V, 14,6 A, boîtier slim de 30 mm. Son bornier ne porte que le secteur et les sorties 24 V : il n'y a **aucune commande externe du ventilateur**, toute modification se fait donc à l'intérieur, sur le connecteur du ventilateur. Sa fiche technique mentionne un ventilateur DC intégré et une protection contre la surchauffe en mode hoquet, mais rien sur la façon dont le ventilateur est commandé ; sur cet exemplaire il tourne à vitesse fixe.

Avant d'y toucher, gardez en tête que le plateau chauffant tire une grosse partie de ces 14,6 A, et qu'une alimentation slim de 350 W chauffe vite en charge. En surchauffe, **elle coupe puis redémarre, ce qui arrête l'impression**. Donc :

- faites démarrer le ventilateur tôt (vers 40 °C) et ne limitez jamais sa vitesse maximale ;
- après toute modification, faites chauffer le plateau à fond 30 minutes et vérifiez que l'alimentation ne coupe jamais.

Le modèle du ventilateur interne n'est pas encore identifié ; cette section sera complétée quand il le sera.

---

Sources: [A-350FAK-24 datasheet (AG Electrónica)](https://agelectronica.lat/pdfs/textos/A/A-350FAK-24.PDF) · [MF72 power NTC datasheet (Cantherm)](https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf) · [Wanhao's D9 firmware sources (garychen99)](https://github.com/garychen99/D9MK2)
