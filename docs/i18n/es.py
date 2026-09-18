"""Español: translation of en.py."""

META = {"name": "Español", "locale": "es_ES", "dir": "ltr"}

UI = {
    "nav": {"index": "Inicio", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Guía de flasheo", "screen": "Pantalla", "sensor": "Sensor de filamento", "slicer": "Slicer", "quiet": "Menos ruido"},
    "language": "Idioma",
    "model": "Modelo",
    "size": "Tamaño", "volume": "Volumen de impresión", "file": "Firmware",
    "footer_src": "Código fuente e issues en GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware bajo licencia GNU GPL v3. Los manuales y firmwares de Wanhao siguen siendo de Wanhao.",
}

# Etiquetas del esquema de conexión del sensor (img/d9-sensor-plug-<idioma>.svg).
SVG = {
    "board": "Placa base Wanhao D9 (vista superior)",
    "plug": "conector del sensor",
    "switch": "fin de filamento",
    "motion": "movimiento",
    "level": "nivel: con / sin filamento",
    "pulses": "pulsos mientras avanza el filamento",
    "names": "los nombres en su sensor pueden variar",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Firmware Marlin actualizado para todas las Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "archivos de pantalla, firmwares originales y manuales de Wanhao, y cómo flashearlos.",
                f"""
<h1>Firmware Wanhao Duplicator 9</h1>
<p class="lead">El sitio de descargas de Wanhao para la Duplicator 9 ya no existe. Aquí está todo lo que necesita
quien tenga una D9: firmware Marlin 2.1 actualizado para cada modelo y tamaño, los archivos de la pantalla táctil
correspondientes, los firmwares originales de Wanhao, los manuales de Wanhao y guías de flasheo paso a paso.</p>
<p><a class="btn" href="{REPO}/releases/latest">Todas las descargas</a> <a class="btn ghost" href="{DISCORD}">Preguntar en Discord</a></p>

<h2>¿Qué D9 tengo?</h2>
<div class="split"><div>
<ol>
<li><strong>Cable plano gris</strong> hasta el cabezal de impresión, una <strong>sonda cilíndrica metálica</strong>
junto a la boquilla y ningún refuerzo lateral en el marco: <a href="{p('mk1')}">MK1</a>.</li>
<li>La misma máquina de primera generación con una <strong>sonda BLTouch blanca</strong> en lugar de la metálica:
una MK1 con el kit de actualización de Wanhao, <a href="{p('mk1u2')}">MK1 + kit MK2</a>.</li>
<li><strong>Refuerzos inclinados</strong> a ambos lados del marco, un <strong>cable negro redondo</strong>
hasta el cabezal y un BLTouch: una MK2 o una MK3. Mire bajo la cama el <strong>motor Y</strong>, el que
mueve la cama: si está atrás, es una <a href="{p('mk2')}">MK2</a>; si está delante, del lado de la pantalla táctil, una
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>El número tras D9 es el tamaño: D9/300, D9/400 o D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 con sus refuerzos laterales">
<figcaption>D9 MK2: refuerzos laterales, cable redondo</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Sonda inductiva, cable plano. Firmware, Wanhao V0.15 a V0.164(B), manual.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + kit MK2</h3><p>MK1 actualizada con el kit BLTouch. Firmware y Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware del kit →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, refuerzos laterales. Firmware, Wanhao V1.1.2, guías.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Motor Y delante, sensor de filamento. Firmware y Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>Qué aportan estos firmwares</h2>
<ul>
<li><strong>Marlin 2.1</strong> compilado a partir de las configuraciones de la Duplicator 9 publicadas en
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
con los cambios propuestos allí: sonda de la MK1 leída en el sentido correcto, dirección Y de la MK3, recuperación tras
corte de luz, filtro de ruido en los finales de carrera.</li>
<li><strong>Los ajustes de fábrica de Wanhao</strong>, tomados del firmware y del código fuente de Wanhao para cada modelo: pasos/mm,
velocidades, aceleraciones, PID del hotend, offsets y márgenes de palpado de la sonda, homing, límites térmicos, jerk y dirección de los ejes.</li>
<li><strong>Recuperación tras corte de luz</strong>: al imprimir desde la SD, el trabajo se guarda en cada cambio de capa y, tras un corte, la pantalla ofrece reanudar desde ese punto.</li>
<li><strong>Sensores de filamento</strong>: un interruptor de fin de filamento en D8, activado por defecto en todos los modelos (sin efecto si no hay ninguno), y el BTT Smart Filament Sensor V2.0, que además detecta atascos. Vea <a href="{p('sensor')}">Sensor de filamento</a>.</li>
<li><strong>El cabezal vuelve al centro tras nivelar la cama</strong>, así la cama ya no tapa la pantalla.</li>
<li><strong>Una nueva interfaz de pantalla táctil en 16 idiomas</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, con una página para configurar el sensor de filamento.</li>
</ul>

<h2>Flashear en tres pasos</h2>
<ol>
<li>Descargue el <strong>.hex</strong> de su modelo y tamaño desde su página.</li>
<li>Flashéelo por USB con AVRDUDESS o avrdude: <a href="{p('flash')}">guía de flasheo</a>.</li>
<li>Flashee la pantalla táctil desde una tarjeta microSD: <a href="{p('screen')}">guía de la pantalla</a>.</li>
</ol>
<p>Los firmwares originales de Wanhao siguen disponibles en la página de cada modelo, así que una máquina siempre puede volver a su estado de fábrica.</p>
""")

    if page == "mk1":
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para la Wanhao D9 MK1 con sonda inductiva, firmwares originales de Wanhao V0.15 a V0.164(B), "
                "archivos de pantalla y manual de usuario de la MK1.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">La primera Duplicator 9: una sonda inductiva metálica junto a la boquilla, un cable plano gris hasta el
cabezal de impresión y un marco sin refuerzos laterales.</p>
<p>Estas compilaciones leen la sonda inductiva en el sentido correcto (se activa en nivel bajo) y toman los ajustes del
último firmware MK1 de Wanhao, la V0.164(B), offsets de la sonda incluidos (X 15, Y 0). El motor Y está atrás, tal como
lo montó Wanhao.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Sonda inductiva y cable plano en el cabezal de una Wanhao D9 MK1">
<figcaption>MK1: sonda inductiva, cable plano</figcaption></figure></div>

<h2>Descarga</h2>
{dl("MK1")}
<p>Elija el archivo de su tamaño y después flashee la pantalla con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documentos de Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Manual de usuario D9 MK1</a> (junio de 2018, en inglés): montaje, cableado, menús, nivelación, solución de problemas.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Guía de inicio D9 MK1</a> (en inglés).</li>
</ul>

<h2>Firmwares originales de Wanhao</h2>
<p>Para dejar una máquina tal como salió de fábrica. Cada firmware de placa base solo funciona con el firmware de pantalla
de la misma versión.</p>
<div class="table"><table><thead><tr><th>Versión</th><th>Tamaño</th><th>Placa base</th><th>Pantalla</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Los ajustes de cada versión (pasos/mm, velocidades, PID, dirección de los ejes) figuran en
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, extraídos de los binarios de Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware Wanhao Duplicator 9 MK1 con kit de actualización MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 para una Wanhao D9 MK1 actualizada con el kit BLTouch MK2 de Wanhao, y firmware original del kit Wanhao V1.1.31.",
                f"""
<h1>Wanhao D9 MK1 con el kit de actualización MK2</h1>
<div class="split"><div>
<p class="lead">Una D9 de primera generación con el kit de actualización MK2 de Wanhao: el marco de la MK1, con una sonda
BLTouch en lugar de la sonda inductiva metálica.</p>
<p>Wanhao publicó un firmware aparte para esta combinación, porque el BLTouch del kit no queda en el mismo sitio que el
de una MK2 de fábrica: el offset Y de la sonda es distinto. Estas compilaciones usan la geometría del kit. El motor Y está
atrás.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Sonda BLTouch en el cabezal de una Wanhao D9">
<figcaption>Sonda BLTouch</figcaption></figure></div>

<h2>Descarga</h2>
{dl("MK1u2")}
<p>Elija el archivo de su tamaño y después flashee la pantalla con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Estas compilaciones usan el offset de sonda del firmware del kit, Y −10. Es la única línea en la que el
código fuente del kit de Wanhao difiere del de la MK2 de fábrica (Y 0): el BLTouch del kit queda más atrás. Si la malla de
la cama parece desplazada de delante hacia atrás, mida su propio offset con la <a href="{REPO}/blob/main/Offset.md">guía de offsets</a>.</div>

<h2>Firmwares originales de Wanhao</h2>
<p>El firmware V1.1.31 del kit de Wanhao (diciembre de 2018), que se usa con el firmware de pantalla de la MK2.</p>
<div class="table"><table><thead><tr><th>Tamaño</th><th>Placa base</th><th>Pantalla</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ajustes extraídos de los binarios de Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para la Wanhao D9 MK2 con BLTouch, firmware y archivos de pantalla originales de Wanhao V1.1.2, y guías de Wanhao para la MK2.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">La segunda Duplicator 9: refuerzos inclinados a ambos lados, un cable de datos negro y redondo hasta el
cabezal de impresión, una sonda BLTouch y un portabobinas arriba.</p>
<p>Wanhao también cambió los carros a cuatro ruedas, montó un eje Y de doble guía y una correa más gruesa en las 400
y 500, y una cama de doble cara en las 300 y 400. El motor Y está atrás; estas compilaciones mueven el eje Y en el mismo
sentido que el firmware V1.1.2 de Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Descarga</h2>
{dl("MK2")}
<p>Elija el archivo de su tamaño. Una MK2 cuyo cabezal también se actualizó a MK3 debe
usar el <a href="{p('mk3')}">firmware MK3</a>. Después flashee la pantalla con <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documentos de Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Guía de inicio D9 MK2</a> (en inglés).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">Las 12 mejoras de la MK1 a la MK2</a>, de Wanhao (en inglés).</li>
</ul>

<h2>Firmwares originales de Wanhao</h2>
<p>La V1.1.2 de Wanhao (octubre de 2018; la 500 se recompiló como V1.1.2.1 en julio de 2019), con el firmware de pantalla MK2 de Wanhao.</p>
<div class="table"><table><thead><tr><th>Tamaño</th><th>Placa base</th><th>Pantalla</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ajustes extraídos de los binarios de Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para la Wanhao D9 MK3 (motor Y delante, sensor de filamento) y firmware original de Wanhao V1.1.3.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK3</h1>
<p class="lead">La última Duplicator 9 conserva el marco y el BLTouch de la MK2, añade un sensor de fin de filamento y
lleva el motor Y a la parte delantera, del lado de la pantalla táctil.</p>
<p>Al cambiar de sitio el motor, el eje Y se invierte: el propio firmware V1.1.3 de Wanhao invierte Y, y estas compilaciones
también. El sensor de fin de filamento está activado por defecto. Wanhao no publicó offsets de sonda para la MK3, así que
estas compilaciones usan los de la MK2.</p>

<h2>Descarga</h2>
{dl("MK3")}
<p>Elija el archivo de su tamaño y después flashee la pantalla con
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Si el sensor de filamento detiene las impresiones al azar, desactívelo con <code>M412 S0</code> y luego
<code>M500</code>. Wanhao Europe había publicado un firmware MK3 «ReverseMode» para ese problema; después se retiró y no
ha sido posible encontrarlo.</div>

<h2>Firmwares originales de Wanhao</h2>
<p>La V1.1.3 de Wanhao (agosto de 2019). Wanhao no publicó ningún firmware de pantalla para la MK3: sus descargas MK3 usaban el de la MK2.</p>
<div class="table"><table><thead><tr><th>Tamaño</th><th>Placa base</th><th>Pantalla</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ajustes extraídos de los binarios de Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Cómo flashear el firmware de la placa base de una Wanhao Duplicator 9 (D9)",
                "Guía paso a paso para flashear Marlin en una Wanhao D9 por USB con AVRDUDESS o avrdude, resolver problemas "
                "de homing y volver al firmware de Wanhao.",
                f"""
<h1>Flashear la placa base de la Duplicator 9</h1>
<p class="lead">La placa base de la D9 es un ATmega2560 con bootloader USB: sin programador, sin abrir la base,
solo un cable USB.</p>

<h2>Qué necesita</h2>
<ul>
<li>Un cable USB entre la impresora y el ordenador, y la impresora <strong>encendida</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, gráfico, lo más sencillo) o
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (línea de comandos, cualquier sistema).</li>
<li>El <strong>.hex</strong> de su modelo y tamaño: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Antes de flashear</h2>
<div class="note">Envíe <code>M503</code> y guarde la respuesta. Desde la v2.0.3, una actualización conserva los ajustes
guardados en la impresora, pero actualizar <strong>a</strong> la v2.0.3 arranca una vez con los valores por defecto de este
firmware (cambió la forma de guardar los ajustes), y lo mismo ocurre al venir del firmware de Wanhao. Después vuelva a
ajustar el offset Z de la sonda con <code>M851 Z…</code> y <code>M500</code>.</div>
<p>Cierre todos los programas que puedan ocupar el puerto de la impresora: Cura, PrusaSlicer, OctoPrint, Pronterface, terminales serie.</p>

