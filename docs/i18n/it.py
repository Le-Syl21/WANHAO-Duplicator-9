"""Italiano: translation of en.py."""

META = {"name": "Italiano", "locale": "it_IT", "dir": "ltr"}

UI = {
    "nav": {"index": "Home", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Guida al flash", "screen": "Schermo", "sensor": "Sensore filamento", "slicer": "Slicer",
            "quiet": "Silenziosità"},
    "language": "Lingua",
    "model": "Modello",
    "size": "Dimensione", "volume": "Volume di stampa", "file": "Firmware",
    "footer_src": "Sorgenti e segnalazioni su GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware sotto licenza GNU GPL v3. I manuali e i firmware Wanhao restano di proprietà di Wanhao.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Scheda madre Wanhao D9 (vista dall'alto)",
    "plug": "connettore sensore",
    "switch": "fine filamento",
    "motion": "movimento",
    "level": "livello: filamento presente / assente",
    "pulses": "impulsi mentre il filamento avanza",
    "names": "i nomi sul tuo sensore possono essere diversi",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Firmware Marlin aggiornato per ogni Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "file per lo schermo, firmware originali e manuali Wanhao, e come flasharli.",
                f"""
<h1>Firmware Wanhao Duplicator 9</h1>
<p class="lead">Il sito di download di Wanhao per la Duplicator 9 non esiste più. Tutto ciò che serve a chi possiede una D9
si trova qui: firmware Marlin 2.1 aggiornato per ogni modello e dimensione, i file corrispondenti per il touchscreen, i
firmware originali Wanhao, i manuali Wanhao e guide al flash passo passo.</p>
<p><a class="btn" href="{REPO}/releases/latest">Tutti i download</a> <a class="btn ghost" href="{DISCORD}">Chiedi su Discord</a></p>

<h2>Quale D9 ho?</h2>
<div class="split"><div>
<ol>
<li><strong>Cavo piatto grigio</strong> che arriva alla testina di stampa, <strong>sonda cilindrica di metallo</strong>
accanto all'ugello, nessun rinforzo sui lati del telaio: <a href="{p('mk1')}">MK1</a>.</li>
<li>La stessa macchina di prima generazione con una <strong>sonda BLTouch bianca</strong> al posto di quella di metallo:
una MK1 con il kit di aggiornamento Wanhao, <a href="{p('mk1u2')}">MK1 + kit MK2</a>.</li>
<li><strong>Nervature di rinforzo inclinate</strong> su entrambi i lati del telaio, un <strong>cavo nero tondo</strong>
verso la testina e un BLTouch: una MK2 o una MK3. Guarda sotto il piatto il <strong>motore Y</strong>, quello che
muove il piatto: se è dietro, è una <a href="{p('mk2')}">MK2</a>; se è davanti, dal lato del touchscreen, una
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Il numero dopo D9 indica la dimensione: D9/300, D9/400 o D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 con le nervature di rinforzo laterali">
<figcaption>D9 MK2: nervature laterali, cavo tondo</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Sonda induttiva, cavo piatto. Firmware, Wanhao da V0.15 a V0.164(B), manuale.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + kit MK2</h3><p>MK1 aggiornata con il kit BLTouch. Firmware e Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware del kit →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, nervature laterali. Firmware, Wanhao V1.1.2, guide.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Motore Y davanti, sensore filamento. Firmware e Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>Cosa portano questi firmware</h2>
<ul>
<li><strong>Marlin 2.1</strong> compilato dalle configurazioni della Duplicator 9 pubblicate in
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
con le modifiche proposte lì: sonda della MK1 letta nel verso giusto, direzione Y della MK3, ripresa dopo un'interruzione
di corrente, filtro antidisturbo sui finecorsa.</li>
<li><strong>Le impostazioni di fabbrica di Wanhao</strong>, prese dal firmware e dai sorgenti Wanhao di ogni modello: passi/mm,
velocità, accelerazioni, PID dell'hotend, offset della sonda e margini di tastatura, homing, limiti termici, jerk e direzione degli assi.</li>
<li><strong>Ripresa dopo un'interruzione di corrente</strong>: durante una stampa da SD il lavoro viene salvato a ogni cambio di layer e, dopo un blackout, lo schermo propone di riprendere da lì.</li>
<li><strong>Sensori filamento</strong>: un interruttore di fine filamento su D8, attivo di default su ogni modello (senza effetto se non c'è), e il BTT Smart Filament Sensor V2.0, che rileva anche gli inceppamenti. Vedi <a href="{p('sensor')}">Sensore filamento</a>.</li>
<li><strong>La testina torna al centro dopo il livellamento del piatto</strong>, così il piatto non copre più lo schermo.</li>
<li><strong>Una nuova interfaccia touchscreen in 16 lingue</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, con una pagina per regolare il sensore filamento.</li>
</ul>

<h2>Flashare in tre passaggi</h2>
<ol>
<li>Scarica il file <strong>.hex</strong> per il tuo modello e la tua dimensione dalla sua pagina.</li>
<li>Flashalo via USB con AVRDUDESS o avrdude: <a href="{p('flash')}">guida al flash</a>.</li>
<li>Flasha il touchscreen da una scheda microSD: <a href="{p('screen')}">guida allo schermo</a>.</li>
</ol>
<p>I firmware originali Wanhao restano disponibili su ogni pagina modello, così una macchina può sempre tornare com'era uscita dalla fabbrica.</p>
""")

    if page == "mk1":
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 per la Wanhao D9 MK1 con sonda induttiva, firmware originali Wanhao da V0.15 a V0.164(B), "
                "file per lo schermo e manuale utente MK1.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">La prima Duplicator 9: una sonda induttiva di metallo accanto all'ugello, un cavo piatto grigio verso la
