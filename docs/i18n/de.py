"""Deutsch: Übersetzung von en.py."""

META = {"name": "Deutsch", "locale": "de_DE", "dir": "ltr"}

UI = {
    "nav": {"index": "Start", "mk1": "MK1", "mk1u2": "MK1 + MK2-Kit", "mk2": "MK2", "mk3": "MK3",
            "flash": "Flash-Anleitung", "screen": "Display", "sensor": "Filamentsensor", "quiet": "Leiser"},
    "language": "Sprache",
    "size": "Größe", "volume": "Bauraum", "file": "Firmware",
    "footer_src": "Quellcode und Issues auf GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware unter GNU GPL v3. Die Handbücher und Firmwares von Wanhao bleiben Eigentum von Wanhao.",
}

# Beschriftungen des Anschlussplans (img/d9-sensor-plug-<Sprache>.svg).
SVG = {
    "board": "Mainboard der Wanhao D9 (Draufsicht)",
    "plug": "Sensorstecker",
    "switch": "Filamentende-Schalter",
    "motion": "Bewegung",
    "level": "Pegel: Filament da / weg",
    "pulses": "Impulse, wenn das Filament läuft",
    "names": "Bezeichnungen an deinem Sensor können abweichen",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware für Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Aktuelle Marlin-Firmware für jede Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "Displaydateien, Wanhaos Original-Firmwares und Handbücher sowie Anleitungen zum Flashen.",
                f"""
<h1>Firmware für die Wanhao Duplicator 9</h1>
<p class="lead">Wanhaos Download-Seite für die Duplicator 9 gibt es nicht mehr. Alles, was D9-Besitzer brauchen, findest
du stattdessen hier: aktuelle Marlin-2.1-Firmware für jedes Modell und jede Größe, die passenden Touchscreen-Dateien,
Wanhaos Original-Firmwares, Wanhaos Handbücher und Schritt-für-Schritt-Anleitungen zum Flashen.</p>
<p><a class="btn" href="{REPO}/releases/latest">Alle Downloads</a> <a class="btn ghost" href="{DISCORD}">Auf Discord fragen</a></p>

<h2>Welche D9 habe ich?</h2>
<div class="split"><div>
<ol>
<li><strong>Graues Flachbandkabel</strong> zum Druckkopf, ein <strong>zylindrischer Metallsensor</strong> neben der
Düse, keine seitlichen Verstrebungen am Rahmen: <a href="{p('mk1')}">MK1</a>.</li>
<li>Dieselbe Maschine der ersten Generation, aber mit einem <strong>weißen BLTouch-Sensor</strong> statt des
Metallsensors: eine MK1 mit Wanhaos Upgrade-Kit, <a href="{p('mk1u2')}">MK1 + MK2-Kit</a>.</li>
<li><strong>Schräge Verstrebungen</strong> an beiden Seiten des Rahmens, ein <strong>rundes schwarzes Kabel</strong>
zum Kopf und ein BLTouch: eine MK2 oder eine MK3. Schau unter dem Druckbett nach dem <strong>Y-Motor</strong>, der das
Bett bewegt: Sitzt er hinten, ist es eine <a href="{p('mk2')}">MK2</a>; sitzt er vorne, auf der Seite des Touchscreens,
eine <a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Die Zahl nach D9 ist die Größe: D9/300, D9/400 oder D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 mit ihren seitlichen Verstrebungen">
<figcaption>D9 MK2: seitliche Verstrebungen, rundes Kabel</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Induktiver Sensor, Flachbandkabel. Firmware, Wanhao V0.15 bis V0.164(B), Handbuch.</p><a class="more" href="{p('mk1')}">MK1-Firmware →</a></div>
<div class="card"><h3>D9 MK1 + MK2-Kit</h3><p>MK1 mit BLTouch-Kit nachgerüstet. Firmware und Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Kit-Firmware →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, seitliche Verstrebungen. Firmware, Wanhao V1.1.2, Anleitungen.</p><a class="more" href="{p('mk2')}">MK2-Firmware →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y-Motor vorne, Filamentsensor. Firmware und Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3-Firmware →</a></div>
</div>

<h2>Was diese Firmwares mitbringen</h2>
<ul>
<li><strong>Marlin 2.1</strong>, gebaut aus den Duplicator-9-Konfigurationen, die in
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>
veröffentlicht sind, mit den dort vorgeschlagenen Änderungen: MK1-Sensor richtig herum ausgelesen, Y-Richtung der MK3,
Druckfortsetzung nach Stromausfall, Störfilter für die Endschalter.</li>
<li><strong>Wanhaos Werkseinstellungen</strong>, übernommen aus Wanhaos eigener Firmware und Quellcode für jedes Modell:
Steps/mm, Geschwindigkeiten, Beschleunigungen, Hotend-PID, Sensor-Offsets und Messränder, Referenzfahrt, thermische
Grenzwerte, Jerk und Achsrichtungen.</li>
<li><strong>Druckfortsetzung nach Stromausfall</strong>: Bei einem Druck von SD-Karte wird der Auftrag bei jedem Schichtwechsel gespeichert, und nach einem Stromausfall bietet das Display an, dort weiterzudrucken.</li>
<li><strong>Filamentsensoren</strong>: ein Filamentende-Schalter an D8, bei jedem Modell standardmäßig aktiv (ohne Schalter wirkungslos), und der BTT Smart Filament Sensor V2.0, der auch Filamentstaus erkennt. Siehe <a href="{p('sensor')}">Filamentsensor</a>.</li>
<li><strong>Der Kopf fährt nach einer Nivellierung zurück in die Mitte</strong>, sodass das Druckbett das Display nicht mehr verdeckt.</li>
<li><strong>Eine neue Touchscreen-Oberfläche in 16 Sprachen</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, mit einer Seite zum Einstellen des Filamentsensors.</li>
</ul>

<h2>Flashen in drei Schritten</h2>
<ol>
<li>Lade die <strong>.hex</strong>-Datei für dein Modell und deine Größe von dessen Seite herunter.</li>
<li>Flashe sie per USB mit AVRDUDESS oder avrdude: <a href="{p('flash')}">Flash-Anleitung</a>.</li>
<li>Flashe den Touchscreen von einer microSD-Karte: <a href="{p('screen')}">Display-Anleitung</a>.</li>
</ol>
<p>Wanhaos Original-Firmwares bleiben auf jeder Modellseite verfügbar, sodass eine Maschine jederzeit in den Auslieferungszustand zurückversetzt werden kann.</p>
""")

    if page == "mk1":
        return ("Firmware für Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin-2.1-Firmware für die Wanhao D9 MK1 mit induktivem Sensor, Wanhaos Original-Firmwares V0.15 bis V0.164(B), "
                "Displaydateien und das Benutzerhandbuch der MK1.",
                f"""
<h1>Firmware für die Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">Die erste Duplicator 9: ein induktiver Metallsensor neben der Düse, ein graues Flachbandkabel zum
Druckkopf und ein Rahmen ohne seitliche Verstrebungen.</p>
<p>Diese Builds lesen den induktiven Sensor richtig herum aus (er schaltet auf LOW) und übernehmen die Einstellungen von
Wanhaos letzter MK1-Firmware, V0.164(B), einschließlich der Sensor-Offsets (X 15, Y 0). Der Y-Motor sitzt hinten, so wie
Wanhao ihn verbaut hat.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Induktiver Sensor und Flachbandkabel am Druckkopf einer Wanhao D9 MK1">
<figcaption>MK1: induktiver Sensor, Flachbandkabel</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Nimm die Datei für deine Größe und flashe danach das Display mit
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumente von Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Benutzerhandbuch D9 MK1</a> (Juni 2018, auf Englisch): Aufbau, Verkabelung, Menüs, Nivellierung, Fehlerbehebung.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Schnellstartanleitung D9 MK1</a>.</li>
</ul>

<h2>Wanhaos Original-Firmwares</h2>
<p>Um eine Maschine in den Auslieferungszustand zurückzuversetzen. Jede Mainboard-Firmware funktioniert nur mit der
Display-Firmware derselben Version.</p>
<div class="table"><table><thead><tr><th>Version</th><th>Größe</th><th>Mainboard</th><th>Display</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Die Einstellungen jeder Version (Steps/mm, Geschwindigkeiten, PID, Achsrichtungen) stehen in
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, ausgelesen aus Wanhaos Binärdateien.</p>
""")

    if page == "mk1u2":
        return ("Firmware für Wanhao Duplicator 9 MK1 mit MK2-Upgrade-Kit (BLTouch) – Marlin 2.1",
                "Marlin-2.1-Firmware für eine Wanhao D9 MK1, nachgerüstet mit Wanhaos MK2-BLTouch-Kit, und Wanhaos Original-Firmware V1.1.31 für das Kit.",
                f"""
<h1>Wanhao D9 MK1 mit dem MK2-Upgrade-Kit</h1>
<div class="split"><div>
<p class="lead">Eine D9 der ersten Generation mit Wanhaos MK2-Upgrade-Kit: der Rahmen der MK1, mit einem BLTouch-Sensor
anstelle des induktiven Metallsensors.</p>
<p>Wanhao hat für diese Kombination eine eigene Firmware herausgebracht, weil der BLTouch des Kits nicht an derselben
Stelle sitzt wie bei einer MK2 ab Werk: Der Y-Offset des Sensors ist ein anderer. Diese Builds verwenden die Geometrie
des Kits. Der Y-Motor sitzt hinten.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="BLTouch-Sensor am Druckkopf einer Wanhao D9">
<figcaption>BLTouch-Sensor</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Nimm die Datei für deine Größe und flashe danach das Display mit
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Diese Builds verwenden den Sensor-Offset der Kit-Firmware, Y −10. Das ist die einzige Zeile, in der
sich Wanhaos Kit-Quellcode von dem der MK2 ab Werk (Y 0) unterscheidet: Der BLTouch des Kits sitzt weiter hinten. Wirkt
dein Bett-Mesh von vorne nach hinten verschoben, miss deinen eigenen Offset mit der
<a href="{REPO}/blob/main/Offset.md">Offset-Anleitung</a>.</div>

<h2>Wanhaos Original-Firmwares</h2>
<p>Wanhaos Kit-Firmware V1.1.31 (Dezember 2018), zusammen mit der Display-Firmware der MK2 verwendet.</p>
<div class="table"><table><thead><tr><th>Größe</th><th>Mainboard</th><th>Display</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Aus Wanhaos Binärdateien ausgelesene Einstellungen: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware für Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin-2.1-Firmware für die Wanhao D9 MK2 mit BLTouch, Wanhaos Original-Firmware V1.1.2 mit Displaydateien und Wanhaos Anleitungen zur MK2.",
                f"""
<h1>Firmware für die Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">Die zweite Duplicator 9: schräge Verstrebungen an beiden Seiten, ein rundes schwarzes Datenkabel zum
Druckkopf, ein BLTouch-Sensor und ein Spulenhalter oben drauf.</p>
<p>Außerdem hat Wanhao die Schlitten auf vier Rollen umgestellt, bei der 400 und 500 eine Y-Achse mit Doppelschiene und
einen dickeren Riemen verbaut und bei der 300 und 400 ein beidseitig nutzbares Druckbett. Der Y-Motor sitzt hinten;
diese Builds drehen die Y-Achse so wie Wanhaos Firmware V1.1.2.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Nimm die Datei für deine Größe. Eine MK2, deren Kopf zusätzlich auf MK3 umgerüstet wurde, sollte
die <a href="{p('mk3')}">MK3-Firmware</a> verwenden. Flashe danach das Display mit <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumente von Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Schnellstartanleitung D9 MK2</a> (auf Englisch).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">Die 12 Verbesserungen von der MK1 zur MK2</a>, von Wanhao.</li>
</ul>

<h2>Wanhaos Original-Firmwares</h2>
<p>Wanhaos V1.1.2 (Oktober 2018; die 500 wurde im Juli 2019 als V1.1.2.1 neu gebaut), mit Wanhaos Display-Firmware für die MK2.</p>
<div class="table"><table><thead><tr><th>Größe</th><th>Mainboard</th><th>Display</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Aus Wanhaos Binärdateien ausgelesene Einstellungen: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware für Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin-2.1-Firmware für die Wanhao D9 MK3 (Y-Motor vorne, Filamentsensor) und Wanhaos Original-Firmware V1.1.3.",
                f"""
<h1>Firmware für die Wanhao Duplicator 9 MK3</h1>
<p class="lead">Die letzte Duplicator 9 behält Rahmen und BLTouch der MK2, bekommt einen Filamentende-Sensor und hat
den Y-Motor vorne, auf der Seite des Touchscreens.</p>
<p>Durch den versetzten Motor dreht sich die Y-Achse andersherum: Wanhaos eigene Firmware V1.1.3 invertiert Y, und diese
Builds tun das ebenfalls. Der Filamentende-Sensor ist standardmäßig aktiv. Wanhao hat für die MK3 keine Sensor-Offsets
veröffentlicht, deshalb verwenden diese Builds die der MK2.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Nimm die Datei für deine Größe und flashe danach das Display mit
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Hält der Filamentsensor Drucke willkürlich an, schalte ihn mit <code>M412 S0</code> und dann
<code>M500</code> ab. Wanhao Europe hatte für dieses Problem eine MK3-Firmware „ReverseMode“ veröffentlicht; sie wurde
inzwischen gelöscht und war nicht mehr aufzufinden.</div>

<h2>Wanhaos Original-Firmwares</h2>
<p>Wanhaos V1.1.3 (August 2019). Wanhao hat keine Display-Firmware für die MK3 veröffentlicht: Die MK3-Downloads setzten auf die der MK2.</p>
<div class="table"><table><thead><tr><th>Größe</th><th>Mainboard</th><th>Display</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Aus Wanhaos Binärdateien ausgelesene Einstellungen: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Mainboard-Firmware der Wanhao Duplicator 9 (D9) flashen: Anleitung",
                "Schritt-für-Schritt-Anleitung: Marlin per USB mit AVRDUDESS oder avrdude auf eine Wanhao D9 flashen, "
                "Probleme bei der Referenzfahrt beheben und mit Wanhaos Firmware zurück zum Werkszustand.",
                f"""
<h1>Das Mainboard der Duplicator 9 flashen</h1>
<p class="lead">Das Mainboard der D9 hat einen ATmega2560 mit USB-Bootloader: kein Programmiergerät, kein Öffnen des
Sockels, nur ein USB-Kabel.</p>

<h2>Was du brauchst</h2>
<ul>
<li>Ein USB-Kabel zwischen Drucker und Computer, und den Drucker <strong>eingeschaltet</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, grafisch, am einfachsten) oder
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (Kommandozeile, alle Betriebssysteme).</li>
<li>Die <strong>.hex</strong>-Datei für dein Modell und deine Größe: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + Kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Vor dem Flashen</h2>
<div class="note">Sende <code>M503</code> und bewahre die Antwort auf. Seit v2.0.3 behält ein Update die im Drucker
gespeicherten Einstellungen, aber das Update <strong>auf</strong> v2.0.3 startet einmalig mit den Standardwerten dieser
Firmware (die Art, wie Einstellungen gespeichert werden, hat sich geändert), ebenso der Umstieg von Wanhaos Firmware.
Stelle danach den Z-Offset deines Sensors erneut mit <code>M851 Z…</code> und <code>M500</code> ein.</div>
<p>Schließe alle Programme, die den Port des Druckers belegen könnten: Cura, PrusaSlicer, OctoPrint, Pronterface, serielle Terminals.</p>