<h2>Flashear con AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: el puerto COM de su impresora (por ejemplo <code>COM3</code>). Deje la velocidad en baudios por defecto.</li>
<li>Flash: elija el archivo .hex y haga clic en <strong>Program!</strong>. Tarda de 30 a 60 segundos.</li>
</ol>

<h2>Flashear con avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Sustituya el puerto y el nombre del archivo por los suyos. El protocolo <code>wiring</code> elige por sí solo la velocidad del bootloader.</p>

<h2>Primer arranque</h2>
<ol>
<li>Desconecte el cable USB, apague y encienda la impresora, y vuelva a conectar el cable.</li>
<li>Conéctese a <strong>250000 baudios</strong> (los firmwares de Wanhao usaban 115200) y envíe <code>M115</code>: la respuesta muestra el nuevo firmware.</li>
<li>Haga homing de todos los ejes, luego nivele la cama desde la pantalla o con <code>G29</code>, y guarde con <code>M500</code>.</li>
</ol>

<h2 id="reset">Volver a los ajustes por defecto de este firmware</h2>
<p>Desde la v2.0.3, una actualización de firmware <strong>conserva</strong> los ajustes guardados en la impresora (offset Z de la
sonda, pasos/mm, PID, malla…). Por eso, los nuevos valores por defecto de una versión no reemplazan a los ya guardados.
Restablezca una vez si actualiza desde la v2.0.2 o anterior y conserva valores guardados a mano, si la impresora se comporta
de forma extraña tras probar otros firmwares, o siempre que quiera empezar de cero:</p>
<ul>
<li><strong>En la pantalla:</strong> <em>Ajustes</em> → <em>Más</em> → <em>Restablecer</em> → ✓.</li>
<li><strong>Por USB:</strong> envíe <code>M502</code> (carga los valores por defecto de este firmware) y luego <code>M500</code> (los guarda).</li>
</ul>
<p>Después vuelva a ajustar el offset Z de la sonda (<code>M851 Z…</code> y luego <code>M500</code>) y nivele la cama. Compruebe el
resultado con <code>M503</code>.</p>

