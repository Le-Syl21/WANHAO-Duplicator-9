"""Nederlands: vertaling van en.py."""

META = {"name": "Nederlands", "locale": "nl_NL", "dir": "ltr"}

UI = {
    "nav": {"index": "Home", "mk1": "MK1", "mk1u2": "MK1 + MK2-kit", "mk2": "MK2", "mk3": "MK3",
            "flash": "Flashhandleiding", "screen": "Scherm", "sensor": "Filamentsensor", "slicer": "Slicer",
            "quiet": "Stiller"},
    "language": "Taal",
    "model": "Model",
    "size": "Formaat", "volume": "Bouwvolume", "file": "Firmware",
    "footer_src": "Broncode en issues op GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware onder GNU GPL v3. De handleidingen en firmwares van Wanhao blijven eigendom van Wanhao.",
}

# Labels van het aansluitschema (img/d9-sensor-plug-<taal>.svg).
SVG = {
    "board": "Moederbord Wanhao D9 (bovenaanzicht)",
    "plug": "sensorconnector",
    "switch": "filamentschakelaar",
    "motion": "beweging",
    "level": "niveau: filament aanwezig / weg",
    "pulses": "pulsen zolang het filament beweegt",
    "names": "de namen op je sensor kunnen afwijken",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware voor de Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Actuele Marlin-firmware voor elke Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "schermbestanden, de originele firmwares en handleidingen van Wanhao, en hoe je ze flasht.",
                f"""
<h1>Firmware voor de Wanhao Duplicator 9</h1>
<p class="lead">De downloadsite van Wanhao voor de Duplicator 9 bestaat niet meer. Alles wat een D9-bezitter nodig heeft,
staat nu hier: actuele Marlin 2.1-firmware voor elk model en elk formaat, de bijbehorende touchscreenbestanden, de
originele firmwares van Wanhao, de handleidingen van Wanhao en stapsgewijze handleidingen om te flashen.</p>
<p><a class="btn" href="{REPO}/releases/latest">Alle downloads</a> <a class="btn ghost" href="{DISCORD}">Vraag het op Discord</a></p>

<h2>Welke D9 heb ik?</h2>
<div class="split"><div>
<ol>
<li>Een <strong>grijze platte lintkabel</strong> naar de printkop, een <strong>cilindervormige metalen sensor</strong>
naast de nozzle en geen verstevigingen aan de zijkanten van het frame: <a href="{p('mk1')}">MK1</a>.</li>
<li>Dezelfde machine van de eerste generatie, maar met een <strong>witte BLTouch-sensor</strong> in plaats van de
metalen: een MK1 met de upgradekit van Wanhao, <a href="{p('mk1u2')}">MK1 + MK2-kit</a>.</li>
<li><strong>Schuine verstevigingsribben</strong> aan beide kanten van het frame, een <strong>ronde zwarte kabel</strong>
naar de kop en een BLTouch: een MK2 of een MK3. Kijk onder het bed naar de <strong>Y-motor</strong>, de motor die het
bed beweegt: zit hij achteraan, dan is het een <a href="{p('mk2')}">MK2</a>; zit hij vooraan, aan de kant van het
touchscreen, dan is het een <a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Het getal na D9 is het formaat: D9/300, D9/400 of D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 met de verstevigingsribben aan de zijkanten">
<figcaption>D9 MK2: ribben aan de zijkanten, ronde kabel</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Inductieve sensor, lintkabel. Firmware, Wanhao V0.15 tot V0.164(B), handleiding.</p><a class="more" href="{p('mk1')}">MK1-firmware →</a></div>
<div class="card"><h3>D9 MK1 + MK2-kit</h3><p>MK1 met de BLTouch-kit geüpgraded. Firmware en Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Kitfirmware →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, ribben aan de zijkanten. Firmware, Wanhao V1.1.2, handleidingen.</p><a class="more" href="{p('mk2')}">MK2-firmware →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y-motor vooraan, filamentsensor. Firmware en Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3-firmware →</a></div>
</div>

<h2>Wat deze firmwares bieden</h2>
<ul>
<li><strong>Marlin 2.1</strong>, gebouwd uit de Duplicator 9-configuraties die gepubliceerd zijn in
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
met de wijzigingen die daar zijn voorgesteld: MK1-sensor op de juiste manier uitgelezen, Y-richting van de MK3, hervatten na
stroomuitval, ruisfilter voor de eindschakelaars.</li>
<li><strong>De fabrieksinstellingen van Wanhao</strong>, overgenomen uit de eigen firmware en broncode van Wanhao voor elk model: steps/mm,
snelheden, versnellingen, hotend-PID, sensor-offsets en meetmarges, homing, temperatuurgrenzen, jerk en asrichtingen.</li>
<li><strong>Hervatten na stroomuitval</strong>: tijdens een print vanaf de SD-kaart wordt de opdracht bij elke laagwissel opgeslagen, en na een stroomuitval biedt het scherm aan om vanaf daar verder te gaan.</li>
<li><strong>Filamentsensoren</strong>: een filamentschakelaar op D8, standaard aan op elk model (zonder schakelaar heeft dat geen effect), en de BTT Smart Filament Sensor V2.0, die ook verstoppingen opmerkt. Zie <a href="{p('sensor')}">Filamentsensor</a>.</li>
<li><strong>De kop keert na het nivelleren terug naar het midden</strong>, zodat het bed het scherm niet meer afdekt.</li>
<li><strong>Een nieuwe touchscreeninterface in 16 talen</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, met een pagina om de filamentsensor in te stellen.</li>
</ul>

<h2>Flashen in drie stappen</h2>
<ol>
<li>Download de <strong>.hex</strong> voor je model en formaat op de pagina van dat model.</li>
<li>Flash hem via USB met AVRDUDESS of avrdude: <a href="{p('flash')}">flashhandleiding</a>.</li>
<li>Flash het touchscreen vanaf een microSD-kaart: <a href="{p('screen')}">schermhandleiding</a>.</li>
</ol>
<p>De originele firmwares van Wanhao blijven beschikbaar op elke modelpagina, zodat een machine altijd terug kan naar de fabrieksstaat.</p>
""")

    if page == "mk1":
        return ("Firmware voor de Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1-firmware voor de Wanhao D9 MK1 met inductieve sensor, de originele Wanhao-firmwares V0.15 tot V0.164(B), "
                "schermbestanden en de gebruikershandleiding van de MK1.",
                f"""
<h1>Firmware voor de Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">De eerste Duplicator 9: een metalen inductieve sensor naast de nozzle, een grijze lintkabel naar de
printkop en een frame zonder ribben aan de zijkanten.</p>
<p>Deze builds lezen de inductieve sensor op de juiste manier uit (hij schakelt LOW) en nemen de instellingen over van
de laatste MK1-firmware van Wanhao, V0.164(B), inclusief de sensor-offsets (X 15, Y 0). De Y-motor zit achteraan, zoals
Wanhao hem heeft gemonteerd.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Inductieve sensor en lintkabel op de printkop van een Wanhao D9 MK1">
<figcaption>MK1: inductieve sensor, lintkabel</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Neem het bestand voor jouw formaat en flash daarna het scherm met
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documenten van Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Gebruikershandleiding D9 MK1</a> (juni 2018, in het Engels): montage, bekabeling, menu's, nivelleren, problemen oplossen.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Snelstartgids D9 MK1</a>.</li>
</ul>

<h2>Originele firmwares van Wanhao</h2>
<p>Om een machine terug te zetten zoals hij de fabriek verliet. Elke moederbordfirmware werkt alleen met de schermfirmware
van dezelfde versie.</p>
<div class="table"><table><thead><tr><th>Versie</th><th>Formaat</th><th>Moederbord</th><th>Scherm</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>De instellingen van elke versie (steps/mm, snelheden, PID, asrichtingen) staan in
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, uitgelezen uit de binaire bestanden van Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware voor de Wanhao Duplicator 9 MK1 met MK2-upgradekit (BLTouch) – Marlin 2.1",
                "Marlin 2.1-firmware voor een Wanhao D9 MK1 met de MK2 BLTouch-kit van Wanhao, en de originele Wanhao-kitfirmware V1.1.31.",
                f"""
<h1>Wanhao D9 MK1 met de MK2-upgradekit</h1>
<div class="split"><div>
<p class="lead">Een D9 van de eerste generatie met de MK2-upgradekit van Wanhao: het frame van de MK1, met een BLTouch-sensor
in plaats van de metalen inductieve sensor.</p>
<p>Wanhao bracht voor deze combinatie een aparte firmware uit, omdat de BLTouch van de kit niet op dezelfde plek zit als
die van een MK2 af fabriek: de Y-offset van de sensor is anders. Deze builds gebruiken de geometrie van de kit. De Y-motor
zit achteraan.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="BLTouch-sensor op de printkop van een Wanhao D9">
<figcaption>BLTouch-sensor</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Neem het bestand voor jouw formaat en flash daarna het scherm met
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Deze builds gebruiken de sensor-offset van de kitfirmware, Y −10. Dat is de enige regel waarin de
kitbroncode van Wanhao verschilt van die van de MK2 af fabriek (Y 0): de BLTouch van de kit zit verder naar achteren. Lijkt je
bedmesh van voor naar achter verschoven, meet dan je eigen offset met de
<a href="{REPO}/blob/main/Offset.md">offsethandleiding</a>.</div>

<h2>Originele firmwares van Wanhao</h2>
<p>De kitfirmware V1.1.31 van Wanhao (december 2018), gebruikt met de schermfirmware van de MK2.</p>
<div class="table"><table><thead><tr><th>Formaat</th><th>Moederbord</th><th>Scherm</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Instellingen uitgelezen uit de binaire bestanden van Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware voor de Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1-firmware voor de Wanhao D9 MK2 met BLTouch, de originele Wanhao-firmware V1.1.2 met schermbestanden, en de MK2-handleidingen van Wanhao.",
                f"""
<h1>Firmware voor de Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">De tweede Duplicator 9: schuine verstevigingsribben aan beide kanten, een ronde zwarte datakabel naar de
printkop, een BLTouch-sensor en een spoelhouder bovenop.</p>
<p>Wanhao zette de sleden ook op vier wieltjes, gaf de 400 en 500 een Y-as met dubbele rail en een dikkere riem, en de
300 en 400 een dubbelzijdig bed. De Y-motor zit achteraan; deze builds laten de Y-as draaien zoals de firmware V1.1.2
van Wanhao dat doet.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Neem het bestand voor jouw formaat. Een MK2 waarvan de kop ook naar de MK3 is geüpgraded, gebruikt
de <a href="{p('mk3')}">MK3-firmware</a>. Flash daarna het scherm met <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documenten van Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Snelstartgids D9 MK2</a> (in het Engels).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">De 12 verbeteringen van MK1 naar MK2</a>, door Wanhao.</li>
</ul>

<h2>Originele firmwares van Wanhao</h2>
<p>V1.1.2 van Wanhao (oktober 2018; de 500 werd in juli 2019 opnieuw gebouwd als V1.1.2.1), met de MK2-schermfirmware van Wanhao.</p>
<div class="table"><table><thead><tr><th>Formaat</th><th>Moederbord</th><th>Scherm</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Instellingen uitgelezen uit de binaire bestanden van Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware voor de Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1-firmware voor de Wanhao D9 MK3 (Y-motor vooraan, filamentsensor) en de originele Wanhao-firmware V1.1.3.",
                f"""
<h1>Firmware voor de Wanhao Duplicator 9 MK3</h1>
<p class="lead">De laatste Duplicator 9 houdt het frame en de BLTouch van de MK2, krijgt er een filamentsensor bij en heeft
de Y-motor naar voren verplaatst, aan de kant van het touchscreen.</p>
<p>Door de verplaatste motor draait de Y-as andersom: de eigen firmware V1.1.3 van Wanhao keert Y om, en deze builds ook. De
filamentsensor staat standaard aan. Wanhao publiceerde geen sensor-offsets voor de MK3, dus deze builds gebruiken die van
de MK2.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Neem het bestand voor jouw formaat en flash daarna het scherm met
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Stopt de filamentsensor prints willekeurig, zet hem dan uit met <code>M412 S0</code> en daarna
<code>M500</code>. Wanhao Europe had voor dat probleem een MK3-firmware “ReverseMode” gepubliceerd; die is inmiddels
verwijderd en was niet meer te vinden.</div>

<h2>Originele firmwares van Wanhao</h2>
<p>V1.1.3 van Wanhao (augustus 2019). Wanhao publiceerde geen schermfirmware voor de MK3: de MK3-downloads gingen uit van die van de MK2.</p>
<div class="table"><table><thead><tr><th>Formaat</th><th>Moederbord</th><th>Scherm</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Instellingen uitgelezen uit de binaire bestanden van Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Zo flash je de moederbordfirmware van een Wanhao Duplicator 9 (D9)",
                "Stapsgewijze handleiding om Marlin via USB met AVRDUDESS of avrdude op een Wanhao D9 te flashen, "
                "homingproblemen op te lossen en terug te gaan naar de firmware van Wanhao.",
                f"""
<h1>Het moederbord van de Duplicator 9 flashen</h1>
<p class="lead">Het moederbord van de D9 is een ATmega2560 met een USB-bootloader: geen programmer, de voet hoeft niet
open, alleen een USB-kabel.</p>

<h2>Wat je nodig hebt</h2>
<ul>
<li>Een USB-kabel tussen de printer en de computer, en de printer <strong>ingeschakeld</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, grafisch, het makkelijkst) of
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (opdrachtregel, elk besturingssysteem).</li>
<li>De <strong>.hex</strong> voor je model en formaat: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Voor het flashen</h2>
<div class="note">Stuur <code>M503</code> en bewaar het antwoord. Sinds v2.0.3 blijven bij een update de instellingen in de
printer bewaard, maar een update <strong>naar</strong> v2.0.3 begint eenmalig met de standaardwaarden van deze firmware (de
manier waarop instellingen worden opgeslagen is veranderd), en dat geldt ook als je van de firmware van Wanhao komt. Stel
daarna de Z-offset van je sensor opnieuw in met <code>M851 Z…</code> en <code>M500</code>.</div>
<p>Sluit alle programma's die de poort van de printer bezet kunnen houden: Cura, PrusaSlicer, OctoPrint, Pronterface, seriële terminals.</p>

<h2>Flashen met AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: de COM-poort van je printer (bijvoorbeeld <code>COM3</code>). Laat de baudrate op de standaardwaarde staan.</li>
<li>Flash: kies het .hex-bestand en klik op <strong>Program!</strong>. Dat duurt 30 tot 60 seconden.</li>
</ol>

<h2>Flashen met avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Vervang de poort en de bestandsnaam door die van jou. Het protocol <code>wiring</code> kiest zelf de snelheid van de bootloader.</p>

<h2>Eerste keer opstarten</h2>
<ol>
<li>Haal de USB-kabel los, zet de printer uit en weer aan, en sluit de kabel weer aan.</li>
<li>Maak verbinding op <strong>250000 baud</strong> (de firmwares van Wanhao gebruikten 115200) en stuur <code>M115</code>: het antwoord toont de nieuwe firmware.</li>
<li>Home alle assen, nivelleer daarna het bed via het scherm of met <code>G29</code>, en sla op met <code>M500</code>.</li>
</ol>

<h2 id="reset">Terug naar de standaardinstellingen van deze firmware</h2>
<p>Sinds v2.0.3 <strong>blijven</strong> bij een firmware-update de instellingen in de printer bewaard (Z-offset van de sensor,
steps/mm, PID, mesh…). Nieuwe standaardwaarden in een release vervangen dus niet de waarden die al zijn opgeslagen. Reset
één keer als je bijwerkt vanaf v2.0.2 of ouder en met de hand opgeslagen waarden hebt, als de printer zich vreemd gedraagt
nadat je andere firmwares hebt geprobeerd, of wanneer je schoon wilt beginnen:</p>
<ul>
<li><strong>Op het scherm:</strong> <em>Instellingen</em> → <em>Meer</em> → <em>Resetten</em> → ✓.</li>
<li><strong>Via USB:</strong> stuur <code>M502</code> (laadt de standaardwaarden van deze firmware) en daarna <code>M500</code> (slaat ze op).</li>
</ul>
<p>Stel daarna de Z-offset van je sensor opnieuw in (<code>M851 Z…</code> en daarna <code>M500</code>) en nivelleer het bed. Controleer het
resultaat met <code>M503</code>.</p>

<h2>Stroomuitval en filamentsensor</h2>
<ul>
<li>Hervatten na stroomuitval staat aan: de opdracht wordt bij elke laagwissel opgeslagen. Zet het uit met <code>M413 S0</code> en daarna <code>M500</code>.</li>
<li>Een print die meteen stopt met <em>power outage</em> zodra hij opwarmt: werk bij naar v2.0.4 of nieuwer. Eerdere builds bewaakten de stroomuitvalingang van het bord, die laag wordt zodra de verwarmingen aangaan.</li>
<li>Detectie van einde filament staat sinds v2.0.8 standaard aan op elk model, en doet niets zonder sensor. Na een update vanaf een eerdere release zet je hem aan met <code>M412 S1</code> en daarna <code>M500</code>, of op het scherm onder <em>Instellingen</em> → <em>Filament</em> → <em>Filamentsensor</em>. Aansluiten en de BTT Smart Filament Sensor: <a href="{p('sensor')}">Filamentsensor</a>.</li>
</ul>

<h2>Problemen oplossen</h2>
<div class="table"><table><thead><tr><th>Probleem</th><th>Oplossing</th></tr></thead><tbody>
<tr><td>Poort in gebruik</td><td>Sluit alle programma's die de poort van de printer gebruiken.</td></tr>
<tr><td>Apparaat niet gevonden</td><td>Installeer de CH340 USB-driver, probeer een andere kabel of USB-poort, controleer of de printer aanstaat.</td></tr>
<tr><td>Onleesbare tekens na het flashen</td><td>Gebruik 250000 baud met deze firmwares, 115200 met die van Wanhao.</td></tr>
<tr><td>Temperaturen ×10 op het scherm (236 voor 23,6 °C)</td><td>Het scherm heeft nog oude bestanden: flash <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>Het scherm springt bij elke start terug naar Engels, of de pagina <em>Filamentsensor</em> doet niets</td><td>De moederbordfirmware is ouder dan v2.0.9: werk hem bij.</td></tr>
<tr><td>Homing stopt een paar millimeter voor de schakelaar, daarna <em>Homing Failed</em></td><td>Elektrische storing op de lijn van de eindschakelaar. Deze firmwares filteren die sinds v2.0.1: werk bij.</td></tr>
<tr><td>De nozzle raakt tijdens het nivelleren een klem van het bed</td><td>Werk bij naar v2.0.2 of nieuwer: de eerste kolom meetpunten ligt 10 mm van de rand, zoals in de firmware van Wanhao.</td></tr>
<tr><td>Het bed beweegt weg van de Y-schakelaar</td><td>Controleer of je de firmware voor jouw model hebt genomen: de Y-motor zit achteraan bij de MK1, MK1 + kit en MK2, vooraan bij de MK3.</td></tr>
</tbody></table></div>

<h2>Terug naar de firmware van Wanhao</h2>
<p>Elke modelpagina linkt naar de originele moederbord- en schermfirmwares van Wanhao. Flash ze op dezelfde manier; de
moederbordfirmware van Wanhao heeft de schermfirmware van Wanhao van dezelfde generatie nodig.</p>
<p>Vragen: <a href="{DISCORD}">Discord</a> of <a href="{REPO}/issues">GitHub-issues</a>.</p>
""")

    if page == "screen":
        return ("Touchscreenfirmware Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 in 16 talen",
                "Zo flash je het DWIN-touchscreen van de Wanhao D9 met DGUS Reloaded 2.0 vanaf een microSD-kaart: nieuwe interface in 16 "
                "talen, pagina voor de filamentsensor, voor Marlin 2.1. En hoe je teruggaat naar de schermfirmware van Wanhao.",
                f"""
<h1>Het touchscreen van de Duplicator 9 flashen</h1>
<p class="lead">Elke D9, van MK1 tot MK3, heeft hetzelfde DWIN T5-touchscreen (480 × 272). Met deze firmwares draait het
DGUS Reloaded 2.0, onze nieuwe interface in 16 talen, geflasht vanaf een microSD-kaart.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">DWIN_SET.zip downloaden (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Wat DGUS Reloaded 2.0 biedt</h2>
<ul>
<li><strong>16 talen</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Tik op het startscherm op de vlag naast de printernaam
om te wisselen; de printer onthoudt de keuze.</li>
<li><strong>Een pagina voor de filamentsensor</strong>: <em>Instellingen</em> → <em>Filament</em> → <em>Filamentsensor</em>. Zie
<a href="{p('sensor')}#screen">Filamentsensor</a>.</li>
<li><strong>Een statusregel die blijft staan</strong>: het laatste bericht, bijvoorbeeld <em>Ready</em>, blijft in beeld in plaats
van na 30 seconden te verdwijnen.</li>
<li><strong>Temperatuurmeters</strong> voor de nozzle en het bed, met de doeltemperatuur gemarkeerd.</li>
<li>Een nieuw uiterlijk voor elke pagina: donker thema, grotere knoppen, pictogrammen in de pop-ups.</li>
</ul>
</div><figure><img src="{img}screen/nl-home.png" width="480" height="272" alt="Startscherm van DGUS Reloaded 2.0 op een Wanhao D9: temperaturen van nozzle en bed met meters, statusregel, knoppen Printen, Temperatuur en Instellingen">
<figcaption>Het startscherm</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 heeft <strong>v2.0.9 of nieuwer</strong> op het moederbord nodig. Met v2.0.8 of ouder springt de
taal bij elke start terug naar Engels en werkt de pagina voor de filamentsensor niet: <a href="{p('flash')}">flash eerst het
moederbord</a>.</div>

<h2>1. De microSD-kaart formatteren</h2>
<div class="note">FAT32 met een grootte van de toewijzingseenheid van <strong>4096 bytes</strong>. Bij elke andere grootte negeert het scherm de kaart.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 wil vaak niet naar FAT32 formatteren; gebruik <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
en zet de grootte van de toewijzingseenheid op 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (controleer eerst het apparaat met <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (controleer met <code>diskutil list</code>).</li>
</ul>

<h2>2. De bestanden kopiëren</h2>
<p>Pak <code>DWIN_SET.zip</code> uit en kopieer de hele map <code>DWIN_SET</code> naar de hoofdmap van de kaart.</p>

<h2>3. Flashen</h2>
<ol>
<li>Zet de printer uit en haal de stekker uit het stopcontact.</li>
<li>Open de voorkant van de voet om bij de achterkant van het scherm te komen, waar de microSD-sleuf zit.</li>
<li>Steek de kaart erin en zet de printer aan. Het scherm toont de update binnen 10 tot 30 seconden; wacht tot het weer
normaal opstart, in totaal 1 tot 3 minuten.</li>
<li>Zet de printer uit, haal de kaart eruit en sluit de voet.</li>
</ol>
<p>De <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">video van Wanhao over een schermupdate van de D9</a> laat zien waar de sleuf zit.</p>

<h2>Waar het vandaan komt</h2>
<p>DGUS Reloaded 2.0 tekent <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(van Desuuuu, daarna Neo2003) pagina voor pagina opnieuw. De broncode, het programma dat de schermbestanden genereert en de
vertalingen staan op <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Een fout of onhandig woord in jouw taal?
Laat het ons weten op <a href="{DISCORD}">Discord</a> of open daar een issue.</p>
<p>Om terug te gaan naar DGUS Reloaded 1.0.3, bijvoorbeeld met een firmware ouder dan v2.0.9, flash je
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> op dezelfde manier.</p>

<h2>Terug naar het scherm van Wanhao</h2>
<p>De schermfirmware van Wanhao werkt alleen met de moederbordfirmware van Wanhao. MK1: het schermbestand van de bijbehorende
versie op de <a href="{p('mk1')}">MK1-pagina</a>. MK1 + kit, MK2 en MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Zelfde werkwijze.</p>
""")

    if page == "sensor":
        return ("Filamentsensoren op de Wanhao Duplicator 9: filamentschakelaar en aansluiten van de BTT Smart Filament Sensor",
                "Waar je een filamentsensor aansluit op het moederbord van de Wanhao D9 (D8, D9, GND, 5V), hoe je een BTT Smart "
                "Filament Sensor V2.0 bedraadt en detectie van einde filament en verstoppingen aanzet met M412.",
                f"""
<h1>Filamentsensoren</h1>
<p class="lead">Vanaf v2.0.5 lezen deze firmwares twee soorten sensoren: de filamentschakelaar van Wanhao, en de
BTT Smart Filament Sensor V2.0, die ook merkt wanneer het filament niet meer beweegt (spoel in de knoop, verstopping,
weggeslepen filament). <strong>Detectie van einde filament staat standaard aan op elk model</strong>, verstoppingsdetectie staat uit.</p>

<h2>De sensorconnector</h2>
<figure><img src="{img}d9-sensor-plug-nl.svg" width="760" height="440" alt="Moederbord van de Wanhao D9: de 4-pins sensorconnector links van POWER-DET, pinnen D9, D8, GND en 5V, aangesloten op een BTT Smart Filament Sensor V2.0"></figure>
<p>De 4-pins connector links van <strong>POWER-DET</strong>, onder de connectoren van de eindschakelaars, voert <strong>D9, D8, GND en 5V</strong>,
in die volgorde. De pinnamen komen uit een aansluitschema van Wanhao dat dustovich vond en deelde op de
<a href="{DISCORD}">Discord</a>; op de achterkant van het bord staan dezelfde vier pinnen als CTRL, BTN, GND en VCC.</p>
<ul>
<li><strong>D8</strong> is de ingang voor einde filament die de eigen firmware van Wanhao leest.</li>
<li><strong>D9</strong> wordt niet gebruikt door de firmware van Wanhao: deze builds lezen daar het bewegingssignaal van de BTT-sensor.</li>
</ul>
<div class="note">Zet de printer <strong>uit</strong> voordat je iets op het bord aansluit of loskoppelt.</div>

<h2 id="screen">Op het scherm</h2>
<div class="split"><div>
<p>Met DGUS Reloaded 2.0 op het scherm (firmware v2.0.9 of nieuwer): <em>Instellingen</em> → <em>Filament</em> →
<em>Filamentsensor</em>.</p>
<ul>
<li><strong>Filament op</strong> zet alle detectie aan of uit, zoals <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Verstoppingsdetectie</strong> zet verstoppingsdetectie aan met de lengte eronder, of uit (<code>L0</code>).</li>
<li><strong>Verstoppingslengte</strong>: − en + veranderen die met 1 mm; tik op het getal om het in te typen.</li>
<li>De stip <strong>Filament</strong> is groen zolang de filamentschakelaar filament ziet, rood als dat niet zo is.</li>
<li>Wijzigingen gelden meteen. <strong>Opslaan</strong> bewaart ze, zoals <code>M500</code>. De terugpijl gaat terug zonder
op te slaan: bij de volgende start zijn de opgeslagen instellingen weer actief.</li>
</ul>
</div><figure><img src="{img}screen/nl-sensor.png" width="480" height="272" alt="Filamentsensorpagina van DGUS Reloaded 2.0: schakelaars voor einde filament en verstoppingsdetectie, verstoppingslengte met min- en plusknop, filamentindicator en knop Opslaan">
<figcaption>Instellingen → Filament → Filamentsensor</figcaption></figure></div>

<h2>De M412-opdrachten</h2>
<p>Alles wordt via USB ingesteld vanuit een seriële terminal (Pronterface, de terminal van je slicer of van OctoPrint,
250000 baud). Parameters kun je in één opdracht combineren, bijvoorbeeld <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Opdracht</th><th>Wat het doet</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Toont de status, bijvoorbeeld <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Zet detectie aan</strong>: de filamentschakelaar, en ook verstoppingsdetectie als de verstoppingslengte niet 0 is.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Zet alle detectie uit</strong>, schakelaar en verstopping.</td></tr>
<tr><td><code>M412 D5</code></td><td>Zodra de schakelaar geen filament meer ziet, wordt nog <strong>5 mm</strong> doorgeprint voordat de print pauzeert, om het filament tussen de sensor en de nozzle op te gebruiken. Standaard 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Zet verstoppingsdetectie aan</strong> (alleen BTT-sensor): pauzeert wanneer er <strong>10 mm</strong> filament door de extruder gaat zonder dat het wieltje van de sensor draait.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Zet verstoppingsdetectie uit</strong> en laat de filamentschakelaar zoals hij is. Dit is de standaardinstelling.</td></tr>
<tr><td><code>M500</code></td><td>Slaat de instellingen op. Zonder deze opdracht gaat een wijziging verloren als de printer wordt uitgezet.</td></tr>
<tr><td><code>M119</code></td><td>De regel <em>filament</em> toont <code>TRIGGERED</code> met filament geladen, <code>open</code> zonder.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, en <code>L</code> op zichzelf, komen uit onze wijziging aan Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), die in deze firmwares is ingebouwd. In Marlin zonder die wijziging wordt <code>L</code>
op zichzelf genegeerd en pauzeert <code>L0</code> de print meteen wegens een verstopping.</p>

<h2>De filamentschakelaar van Wanhao</h2>
<p>Die vertelt de firmware of er filament is. Raakt het filament op, dan pauzeert de print na nog 5 mm filament en start het
scherm een filamentwissel.</p>
<p><strong>Hij staat sinds v2.0.8 standaard aan op elk model.</strong> Als er niets op D8 is aangesloten, houdt de
pull-upweerstand van het bord de pin op 5 V, wat wordt gelezen als “filament aanwezig”: de detectie gaat dan nooit af, dus hij kan
aan blijven staan, met of zonder sensor. Sluit je een filamentschakelaar aan op D8, dan werkt die meteen.</p>
<ul>
<li>Verstoppingsdetectie blijft uit (<code>L0</code>): deze schakelaar kan niet zien of het filament beweegt.</li>
<li>De schakelaar uitzetten: <code>M412 S0</code> en daarna <code>M500</code>.</li>
<li>Instellingen die door een eerdere release zijn opgeslagen, houden hun aan/uit-stand. Aanzetten: <code>M412 S1</code> en daarna
<code>M500</code>, of terug naar de standaardwaarden (<code>M502</code> en daarna <code>M500</code>, wat ook de Z-offset van je sensor
en de mesh wist).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Deze sensor heeft twee uitgangen, en de firmware leest ze verschillend:</p>
<ul>
<li><strong>De filamentschakelaar</strong> (naar D8) geeft een niveau: 5 V zolang er filament is, 0 V zodra het weg is.</li>
<li><strong>De bewegingsuitgang</strong> (naar D9) komt van een klein wieltje dat door het passerende filament wordt rondgedraaid. Om de paar
millimeter filament wisselt de uitgang tussen 0 V en 5 V. De firmware let alleen op die wisselingen: duwt de extruder
de verstoppingslengte aan filament door zonder één wisseling, dan volgt het filament niet (spoel in de knoop, verstopping,
weggeslepen filament) en pauzeert de print. De filamentschakelaar kan dat niet zien: bij een verstopping is het filament er nog gewoon.</li>
</ul>
<h3>Aansluiten</h3>
<p><strong>5V</strong> op 5V, <strong>GND</strong> op GND, het signaal van de <strong>filamentschakelaar</strong> op <strong>D8</strong>
en het <strong>bewegingssignaal</strong> op <strong>D9</strong>. De namen op de kabel van de sensor kunnen afwijken.</p>
<h3>Aanzetten</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Pauzeren prints zonder reden, verhoog dan de verstoppingslengte: <code>M412 L15</code> en daarna <code>M500</code>. Om alleen
de filamentschakelaar te houden: <code>M412 L0</code> en daarna <code>M500</code>.</p>
<h3>Controleren</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> met filament geladen: <em>filament: TRIGGERED</em>. Verandert die regel als je het filament met de hand
doorduwt in plaats van wanneer je het erin steekt of eruit haalt, dan zijn de twee signaaldraden verwisseld: wissel D8 en D9 om.</li>
</ul>
<div class="note">Verstoppingsdetectie is getest op een MK2 300 zonder de sensor (een verstoppingslengte van 2 mm gaat af, <code>L0</code> nooit),
maar nog niet met de BTT-sensor zelf. Leest de schakelaar andersom (<em>open</em> met filament
geladen), laat het ons dan weten op <a href="{DISCORD}">Discord</a>.</div>

<h2>Bijwerken vanaf v2.0.5 of v2.0.6</h2>
<p>Die releases konden verstoppingsdetectie niet uitzetten, dus gebruikten ze een verstoppingslengte die nooit bereikt zou worden: 100 m in
v2.0.5 (eigenlijk te kort: ongeveer een derde van een spoel van 1 kg, waarna een printer die aan bleef staan zonder reden kon pauzeren) en
10 km in v2.0.6. Bij het opstarten van de printer laadt v2.0.7 die twee waarden als <code>L0</code>. Een echte lengte die je
voor een BTT-sensor hebt ingesteld, zoals <code>L10</code>, blijft behouden. Vanaf v2.0.4 of ouder wordt de afstand van 5 mm voor
einde filament geladen in plaats van de 0 die die versies opsloegen.</p>
""")

    if page == "slicer":
        return ("Cura- en OrcaSlicer-profielen voor de Wanhao Duplicator 9, en de Z-offset instellen",
                "Kant-en-klare profielen voor UltiMaker Cura en OrcaSlicer voor elke Wanhao D9, PLA, PETG en ABS, hoe "
                "je de Z-offset van de sensor instelt, het bed laat meten en een 3DBenchy als test print.",
                f"""
<h1>Slicen voor de Duplicator 9</h1>
<p class="lead">Eén profiel voor elk van de twaalf printers, voor <strong>UltiMaker Cura</strong> en
<strong>OrcaSlicer</strong>, allebei gratis en beschikbaar voor Windows, macOS en Linux. Elk profiel neemt het
bouwvolume, de versnellingen en de hoogste bedtemperatuur van zijn eigen firmware over.</p>

<h2>Downloaden</h2>
{h.slicer}
<p>Ze zijn gemaakt voor de firmware van deze site, <a href="{p('flash')}">v2.0.9 of nieuwer</a>.</p>

<h2>Installeren</h2>
<p><strong>OrcaSlicer</strong>: <em>Bestand</em> → <em>Importeren</em> → <em>Configuraties importeren…</em>, kies
daarna het bestand <code>.orca_printer</code>. De printer, zijn drie kwaliteiten (0,12, 0,20 en 0,28 mm) en de
filamenten PLA, PETG en ABS verschijnen in je presets.</p>
<p><strong>Cura</strong>: <em>Help</em> → <em>Configuratiemap weergeven</em>, sluit Cura, pak het bestand uit in die
map, start Cura opnieuw en ga dan naar <em>Instellingen</em> → <em>Printer</em> → <em>Printer toevoegen…</em> →
<em>Een niet-netwerkprinter toevoegen</em> → <em>Wanhao</em> → jouw model. De <em>Wanhao Duplicator 9</em> die met
Cura meekomt is een ouder profiel: alleen de 300, met raft en supports standaard aan.</p>

<h2 id="first-print">Voor de eerste print: de Z-offset, daarna een meting</h2>
<p>De sensor schakelt een stukje boven het bed, en de firmware moet weten hoeveel dat is. Dat is de
<strong>Z-offset</strong>. Te hoog en de eerste laag hecht niet; te laag en de nozzle schraapt over het bed. Je stelt
hem één keer in, en het is de instelling die bepaalt of je prints blijven zitten.</p>
<div class="note">Alles hieronder blijft in het geheugen van de printer, niet in de slicer. Het overleeft een
firmware-update (sinds v2.0.3).</div>

<h3>1. Eerst opwarmen</h3>
<p>Een hete nozzle is een paar honderdsten van een millimeter langer. Warm op zoals voor een print — op het scherm
<em>Temperatuur</em> → <em>Voorverwarmen</em> → <em>PLA</em> (200 °C en 60 °C) — en wacht een paar minuten.</p>

<h3>2. Home de assen</h3>
<p>Op het scherm: <em>Instellingen</em> → <em>Bewegen</em> → <em>Home</em>. Via USB: <code>G28</code>.</p>

<h3>3. Stel de Z-offset in</h3>
<p><strong>De makkelijke manier, tijdens het printen.</strong> Start een print en ga tijdens de
<strong>eerste laag</strong> op het scherm naar <em>Aanpassen</em> → <em>Z-offset</em>. Ga in stapjes van 0,01 mm
omlaag terwijl de lijn getrokken wordt, tot hij plat is en zijn buurlijn zonder gaatje raakt. Te hoog laat ronde,
losse draadjes achter; te laag geeft een ruw, platgedrukt oppervlak en je ziet de nozzle graven. De waarde wordt
vanzelf opgeslagen.</p>
<p><strong>Met een velletje papier, zonder te printen.</strong> Via USB, op printtemperatuur:</p>
<pre><code>M851 Z0     ; vergeet de huidige offset
M500
G28         ; opnieuw homen zodat hij meetelt
M420 S0     ; negeer het mesh tijdens het meten
M211 S0     ; sta toe om onder Z0 te gaan: de software-eindstops houden de nozzle daar tegen
G1 Z0 F300  ; de nozzle zakt naar de nul die de firmware denkt te hebben</code></pre>
<p>Schuif een velletje papier onder de nozzle en ga daarna met <code>G91</code> en <code>G1 Z-0.05 F60</code> in
kleine stapjes omlaag, keer op keer, tot het papier nog net stroef loopt. Lees de waarde af met <code>M114</code>:
hij is negatief, bijvoorbeeld −1,30. Daarna:</p>
<pre><code>G90
M851 Z-1.30 ; jouw waarde
M500
M211 S1     ; zet de software-eindstops weer aan, ze beschermen het bed</code></pre>

<h3>4. Meet het bed</h3>
<p>Op het scherm: <em>Instellingen</em> → <em>Nivelleren</em> → <em>Automatisch</em> → <em>Meten</em>. De printer meet
25 punten en <strong>slaat het mesh vanzelf op</strong> (hij voert <code>G29</code> en daarna <code>M500</code> uit).
Reken op een paar minuten. Via USB: <code>G29</code> en daarna <code>M500</code>.</p>
<p>Onze profielen meten niet voor elke print: ze zetten het opgeslagen mesh weer aan met <code>M420 S1</code>, vlak na
het homen. Meet dus opnieuw als je de printer verplaatst, het printoppervlak of de nozzle wisselt, of als de eerste
laag aan de ene kant van het bed goed is en aan de andere kant niet.</p>

<h3>5. Controleren</h3>
<p><code>M503</code> laat zien wat er is opgeslagen: de regel <code>M851</code> is je Z-offset, en
<code>M420 S1</code> geeft aan dat het mesh aanstaat. Op het scherm toont de pagina <em>Automatisch</em> de 25 gemeten
punten.</p>

<h2>Testprints</h2>
<p>Een 3DBenchy, al gesliced voor een <strong>D9 MK2 300</strong>, om de twee slicers te vergelijken of een instelling
te controleren zonder iets te installeren:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Elk ongeveer anderhalf uur en 4 m filament. Voor een ander model of een ander formaat slice je de
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> zelf met jouw profiel.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy geprint met het OrcaSlicer-profiel op een Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 uur 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy geprint met het Cura-profiel op een Wanhao D9 MK2 300"><figcaption>Cura, 1 uur 22</figcaption></figure>
</div>
<p><strong>Waarmee je begint:</strong> op een D9 MK2 300 in PLA deed dezelfde Benchy er <strong>1 uur 14 met
OrcaSlicer</strong> en <strong>1 uur 22 met Cura</strong> over, en de wanden van OrcaSlicer kwamen er iets netter
uit. Allebei zijn ze goed; OrcaSlicer is degene waarmee wij zouden beginnen, en zijn kalibratiegereedschap
(doorvoer, pressure advance, temperatuurtorens) helpt zodra je meer wilt.</p>
<div class="note">De D9 is open: ABS vraagt op zijn minst een kamer zonder tocht, en de bedtemperatuur ervan is
teruggebracht tot wat jouw model aankan (80 °C op een MK3 500).</div>

<h2>Wat er in de profielen zit</h2>
<ul>
<li><strong>Lagen</strong> van 0,20 mm, <strong>3 wanden</strong>, 4 lagen boven en 3 onder, gyroïde vulling van 15 %,
een skirt van 2 lijnen, geen support.</li>
<li><strong>Snelheden</strong>: 40 mm/s op de buitenwand, 60 binnenin, 70 voor de vulling, 20 op de eerste laag, 150
voor verplaatsingen. Wanhao geeft 70 mm/s op als hoogste printsnelheid van de D9.</li>
<li><strong>Retractie</strong> van 1,5 mm op 25 mm/s: elke D9 heeft een MK10-extruder met directe aandrijving, en de
firmware begrenst de extruder op 25 mm/s.</li>
<li><strong>Temperaturen</strong>: PLA 210 °C en daarna 205, bed 65 en daarna 60. PETG 240 / 80 en daarna 235 / 75.
ABS 245 / 105 en daarna 245 / 100.</li>
<li><strong>Een aanlooplijn</strong> op 15 mm van de linkerrand, voorbij de klemmen van het bed, zodat de nozzle
schoon bij het model aankomt.</li>
<li>Op het eind gaat de nozzle omhoog en komt het bed naar voren.</li>
</ul>
<p>Alle instellingen en hoe je ze aanpast: <a href="{REPO}/tree/main/Slicer">map Slicer</a> op GitHub.</p>
""")

    if page == "quiet":
        return ("Een Wanhao Duplicator 9 stiller maken: welke ventilatoren, en de bordventilator op NTC-thermistors",
                "Welke ventilatoren van de Wanhao D9 stiller kunnen: de hotendventilator moet blijven, de ventilator van de voeding "
                "regelt zichzelf al, en de bordventilator kan worden losgekoppeld of via NTC-thermistors lopen.",
                f"""
<h1>De Duplicator 9 stiller maken</h1>
<p class="lead">In rust komt het geluid van de D9 van zijn ventilatoren. Hier lees je welke stiller kan, en hoe.</p>
<div class="note">Werk met de <strong>stekker uit het stopcontact</strong>. Houd alle draden weg van de 230 V-kant.</div>

<h2>De ventilatoren</h2>
<div class="table"><table class="stack"><thead><tr><th>Ventilator</th><th>Aangestuurd door</th><th>Kan hij stiller?</th></tr></thead><tbody>
<tr><td><strong>Koelventilator van de hotend</strong> (printkop)</td><td>niets: 24 V, altijd aan</td><td><strong>nee</strong>: meestal de luidste, maar als hij langzamer draait kruipt de warmte omhoog in de hotend en loopt het filament vast (heat creep)</td></tr>
<tr><td><strong>Printkoelventilator</strong> (printkop)</td><td>firmware, pin D5 (PWM)</td><td>al regelbaar: ingesteld door de slicer en <code>M106</code></td></tr>
<tr><td><strong>Ventilator van de voeding</strong></td><td>de voeding zelf</td><td>niets aan doen: bij het hier gecontroleerde exemplaar (Chuanglian A-350FAK-24) volgt hij al de temperatuur van de voeding</td></tr>
<tr><td><strong>Bordventilator</strong> (elektronicabehuizing)</td><td>niets: 24 V, altijd aan</td><td><strong>ja</strong>, zie hieronder</td></tr>
</tbody></table></div>
<p>De firmware van Wanhao stuurt geen bordventilator en geen hotendventilator aan (<code>CONTROLLER_FAN_PIN</code> en
<code>E0_AUTO_FAN_PIN</code> zijn allebei <code>-1</code>), en het bord heeft geen vrije schakelbare uitgang. Daarom hangen
deze twee aan de altijd gevoede “24V OUT”-aansluitingen, en daarom kan geen enkele firmware ze langzamer laten draaien.</p>

<h2>Bordventilator</h2>
<p>Bij het hier gemeten exemplaar: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max., glijlager</strong>.</p>
<p><strong>Veel bezitters koppelen hem gewoon los.</strong> Het bord blijft koel: het zit onderin de elektronicabehuizing, onder
het verwarmde bed, en de warmte van het bed stijgt van het bord weg. Doe je dit, houd dan je eerste lange prints in de gaten:
een oververhitte stappenmotordriver valt even uit, en dat zie je als <strong>verschoven lagen</strong>, niet als foutmelding.</p>
<h3>Hem houden, maar alleen als de drivers warm zijn</h3>
<p>Twee vermogens-NTC-thermistors in serie laten de ventilator rond 45–50 °C starten en sneller draaien naarmate de drivers
warmer worden: <strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), met warmtegeleidende lijm op een
koellichaam van een driver geplakt, aansluitdraden geïsoleerd.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ventilator (+)
                                    ventilator (−) ── 0V</code></pre>
<ul>
<li>Dit is een berekening, <strong>nog niet getest op een printer</strong>: de tolerantie van de MF72 is ±20 %, en een kleine ventilator
kan al bij een lagere temperatuur starten dan verwacht. Controleer de starttemperatuur op de werkbank (NTC's in een zakje in heet
water, met een keukenthermometer); voeg een tweede 200 Ω toe als hij te vroeg start, laat de 200 Ω weg als hij te laat start.</li>
<li>De NTC's moeten op een koellichaam geplakt zijn: in de vrije lucht warmt de ventilatorstroom (tot ongeveer 0,6 W in de NTC's) ze
tientallen graden op.</li>
<li>De ventilator haalt zo nooit zijn volle toerental (ongeveer 75 % bij 80 °C), en een NTC die defect raakt, wordt een open verbinding: de ventilator
staat dan definitief stil.</li>
</ul>
<p>Bronnen: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">datasheet MF72</a>.</p>
""")
    raise KeyError(page)