<h2>Flashen mit AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: der COM-Port deines Druckers (zum Beispiel <code>COM3</code>). Die Baudrate auf dem Standardwert lassen.</li>
<li>Flash: die .hex-Datei auswählen und auf <strong>Program!</strong> klicken. Das dauert 30 bis 60 Sekunden.</li>
</ol>

<h2>Flashen mit avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Ersetze Port und Dateinamen durch deine eigenen. Das Protokoll <code>wiring</code> wählt die Geschwindigkeit des Bootloaders selbst.</p>

<h2>Erster Start</h2>
<ol>
<li>USB-Kabel abziehen, den Drucker aus- und wieder einschalten, das Kabel wieder einstecken.</li>
<li>Mit <strong>250000 Baud</strong> verbinden (Wanhaos Firmwares nutzten 115200) und <code>M115</code> senden: Die Antwort zeigt die neue Firmware.</li>
<li>Alle Achsen referenzieren, dann eine Bettnivellierung über das Display oder mit <code>G29</code> ausführen und mit <code>M500</code> speichern.</li>
</ol>

<h2 id="reset">Zurück zu den Standardeinstellungen dieser Firmware</h2>
<p>Seit v2.0.3 <strong>behält</strong> ein Firmware-Update die im Drucker gespeicherten Einstellungen (Z-Offset des Sensors,
Steps/mm, PID, Mesh…). Neue Standardwerte eines Releases ersetzen die bereits gespeicherten also nicht. Setze einmal
zurück, wenn du von v2.0.2 oder älter aktualisierst und dabei von Hand gespeicherte Werte hast, wenn sich der Drucker nach
dem Ausprobieren anderer Firmwares seltsam verhält, oder immer dann, wenn du sauber neu anfangen willst:</p>
<ul>
<li><strong>Am Display:</strong> <em>Einstellungen</em> → <em>Mehr</em> → <em>Zurücksetzen</em> → ✓.</li>
<li><strong>Per USB:</strong> <code>M502</code> senden (lädt die Standardwerte dieser Firmware), dann <code>M500</code> (speichert sie).</li>
</ul>
<p>Stelle danach den Z-Offset deines Sensors erneut ein (<code>M851 Z…</code>, dann <code>M500</code>) und führe eine
Bettnivellierung aus. Prüfe das Ergebnis mit <code>M503</code>.</p>

