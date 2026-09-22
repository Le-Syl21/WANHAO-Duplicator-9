"""English: the site's reference text. Every other language in this folder is a translation of this file.

content(page, h) returns (title, description, body HTML) for one page. `h` carries the links and the pieces
built by build_site.py: h.p(page) links to another page in the same language, h.img is the image folder,
h.dl(model) is the download table and h.rows the table of Wanhao's firmwares for a model page.
"""

META = {"name": "English", "locale": "en_GB", "dir": "ltr"}

UI = {
    "nav": {"index": "Home", "mk1": "MK1", "mk1u2": "MK1 + MK2 kit", "mk2": "MK2", "mk3": "MK3",
            "flash": "Flash guide", "screen": "Screen", "sensor": "Filament sensor", "slicer": "Slicer", "quiet": "Quieter"},
    "language": "Language",
    "model": "Model",
    "size": "Size", "volume": "Build volume", "file": "Firmware",
    "footer_src": "Source and issues on GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware under GNU GPL v3. Wanhao's manuals and firmwares remain Wanhao's.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Wanhao D9 main board (top view)",
    "plug": "sensor plug",
    "switch": "runout switch",
    "motion": "motion",
    "level": "level: filament in / out",
    "pulses": "pulses while filament moves",
    "names": "names on your sensor may differ",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Wanhao Duplicator 9 firmware (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Up-to-date Marlin firmware for every Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "screen files, Wanhao's original firmwares and manuals, and how to flash them.",
                f"""
<h1>Wanhao Duplicator 9 firmware</h1>
<p class="lead">Wanhao's download site for the Duplicator 9 is gone. Everything a D9 owner needs is here instead:
current Marlin 2.1 firmware for every model and size, the matching touchscreen files, Wanhao's original
firmwares, Wanhao's manuals, and step-by-step flashing guides.</p>
<p><a class="btn" href="{REPO}/releases/latest">All downloads</a> <a class="btn ghost" href="{DISCORD}">Ask on Discord</a></p>

<h2>Which D9 do I have?</h2>
<div class="split"><div>
<ol>
<li><strong>Grey flat ribbon cable</strong> running to the print head, and a <strong>metal cylinder probe</strong>
next to the nozzle, no side reinforcements on the frame: <a href="{p('mk1')}">MK1</a>.</li>
<li>The same first-generation machine with a <strong>white BLTouch probe</strong> instead of the metal one:
an MK1 fitted with Wanhao's upgrade kit, <a href="{p('mk1u2')}">MK1 + MK2 kit</a>.</li>
<li><strong>Angled reinforcement ribs</strong> on both sides of the frame, a <strong>round black cable</strong>
to the head and a BLTouch: an MK2 or an MK3. Look under the bed at the <strong>Y motor</strong>, the one that
moves the bed: at the back, it is an <a href="{p('mk2')}">MK2</a>; at the front, on the touchscreen side, an
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>The number after D9 is the size: D9/300, D9/400 or D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 with its side reinforcement ribs">
<figcaption>D9 MK2: side ribs, round cable</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Inductive probe, ribbon cable. Firmware, Wanhao V0.15 to V0.164(B), manual.</p><a class="more" href="{p('mk1')}">MK1 firmware →</a></div>
<div class="card"><h3>D9 MK1 + MK2 kit</h3><p>MK1 upgraded with the BLTouch kit. Firmware and Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Kit firmware →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, side ribs. Firmware, Wanhao V1.1.2, guides.</p><a class="more" href="{p('mk2')}">MK2 firmware →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y motor at the front, filament sensor. Firmware and Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3 firmware →</a></div>
</div>

<h2>What these firmwares bring</h2>
<ul>
<li><strong>Marlin 2.1</strong> built from the Duplicator 9 configurations published in
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
with the changes proposed there: MK1 probe read the right way round, MK3 Y direction, power-loss recovery,
endstop noise filter.</li>
<li><strong>Wanhao's factory settings</strong>, taken from Wanhao's own firmware and source for each model: steps/mm,
speeds, accelerations, hotend PID, probe offsets and probing margins, homing, thermal limits, jerk and axis directions.</li>
<li><strong>Power-loss recovery</strong>: during an SD print the job is saved on each layer change, and after an outage the screen offers to resume from there.</li>
<li><strong>Filament sensors</strong>: a runout switch on D8, on by default on every model (no effect without one), and the BTT Smart Filament Sensor V2.0, which also catches jams. See <a href="{p('sensor')}">Filament sensor</a>.</li>
<li><strong>The head returns to the centre after a bed levelling</strong>, so the bed no longer hides the screen.</li>
<li><strong>A new touchscreen interface in 16 languages</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, with a page to set the filament sensor.</li>
</ul>

<h2>Flashing in three steps</h2>
<ol>
<li>Download the <strong>.hex</strong> for your model and size from its page.</li>
<li>Flash it over USB with AVRDUDESS or avrdude: <a href="{p('flash')}">flash guide</a>.</li>
<li>Flash the touchscreen from a microSD card: <a href="{p('screen')}">screen guide</a>.</li>
</ol>
<p>Wanhao's original firmwares stay available on each model page, so a machine can always go back to how it left the factory.</p>
""")

    if page == "mk1":
        return ("Wanhao Duplicator 9 MK1 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1 firmware for the Wanhao D9 MK1 with inductive probe, Wanhao's original V0.15 to V0.164(B) firmwares, "
                "screen files and the MK1 user manual.",
                f"""
<h1>Wanhao Duplicator 9 MK1 firmware</h1>
<div class="split"><div>
<p class="lead">The first Duplicator 9: a metal inductive probe next to the nozzle, a grey ribbon cable to the
print head, and a frame without side ribs.</p>
<p>These builds read the inductive probe the right way round (it triggers LOW) and take the settings of Wanhao's
last MK1 firmware, V0.164(B), probe offsets included (X 15, Y 0). The Y motor sits at the back, as Wanhao built it.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Inductive probe and ribbon cable on a Wanhao D9 MK1 print head">
<figcaption>MK1: inductive probe, ribbon cable</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Take the file for your size, then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Wanhao's documents</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 user manual</a> (June 2018): assembly, wiring, menus, levelling, troubleshooting.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 getting started guide</a>.</li>
</ul>

<h2>Wanhao's original firmwares</h2>
<p>To put a machine back as it left the factory. Each motherboard firmware only works with the screen firmware
of the same version.</p>
<div class="table"><table><thead><tr><th>Version</th><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>The settings of each version (steps/mm, speeds, PID, axis directions) are listed in
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, read out of Wanhao's binaries.</p>
""")

    if page == "mk1u2":
        return ("Wanhao Duplicator 9 MK1 with MK2 upgrade kit (BLTouch) firmware – Marlin 2.1",
                "Marlin 2.1 firmware for a Wanhao D9 MK1 upgraded with Wanhao's MK2 BLTouch kit, and Wanhao's original V1.1.31 kit firmware.",
                f"""
<h1>Wanhao D9 MK1 with the MK2 upgrade kit</h1>
<div class="split"><div>
<p class="lead">A first-generation D9 fitted with Wanhao's MK2 upgrade kit: the MK1 frame, with a BLTouch probe
instead of the metal inductive one.</p>
<p>Wanhao shipped a separate firmware for this combination, because the kit's BLTouch does not sit where the
factory MK2's does: the probe's Y offset differs. These builds use the kit's geometry. The Y motor sits at the
back.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="BLTouch probe on a Wanhao D9 print head">
<figcaption>BLTouch probe</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Take the file for your size, then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">These builds use the kit firmware's probe offset, Y −10. It is the only line where Wanhao's kit
source differs from the factory MK2's (Y 0): the kit's BLTouch sits further back. If your bed mesh looks shifted front
to back, measure your own offset with the <a href="{REPO}/blob/main/Offset.md">offset guide</a>.</div>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.31 kit firmware (December 2018), used with the MK2 screen firmware.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Wanhao Duplicator 9 MK2 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1 firmware for the Wanhao D9 MK2 with BLTouch, Wanhao's original V1.1.2 firmware and screen files, and Wanhao's MK2 guides.",
                f"""
<h1>Wanhao Duplicator 9 MK2 firmware</h1>
<div class="split"><div>
<p class="lead">The second Duplicator 9: angled reinforcement ribs on both sides, a round black data cable to the
print head, a BLTouch probe and a spool holder on top.</p>
<p>Wanhao also changed the carriages to four rollers, fitted a double-rail Y axis and a thicker belt on the 400
and 500, and a double-sided bed on the 300 and 400. The Y motor sits at the back; these builds turn the Y axis the
way Wanhao's V1.1.2 firmware does.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Take the file for your size. An MK2 whose head was also upgraded to the MK3 should
use the <a href="{p('mk3')}">MK3 firmware</a>. Then flash the screen with <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Wanhao's documents</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 getting started guide</a>.</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">The 12 improvements from MK1 to MK2</a>, by Wanhao.</li>
</ul>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.2 (October 2018; the 500 was rebuilt as V1.1.2.1 in July 2019), with Wanhao's MK2 screen firmware.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Wanhao Duplicator 9 MK3 firmware (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Marlin 2.1 firmware for the Wanhao D9 MK3 (Y motor at the front, filament sensor) and Wanhao's original V1.1.3 firmware.",
                f"""
<h1>Wanhao Duplicator 9 MK3 firmware</h1>
<p class="lead">The last Duplicator 9 keeps the MK2's frame and BLTouch, adds a filament runout sensor and moves
the Y motor to the front, on the touchscreen side.</p>
<p>Moving the motor reverses the Y axis: Wanhao's own V1.1.3 firmware inverts Y, and so do these builds. The
filament runout sensor is on by default. Wanhao published no probe offsets for the MK3, so these builds use the
MK2's.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Take the file for your size, then flash the screen with
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">If the filament sensor stops prints at random, turn it off with <code>M412 S0</code> then
<code>M500</code>. Wanhao Europe had published a "ReverseMode" MK3 firmware for that problem; it has since been
deleted and could not be found.</div>

<h2>Wanhao's original firmwares</h2>
<p>Wanhao's V1.1.3 (August 2019). Wanhao published no MK3 screen firmware: its MK3 downloads relied on the MK2 one.</p>
<div class="table"><table><thead><tr><th>Size</th><th>Motherboard</th><th>Screen</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Settings read out of Wanhao's binaries: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("How to flash a Wanhao Duplicator 9 (D9) motherboard firmware",
                "Step-by-step guide to flash Marlin on a Wanhao D9 over USB with AVRDUDESS or avrdude, fix homing "
                "problems, and recover with Wanhao's firmware.",
                f"""
<h1>Flashing the Duplicator 9 motherboard</h1>
<p class="lead">The D9's motherboard is an ATmega2560 with a USB bootloader: no programmer, no opening the base,
just a USB cable.</p>

<h2>What you need</h2>
<ul>
<li>A USB cable between the printer and the computer, and the printer <strong>switched on</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, graphical, easiest) or
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (command line, every system).</li>
<li>The <strong>.hex</strong> for your model and size: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Before flashing</h2>
<div class="note">Send <code>M503</code> and keep the answer. Since v2.0.3 an update keeps the settings stored in the
printer, but updating <strong>to</strong> v2.0.3 starts once from this firmware's defaults (the way settings are stored
changed), and so does coming from Wanhao's firmware. Set your probe Z offset again afterwards with <code>M851 Z…</code>
and <code>M500</code>.</div>
<p>Close every program that may hold the printer's port: Cura, PrusaSlicer, OctoPrint, Pronterface, serial terminals.</p>