<h2>Corte de luz y sensor de filamento</h2>
<ul>
<li>La recuperación tras corte de luz está activada: el trabajo se guarda en cada cambio de capa. Desactívela con <code>M413 S0</code> y luego <code>M500</code>.</li>
<li>Una impresión que se detiene de inmediato con <em>power outage</em> en cuanto empieza a calentar: actualice a la v2.0.4 o posterior. Las versiones anteriores vigilaban la entrada de fallo de alimentación de la placa, que pasa a nivel bajo en cuanto arrancan los calentadores.</li>
<li>La detección de fin de filamento está activada por defecto en todos los modelos desde la v2.0.8, y no hace nada si no hay sensor. Tras actualizar desde una versión anterior, actívela con <code>M412 S1</code> y luego <code>M500</code>, o en la pantalla en <em>Ajustes</em> → <em>Filamento</em> → <em>Sensor de filamento</em>. Conexión y BTT Smart Filament Sensor: <a href="{p('sensor')}">Sensor de filamento</a>.</li>
</ul>

<h2>Solución de problemas</h2>
<div class="table"><table><thead><tr><th>Problema</th><th>Solución</th></tr></thead><tbody>
<tr><td>Puerto en uso</td><td>Cierre todos los programas que usan el puerto de la impresora.</td></tr>
<tr><td>Dispositivo no encontrado</td><td>Instale el controlador USB CH340, pruebe otro cable u otro puerto USB, compruebe que la impresora está encendida.</td></tr>
<tr><td>Caracteres ilegibles tras flashear</td><td>Use 250000 baudios con estos firmwares, 115200 con los de Wanhao.</td></tr>
<tr><td>Temperaturas multiplicadas por 10 en la pantalla (236 para 23,6 °C)</td><td>La pantalla aún tiene archivos antiguos: flashee <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>La pantalla vuelve al inglés en cada arranque, o su página <em>Sensor de filamento</em> no hace nada</td><td>El firmware de la placa base es anterior a la v2.0.9: actualícelo.</td></tr>
<tr><td>El homing se detiene unos milímetros antes del final de carrera, y luego <em>Homing Failed</em></td><td>Ruido eléctrico en la línea del final de carrera. Estos firmwares lo filtran desde la v2.0.1: actualice.</td></tr>
<tr><td>La boquilla golpea una pinza de la cama durante la nivelación</td><td>Actualice a la v2.0.2 o posterior: la primera columna de palpado queda a 10 mm del borde, como en el firmware de Wanhao.</td></tr>
<tr><td>La cama se aleja del final de carrera Y</td><td>Compruebe que tomó el firmware de su modelo: el motor Y está atrás en la MK1, la MK1 + kit y la MK2, y delante en la MK3.</td></tr>
</tbody></table></div>