<h2>Stromausfall und Filamentsensor</h2>
<ul>
<li>Die Druckfortsetzung nach Stromausfall ist aktiv: Der Auftrag wird bei jedem Schichtwechsel gespeichert. Abschalten mit <code>M413 S0</code>, dann <code>M500</code>.</li>
<li>Ein Druck bricht sofort mit <em>power outage</em> ab, sobald das Aufheizen beginnt: Aktualisiere auf v2.0.4 oder neuer. Frühere Builds überwachten den Stromausfall-Eingang des Boards, der auf LOW geht, sobald die Heizungen starten.</li>
<li>Die Filamentende-Erkennung ist seit v2.0.8 bei jedem Modell standardmäßig aktiv und tut ohne Sensor nichts. Nach einem Update von einem früheren Release schaltest du sie mit <code>M412 S1</code> und dann <code>M500</code> ein, oder am Display unter <em>Einstellungen</em> → <em>Filament</em> → <em>Filamentsensor</em>. Verkabelung und BTT Smart Filament Sensor: <a href="{p('sensor')}">Filamentsensor</a>.</li>
</ul>

<h2>Fehlerbehebung</h2>
<div class="table"><table><thead><tr><th>Problem</th><th>Lösung</th></tr></thead><tbody>
<tr><td>Port belegt</td><td>Alle Programme schließen, die den Port des Druckers verwenden.</td></tr>
<tr><td>Gerät nicht gefunden</td><td>Den USB-Treiber CH340 installieren, ein anderes Kabel oder einen anderen USB-Port probieren, prüfen, ob der Drucker eingeschaltet ist.</td></tr>
<tr><td>Unlesbare Zeichen nach dem Flashen</td><td>Mit diesen Firmwares 250000 Baud verwenden, mit denen von Wanhao 115200.</td></tr>
<tr><td>Temperaturen am Display ×10 angezeigt (236 für 23,6 °C)</td><td>Das Display hat noch alte Dateien: <a href="{p('screen')}">DGUS Reloaded 2.0</a> flashen.</td></tr>
<tr><td>Das Display springt bei jedem Start zurück auf Englisch, oder seine Seite <em>Filamentsensor</em> tut nichts</td><td>Die Mainboard-Firmware ist älter als v2.0.9: aktualisieren.</td></tr>
<tr><td>Die Referenzfahrt stoppt einige Millimeter vor dem Schalter, dann <em>Homing Failed</em></td><td>Elektrische Störungen auf der Endschalterleitung. Diese Firmwares filtern sie seit v2.0.1: aktualisieren.</td></tr>
<tr><td>Die Düse stößt bei der Nivellierung an eine Klammer des Druckbetts</td><td>Auf v2.0.2 oder neuer aktualisieren: Die erste Messpunktspalte liegt 10 mm vom Rand entfernt, wie in Wanhaos Firmware.</td></tr>
<tr><td>Das Bett fährt vom Y-Endschalter weg</td><td>Prüfen, ob du die Firmware für dein Modell genommen hast: Der Y-Motor sitzt bei MK1, MK1 + Kit und MK2 hinten, bei der MK3 vorne.</td></tr>
</tbody></table></div>