testina di stampa e un telaio senza nervature laterali.</p>
<p>Queste build leggono la sonda induttiva nel verso giusto (si attiva a livello LOW) e riprendono le impostazioni
dell'ultimo firmware MK1 di Wanhao, la V0.164(B), offset della sonda compresi (X 15, Y 0). Il motore Y è dietro, come l'ha montato Wanhao.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Sonda induttiva e cavo piatto sulla testina di una Wanhao D9 MK1">
<figcaption>MK1: sonda induttiva, cavo piatto</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Prendi il file per la tua dimensione, poi flasha lo schermo con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documenti Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Manuale utente D9 MK1</a> (giugno 2018, in inglese): montaggio, cablaggio, menu, livellamento, risoluzione dei problemi.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Guida introduttiva D9 MK1</a>.</li>
</ul>

<h2>Firmware originali Wanhao</h2>
<p>Per riportare una macchina com'era uscita dalla fabbrica. Ogni firmware della scheda madre funziona solo con il firmware
dello schermo della stessa versione.</p>
<div class="table"><table><thead><tr><th>Versione</th><th>Dimensione</th><th>Scheda madre</th><th>Schermo</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Le impostazioni di ogni versione (passi/mm, velocità, PID, direzione degli assi) sono elencate in
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, lette dai binari di Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware Wanhao Duplicator 9 MK1 con kit di aggiornamento MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 per una Wanhao D9 MK1 aggiornata con il kit BLTouch MK2 di Wanhao, e firmware originale Wanhao V1.1.31 del kit.",
                f"""
<h1>Wanhao D9 MK1 con il kit di aggiornamento MK2</h1>
<div class="split"><div>
<p class="lead">Una D9 di prima generazione con il kit di aggiornamento MK2 di Wanhao: il telaio della MK1, con una sonda
BLTouch al posto di quella induttiva di metallo.</p>
<p>Wanhao ha distribuito un firmware a parte per questa combinazione, perché il BLTouch del kit non è montato nella stessa
posizione di quello della MK2 di fabbrica: l'offset Y della sonda è diverso. Queste build usano la geometria del kit. Il
motore Y è dietro.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Sonda BLTouch sulla testina di una Wanhao D9">
<figcaption>Sonda BLTouch</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Prendi il file per la tua dimensione, poi flasha lo schermo con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Queste build usano l'offset della sonda del firmware del kit, Y −10. È l'unica riga in cui il sorgente
del kit Wanhao differisce da quello della MK2 di fabbrica (Y 0): il BLTouch del kit è più indietro. Se la mesh del piatto
sembra spostata avanti o indietro, misura il tuo offset con la <a href="{REPO}/blob/main/Offset.md">guida agli offset</a>.</div>

<h2>Firmware originali Wanhao</h2>
<p>Il firmware V1.1.31 del kit Wanhao (dicembre 2018), usato con il firmware dello schermo della MK2.</p>
<div class="table"><table><thead><tr><th>Dimensione</th><th>Scheda madre</th><th>Schermo</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Impostazioni lette dai binari di Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 per la Wanhao D9 MK2 con BLTouch, firmware e file per lo schermo originali Wanhao V1.1.2, e le guide Wanhao della MK2.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">La seconda Duplicator 9: nervature di rinforzo inclinate su entrambi i lati, un cavo dati nero e tondo verso
la testina di stampa, una sonda BLTouch e un portabobina in alto.</p>
<p>Wanhao ha anche montato carrelli a quattro ruote, un asse Y a doppio binario e una cinghia più spessa sulla 400 e
sulla 500, e un piatto a doppia faccia sulla 300 e sulla 400. Il motore Y è dietro; queste build fanno girare l'asse Y
come il firmware V1.1.2 di Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Prendi il file per la tua dimensione. Una MK2 la cui testina è stata aggiornata anche alla MK3 deve
usare il <a href="{p('mk3')}">firmware MK3</a>. Poi flasha lo schermo con <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documenti Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Guida introduttiva D9 MK2</a> (in inglese).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">I 12 miglioramenti dalla MK1 alla MK2</a>, a cura di Wanhao.</li>
</ul>

<h2>Firmware originali Wanhao</h2>
<p>La V1.1.2 di Wanhao (ottobre 2018; per la 500 è stata ricompilata come V1.1.2.1 a luglio 2019), con il firmware dello schermo MK2 di Wanhao.</p>
<div class="table"><table><thead><tr><th>Dimensione</th><th>Scheda madre</th><th>Schermo</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Impostazioni lette dai binari di Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 per la Wanhao D9 MK3 (motore Y davanti, sensore filamento) e firmware originale Wanhao V1.1.3.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK3</h1>
<p class="lead">L'ultima Duplicator 9 mantiene il telaio e il BLTouch della MK2, aggiunge un sensore di fine filamento e sposta
il motore Y davanti, dal lato del touchscreen.</p>
<p>Spostare il motore inverte l'asse Y: il firmware V1.1.3 di Wanhao inverte Y, e così fanno queste build. Il sensore di
fine filamento è attivo di default. Wanhao non ha pubblicato offset della sonda per la MK3, quindi queste build usano
quelli della MK2.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Prendi il file per la tua dimensione, poi flasha lo schermo con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Se il sensore filamento interrompe le stampe a caso, disattivalo con <code>M412 S0</code> e poi
<code>M500</code>. Wanhao Europe aveva pubblicato un firmware MK3 «ReverseMode» per questo problema; da allora è stato
cancellato e non è stato possibile ritrovarlo.</div>

<h2>Firmware originali Wanhao</h2>
<p>La V1.1.3 di Wanhao (agosto 2019). Wanhao non ha pubblicato nessun firmware dello schermo per la MK3: i suoi download MK3 rimandavano a quello della MK2.</p>
<div class="table"><table><thead><tr><th>Dimensione</th><th>Scheda madre</th><th>Schermo</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Impostazioni lette dai binari di Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Come flashare il firmware della scheda madre di una Wanhao Duplicator 9 (D9)",
                "Guida passo passo per flashare Marlin su una Wanhao D9 via USB con AVRDUDESS o avrdude, risolvere i "
                "problemi di homing e tornare al firmware Wanhao.",
                f"""