<h2>Flash with AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: your printer's COM port (for instance <code>COM3</code>). Leave the baud rate at its default.</li>
<li>Flash: choose the .hex file, then click <strong>Program!</strong>. It takes 30 to 60 seconds.</li>
</ol>

<h2>Flash with avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Replace the port and the file name with yours. The <code>wiring</code> protocol picks the bootloader's speed by itself.</p>

<h2>First boot</h2>
<ol>
<li>Unplug the USB cable, switch the printer off and on, plug the cable back.</li>
<li>Connect at <strong>250000 baud</strong> (Wanhao's firmwares used 115200) and send <code>M115</code>: the answer shows the new firmware.</li>
<li>Home all axes, then run a bed levelling from the screen or with <code>G29</code>, and save with <code>M500</code>.</li>
</ol>

<h2 id="reset">Back to this firmware's default settings</h2>
<p>Since v2.0.3, a firmware update <strong>keeps</strong> the settings stored in the printer (probe Z offset, steps/mm,
PID, mesh…). New default values in a release therefore do not replace the ones already stored. Reset once when you
update from v2.0.2 or earlier while keeping values saved by hand, when the printer behaves oddly after trying other
firmwares, or whenever you want to start clean:</p>
<ul>
<li><strong>On the screen:</strong> <em>Settings</em> → <em>More</em> → <em>Reset settings</em> → ✓.</li>
<li><strong>Over USB:</strong> send <code>M502</code> (load this firmware's defaults) then <code>M500</code> (save them).</li>
</ul>
<p>Then set your probe Z offset again (<code>M851 Z…</code> then <code>M500</code>) and run a bed levelling. Check the
result with <code>M503</code>.</p>

<h2>Power loss and filament sensor</h2>
<ul>
<li>Power-loss recovery is on: the job is saved on each layer change. Turn it off with <code>M413 S0</code> then <code>M500</code>.</li>
<li>A print that stops at once with <em>power outage</em> as soon as it heats: update to v2.0.4 or later. Earlier builds watched the board's power-fail input, which reads low as soon as the heaters start.</li>
<li>Filament runout detection is on by default on every model since v2.0.8, and does nothing without a sensor. After an update from an earlier release, turn it on with <code>M412 S1</code> then <code>M500</code>, or on the screen under <em>Settings</em> → <em>Filament</em> → <em>Filament sensor</em>. Wiring and the BTT Smart Filament Sensor: <a href="{p('sensor')}">Filament sensor</a>.</li>
</ul>

<h2>Troubleshooting</h2>
<div class="table"><table><thead><tr><th>Problem</th><th>Solution</th></tr></thead><tbody>
<tr><td>Port in use</td><td>Close every program using the printer's port.</td></tr>
<tr><td>Device not found</td><td>Install the CH340 USB driver, try another cable or USB port, check the printer is switched on.</td></tr>
<tr><td>Unreadable characters after flashing</td><td>Use 250000 baud with these firmwares, 115200 with Wanhao's.</td></tr>
<tr><td>Temperatures shown ×10 on the screen (236 for 23.6 °C)</td><td>The screen still has old files: flash <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>The screen goes back to English at each start, or its <em>Filament sensor</em> page does nothing</td><td>The motherboard firmware is older than v2.0.9: update it.</td></tr>
<tr><td>Homing stops a few millimetres before the switch, then <em>Homing Failed</em></td><td>Electrical noise on the endstop line. These firmwares filter it since v2.0.1: update.</td></tr>
<tr><td>The nozzle hits a bed clip during levelling</td><td>Update to v2.0.2 or later: the first probing column is 10 mm in from the edge, as on Wanhao's firmware.</td></tr>
<tr><td>The bed moves away from the Y switch</td><td>Check you took your model's firmware: the Y motor is at the back on the MK1, MK1 + kit and MK2, at the front on the MK3.</td></tr>
</tbody></table></div>

<h2>Going back to Wanhao's firmware</h2>
<p>Each model page links Wanhao's original motherboard and screen firmwares. Flash them the same way; Wanhao's
motherboard firmware needs Wanhao's screen firmware of the same generation.</p>
<p>Questions: <a href="{DISCORD}">Discord</a> or <a href="{REPO}/issues">GitHub issues</a>.</p>
""")

    if page == "screen":
        return ("Wanhao Duplicator 9 touchscreen firmware (DWIN DGUS) – DGUS Reloaded 2.0 in 16 languages",
                "How to flash the Wanhao D9 DWIN touchscreen with DGUS Reloaded 2.0 from a microSD card: new interface in 16 "
                "languages, filament sensor page, for Marlin 2.1. And how to go back to Wanhao's screen firmware.",
                f"""
<h1>Flashing the Duplicator 9 touchscreen</h1>
<p class="lead">Every D9, MK1 to MK3, has the same DWIN T5 touchscreen (480 × 272). With these firmwares it runs
DGUS Reloaded 2.0, our new interface in 16 languages, flashed from a microSD card.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Download DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>What DGUS Reloaded 2.0 brings</h2>
<ul>
<li><strong>16 languages</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Tap the flag next to the printer name on the home screen
to switch; the printer remembers the choice.</li>
<li><strong>A filament sensor page</strong>: <em>Settings</em> → <em>Filament</em> → <em>Filament sensor</em>. See
<a href="{p('sensor')}#screen">Filament sensor</a>.</li>
<li><strong>A status line that stays</strong>: the last message, <em>Ready</em> for example, remains on screen instead
of disappearing after 30 seconds.</li>
<li><strong>Temperature gauges</strong> for the nozzle and the bed, with the target marked.</li>
<li>A new look for every page: dark theme, larger buttons, pictograms on the popups.</li>
</ul>
</div><figure><img src="{img}screen/en-home.png" width="480" height="272" alt="DGUS Reloaded 2.0 home screen on a Wanhao D9: nozzle and bed temperatures with gauges, status line, Print, Temperature and Settings buttons">
<figcaption>The home screen</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 needs <strong>v2.0.9 or later</strong> on the motherboard. With v2.0.8 or earlier, the
language goes back to English at each start and the filament sensor page does not work: <a href="{p('flash')}">flash the
motherboard</a> first.</div>

<h2>1. Format the microSD card</h2>
<div class="note">FAT32 with an allocation unit of <strong>4096 bytes</strong>. With any other size the screen ignores the card.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 often won't format FAT32; use <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
and set the allocation unit size to 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (check the device with <code>lsblk</code> first).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (check with <code>diskutil list</code>).</li>
</ul>

<h2>2. Copy the files</h2>
<p>Unzip <code>DWIN_SET.zip</code> and copy the whole <code>DWIN_SET</code> folder to the root of the card.</p>

<h2>3. Flash</h2>
<ol>
<li>Switch the printer off and unplug it.</li>
<li>Open the front of the base to reach the back of the screen, where its microSD slot is.</li>
<li>Insert the card and switch on. The screen shows the update within 10 to 30 seconds; wait until it restarts
normally, 1 to 3 minutes in all.</li>
<li>Switch off, remove the card, close the base.</li>
</ol>
<p>Wanhao's <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">video of a D9 screen update</a> shows where the slot is.</p>

<h2>Where it comes from</h2>
<p>DGUS Reloaded 2.0 redraws <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(by Desuuuu, then Neo2003) page by page. Its source, the program that generates the screen files and the translations are
on <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. A wrong or awkward word in your language? Tell us on
<a href="{DISCORD}">Discord</a> or open an issue there.</p>
<p>To go back to DGUS Reloaded 1.0.3, for example with a firmware older than v2.0.9, flash
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> the same way.</p>

<h2>Going back to Wanhao's screen</h2>
<p>Wanhao's screen firmware only works with Wanhao's motherboard firmware. MK1: the screen file of the matching
version on the <a href="{p('mk1')}">MK1 page</a>. MK1 + kit, MK2 and MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Same procedure.</p>
""")

    if page == "sensor":
        return ("Filament sensors on the Wanhao Duplicator 9: runout switch and BTT Smart Filament Sensor wiring",
                "Where to plug a filament sensor on the Wanhao D9 main board (D8, D9, GND, 5V), how to wire a BTT Smart "
                "Filament Sensor V2.0 and turn runout and jam detection on with M412.",
                f"""
<h1>Filament sensors</h1>
<p class="lead">From v2.0.5 these firmwares read two kinds of sensor: Wanhao's runout switch, and the
BTT Smart Filament Sensor V2.0, which also notices when the filament stops moving (tangled spool, jam, stripped
filament). <strong>Runout detection is on by default on every model</strong>, and jam detection is off.</p>

<h2>The sensor plug</h2>
<figure><img src="{img}d9-sensor-plug-en.svg" width="760" height="440" alt="Wanhao D9 main board: the 4-pin sensor plug left of POWER-DET, pins D9, D8, GND and 5V, wired to a BTT Smart Filament Sensor V2.0"></figure>
<p>The 4-pin plug to the left of <strong>POWER-DET</strong>, below the endstop plugs, carries <strong>D9, D8, GND and 5V</strong>,
in that order. The pin names come from a wiring diagram by Wanhao that dustovich found and shared on the
<a href="{DISCORD}">Discord</a>; the back of the board prints the same four pins as CTRL, BTN, GND and VCC.</p>
<ul>
<li><strong>D8</strong> is the runout input Wanhao's own firmware reads.</li>
<li><strong>D9</strong> is not used by Wanhao's firmware: these builds read the BTT sensor's motion signal on it.</li>
</ul>
<div class="note">Printer <strong>switched off</strong> while you plug or unplug anything on the board.</div>

<h2 id="screen">On the screen</h2>
<div class="split"><div>
<p>With DGUS Reloaded 2.0 on the screen (firmware v2.0.9 or later): <em>Settings</em> → <em>Filament</em> →
<em>Filament sensor</em>.</p>
<ul>
<li><strong>Runout detection</strong> turns all detection on or off, like <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Jam detection</strong> turns jam detection on with the length below, or off (<code>L0</code>).</li>
<li><strong>Jam length</strong>: − and + change it by 1 mm; tap the number to type it.</li>
<li>The <strong>Filament</strong> dot is green while the runout switch sees filament, red when it does not.</li>
<li>Changes apply at once. <strong>Save</strong> stores them, like <code>M500</code>. The back arrow leaves without
saving: the stored settings come back at the next start.</li>
</ul>
</div><figure><img src="{img}screen/en-sensor.png" width="480" height="272" alt="Filament sensor page of DGUS Reloaded 2.0: runout and jam detection switches, jam length with minus and plus buttons, filament indicator and Save button">
<figcaption>Settings → Filament → Filament sensor</figcaption></figure></div>

<h2>The M412 commands</h2>
<p>Everything is set over USB from a serial terminal (Pronterface, the terminal of your slicer or of OctoPrint,
250000 baud). Parameters can be combined in one command, for example <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Command</th><th>What it does</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Shows the state, for example <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Turns detection on</strong>: the runout switch, and jam detection too if the jam length is not 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Turns all detection off</strong>, switch and jam.</td></tr>
<tr><td><code>M412 D5</code></td><td>Once the switch sees no filament, keeps printing <strong>5 mm</strong> before pausing, to use the filament left between the sensor and the nozzle. Default 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Turns jam detection on</strong> (BTT sensor only): pauses when <strong>10 mm</strong> of filament go through the extruder without the sensor's wheel moving.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Turns jam detection off</strong> and leaves the runout switch as it is. This is the default.</td></tr>
<tr><td><code>M500</code></td><td>Saves the settings. Without it, a change is lost when the printer is switched off.</td></tr>
<tr><td><code>M119</code></td><td>The <em>filament</em> line reads <code>TRIGGERED</code> with filament loaded, <code>open</code> without.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, and <code>L</code> used on its own, come from our change to Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), built into these firmwares. In Marlin without it, <code>L</code>
alone is ignored and <code>L0</code> pauses the print as a jam at once.</p>

<h2>Wanhao's runout switch</h2>
<p>It tells the firmware whether filament is there. When it goes missing, the print pauses after 5 more mm of
filament and the screen starts a filament change.</p>
<p><strong>It is on by default on every model, since v2.0.8.</strong> With nothing plugged into D8, the board's
pull-up holds the pin at 5 V, which reads as "filament present": detection then never triggers, so it can stay on
whether or not a sensor is fitted. Plug a runout switch into D8 and it works straight away.</p>
<ul>
<li>Jam detection stays off (<code>L0</code>): this switch cannot see filament move.</li>
<li>To turn the switch off: <code>M412 S0</code> then <code>M500</code>.</li>
<li>Settings saved by an earlier release keep their on/off state. To turn it on: <code>M412 S1</code> then
<code>M500</code>, or reset to the defaults (<code>M502</code> then <code>M500</code>, which also clears your probe Z
offset and mesh).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>This sensor has two outputs, and the firmware reads them differently:</p>
<ul>
<li><strong>The runout switch</strong> (to D8) is a level: 5 V while filament is there, 0 V once it has gone.</li>
<li><strong>The motion output</strong> (to D9) comes from a small wheel the filament turns as it passes. Each few
millimetres of filament, the output flips between 0 V and 5 V. The firmware only watches for those changes: if the
extruder pushes the jam length of filament without a single one, the filament is not following (tangled spool, jam,
stripped filament), and the print pauses. The runout switch cannot see that: during a jam the filament is still there.</li>
</ul>
<h3>Wiring</h3>
<p><strong>5V</strong> to 5V, <strong>GND</strong> to GND, the <strong>runout switch</strong> signal to <strong>D8</strong>
and the <strong>motion</strong> signal to <strong>D9</strong>. The names printed on the sensor's cable may differ.</p>
<h3>Turning it on</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>If prints pause without a reason, raise the jam length: <code>M412 L15</code> then <code>M500</code>. To keep only
the runout switch: <code>M412 L0</code> then <code>M500</code>.</p>
<h3>Checking it</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> with filament loaded: <em>filament: TRIGGERED</em>. If that line changes while you push filament
through by hand instead of when you insert or remove it, the two signal wires are swapped: swap D8 and D9.</li>
</ul>
<div class="note">Jam detection was tested on an MK2 300 without the sensor (a 2 mm jam length triggers, <code>L0</code> never
does), but not yet with the BTT sensor itself. If the switch reads the wrong way round (<em>open</em> with filament
loaded), tell us on <a href="{DISCORD}">Discord</a>.</div>

<h2>Updating from v2.0.5 or v2.0.6</h2>
<p>Those releases had no way to turn jam detection off, so they used a jam length too long to ever be reached: 100 m in
v2.0.5 (too short in fact: about a third of a 1 kg spool, after which a printer left on could pause for nothing) and
10 km in v2.0.6. When the printer starts, v2.0.7 loads those two values as <code>L0</code>. A real length you set
for a BTT sensor, such as <code>L10</code>, is kept. From v2.0.4 or earlier, the 5 mm runout distance is loaded
instead of the 0 those versions saved.</p>
""")

    if page == "slicer":
        return ("Cura, OrcaSlicer and Simplify3D profiles for the Wanhao Duplicator 9, and how to set the Z offset",
                "Ready-made UltiMaker Cura, OrcaSlicer and Simplify3D profiles for every Wanhao D9, PLA, PETG and ABS, how to set "
                "the probe Z offset, run a bed probing and print a test 3DBenchy.",
                f"""
<h1>Slicing for the Duplicator 9</h1>
<p class="lead">A profile for each of the twelve printers, for <strong>UltiMaker Cura</strong> and
<strong>OrcaSlicer</strong>, both free and available on Windows, macOS and Linux, and for
<strong>Simplify3D</strong> if you already own it. Each one carries the build volume, the accelerations and the
highest bed temperature of its own firmware.</p>

<h2>Download</h2>
{h.slicer}
<p>They are made for the firmware of this site, <a href="{p('flash')}">v2.0.9 or later</a>.</p>

<h2>Install them</h2>
<p><strong>OrcaSlicer</strong>: <em>File</em> → <em>Import</em> → <em>Import Configs…</em>, then choose the
<code>.orca_printer</code> file. The printer, its three qualities (0.12, 0.20 and 0.28 mm) and the PLA, PETG and ABS
filaments appear in your presets.</p>
<p><strong>Cura</strong>: <em>Help</em> → <em>Show Configuration Folder</em>, close Cura, unzip the file into that
folder, start Cura again, then <em>Settings</em> → <em>Printer</em> → <em>Add Printer…</em> → <em>Add a non-networked
printer</em> → <em>Wanhao</em> → your model. The <em>Wanhao Duplicator 9</em> that comes with Cura is an older profile:
300 only, raft and supports on by default.</p>
<p><strong>Simplify3D</strong> (version 5, paid): <em>File</em> → <em>Import Printer Profiles…</em>, then
choose the <code>.fff</code> file. The printer arrives with its three qualities (0.30, 0.20 and 0.10 mm) and the PLA,
PETG and ABS materials, in the <em>Auto-Configure</em> lists above the settings.</p>

<h2 id="first-print">Before the first print: the Z offset, then a probing</h2>
<p>The probe triggers a little above the bed, and the firmware has to know by how much. That is the
<strong>Z offset</strong>. Too high and the first layer does not stick; too low and the nozzle scrapes the bed. It is
set once, and it is the one setting that decides whether prints stick.</p>
<div class="note">Everything below is kept in the printer's memory, not in the slicer. It stays after a firmware
update (since v2.0.3).</div>

<h3>1. Heat first</h3>
<p>A hot nozzle is a few hundredths of a millimetre longer. Heat as for a print — on the screen, <em>Temperature</em> →
<em>Preheat</em> → <em>PLA</em> (200 °C and 60 °C), and wait a couple of minutes.</p>

<h3>2. Home the axes</h3>
<p>On the screen: <em>Settings</em> → <em>Move</em> → <em>Home</em>. Over USB: <code>G28</code>.</p>

<h3>3. Set the Z offset</h3>
<p><strong>The simple way, while printing.</strong> Start a print, and during the <strong>first layer</strong> go to
<em>Adjust</em> → <em>Z offset</em> on the screen. Lower in 0.01 mm steps while the line is being drawn, until it is
flat and touches its neighbour with no gap. Too high leaves round, separate strings; too low leaves a rough, squashed
surface and shows the nozzle digging in. The value is saved on its own.</p>
<p><strong>The paper way, without printing.</strong> Over USB, at printing temperature:</p>
<pre><code>M851 Z0     ; forget the current offset
M500
G28         ; home again so it is taken into account
M420 S0     ; ignore the mesh while measuring
M211 S0     ; allow going below Z0: the soft limits stop the nozzle there
G1 Z0 F300  ; the nozzle comes down to what the firmware thinks is zero</code></pre>
<p>Slide a sheet of paper under the nozzle, then lower in small steps with <code>G91</code> then
<code>G1 Z-0.05 F60</code>, over and over, until the paper only just drags. Read the value with <code>M114</code>: it
is negative, for example −1.30. Then:</p>
<pre><code>G90
M851 Z-1.30 ; your value
M500
M211 S1     ; put the soft limits back, they protect the bed</code></pre>
<p>With v2.1.1 or later you can leave out the two <code>M211</code> lines: the firmware already lets the nozzle go 3 mm below zero.</p>

<h3>4. Probe the bed</h3>
<p>On the screen: <em>Settings</em> → <em>Levelling</em> → <em>Automatic</em> → <em>Probe</em>. The printer measures
25 points and <strong>saves the mesh by itself</strong> (it runs <code>G29</code> then <code>M500</code>). It takes a
few minutes. Over USB: <code>G29</code> then <code>M500</code>.</p>
<p>Our profiles do not probe before each print: they turn the saved mesh back on with <code>M420 S1</code>, right after
the homing. So probe again when you move the printer, change the surface or the nozzle, or when the first layer is good
on one side of the bed and not on the other.</p>

<h3>5. Check</h3>
<p><code>M503</code> lists what is stored: the <code>M851</code> line is your Z offset, and <code>M420 S1</code> shows
the mesh is on. On the screen, the <em>Automatic</em> page shows the 25 measured points.</p>

<h2>Test prints</h2>
<p>A 3DBenchy, already sliced for a <strong>D9 MK2 300</strong>, to compare the two slicers or to check a setting
without installing anything:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>About an hour and a half and 4 m of filament each. For another model or size, slice the
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> yourself with your profile.</p>
<h3>The all-in-one test</h3>
<p>Overhang bars, a bridge, stringing towers, tolerance holes and a fineness scale in one 65 mm piece, about 2 h 30.
It is the <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> by <strong>majda107</strong>
(CC BY 4.0), sliced for <strong>every printer</strong> and both slicers, in the three materials. The files of the
<a href="{REPO}/releases/latest">latest release</a> are named
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, for example
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy printed with the OrcaSlicer profile on a Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy printed with the Cura profile on a Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="3DBenchy printed in PETG on a Wanhao D9, by dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Which one to start with:</strong> on a D9 MK2 300 in PLA, the same Benchy took <strong>1 h 14 with
OrcaSlicer</strong> and <strong>1 h 22 with Cura</strong>, and OrcaSlicer's walls came out slightly cleaner. Both are
good; OrcaSlicer is the one we would start with, and its calibration tools (flow, pressure advance, temperature
towers) help once you want more.</p>
<div class="note">The D9 is open: ABS needs at least a room without draughts, and its bed temperature is brought down to
what your model accepts (80 °C on an MK3 500).</div>

<h2>What is in the profiles</h2>
<ul>
<li><strong>Layers</strong> 0.20 mm, <strong>3 walls</strong>, 4 top and 3 bottom layers, gyroid infill at 15 %, a
2-line skirt, no support.</li>
<li><strong>Speeds</strong>: 40 mm/s on the outer wall, 60 inside, 70 for infill, 20 on the first layer, 150 for
travel. Wanhao gives 70 mm/s as the D9's top printing speed.</li>
<li><strong>Retraction</strong> 1.5 mm at 25 mm/s: every D9 has a direct-drive MK10 extruder, and the firmware limits
the extruder to 25 mm/s.</li>
<li><strong>Temperatures</strong>: PLA 210 °C then 205, bed 65 then 60. PETG 240 / 80 then 235 / 75. ABS 245 / 105
then 245 / 100.</li>
<li><strong>A priming line</strong> 15 mm from the left edge, clear of the bed clips, so the nozzle arrives clean on
the model.</li>
<li>At the end, the nozzle rises and the bed comes to the front.</li>
</ul>
<p>Every setting and how to change them: <a href="{REPO}/tree/main/Slicer">Slicer folder</a> on GitHub.</p>
""")

    if page == "quiet":
        return ("Make a Wanhao Duplicator 9 quieter: which fans, and the board fan on NTC thermistors",
                "Which of the Wanhao D9's fans can be quietened: the hotend fan must stay, the power supply fan already "
                "regulates itself, and the board fan can be unplugged or run on NTC thermistors.",
                f"""
<h1>Making the Duplicator 9 quieter</h1>
<p class="lead">At rest, the D9's noise comes from its fans. Here is which one can be quietened, and how.</p>
<div class="note">Work with the printer <strong>unplugged</strong>. Keep every wire away from the 230 V side.</div>

<h2>The fans</h2>
<div class="table"><table class="stack"><thead><tr><th>Fan</th><th>Controlled by</th><th>Can it be quietened?</th></tr></thead><tbody>
<tr><td><strong>Hotend heatsink fan</strong> (print head)</td><td>nothing: 24 V always on</td><td><strong>no</strong>: usually the loudest, but slowing it lets heat climb up the hotend and jams the filament (heat creep)</td></tr>
<tr><td><strong>Part cooling fan</strong> (print head)</td><td>firmware, pin D5 (PWM)</td><td>already variable: set by the slicer and <code>M106</code></td></tr>
<tr><td><strong>Power supply fan</strong></td><td>the power supply itself</td><td>nothing to do: on the unit checked here (Chuanglian A-350FAK-24) it already follows the supply's temperature</td></tr>
<tr><td><strong>Board fan</strong> (control box)</td><td>nothing: 24 V always on</td><td><strong>yes</strong>, see below</td></tr>
</tbody></table></div>
<p>Wanhao's firmware drives no board fan and no hotend fan (<code>CONTROLLER_FAN_PIN</code> and
<code>E0_AUTO_FAN_PIN</code> are both <code>-1</code>), and the board has no spare switched output. That is why these
two run from the always-on "24V OUT" connectors, and why no firmware can slow them down.</p>