<h2>Volver al firmware de Wanhao</h2>
<p>La página de cada modelo enlaza los firmwares originales de placa base y de pantalla de Wanhao. Se flashean del mismo modo;
el firmware de placa base de Wanhao necesita el firmware de pantalla de Wanhao de la misma generación.</p>
<p>Preguntas: <a href="{DISCORD}">Discord</a> o <a href="{REPO}/issues">issues de GitHub</a>.</p>
""")

    if page == "screen":
        return ("Firmware de la pantalla táctil Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 en 16 idiomas",
                "Cómo flashear la pantalla táctil DWIN de la Wanhao D9 con DGUS Reloaded 2.0 desde una tarjeta microSD: nueva interfaz en 16 "
                "idiomas, página del sensor de filamento, para Marlin 2.1. Y cómo volver al firmware de pantalla de Wanhao.",
                f"""
<h1>Flashear la pantalla táctil de la Duplicator 9</h1>
<p class="lead">Todas las D9, de la MK1 a la MK3, tienen la misma pantalla táctil DWIN T5 (480 × 272). Con estos firmwares
funciona con DGUS Reloaded 2.0, nuestra nueva interfaz en 16 idiomas, que se flashea desde una tarjeta microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Descargar DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Qué aporta DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 idiomas</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Toque la bandera junto al nombre de la impresora en la pantalla
de inicio para cambiarlo; la impresora recuerda la elección.</li>
<li><strong>Una página para el sensor de filamento</strong>: <em>Ajustes</em> → <em>Filamento</em> → <em>Sensor de filamento</em>. Vea
<a href="{p('sensor')}#screen">Sensor de filamento</a>.</li>
<li><strong>Una línea de estado que permanece</strong>: el último mensaje, <em>Ready</em> por ejemplo, sigue en pantalla en lugar
de desaparecer a los 30 segundos.</li>
<li><strong>Indicadores de temperatura</strong> para la boquilla y la cama, con la temperatura objetivo marcada.</li>
<li>Un nuevo aspecto en todas las páginas: tema oscuro, botones más grandes, pictogramas en las ventanas emergentes.</li>
</ul>
</div><figure><img src="{img}screen/es-home.png" width="480" height="272" alt="Pantalla de inicio de DGUS Reloaded 2.0 en una Wanhao D9: temperaturas de la boquilla y la cama con indicadores, línea de estado, botones Imprimir, Temperatura y Ajustes">
<figcaption>La pantalla de inicio</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 necesita la <strong>v2.0.9 o posterior</strong> en la placa base. Con la v2.0.8 o anterior, el
idioma vuelve al inglés en cada arranque y la página del sensor de filamento no funciona: <a href="{p('flash')}">flashee la
placa base</a> primero.</div>