<h1>Flashare la scheda madre della Duplicator 9</h1>
<p class="lead">La scheda madre della D9 è un ATmega2560 con bootloader USB: niente programmatore, niente da aprire nella base,
basta un cavo USB.</p>

<h2>Cosa serve</h2>
<ul>
<li>Un cavo USB tra la stampante e il computer, e la stampante <strong>accesa</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, grafico, il più semplice) o
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (riga di comando, tutti i sistemi).</li>
<li>Il file <strong>.hex</strong> per il tuo modello e la tua dimensione: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Prima di flashare</h2>
<div class="note">Invia <code>M503</code> e conserva la risposta. Dalla v2.0.3 un aggiornamento mantiene le impostazioni salvate
nella stampante, ma l'aggiornamento <strong>alla</strong> v2.0.3 riparte una volta dai valori predefiniti di questo firmware (è
cambiato il modo in cui le impostazioni vengono memorizzate), e lo stesso vale se si arriva dal firmware Wanhao. Dopo, reimposta
lo Z offset della sonda con <code>M851 Z…</code> e <code>M500</code>.</div>
<p>Chiudi ogni programma che possa occupare la porta della stampante: Cura, PrusaSlicer, OctoPrint, Pronterface, terminali seriali.</p>

<h2>Flashare con AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: la porta COM della stampante (per esempio <code>COM3</code>). Lascia il baud rate al valore predefinito.</li>
<li>Flash: scegli il file .hex, poi clicca su <strong>Program!</strong>. Ci vogliono da 30 a 60 secondi.</li>
</ol>

<h2>Flashare con avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Sostituisci la porta e il nome del file con i tuoi. Il protocollo <code>wiring</code> sceglie da solo la velocità del bootloader.</p>

<h2>Primo avvio</h2>
<ol>
<li>Scollega il cavo USB, spegni e riaccendi la stampante, ricollega il cavo.</li>
<li>Connettiti a <strong>250000 baud</strong> (i firmware Wanhao usavano 115200) e invia <code>M115</code>: la risposta mostra il nuovo firmware.</li>
<li>Esegui l'homing di tutti gli assi, poi un livellamento del piatto dallo schermo o con <code>G29</code>, e salva con <code>M500</code>.</li>
</ol>

<h2 id="reset">Tornare alle impostazioni predefinite di questo firmware</h2>
<p>Dalla v2.0.3, un aggiornamento del firmware <strong>mantiene</strong> le impostazioni salvate nella stampante (Z offset della
sonda, passi/mm, PID, mesh…). I nuovi valori predefiniti di una release quindi non sostituiscono quelli già salvati. Fai un
ripristino una volta quando aggiorni dalla v2.0.2 o precedente mantenendo valori salvati a mano, quando la stampante si
comporta in modo strano dopo aver provato altri firmware, o ogni volta che vuoi ripartire da zero:</p>
<ul>
<li><strong>Sullo schermo:</strong> <em>Impostazioni</em> → <em>Altro</em> → <em>Ripristina</em> → ✓.</li>
<li><strong>Via USB:</strong> invia <code>M502</code> (carica i valori predefiniti di questo firmware) poi <code>M500</code> (li salva).</li>
</ul>
<p>Poi reimposta lo Z offset della sonda (<code>M851 Z…</code> poi <code>M500</code>) ed esegui un livellamento del piatto. Controlla il
risultato con <code>M503</code>.</p>

<h2>Interruzione di corrente e sensore filamento</h2>
<ul>
<li>La ripresa dopo un'interruzione di corrente è attiva: il lavoro viene salvato a ogni cambio di layer. Per disattivarla: <code>M413 S0</code> poi <code>M500</code>.</li>
<li>Una stampa che si ferma subito con <em>power outage</em> appena inizia a scaldare: aggiorna alla v2.0.4 o successiva. Le build precedenti sorvegliavano l'ingresso di rilevamento mancanza corrente della scheda, che legge un livello basso non appena partono i riscaldatori.</li>
<li>Il rilevamento di fine filamento è attivo di default su ogni modello dalla v2.0.8, e senza sensore non fa nulla. Dopo un aggiornamento da una release precedente, attivalo con <code>M412 S1</code> poi <code>M500</code>, oppure sullo schermo in <em>Impostazioni</em> → <em>Filamento</em> → <em>Sensore filamento</em>. Cablaggio e BTT Smart Filament Sensor: <a href="{p('sensor')}">Sensore filamento</a>.</li>
</ul>