<h2>Board fan</h2>
<p>On the unit measured here: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0.10 A max, sleeve bearing</strong>.</p>
<p><strong>Many owners simply unplug it.</strong> The board runs cool: it sits at the bottom of the control box, below
the heated bed, and the bed's heat rises away from it. If you do, keep an eye on your first long prints: an overheating
stepper driver cuts out briefly, which shows up as <strong>shifted layers</strong>, not as an error message.</p>
<h3>Keeping it, but only when the drivers are warm</h3>
<p>Two power NTC thermistors in series make the fan start around 45–50 °C and speed up as the drivers heat:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), glued to a driver heatsink with thermal
adhesive, leads insulated.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V</code></pre>
<ul>
<li>This is a calculation, <strong>not tested on a printer yet</strong>: MF72 tolerance is ±20 %, and a small fan may
start lower than expected. Check the start temperature on the bench (NTCs in a small bag in hot water, with a kitchen
thermometer); add a second 200 Ω if it starts too early, drop the 200 Ω if too late.</li>
<li>The NTCs must be glued to a heatsink: in free air, the fan current (up to about 0.6 W in the NTCs) heats them by
tens of degrees.</li>
<li>The fan never reaches full speed this way (about 75 % at 80 °C), and an NTC that fails goes open: the fan then stops
for good.</li>
</ul>
<p>Sources: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 datasheet</a>.</p>
""")
    raise KeyError(page)