<h2>1. Formatear la tarjeta microSD</h2>
<div class="note">FAT32 con un tamaño de unidad de asignación de <strong>4096 bytes</strong>. Con cualquier otro tamaño, la pantalla ignora la tarjeta.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 a menudo no formatea en FAT32; use <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
con un tamaño de unidad de asignación de 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (compruebe antes el dispositivo con <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (compruébelo con <code>diskutil list</code>).</li>
</ul>

<h2>2. Copiar los archivos</h2>
<p>Descomprima <code>DWIN_SET.zip</code> y copie la carpeta <code>DWIN_SET</code> completa en la raíz de la tarjeta.</p>

<h2>3. Flashear</h2>
<ol>
<li>Apague la impresora y desenchúfela.</li>
<li>Abra la parte delantera de la base para llegar a la parte trasera de la pantalla, donde está su ranura microSD.</li>
<li>Inserte la tarjeta y encienda. La pantalla muestra la actualización en 10 a 30 segundos; espere a que se reinicie
con normalidad, de 1 a 3 minutos en total.</li>
<li>Apague, retire la tarjeta y cierre la base.</li>
</ol>
<p>El <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">vídeo de Wanhao sobre la actualización de la pantalla de la D9</a> muestra dónde está la ranura.</p>

<h2>De dónde viene</h2>
<p>DGUS Reloaded 2.0 redibuja página por página <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(de Desuuuu y luego Neo2003). Su código fuente, el programa que genera los archivos de la pantalla y las traducciones están
en <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. ¿Una palabra incorrecta o poco natural en su idioma? Díganoslo en
<a href="{DISCORD}">Discord</a> o abra un issue allí.</p>
<p>Para volver a DGUS Reloaded 1.0.3, por ejemplo con un firmware anterior a la v2.0.9, flashee
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> del mismo modo.</p>

<h2>Volver a la pantalla de Wanhao</h2>
<p>El firmware de pantalla de Wanhao solo funciona con el firmware de placa base de Wanhao. MK1: el archivo de pantalla de la
versión correspondiente en la <a href="{p('mk1')}">página MK1</a>. MK1 + kit, MK2 y MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Mismo procedimiento.</p>
""")

    if page == "sensor":
        return ("Sensores de filamento en la Wanhao Duplicator 9: interruptor de fin de filamento y conexión del BTT Smart Filament Sensor",
                "Dónde conectar un sensor de filamento en la placa base de la Wanhao D9 (D8, D9, GND, 5V), cómo cablear un BTT Smart "
                "Filament Sensor V2.0 y activar la detección de fin de filamento y de atascos con M412.",
                f"""
<h1>Sensores de filamento</h1>
<p class="lead">Desde la v2.0.5, estos firmwares leen dos tipos de sensor: el interruptor de fin de filamento de Wanhao y el
BTT Smart Filament Sensor V2.0, que además detecta cuando el filamento deja de avanzar (bobina enredada, atasco, filamento
mordido). <strong>La detección de fin de filamento está activada por defecto en todos los modelos</strong>, y la detección de atascos está desactivada.</p>

<h2>El conector del sensor</h2>
<figure><img src="{img}d9-sensor-plug-es.svg" width="760" height="440" alt="Placa base de la Wanhao D9: el conector de sensor de 4 pines a la izquierda de POWER-DET, pines D9, D8, GND y 5V, cableado a un BTT Smart Filament Sensor V2.0"></figure>
<p>El conector de 4 pines a la izquierda de <strong>POWER-DET</strong>, debajo de los conectores de los finales de carrera, lleva <strong>D9, D8, GND y 5V</strong>,
en ese orden. Los nombres de los pines vienen de un esquema de cableado de Wanhao que dustovich encontró y compartió en el
<a href="{DISCORD}">Discord</a>; en la parte trasera de la placa, los mismos cuatro pines están rotulados CTRL, BTN, GND y VCC.</p>
<ul>
<li><strong>D8</strong> es la entrada de fin de filamento que lee el propio firmware de Wanhao.</li>
<li><strong>D9</strong> no la usa el firmware de Wanhao: estas compilaciones leen en ella la señal de movimiento del sensor BTT.</li>
</ul>
<div class="note">Impresora <strong>apagada</strong> siempre que conecte o desconecte algo en la placa.</div>

<h2 id="screen">En la pantalla</h2>
<div class="split"><div>
<p>Con DGUS Reloaded 2.0 en la pantalla (firmware v2.0.9 o posterior): <em>Ajustes</em> → <em>Filamento</em> →
<em>Sensor de filamento</em>.</p>
<ul>
<li><strong>Fin de filamento</strong> activa o desactiva toda la detección, como <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Detección de atasco</strong> activa la detección de atascos con la longitud de abajo, o la desactiva (<code>L0</code>).</li>
<li><strong>Longitud de atasco</strong>: − y + la cambian de 1 mm en 1 mm; toque el número para escribirlo.</li>
<li>El punto <strong>Filamento</strong> se ve verde cuando el interruptor detecta filamento, y rojo cuando no.</li>
<li>Los cambios se aplican al instante. <strong>Guardar</strong> los almacena, como <code>M500</code>. La flecha de volver sale sin
guardar: los ajustes guardados vuelven en el siguiente arranque.</li>
</ul>
</div><figure><img src="{img}screen/es-sensor.png" width="480" height="272" alt="Página del sensor de filamento de DGUS Reloaded 2.0: interruptores de detección de fin de filamento y de atasco, longitud de atasco con botones menos y más, indicador de filamento y botón Guardar">
<figcaption>Ajustes → Filamento → Sensor de filamento</figcaption></figure></div>

<h2>Los comandos M412</h2>
<p>Todo se configura por USB desde un terminal serie (Pronterface, el terminal de su slicer o de OctoPrint,
250000 baudios). Los parámetros se pueden combinar en un mismo comando, por ejemplo <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Comando</th><th>Qué hace</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Muestra el estado, por ejemplo <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Activa la detección</strong>: el interruptor de fin de filamento y también la detección de atascos si la longitud de atasco no es 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Desactiva toda la detección</strong>, interruptor y atascos.</td></tr>
<tr><td><code>M412 D5</code></td><td>Cuando el interruptor deja de detectar filamento, sigue imprimiendo <strong>5 mm</strong> antes de pausar, para aprovechar el filamento que queda entre el sensor y la boquilla. Por defecto, 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Activa la detección de atascos</strong> (solo sensor BTT): pausa cuando pasan <strong>10 mm</strong> de filamento por el extrusor sin que se mueva la rueda del sensor.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Desactiva la detección de atascos</strong> y deja el interruptor de fin de filamento como está. Es el valor por defecto.</td></tr>
<tr><td><code>M500</code></td><td>Guarda los ajustes. Sin él, los cambios se pierden al apagar la impresora.</td></tr>
<tr><td><code>M119</code></td><td>La línea <em>filament</em> muestra <code>TRIGGERED</code> con filamento cargado y <code>open</code> sin él.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, y <code>L</code> usado solo, vienen de nuestra modificación de Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), incluida en estos firmwares. En un Marlin sin ella, <code>L</code>
solo se ignora y <code>L0</code> pausa la impresión de inmediato como si hubiera un atasco.</p>