<h2>Zurück zu Wanhaos Firmware</h2>
<p>Jede Modellseite verlinkt Wanhaos Original-Firmwares für Mainboard und Display. Sie werden genauso geflasht; Wanhaos
Mainboard-Firmware braucht Wanhaos Display-Firmware derselben Generation.</p>
<p>Fragen: <a href="{DISCORD}">Discord</a> oder <a href="{REPO}/issues">GitHub-Issues</a>.</p>
""")

    if page == "screen":
        return ("Touchscreen-Firmware der Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 in 16 Sprachen",
                "So flashst du den DWIN-Touchscreen der Wanhao D9 mit DGUS Reloaded 2.0 von einer microSD-Karte: neue Oberfläche in 16 "
                "Sprachen, Seite für den Filamentsensor, für Marlin 2.1. Und so geht es zurück zu Wanhaos Display-Firmware.",
                f"""
<h1>Den Touchscreen der Duplicator 9 flashen</h1>
<p class="lead">Jede D9, von MK1 bis MK3, hat denselben DWIN-T5-Touchscreen (480 × 272). Mit diesen Firmwares läuft darauf
DGUS Reloaded 2.0, unsere neue Oberfläche in 16 Sprachen, die von einer microSD-Karte geflasht wird.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">DWIN_SET.zip herunterladen (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Was DGUS Reloaded 2.0 mitbringt</h2>
<ul>
<li><strong>16 Sprachen</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Zum Wechseln auf dem Startbildschirm die Flagge neben dem
Druckernamen antippen; der Drucker merkt sich die Wahl.</li>
<li><strong>Eine Seite für den Filamentsensor</strong>: <em>Einstellungen</em> → <em>Filament</em> → <em>Filamentsensor</em>. Siehe
<a href="{p('sensor')}#screen">Filamentsensor</a>.</li>
<li><strong>Eine Statuszeile, die stehen bleibt</strong>: Die letzte Meldung, zum Beispiel <em>Ready</em>, bleibt auf dem
Display, statt nach 30 Sekunden zu verschwinden.</li>
<li><strong>Temperaturanzeigen</strong> für Düse und Druckbett, mit markierter Solltemperatur.</li>
<li>Ein neues Aussehen für jede Seite: dunkles Design, größere Schaltflächen, Piktogramme in den Pop-ups.</li>
</ul>
</div><figure><img src="{img}screen/de-home.png" width="480" height="272" alt="Startbildschirm von DGUS Reloaded 2.0 auf einer Wanhao D9: Düsen- und Betttemperatur mit Anzeigen, Statuszeile, Schaltflächen Drucken, Temperatur und Einstellungen">
<figcaption>Der Startbildschirm</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 braucht <strong>v2.0.9 oder neuer</strong> auf dem Mainboard. Mit v2.0.8 oder älter springt
die Sprache bei jedem Start zurück auf Englisch, und die Seite für den Filamentsensor funktioniert nicht: zuerst
<a href="{p('flash')}">das Mainboard flashen</a>.</div>