<h2>Risoluzione dei problemi</h2>
<div class="table"><table><thead><tr><th>Problema</th><th>Soluzione</th></tr></thead><tbody>
<tr><td>Porta in uso</td><td>Chiudi ogni programma che usa la porta della stampante.</td></tr>
<tr><td>Dispositivo non trovato</td><td>Installa il driver USB CH340, prova un altro cavo o un'altra porta USB, controlla che la stampante sia accesa.</td></tr>
<tr><td>Caratteri illeggibili dopo il flash</td><td>Usa 250000 baud con questi firmware, 115200 con quelli Wanhao.</td></tr>
<tr><td>Temperature mostrate ×10 sullo schermo (236 per 23,6 °C)</td><td>Lo schermo ha ancora i vecchi file: flasha <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>Lo schermo torna in inglese a ogni avvio, oppure la sua pagina <em>Sensore filamento</em> non fa nulla</td><td>Il firmware della scheda madre è più vecchio della v2.0.9: aggiornalo.</td></tr>
<tr><td>L'homing si ferma qualche millimetro prima del finecorsa, poi <em>Homing Failed</em></td><td>Disturbi elettrici sulla linea del finecorsa. Questi firmware li filtrano dalla v2.0.1: aggiorna.</td></tr>
<tr><td>L'ugello urta una clip del piatto durante il livellamento</td><td>Aggiorna alla v2.0.2 o successiva: la prima colonna di tastatura è a 10 mm dal bordo, come nel firmware Wanhao.</td></tr>
<tr><td>Il piatto si allontana dal finecorsa Y</td><td>Controlla di aver preso il firmware del tuo modello: il motore Y è dietro sulla MK1, sulla MK1 + kit e sulla MK2, davanti sulla MK3.</td></tr>
</tbody></table></div>

<h2>Tornare al firmware Wanhao</h2>
<p>Ogni pagina modello rimanda ai firmware originali Wanhao della scheda madre e dello schermo. Si flashano allo stesso modo; il
firmware Wanhao della scheda madre ha bisogno del firmware Wanhao dello schermo della stessa generazione.</p>
<p>Domande: <a href="{DISCORD}">Discord</a> o <a href="{REPO}/issues">issue su GitHub</a>.</p>
""")

    if page == "screen":
        return ("Firmware del touchscreen Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 in 16 lingue",
                "Come flashare il touchscreen DWIN della Wanhao D9 con DGUS Reloaded 2.0 da una scheda microSD: nuova interfaccia in 16 "
                "lingue, pagina del sensore filamento, per Marlin 2.1. E come tornare al firmware dello schermo Wanhao.",
                f"""
<h1>Flashare il touchscreen della Duplicator 9</h1>
<p class="lead">Tutte le D9, dalla MK1 alla MK3, hanno lo stesso touchscreen DWIN T5 (480 × 272). Con questi firmware esegue
DGUS Reloaded 2.0, la nostra nuova interfaccia in 16 lingue, che si flasha da una scheda microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Scarica DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Cosa porta DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 lingue</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Tocca la bandiera accanto al nome della stampante nella schermata
principale per cambiarla; la stampante ricorda la scelta.</li>
<li><strong>Una pagina per il sensore filamento</strong>: <em>Impostazioni</em> → <em>Filamento</em> → <em>Sensore filamento</em>. Vedi
<a href="{p('sensor')}#screen">Sensore filamento</a>.</li>
<li><strong>Una riga di stato che resta</strong>: l'ultimo messaggio, per esempio <em>Ready</em>, rimane sullo schermo invece
di sparire dopo 30 secondi.</li>
<li><strong>Indicatori di temperatura</strong> per l'ugello e il piatto, con il valore impostato segnato.</li>
<li>Un nuovo aspetto per ogni pagina: tema scuro, pulsanti più grandi, pittogrammi nei popup.</li>
</ul>
</div><figure><img src="{img}screen/it-home.png" width="480" height="272" alt="Schermata principale di DGUS Reloaded 2.0 su una Wanhao D9: temperature dell'ugello e del piatto con indicatori, riga di stato, pulsanti Stampa, Temperatura e Impostazioni">
<figcaption>La schermata principale</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 richiede la <strong>v2.0.9 o successiva</strong> sulla scheda madre. Con la v2.0.8 o precedenti, la
lingua torna all'inglese a ogni avvio e la pagina del sensore filamento non funziona: prima <a href="{p('flash')}">flasha la
scheda madre</a>.</div>

<h2>1. Formattare la scheda microSD</h2>
<div class="note">FAT32 con dimensione dell'unità di allocazione di <strong>4096 byte</strong>. Con qualsiasi altra dimensione lo schermo ignora la scheda.</div>
<ul>
<li><strong>Windows</strong>: spesso Windows 11 non formatta in FAT32; usa <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
e imposta la dimensione dell'unità di allocazione a 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (prima controlla il dispositivo con <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (controlla con <code>diskutil list</code>).</li>
</ul>

<h2>2. Copiare i file</h2>
<p>Estrai <code>DWIN_SET.zip</code> e copia l'intera cartella <code>DWIN_SET</code> nella radice della scheda.</p>

<h2>3. Flashare</h2>
<ol>
<li>Spegni la stampante e scollegala dalla presa.</li>
<li>Apri la parte anteriore della base per raggiungere il retro dello schermo, dove si trova il suo slot microSD.</li>
<li>Inserisci la scheda e accendi. Lo schermo mostra l'aggiornamento entro 10-30 secondi; aspetta che si riavvii
normalmente, da 1 a 3 minuti in tutto.</li>
<li>Spegni, togli la scheda, richiudi la base.</li>
</ol>
<p>Il <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">video di Wanhao sull'aggiornamento dello schermo della D9</a> mostra dove si trova lo slot.</p>

<h2>Da dove viene</h2>
<p>DGUS Reloaded 2.0 ridisegna pagina per pagina <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(di Desuuuu, poi Neo2003). I sorgenti, il programma che genera i file dello schermo e le traduzioni sono
su <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Una parola sbagliata o goffa nella tua lingua? Diccelo su
<a href="{DISCORD}">Discord</a> o apri una issue lì.</p>
<p>Per tornare a DGUS Reloaded 1.0.3, per esempio con un firmware più vecchio della v2.0.9, flasha
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> allo stesso modo.</p>