<h2>El interruptor de fin de filamento de Wanhao</h2>
<p>Indica al firmware si hay filamento. Cuando se acaba, la impresión se pausa tras 5 mm más de filamento
y la pantalla inicia un cambio de filamento.</p>
<p><strong>Está activado por defecto en todos los modelos desde la v2.0.8.</strong> Sin nada conectado en D8, la resistencia
pull-up de la placa mantiene el pin a 5 V, lo que se lee como «hay filamento»: la detección nunca salta, así que puede quedar
activada tanto si hay sensor como si no. Conecte un interruptor de fin de filamento en D8 y funciona directamente.</p>
<ul>
<li>La detección de atascos sigue desactivada (<code>L0</code>): este interruptor no puede ver si el filamento avanza.</li>
<li>Para desactivar el interruptor: <code>M412 S0</code> y luego <code>M500</code>.</li>
<li>Los ajustes guardados por una versión anterior conservan su estado activado o desactivado. Para activarlo: <code>M412 S1</code> y luego
<code>M500</code>, o vuelva a los valores por defecto (<code>M502</code> y luego <code>M500</code>, lo que también borra el offset Z de la
sonda y la malla).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Este sensor tiene dos salidas, y el firmware las lee de forma distinta:</p>
<ul>
<li><strong>El interruptor de fin de filamento</strong> (a D8) da un nivel: 5 V mientras hay filamento, 0 V cuando se ha acabado.</li>
<li><strong>La salida de movimiento</strong> (a D9) viene de una pequeña rueda que el filamento hace girar al pasar. Cada pocos
milímetros de filamento, la salida cambia entre 0 V y 5 V. El firmware solo vigila esos cambios: si el
extrusor empuja la longitud de atasco sin que se produzca ni uno, el filamento no está avanzando (bobina enredada, atasco,
filamento mordido) y la impresión se pausa. El interruptor de fin de filamento no puede verlo: durante un atasco, el filamento sigue ahí.</li>
</ul>
<h3>Cableado</h3>
<p><strong>5V</strong> a 5V, <strong>GND</strong> a GND, la señal del <strong>interruptor de fin de filamento</strong> a <strong>D8</strong>
y la señal de <strong>movimiento</strong> a <strong>D9</strong>. Los nombres impresos en el cable del sensor pueden ser distintos.</p>
<h3>Activarlo</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Si las impresiones se pausan sin motivo, aumente la longitud de atasco: <code>M412 L15</code> y luego <code>M500</code>. Para dejar solo
el interruptor de fin de filamento: <code>M412 L0</code> y luego <code>M500</code>.</p>
<h3>Comprobarlo</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> con filamento cargado: <em>filament: TRIGGERED</em>. Si esa línea cambia cuando empuja el filamento
a mano en lugar de cuando lo introduce o lo retira, los dos cables de señal están intercambiados: intercambie D8 y D9.</li>
</ul>
<div class="note">La detección de atascos se probó en una MK2 300 sin el sensor (con una longitud de atasco de 2 mm salta, con <code>L0</code> nunca),
pero todavía no con el propio sensor BTT. Si el interruptor se lee al revés (<em>open</em> con filamento
cargado), díganoslo en <a href="{DISCORD}">Discord</a>.</div>

<h2>Actualizar desde la v2.0.5 o la v2.0.6</h2>
<p>Esas versiones no permitían desactivar la detección de atascos, así que usaban una longitud de atasco tan larga que nunca se alcanzara: 100 m en
la v2.0.5 (en realidad demasiado corta: más o menos un tercio de una bobina de 1 kg, tras lo cual una impresora que se quedara encendida podía pausarse sin motivo) y
10 km en la v2.0.6. Al arrancar la impresora, la v2.0.7 carga esos dos valores como <code>L0</code>. Una longitud real que haya ajustado
para un sensor BTT, como <code>L10</code>, se conserva. Desde la v2.0.4 o anterior, se carga la distancia de fin de filamento de 5 mm
en lugar del 0 que guardaban esas versiones.</p>
""")

    if page == "slicer":
        return ("Perfiles de Cura y OrcaSlicer para la Wanhao Duplicator 9, y ajuste del offset Z",
                "Perfiles UltiMaker Cura y OrcaSlicer listos para usar para todas las Wanhao D9, PLA, PETG y ABS, cómo "
                "ajustar el offset Z de la sonda, lanzar un palpado de la cama e imprimir un 3DBenchy de prueba.",
                f"""
<h1>Laminar para la Duplicator 9</h1>
<p class="lead">Un perfil para cada una de las doce impresoras, para <strong>UltiMaker Cura</strong> y
<strong>OrcaSlicer</strong>, los dos gratuitos y disponibles en Windows, macOS y Linux. Cada uno lleva el volumen de
impresión, las aceleraciones y la temperatura de cama máxima de su propio firmware.</p>

<h2>Descarga</h2>
{h.slicer}
<p>Están hechos para el firmware de este sitio, <a href="{p('flash')}">v2.0.9 o posterior</a>.</p>

<h2>Instalarlos</h2>
<p><strong>OrcaSlicer</strong>: <em>Archivo</em> → <em>Importar</em> → <em>Importar configuraciones…</em>, y luego elija
el archivo <code>.orca_printer</code>. La impresora, sus tres calidades (0,12, 0,20 y 0,28 mm) y los filamentos PLA,
PETG y ABS aparecen en sus preajustes.</p>
<p><strong>Cura</strong>: <em>Ayuda</em> → <em>Mostrar carpeta de configuración</em>, cierre Cura, descomprima el
archivo en esa carpeta, vuelva a abrir Cura y luego <em>Ajustes</em> → <em>Impresora</em> → <em>Añadir impresora…</em>
→ <em>Añadir una impresora no conectada en red</em> → <em>Wanhao</em> → su modelo. La <em>Wanhao Duplicator 9</em> que
viene con Cura es un perfil más antiguo: solo la 300, con balsa y soportes activados por defecto.</p>