<h2>1. Die microSD-Karte formatieren</h2>
<div class="note">FAT32 mit einer Größe der Zuordnungseinheit von <strong>4096 Bytes</strong>. Bei jeder anderen Größe ignoriert das Display die Karte.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 formatiert oft nicht in FAT32; nimm <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
und stelle die Größe der Zuordnungseinheit auf 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (vorher das Gerät mit <code>lsblk</code> prüfen).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (mit <code>diskutil list</code> prüfen).</li>
</ul>

<h2>2. Die Dateien kopieren</h2>
<p>Entpacke <code>DWIN_SET.zip</code> und kopiere den ganzen Ordner <code>DWIN_SET</code> ins Stammverzeichnis der Karte.</p>

<h2>3. Flashen</h2>
<ol>
<li>Den Drucker ausschalten und den Netzstecker ziehen.</li>
<li>Die Vorderseite des Sockels öffnen, um an die Rückseite des Displays zu kommen, wo sich sein microSD-Steckplatz befindet.</li>
<li>Die Karte einstecken und einschalten. Das Display zeigt das Update nach 10 bis 30 Sekunden an; warten, bis es wieder
normal startet, insgesamt 1 bis 3 Minuten.</li>
<li>Ausschalten, die Karte entnehmen, den Sockel schließen.</li>
</ol>
<p>Wanhaos <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">Video zum Display-Update einer D9</a> zeigt, wo der Steckplatz sitzt.</p>

<h2>Woher es stammt</h2>
<p>DGUS Reloaded 2.0 zeichnet <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(von Desuuuu, dann Neo2003) Seite für Seite neu. Der Quellcode, das Programm, das die Displaydateien erzeugt, und die
Übersetzungen liegen auf <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Ein falsches oder holpriges Wort
in deiner Sprache? Sag es uns auf <a href="{DISCORD}">Discord</a> oder eröffne dort ein Issue.</p>
<p>Um zu DGUS Reloaded 1.0.3 zurückzukehren, zum Beispiel mit einer Firmware älter als v2.0.9, flashe
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> auf dieselbe Weise.</p>