<h2>Tornare allo schermo Wanhao</h2>
<p>Il firmware dello schermo Wanhao funziona solo con il firmware Wanhao della scheda madre. MK1: il file dello schermo della
versione corrispondente nella <a href="{p('mk1')}">pagina MK1</a>. MK1 + kit, MK2 e MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Stessa procedura.</p>
""")

    if page == "sensor":
        return ("Sensori filamento sulla Wanhao Duplicator 9: cablaggio del sensore di fine filamento e del BTT Smart Filament Sensor",
                "Dove collegare un sensore filamento sulla scheda madre della Wanhao D9 (D8, D9, GND, 5V), come cablare un BTT Smart "
                "Filament Sensor V2.0 e attivare il rilevamento di fine filamento e di inceppamento con M412.",
                f"""
<h1>Sensori filamento</h1>
<p class="lead">Dalla v2.0.5 questi firmware leggono due tipi di sensore: l'interruttore di fine filamento Wanhao e il
BTT Smart Filament Sensor V2.0, che si accorge anche quando il filamento smette di muoversi (bobina aggrovigliata,
inceppamento, filamento mangiato dall'estrusore). <strong>Il rilevamento di fine filamento è attivo di default su ogni modello</strong>, mentre il rilevamento di inceppamento è disattivato.</p>

<h2>Il connettore del sensore</h2>
<figure><img src="{img}d9-sensor-plug-it.svg" width="760" height="440" alt="Scheda madre della Wanhao D9: il connettore sensore a 4 pin a sinistra di POWER-DET, pin D9, D8, GND e 5V, collegato a un BTT Smart Filament Sensor V2.0"></figure>
<p>Il connettore a 4 pin a sinistra di <strong>POWER-DET</strong>, sotto i connettori dei finecorsa, porta <strong>D9, D8, GND e 5V</strong>,
in quest'ordine. I nomi dei pin vengono da uno schema di cablaggio di Wanhao che dustovich ha trovato e condiviso sul
<a href="{DISCORD}">Discord</a>; sul retro della scheda gli stessi quattro pin sono stampati come CTRL, BTN, GND e VCC.</p>
<ul>
<li><strong>D8</strong> è l'ingresso di fine filamento letto dal firmware Wanhao.</li>
<li><strong>D9</strong> non è usato dal firmware Wanhao: queste build ci leggono il segnale di movimento del sensore BTT.</li>
</ul>
<div class="note">Stampante <strong>spenta</strong> mentre colleghi o scolleghi qualsiasi cosa sulla scheda.</div>

<h2 id="screen">Sullo schermo</h2>
<div class="split"><div>
<p>Con DGUS Reloaded 2.0 sullo schermo (firmware v2.0.9 o successivo): <em>Impostazioni</em> → <em>Filamento</em> →
<em>Sensore filamento</em>.</p>
<ul>
<li><strong>Fine filamento</strong> attiva o disattiva tutto il rilevamento, come <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Rilevamento inceppamento</strong> attiva il rilevamento di inceppamento con la lunghezza indicata sotto, o lo disattiva (<code>L0</code>).</li>
<li><strong>Lunghezza inceppamento</strong>: − e + la cambiano di 1 mm; tocca il numero per digitarla.</li>
<li>Il pallino <strong>Filamento</strong> è verde quando l'interruttore di fine filamento vede il filamento, rosso quando non lo vede.</li>
<li>Le modifiche si applicano subito. <strong>Salva</strong> le memorizza, come <code>M500</code>. La freccia indietro esce senza
salvare: le impostazioni memorizzate tornano al prossimo avvio.</li>
</ul>
</div><figure><img src="{img}screen/it-sensor.png" width="480" height="272" alt="Pagina del sensore filamento di DGUS Reloaded 2.0: interruttori di fine filamento e di rilevamento inceppamento, lunghezza di inceppamento con pulsanti meno e più, indicatore del filamento e pulsante Salva">
<figcaption>Impostazioni → Filamento → Sensore filamento</figcaption></figure></div>

<h2>I comandi M412</h2>
<p>Tutto si imposta via USB da un terminale seriale (Pronterface, il terminale del tuo slicer o di OctoPrint,
250000 baud). I parametri si possono combinare in un unico comando, per esempio <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Comando</th><th>Cosa fa</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Mostra lo stato, per esempio <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Attiva il rilevamento</strong>: l'interruttore di fine filamento, e anche il rilevamento di inceppamento se la lunghezza di inceppamento non è 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Disattiva tutto il rilevamento</strong>, fine filamento e inceppamento.</td></tr>
<tr><td><code>M412 D5</code></td><td>Quando l'interruttore non vede più il filamento, continua a stampare per <strong>5 mm</strong> prima della pausa, per usare il filamento rimasto tra il sensore e l'ugello. Predefinito 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Attiva il rilevamento di inceppamento</strong> (solo sensore BTT): mette in pausa quando <strong>10 mm</strong> di filamento passano nell'estrusore senza che la rotella del sensore si muova.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Disattiva il rilevamento di inceppamento</strong> e lascia l'interruttore di fine filamento com'è. È l'impostazione predefinita.</td></tr>
<tr><td><code>M500</code></td><td>Salva le impostazioni. Senza, una modifica va persa quando la stampante viene spenta.</td></tr>
<tr><td><code>M119</code></td><td>La riga <em>filament</em> mostra <code>TRIGGERED</code> con il filamento caricato, <code>open</code> senza.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, e <code>L</code> usato da solo, vengono dalla nostra modifica a Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), inclusa in questi firmware. Nel Marlin senza questa modifica, <code>L</code>
da solo viene ignorato e <code>L0</code> mette subito in pausa la stampa come se fosse un inceppamento.</p>