<h2 id="first-print">Antes de la primera impresión: el offset Z, y luego un palpado</h2>
<p>La sonda se dispara un poco por encima de la cama, y el firmware tiene que saber cuánto. Eso es el
<strong>offset Z</strong>. Demasiado alto, la primera capa no agarra; demasiado bajo, la boquilla raya la cama. Se
ajusta una sola vez, y es el ajuste que decide si sus impresiones se pegan o no.</p>
<div class="note">Todo lo que sigue se guarda en la memoria de la impresora, no en el slicer. Sobrevive a una
actualización del firmware (desde la v2.0.3).</div>

<h3>1. Caliente primero</h3>
<p>Una boquilla caliente es unas centésimas de milímetro más larga. Caliente como para imprimir: en la pantalla,
<em>Temperatura</em> → <em>Precalentar</em> → <em>PLA</em> (200 °C y 60 °C), y espere un par de minutos.</p>

<h3>2. Haga el origen de los ejes</h3>
<p>En la pantalla: <em>Ajustes</em> → <em>Mover</em> → <em>Origen</em>. Por USB: <code>G28</code>.</p>

<h3>3. Ajuste el offset Z</h3>
<p><strong>Lo más sencillo, imprimiendo.</strong> Lance una impresión y, durante la <strong>primera capa</strong>, vaya
a <em>Ajustar</em> → <em>Offset Z</em> en la pantalla. Baje de 0,01 en 0,01 mm mientras se traza la línea, hasta que
quede plana y toque a su vecina sin dejar hueco. Demasiado alto deja cordones redondos y separados; demasiado bajo deja
una superficie rugosa y aplastada donde se ve la boquilla escarbando. El valor se guarda solo.</p>
<p><strong>Con una hoja de papel, sin imprimir.</strong> Por USB, a temperatura de impresión:</p>
<pre><code>M851 Z0     ; olvida el offset actual
M500
G28         ; vuelve a hacer el origen para que se tenga en cuenta
M420 S0     ; ignora la malla durante la medición
M211 S0     ; permite bajar por debajo de Z0: los finales de carrera por software paran ahí la boquilla
G1 Z0 F300  ; la boquilla baja al cero que cree el firmware</code></pre>
<p>Deslice una hoja de papel bajo la boquilla y luego baje a pasos pequeños con <code>G91</code> y
<code>G1 Z-0.05 F60</code>, una y otra vez, hasta que la hoja apenas empiece a rozar. Lea el valor con
<code>M114</code>: es negativo, por ejemplo −1,30. Después:</p>
<pre><code>G90
M851 Z-1.30 ; su valor
M500
M211 S1     ; vuelve a poner los finales de carrera por software, protegen la cama</code></pre>

<h3>4. Palpe la cama</h3>
<p>En la pantalla: <em>Ajustes</em> → <em>Nivelación</em> → <em>Automático</em> → <em>Palpar</em>. La impresora mide
25 puntos y <strong>guarda la malla ella sola</strong> (lanza <code>G29</code> y luego <code>M500</code>). Cuente unos
minutos. Por USB: <code>G29</code> y luego <code>M500</code>.</p>
<p>Nuestros perfiles no palpan antes de cada impresión: reactivan la malla guardada con <code>M420 S1</code>, justo
después del origen. Así que vuelva a palpar cuando mueva la impresora, cambie de superficie o de boquilla, o cuando la
primera capa salga bien en un lado de la cama y no en el otro.</p>

<h3>5. Compruebe</h3>
<p><code>M503</code> muestra lo que hay guardado: la línea <code>M851</code> es su offset Z, y <code>M420 S1</code>
indica que la malla está activa. En la pantalla, la página <em>Automático</em> muestra los 25 puntos medidos.</p>

<h2>Impresiones de prueba</h2>
<p>Un 3DBenchy ya laminado para una <strong>D9 MK2 300</strong>, para comparar los dos slicers o comprobar un ajuste
sin instalar nada:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Alrededor de una hora y media y 4 m de filamento cada uno. Para otro modelo u otro tamaño, lamine usted mismo el
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> con su perfil.</p>
<h3>La prueba todo en uno</h3>
<p>Barras en voladizo, un puente, torres de stringing, agujeros de tolerancia y una escala de finura en una pieza de
65 mm, unas 2 h 30. Es el <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> de
<strong>majda107</strong> (CC BY 4.0), laminado para <strong>todas las impresoras</strong> y los dos slicers, en los
tres materiales. Los archivos de la <a href="{REPO}/releases/latest">última versión</a> se llaman
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, por ejemplo
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy impreso con el perfil OrcaSlicer en una Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy impreso con el perfil Cura en una Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
</div>
<p><strong>Por cuál empezar:</strong> en una D9 MK2 300 en PLA, el mismo Benchy tardó <strong>1 h 14 con
OrcaSlicer</strong> y <strong>1 h 22 con Cura</strong>, y las paredes de OrcaSlicer salieron algo más limpias. Los
dos son buenos; OrcaSlicer es por el que nosotros empezaríamos, y sus herramientas de calibración (flujo, pressure
advance, torres de temperatura) sirven en cuanto quiera ir más lejos.</p>
<div class="note">La D9 es abierta: el ABS pide como mínimo una habitación sin corrientes de aire, y su temperatura de
cama se rebaja a lo que acepte su modelo (80 °C en una MK3 500).</div>