<h2>Zurück zu Wanhaos Display</h2>
<p>Wanhaos Display-Firmware funktioniert nur mit Wanhaos Mainboard-Firmware. MK1: die Displaydatei der passenden
Version auf der <a href="{p('mk1')}">MK1-Seite</a>. MK1 + Kit, MK2 und MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Gleiches Vorgehen.</p>
""")

    if page == "sensor":
        return ("Filamentsensoren an der Wanhao Duplicator 9: Filamentende-Schalter und Anschluss des BTT Smart Filament Sensor",
                "Wo ein Filamentsensor am Mainboard der Wanhao D9 angeschlossen wird (D8, D9, GND, 5V), wie ein BTT Smart "
                "Filament Sensor V2.0 verkabelt wird und wie man Filamentende- und Stauerkennung mit M412 einschaltet.",
                f"""
<h1>Filamentsensoren</h1>
<p class="lead">Ab v2.0.5 lesen diese Firmwares zwei Arten von Sensoren: Wanhaos Filamentende-Schalter und den
BTT Smart Filament Sensor V2.0, der auch bemerkt, wenn sich das Filament nicht mehr bewegt (verhedderte Spule, Stau,
abgeschliffenes Filament). <strong>Die Filamentende-Erkennung ist bei jedem Modell standardmäßig aktiv</strong>, die
Stauerkennung ist aus.</p>

<h2>Der Sensorstecker</h2>
<figure><img src="{img}d9-sensor-plug-de.svg" width="760" height="440" alt="Mainboard der Wanhao D9: der 4-polige Sensorstecker links von POWER-DET, Pins D9, D8, GND und 5V, verkabelt mit einem BTT Smart Filament Sensor V2.0"></figure>
<p>Der 4-polige Stecker links von <strong>POWER-DET</strong>, unterhalb der Endschalter-Stecker, führt <strong>D9, D8, GND und 5V</strong>,
in dieser Reihenfolge. Die Pin-Namen stammen aus einem Anschlussplan von Wanhao, den dustovich gefunden und auf dem
<a href="{DISCORD}">Discord</a> geteilt hat; auf der Rückseite des Boards sind dieselben vier Pins als CTRL, BTN, GND und VCC beschriftet.</p>
<ul>
<li><strong>D8</strong> ist der Filamentende-Eingang, den Wanhaos eigene Firmware liest.</li>
<li><strong>D9</strong> wird von Wanhaos Firmware nicht genutzt: Diese Builds lesen dort das Bewegungssignal des BTT-Sensors.</li>
</ul>
<div class="note">Drucker <strong>ausschalten</strong>, bevor du etwas am Board ansteckst oder abziehst.</div>

<h2 id="screen">Am Display</h2>
<div class="split"><div>
<p>Mit DGUS Reloaded 2.0 auf dem Display (Firmware v2.0.9 oder neuer): <em>Einstellungen</em> → <em>Filament</em> →
<em>Filamentsensor</em>.</p>
<ul>
<li><strong>Filamentende</strong> schaltet die gesamte Erkennung ein oder aus, wie <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Stauerkennung</strong> schaltet die Stauerkennung mit der darunter eingestellten Länge ein oder aus (<code>L0</code>).</li>
<li><strong>Staulänge</strong>: − und + ändern sie um 1 mm; die Zahl antippen, um sie einzutippen.</li>
<li>Der Punkt <strong>Filament</strong> ist grün, solange der Filamentende-Schalter Filament erkennt, und rot, wenn nicht.</li>
<li>Änderungen wirken sofort. <strong>Speichern</strong> speichert sie dauerhaft, wie <code>M500</code>. Der Zurück-Pfeil verlässt die Seite
ohne zu speichern: Beim nächsten Start gelten wieder die gespeicherten Einstellungen.</li>
</ul>
</div><figure><img src="{img}screen/de-sensor.png" width="480" height="272" alt="Filamentsensor-Seite von DGUS Reloaded 2.0: Schalter für Filamentende- und Stauerkennung, Staulänge mit Minus- und Plus-Schaltflächen, Filamentanzeige und Schaltfläche Speichern">
<figcaption>Einstellungen → Filament → Filamentsensor</figcaption></figure></div>