<h2>L'interruttore di fine filamento Wanhao</h2>
<p>Dice al firmware se il filamento c'è. Quando manca, la stampa va in pausa dopo altri 5 mm di
filamento e lo schermo avvia un cambio filamento.</p>
<p><strong>È attivo di default su ogni modello, dalla v2.0.8.</strong> Se su D8 non è collegato nulla, la resistenza di
pull-up della scheda tiene il pin a 5 V, che viene letto come «filamento presente»: il rilevamento quindi non scatta mai, per cui può restare attivo
che il sensore sia montato o no. Collega un interruttore di fine filamento a D8 e funziona subito.</p>
<ul>
<li>Il rilevamento di inceppamento resta disattivato (<code>L0</code>): questo interruttore non può vedere il filamento muoversi.</li>
<li>Per disattivare l'interruttore: <code>M412 S0</code> poi <code>M500</code>.</li>
<li>Le impostazioni salvate da una release precedente mantengono il loro stato attivo/disattivo. Per attivarlo: <code>M412 S1</code> poi
<code>M500</code>, oppure torna ai valori predefiniti (<code>M502</code> poi <code>M500</code>, che cancella anche lo Z offset
della sonda e la mesh).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Questo sensore ha due uscite, e il firmware le legge in modo diverso:</p>
<ul>
<li><strong>L'interruttore di fine filamento</strong> (su D8) è un livello: 5 V finché il filamento c'è, 0 V quando non c'è più.</li>
<li><strong>L'uscita di movimento</strong> (su D9) viene da una piccola rotella che il filamento fa girare passando. Ogni pochi
millimetri di filamento l'uscita commuta tra 0 V e 5 V. Il firmware guarda solo questi cambi: se
l'estrusore spinge la lunghezza di inceppamento senza nemmeno un cambio, il filamento non sta seguendo (bobina aggrovigliata, inceppamento,
filamento mangiato dall'estrusore) e la stampa va in pausa. L'interruttore di fine filamento non può accorgersene: durante un inceppamento il filamento c'è ancora.</li>
</ul>
<h3>Cablaggio</h3>
<p><strong>5V</strong> su 5V, <strong>GND</strong> su GND, il segnale di <strong>fine filamento</strong> su <strong>D8</strong>
e il segnale di <strong>movimento</strong> su <strong>D9</strong>. I nomi stampati sul cavo del sensore possono essere diversi.</p>
<h3>Attivarlo</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Se le stampe vanno in pausa senza motivo, aumenta la lunghezza di inceppamento: <code>M412 L15</code> poi <code>M500</code>. Per tenere solo
l'interruttore di fine filamento: <code>M412 L0</code> poi <code>M500</code>.</p>
<h3>Verificarlo</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> con il filamento caricato: <em>filament: TRIGGERED</em>. Se quella riga cambia mentre spingi il filamento
a mano invece che quando lo inserisci o lo togli, i due fili di segnale sono invertiti: scambia D8 e D9.</li>
</ul>
<div class="note">Il rilevamento di inceppamento è stato testato su una MK2 300 senza il sensore (una lunghezza di inceppamento di 2 mm scatta, <code>L0</code> mai),
ma non ancora con il sensore BTT vero e proprio. Se l'interruttore viene letto al contrario (<em>open</em> con il filamento
caricato), diccelo su <a href="{DISCORD}">Discord</a>.</div>

<h2>Aggiornare dalla v2.0.5 o dalla v2.0.6</h2>
<p>Quelle release non permettevano di disattivare il rilevamento di inceppamento, quindi usavano una lunghezza di inceppamento troppo grande per essere mai raggiunta: 100 m nella
v2.0.5 (in realtà troppo poco: circa un terzo di una bobina da 1 kg, dopo di che una stampante lasciata accesa poteva mettersi in pausa senza motivo) e
10 km nella v2.0.6. All'avvio della stampante, la v2.0.7 carica questi due valori come <code>L0</code>. Una lunghezza reale impostata
per un sensore BTT, come <code>L10</code>, viene mantenuta. Dalla v2.0.4 o precedenti, viene caricata la distanza di fine filamento di 5 mm
al posto dello 0 salvato da quelle versioni.</p>
""")

    if page == "slicer":
        return ("Profili Cura e OrcaSlicer per la Wanhao Duplicator 9, e regolazione dell'offset Z",
                "Profili UltiMaker Cura e OrcaSlicer pronti all'uso per tutte le Wanhao D9, PLA, PETG e ABS, come "
                "regolare l'offset Z della sonda, lanciare una tastatura del piatto e stampare un 3DBenchy di prova.",
                f"""
<h1>Slicing per la Duplicator 9</h1>
<p class="lead">Un profilo per ognuna delle dodici stampanti, per <strong>UltiMaker Cura</strong> e
<strong>OrcaSlicer</strong>, entrambi gratuiti e disponibili su Windows, macOS e Linux. Ognuno riprende il volume di
stampa, le accelerazioni e la temperatura massima del piatto del proprio firmware.</p>

<h2>Download</h2>
{h.slicer}
<p>Sono fatti per il firmware di questo sito, <a href="{p('flash')}">v2.0.9 o successivo</a>.</p>

<h2>Installarli</h2>
<p><strong>OrcaSlicer</strong>: <em>File</em> → <em>Importa</em> → <em>Importa configurazioni…</em>, poi scegli il file
<code>.orca_printer</code>. La stampante, le sue tre qualità (0,12, 0,20 e 0,28 mm) e i filamenti PLA, PETG e ABS
compaiono tra i tuoi preset.</p>
<p><strong>Cura</strong>: <em>Guida</em> → <em>Mostra cartella di configurazione</em>, chiudi Cura, scompatta il file in
quella cartella, riavvia Cura, poi <em>Impostazioni</em> → <em>Stampante</em> → <em>Aggiungi stampante…</em> →
<em>Aggiungi una stampante non in rete</em> → <em>Wanhao</em> → il tuo modello. La <em>Wanhao Duplicator 9</em> fornita
con Cura è un profilo più vecchio: solo la 300, con raft e supporti attivi di default.</p>