<h2>Qué contienen los perfiles</h2>
<ul>
<li><strong>Capas</strong> de 0,20 mm, <strong>3 paredes</strong>, 4 capas sólidas arriba y 3 abajo, relleno giroide
al 15 %, una falda de 2 líneas, sin soportes.</li>
<li><strong>Velocidades</strong>: 40 mm/s en la pared exterior, 60 dentro, 70 para el relleno, 20 en la primera capa,
150 en desplazamiento. Wanhao da 70 mm/s como velocidad de impresión máxima de la D9.</li>
<li><strong>Retracción</strong> de 1,5 mm a 25 mm/s: todas las D9 llevan un extrusor MK10 de tracción directa, y el
firmware limita el extrusor a 25 mm/s.</li>
<li><strong>Temperaturas</strong>: PLA 210 °C y luego 205, cama 65 y luego 60. PETG 240 / 80 y luego 235 / 75. ABS
245 / 105 y luego 245 / 100.</li>
<li><strong>Una línea de cebado</strong> a 15 mm del borde izquierdo, más allá de las pinzas de la cama: la boquilla
llega limpia a la pieza.</li>
<li>Al final, la boquilla sube y la cama viene hacia delante.</li>
</ul>
<p>Todos los ajustes y cómo cambiarlos: <a href="{REPO}/tree/main/Slicer">carpeta Slicer</a> en GitHub.</p>
""")

    if page == "quiet":
        return ("Hacer más silenciosa una Wanhao Duplicator 9: qué ventiladores, y el ventilador de la placa con termistores NTC",
                "Qué ventiladores de la Wanhao D9 se pueden silenciar: el del hotend debe quedarse, el de la fuente de alimentación ya "
                "se regula solo, y el de la placa se puede desconectar o alimentar a través de termistores NTC.",
                f"""
<h1>Hacer más silenciosa la Duplicator 9</h1>
<p class="lead">En reposo, el ruido de la D9 viene de sus ventiladores. Aquí se explica cuál se puede silenciar y cómo.</p>
<div class="note">Trabaje con la impresora <strong>desenchufada</strong>. Mantenga todos los cables alejados del lado de 230 V.</div>

<h2>Los ventiladores</h2>
<div class="table"><table class="stack"><thead><tr><th>Ventilador</th><th>Controlado por</th><th>¿Se puede silenciar?</th></tr></thead><tbody>
<tr><td><strong>Ventilador del disipador del hotend</strong> (cabezal)</td><td>nada: 24 V siempre encendido</td><td><strong>no</strong>: suele ser el más ruidoso, pero si se ralentiza el calor sube por el hotend y atasca el filamento (heat creep)</td></tr>
<tr><td><strong>Ventilador de capa</strong> (cabezal)</td><td>el firmware, pin D5 (PWM)</td><td>ya es variable: lo ajustan el slicer y <code>M106</code></td></tr>
<tr><td><strong>Ventilador de la fuente de alimentación</strong></td><td>la propia fuente</td><td>no hace falta nada: en la unidad revisada aquí (Chuanglian A-350FAK-24) ya sigue la temperatura de la fuente</td></tr>
<tr><td><strong>Ventilador de la placa</strong> (caja de control)</td><td>nada: 24 V siempre encendido</td><td><strong>sí</strong>, vea más abajo</td></tr>
</tbody></table></div>
<p>El firmware de Wanhao no controla ningún ventilador de placa ni de hotend (<code>CONTROLLER_FAN_PIN</code> y
<code>E0_AUTO_FAN_PIN</code> valen ambos <code>-1</code>), y la placa no tiene ninguna salida conmutada libre. Por eso estos
dos van conectados a los conectores «24V OUT», siempre encendidos, y por eso ningún firmware puede ralentizarlos.</p>

<h2>Ventilador de la placa</h2>
<p>En la unidad medida aquí: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A máx., cojinete de deslizamiento (sleeve)</strong>.</p>
<p><strong>Muchos usuarios simplemente lo desconectan.</strong> La placa trabaja fría: está en el fondo de la caja de control, debajo de
la cama caliente, y el calor de la cama sube, alejándose de ella. Si lo hace, vigile sus primeras impresiones largas: un driver
de motor que se sobrecalienta se corta un instante, lo que se nota como <strong>capas desplazadas</strong>, no como un mensaje de error.</p>
<h3>Conservarlo, pero solo cuando los drivers se calientan</h3>
<p>Dos termistores NTC de potencia en serie hacen que el ventilador arranque hacia 45–50 °C y acelere a medida que se calientan los drivers:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), pegados al disipador de un driver con adhesivo
térmico, con las patas aisladas.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ventilador (+)
                                    ventilador (−) ── 0V</code></pre>
<ul>
<li>Esto es un cálculo, <strong>todavía no probado en una impresora</strong>: la tolerancia de los MF72 es de ±20 %, y un ventilador pequeño puede
arrancar a una temperatura más baja de lo previsto. Compruebe la temperatura de arranque en el banco de trabajo (los NTC en una bolsita dentro de agua caliente, con un
termómetro de cocina); añada un segundo de 200 Ω si arranca demasiado pronto, quite el de 200 Ω si arranca demasiado tarde.</li>
<li>Los NTC deben ir pegados a un disipador: al aire libre, la corriente del ventilador (hasta unos 0,6 W en los NTC) los calienta
decenas de grados.</li>
<li>Así el ventilador nunca llega a su velocidad máxima (alrededor del 75 % a 80 °C), y un NTC que falla queda en circuito abierto: entonces el ventilador se para
definitivamente.</li>
</ul>
<p>Fuentes: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">hoja de datos de los MF72</a>.</p>
""")
    raise KeyError(page)