<h2>Die M412-Befehle</h2>
<p>Alles wird per USB über ein serielles Terminal eingestellt (Pronterface, das Terminal deines Slicers oder von OctoPrint,
250000 Baud). Parameter lassen sich in einem Befehl kombinieren, zum Beispiel <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Befehl</th><th>Was er bewirkt</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Zeigt den Status an, zum Beispiel <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Schaltet die Erkennung ein</strong>: den Filamentende-Schalter und, wenn die Staulänge nicht 0 ist, auch die Stauerkennung.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Schaltet die gesamte Erkennung aus</strong>, Schalter und Stau.</td></tr>
<tr><td><code>M412 D5</code></td><td>Sobald der Schalter kein Filament mehr erkennt, wird noch <strong>5 mm</strong> weitergedruckt, bevor pausiert wird, um das Filament zwischen Sensor und Düse aufzubrauchen. Standard 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Schaltet die Stauerkennung ein</strong> (nur BTT-Sensor): pausiert, wenn <strong>10 mm</strong> Filament durch den Extruder gehen, ohne dass sich das Rad des Sensors dreht.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Schaltet die Stauerkennung aus</strong> und lässt den Filamentende-Schalter, wie er ist. Das ist die Standardeinstellung.</td></tr>
<tr><td><code>M500</code></td><td>Speichert die Einstellungen. Ohne diesen Befehl geht eine Änderung beim Ausschalten des Druckers verloren.</td></tr>
<tr><td><code>M119</code></td><td>Die Zeile <em>filament</em> zeigt <code>TRIGGERED</code> mit eingelegtem Filament, <code>open</code> ohne.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code> und <code>L</code> allein stammen aus unserer Änderung an Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), die in diese Firmwares eingebaut ist. In Marlin ohne sie wird <code>L</code>
allein ignoriert, und <code>L0</code> pausiert den Druck sofort wegen eines Staus.</p>

<h2>Wanhaos Filamentende-Schalter</h2>
<p>Er meldet der Firmware, ob Filament vorhanden ist. Fehlt es, pausiert der Druck nach weiteren 5 mm Filament, und das
Display startet einen Filamentwechsel.</p>
<p><strong>Er ist seit v2.0.8 bei jedem Modell standardmäßig aktiv.</strong> Ist an D8 nichts angeschlossen, hält der
Pull-up-Widerstand des Boards den Pin auf 5 V, was als „Filament vorhanden“ gelesen wird: Die Erkennung löst dann nie aus,
sie kann also aktiv bleiben, ob ein Sensor verbaut ist oder nicht. Schließt man einen Filamentende-Schalter an D8 an,
funktioniert er sofort.</p>
<ul>
<li>Die Stauerkennung bleibt aus (<code>L0</code>): Dieser Schalter kann nicht sehen, ob sich das Filament bewegt.</li>
<li>Um den Schalter abzuschalten: <code>M412 S0</code>, dann <code>M500</code>.</li>
<li>Von einem früheren Release gespeicherte Einstellungen behalten ihren Ein/Aus-Zustand. Zum Einschalten: <code>M412 S1</code>, dann
<code>M500</code>, oder auf die Standardwerte zurücksetzen (<code>M502</code>, dann <code>M500</code>, was auch den Z-Offset deines
Sensors und das Mesh löscht).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Dieser Sensor hat zwei Ausgänge, und die Firmware liest sie unterschiedlich:</p>
<ul>
<li><strong>Der Filamentende-Schalter</strong> (an D8) liefert einen Pegel: 5 V, solange Filament da ist, 0 V, sobald es weg ist.</li>
<li><strong>Der Bewegungsausgang</strong> (an D9) kommt von einem kleinen Rad, das das durchlaufende Filament dreht. Alle paar
Millimeter Filament wechselt der Ausgang zwischen 0 V und 5 V. Die Firmware achtet nur auf diese Wechsel: Schiebt der
Extruder die Staulänge an Filament durch, ohne dass ein einziger kommt, folgt das Filament nicht (verhedderte Spule, Stau,
abgeschliffenes Filament), und der Druck pausiert. Der Filamentende-Schalter kann das nicht erkennen: Bei einem Stau ist das Filament ja noch da.</li>
</ul>
<h3>Verkabelung</h3>
<p><strong>5V</strong> an 5V, <strong>GND</strong> an GND, das Signal des <strong>Filamentende-Schalters</strong> an <strong>D8</strong>
und das <strong>Bewegungssignal</strong> an <strong>D9</strong>. Die Bezeichnungen am Kabel des Sensors können abweichen.</p>
<h3>Einschalten</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Pausieren Drucke ohne Grund, erhöhe die Staulänge: <code>M412 L15</code>, dann <code>M500</code>. Um nur den
Filamentende-Schalter zu behalten: <code>M412 L0</code>, dann <code>M500</code>.</p>
<h3>Prüfen</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> mit eingelegtem Filament: <em>filament: TRIGGERED</em>. Ändert sich diese Zeile, wenn du Filament von Hand
durchschiebst, statt beim Einlegen oder Herausziehen, sind die beiden Signalleitungen vertauscht: D8 und D9 tauschen.</li>
</ul>
<div class="note">Die Stauerkennung wurde an einer MK2 300 ohne den Sensor getestet (eine Staulänge von 2 mm löst aus, <code>L0</code> nie),
aber noch nicht mit dem BTT-Sensor selbst. Wird der Schalter falsch herum gelesen (<em>open</em> mit eingelegtem
Filament), sag uns auf <a href="{DISCORD}">Discord</a> Bescheid.</div>