<h2 id="first-print">Prima della prima stampa: l'offset Z, poi una tastatura</h2>
<p>La sonda scatta un po' sopra il piatto, e il firmware deve sapere di quanto. È l'<strong>offset Z</strong>. Troppo in
alto, il primo strato non aderisce; troppo in basso, l'ugello raschia il piatto. Si regola una volta sola, ed è il
parametro che decide se le tue stampe tengono o no.</p>
<div class="note">Tutto quello che segue resta nella memoria della stampante, non nello slicer. Sopravvive a un
aggiornamento del firmware (dalla v2.0.3).</div>

<h3>1. Scalda prima di tutto</h3>
<p>Un ugello caldo è più lungo di qualche centesimo di millimetro. Scalda come per una stampa: sullo schermo,
<em>Temperatura</em> → <em>Preriscaldo</em> → <em>PLA</em> (200 °C e 60 °C), e aspetta un paio di minuti.</p>

<h3>2. Azzera gli assi</h3>
<p>Sullo schermo: <em>Impostazioni</em> → <em>Muovi</em> → <em>Home</em>. Via USB: <code>G28</code>.</p>

<h3>3. Regola l'offset Z</h3>
<p><strong>Il modo più semplice, stampando.</strong> Avvia una stampa e, durante il <strong>primo strato</strong>, vai
in <em>Regola</em> → <em>Offset Z</em> sullo schermo. Scendi a passi di 0,01 mm mentre la linea viene tracciata, finché
non è piatta e tocca la vicina senza lasciare vuoti. Troppo in alto, restano cordoncini tondi e separati; troppo in
basso, la superficie diventa ruvida e schiacciata e si vede l'ugello che scava. Il valore viene salvato da solo.</p>
<p><strong>Con il foglio di carta, senza stampare.</strong> Via USB, a temperatura di stampa:</p>
<pre><code>M851 Z0     ; dimentica l'offset attuale
M500
G28         ; rifai l'azzeramento perché venga preso in conto
M420 S0     ; ignora la mesh durante la misura
M211 S0     ; permette di scendere sotto Z0: i finecorsa software fermano lì l'ugello
G1 Z0 F300  ; l'ugello scende allo zero che crede il firmware</code></pre>
<p>Infila un foglio di carta sotto l'ugello, poi scendi a piccoli passi con <code>G91</code> e poi
<code>G1 Z-0.05 F60</code>, ancora e ancora, finché il foglio comincia appena a fare attrito. Leggi il valore con
<code>M114</code>: è negativo, per esempio −1,30. Poi:</p>
<pre><code>G90
M851 Z-1.30 ; il tuo valore
M500
M211 S1     ; rimette i finecorsa software, proteggono il piatto</code></pre>
<p>Dalla v2.1.0 le due righe <code>M211</code> non servono: il firmware permette già all'ugello di scendere 3 mm sotto lo zero.</p>

<h3>4. Tasta il piatto</h3>
<p>Sullo schermo: <em>Impostazioni</em> → <em>Livellamento</em> → <em>Automatico</em> → <em>Tasta</em>. La stampante
misura 25 punti e <strong>salva la mesh da sola</strong> (esegue <code>G29</code> e poi <code>M500</code>). Conta
qualche minuto. Via USB: <code>G29</code> e poi <code>M500</code>.</p>
<p>I nostri profili non tastano prima di ogni stampa: riattivano la mesh salvata con <code>M420 S1</code>, subito dopo
l'azzeramento. Rifai quindi una tastatura quando sposti la stampante, cambi la superficie o l'ugello, oppure quando il
primo strato è buono da un lato del piatto e non dall'altro.</p>

<h3>5. Verifica</h3>
<p><code>M503</code> elenca quello che è memorizzato: la riga <code>M851</code> è il tuo offset Z, e
<code>M420 S1</code> indica che la mesh è attiva. Sullo schermo, la pagina <em>Automatico</em> mostra i 25 punti
misurati.</p>

<h2>Stampe di prova</h2>
<p>Un 3DBenchy già affettato per una <strong>D9 MK2 300</strong>, per confrontare i due slicer o per verificare un
parametro senza installare niente:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Circa un'ora e mezza e 4 m di filamento ciascuno. Per un altro modello o un'altra taglia, affetta il
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> da te con il tuo profilo.</p>
<h3>Il test tutto-in-uno</h3>
<p>Barre a sbalzo, un ponte, torri per lo stringing, fori di tolleranza e una scala di finezza in un pezzo da 65 mm,
circa 2 h 30. È l'<a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> di
<strong>majda107</strong> (CC BY 4.0), affettato per <strong>ogni stampante</strong> e per entrambi gli slicer, nei tre
materiali. I file dell'<a href="{REPO}/releases/latest">ultima versione</a> si chiamano
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, per esempio
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy stampato con il profilo OrcaSlicer su una Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy stampato con il profilo Cura su una Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="3DBenchy stampato in PETG su una Wanhao D9, da dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Da quale cominciare:</strong> su una D9 MK2 300 in PLA, lo stesso Benchy ha richiesto <strong>1 h 14 con
OrcaSlicer</strong> e <strong>1 h 22 con Cura</strong>, e le pareti di OrcaSlicer sono venute un po' più pulite. Sono
buoni entrambi; OrcaSlicer è quello da cui partiremmo noi, e i suoi strumenti di calibrazione (flusso, pressure
advance, torri di temperatura) servono appena vuoi andare oltre.</p>
<div class="note">La D9 è aperta: l'ABS chiede come minimo una stanza senza correnti d'aria, e la sua temperatura di
piatto è riportata a quello che accetta il tuo modello (80 °C su una MK3 500).</div>

<h2>Cosa contengono i profili</h2>
<ul>
<li><strong>Strati</strong> da 0,20 mm, <strong>3 pareti</strong>, 4 strati pieni sopra e 3 sotto, riempimento giroide
al 15 %, uno skirt di 2 giri, niente supporti.</li>
<li><strong>Velocità</strong>: 40 mm/s sulla parete esterna, 60 all'interno, 70 per il riempimento, 20 sul primo
strato, 150 negli spostamenti. Wanhao indica 70 mm/s come velocità di stampa massima della D9.</li>
<li><strong>Retrazione</strong> di 1,5 mm a 25 mm/s: tutte le D9 hanno un estrusore MK10 diretto, e il firmware limita
l'estrusore a 25 mm/s.</li>
<li><strong>Temperature</strong>: PLA 210 °C poi 205, piatto 65 poi 60. PETG 240 / 80 poi 235 / 75. ABS 245 / 105 poi
245 / 100.</li>
<li><strong>Una linea di innesco</strong> a 15 mm dal bordo sinistro, oltre le clip del piatto: l'ugello arriva pulito
sul pezzo.</li>
<li>Alla fine, l'ugello sale e il piatto viene in avanti.</li>
</ul>
<p>Tutti i parametri e come modificarli: <a href="{REPO}/tree/main/Slicer">cartella Slicer</a> su GitHub.</p>
""")

    if page == "quiet":
        return ("Rendere più silenziosa una Wanhao Duplicator 9: quali ventole, e la ventola della scheda con termistori NTC",
                "Quali ventole della Wanhao D9 si possono rendere più silenziose: quella dell'hotend deve restare, quella dell'alimentatore "
                "si regola già da sola, e quella della scheda si può scollegare o far funzionare con termistori NTC.",
                f"""
<h1>Rendere più silenziosa la Duplicator 9</h1>
<p class="lead">A riposo, il rumore della D9 viene dalle sue ventole. Ecco quale si può rendere più silenziosa, e come.</p>
<div class="note">Lavora con la stampante <strong>scollegata dalla presa</strong>. Tieni ogni filo lontano dalla parte a 230 V.</div>

<h2>Le ventole</h2>
<div class="table"><table class="stack"><thead><tr><th>Ventola</th><th>Comandata da</th><th>Si può rendere più silenziosa?</th></tr></thead><tbody>
<tr><td><strong>Ventola del dissipatore dell'hotend</strong> (testina)</td><td>niente: 24 V sempre accesa</td><td><strong>no</strong>: di solito è la più rumorosa, ma rallentarla lascia salire il calore lungo l'hotend e inceppa il filamento (heat creep)</td></tr>
<tr><td><strong>Ventola di raffreddamento del pezzo</strong> (testina)</td><td>firmware, pin D5 (PWM)</td><td>già variabile: impostata dallo slicer e da <code>M106</code></td></tr>
<tr><td><strong>Ventola dell'alimentatore</strong></td><td>l'alimentatore stesso</td><td>niente da fare: sull'esemplare controllato qui (Chuanglian A-350FAK-24) segue già la temperatura dell'alimentatore</td></tr>
<tr><td><strong>Ventola della scheda</strong> (scatola dell'elettronica)</td><td>niente: 24 V sempre accesa</td><td><strong>sì</strong>, vedi sotto</td></tr>
</tbody></table></div>
<p>Il firmware Wanhao non comanda né una ventola della scheda né una ventola dell'hotend (<code>CONTROLLER_FAN_PIN</code> e
<code>E0_AUTO_FAN_PIN</code> valgono entrambi <code>-1</code>), e la scheda non ha uscite commutate libere. Per questo queste
due sono collegate ai connettori «24V OUT» sempre alimentati, e nessun firmware può rallentarle.</p>

<h2>Ventola della scheda</h2>
<p>Sull'esemplare misurato qui: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A max, cuscinetto a bronzina</strong>.</p>
<p><strong>Molti possessori la scollegano e basta.</strong> La scheda resta fresca: si trova sul fondo della scatola dell'elettronica, sotto
il piatto riscaldato, e il calore del piatto sale allontanandosi da lei. Se lo fai, tieni d'occhio le prime stampe lunghe: un driver
dei motori passo-passo che si surriscalda si spegne per un attimo, e questo si vede come <strong>layer spostati</strong>, non come un messaggio d'errore.</p>
<h3>Tenerla, ma solo quando i driver sono caldi</h3>
<p>Due termistori NTC di potenza in serie fanno partire la ventola intorno a 45–50 °C e la fanno accelerare man mano che i driver si scaldano:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), incollati a un dissipatore di un driver con adesivo
termoconduttivo, reofori isolati.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ventola (+)
                                    ventola (−) ── 0V</code></pre>
<ul>
<li>Questo è un calcolo, <strong>non ancora testato su una stampante</strong>: la tolleranza degli MF72 è ±20 %, e una piccola ventola può
partire più in basso del previsto. Verifica la temperatura di avvio al banco (NTC in un sacchetto nell'acqua calda, con un termometro
da cucina); aggiungi un secondo 200 Ω se parte troppo presto, togli il 200 Ω se parte troppo tardi.</li>
<li>Gli NTC devono essere incollati a un dissipatore: all'aria libera, la corrente della ventola (fino a circa 0,6 W negli NTC) li scalda di
decine di gradi.</li>
<li>In questo modo la ventola non raggiunge mai la piena velocità (circa 75 % a 80 °C), e un NTC che si guasta si apre: la ventola allora si ferma
per sempre.</li>
</ul>
<p>Fonti: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">datasheet MF72</a>.</p>
""")
    raise KeyError(page)