<h2>Update von v2.0.5 oder v2.0.6</h2>
<p>Diese Releases konnten die Stauerkennung nicht abschalten und nutzten daher eine Staulänge, die nie erreicht werden sollte: 100 m in
v2.0.5 (tatsächlich zu kurz: etwa ein Drittel einer 1-kg-Spule, danach konnte ein eingeschaltet gelassener Drucker grundlos pausieren) und
10 km in v2.0.6. Beim Start des Druckers lädt v2.0.7 diese beiden Werte als <code>L0</code>. Eine echte Länge, die du
für einen BTT-Sensor eingestellt hast, etwa <code>L10</code>, bleibt erhalten. Von v2.0.4 oder älter wird die Filamentende-Distanz
von 5 mm geladen statt der 0, die diese Versionen gespeichert haben.</p>
""")

    if page == "quiet":
        return ("Wanhao Duplicator 9 leiser machen: welche Lüfter, und der Mainboard-Lüfter mit NTC-Thermistoren",
                "Welche Lüfter der Wanhao D9 sich leiser machen lassen: Der Hotend-Lüfter muss bleiben, der Netzteillüfter "
                "regelt sich bereits selbst, und der Mainboard-Lüfter kann abgesteckt oder über NTC-Thermistoren betrieben werden.",
                f"""
<h1>Die Duplicator 9 leiser machen</h1>
<p class="lead">Im Ruhezustand kommt das Geräusch der D9 von ihren Lüftern. Hier steht, welcher leiser werden kann und wie.</p>
<div class="note">Nur mit <strong>ausgestecktem</strong> Drucker arbeiten. Alle Leitungen von der 230-V-Seite fernhalten.</div>

<h2>Die Lüfter</h2>
<div class="table"><table class="stack"><thead><tr><th>Lüfter</th><th>Gesteuert von</th><th>Lässt er sich leiser machen?</th></tr></thead><tbody>
<tr><td><strong>Hotend-Kühlkörperlüfter</strong> (Druckkopf)</td><td>nichts: 24 V, immer an</td><td><strong>nein</strong>: meist der lauteste, aber wird er langsamer, steigt die Wärme im Hotend nach oben und das Filament verstopft (Heat Creep)</td></tr>
<tr><td><strong>Bauteillüfter</strong> (Druckkopf)</td><td>Firmware, Pin D5 (PWM)</td><td>bereits regelbar: gesteuert vom Slicer und von <code>M106</code></td></tr>
<tr><td><strong>Netzteillüfter</strong></td><td>das Netzteil selbst</td><td>nichts zu tun: Beim hier geprüften Gerät (Chuanglian A-350FAK-24) folgt er bereits der Temperatur des Netzteils</td></tr>
<tr><td><strong>Mainboard-Lüfter</strong> (Elektronikgehäuse)</td><td>nichts: 24 V, immer an</td><td><strong>ja</strong>, siehe unten</td></tr>
</tbody></table></div>
<p>Wanhaos Firmware steuert weder einen Mainboard-Lüfter noch einen Hotend-Lüfter (<code>CONTROLLER_FAN_PIN</code> und
<code>E0_AUTO_FAN_PIN</code> sind beide <code>-1</code>), und das Board hat keinen freien schaltbaren Ausgang. Deshalb hängen
diese beiden an den dauerhaft versorgten „24V OUT“-Anschlüssen, und deshalb kann keine Firmware sie verlangsamen.</p>

<h2>Mainboard-Lüfter</h2>
<p>Beim hier vermessenen Exemplar: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max., Gleitlager</strong>.</p>
<p><strong>Viele Besitzer stecken ihn einfach ab.</strong> Das Board bleibt kühl: Es sitzt unten im Elektronikgehäuse, unter
dem beheizten Druckbett, und die Wärme des Betts steigt von ihm weg nach oben. Wenn du das machst, behalte deine ersten langen
Drucke im Auge: Ein überhitzter Schrittmotortreiber schaltet kurz ab, was sich als <strong>Schichtversatz</strong> zeigt, nicht
als Fehlermeldung.</p>
<h3>Ihn behalten, aber nur, wenn die Treiber warm sind</h3>
<p>Zwei Leistungs-NTC-Thermistoren in Reihe lassen den Lüfter bei etwa 45–50 °C anlaufen und schneller werden, je wärmer
die Treiber werden: <strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), mit Wärmeleitkleber auf einen
Treiberkühlkörper geklebt, Anschlussdrähte isoliert.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── Lüfter (+)
                                    Lüfter (−) ── 0V</code></pre>
<ul>
<li>Das ist eine Berechnung, <strong>noch nicht an einem Drucker getestet</strong>: Die Toleranz der MF72 liegt bei ±20 %, und
ein kleiner Lüfter kann schon bei einer niedrigeren Temperatur als erwartet anlaufen. Prüfe die Anlauftemperatur auf dem Tisch (NTCs in einem kleinen Beutel
in heißem Wasser, mit einem Küchenthermometer); füge einen zweiten 200-Ω-NTC hinzu, wenn er zu früh anläuft, lass den 200-Ω-NTC
weg, wenn zu spät.</li>
<li>Die NTCs müssen auf einen Kühlkörper geklebt sein: An freier Luft erwärmt der Lüfterstrom (bis etwa 0,6 W in den NTCs) sie um
mehrere zehn Grad.</li>
<li>Der Lüfter erreicht so nie die volle Drehzahl (etwa 75 % bei 80 °C), und ein ausfallender NTC wird hochohmig: Der Lüfter
steht dann dauerhaft still.</li>
</ul>
<p>Quellen: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">Datenblatt MF72</a>.</p>
""")
    raise KeyError(page)
