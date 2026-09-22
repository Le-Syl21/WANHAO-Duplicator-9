"""Bahasa Indonesia: translation of en.py."""

META = {"name": "Bahasa Indonesia", "locale": "id_ID", "dir": "ltr"}

UI = {
    "nav": {"index": "Beranda", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Panduan flash", "screen": "Layar", "sensor": "Sensor filamen", "slicer": "Slicer",
            "quiet": "Lebih senyap"},
    "language": "Bahasa",
    "model": "Model",
    "size": "Ukuran", "volume": "Volume cetak", "file": "Firmware",
    "footer_src": "Kode sumber dan issue di GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware berlisensi GNU GPL v3. Manual dan firmware Wanhao tetap milik Wanhao.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Mainboard Wanhao D9 (tampak atas)",
    "plug": "soket sensor",
    "switch": "sakelar filamen habis",
    "motion": "gerakan",
    "level": "level: filamen ada / tidak ada",
    "pulses": "pulsa saat filamen bergerak",
    "names": "nama di sensor Anda bisa berbeda",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Firmware Marlin terbaru untuk semua Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "file layar, firmware asli dan manual Wanhao, serta cara mem-flash-nya.",
                f"""
<h1>Firmware Wanhao Duplicator 9</h1>
<p class="lead">Situs unduhan Wanhao untuk Duplicator 9 sudah tidak ada. Semua yang dibutuhkan pemilik D9 kini ada di sini:
firmware Marlin 2.1 terbaru untuk setiap model dan ukuran, file layar sentuh yang sesuai, firmware asli Wanhao,
manual Wanhao, dan panduan flash langkah demi langkah.</p>
<p><a class="btn" href="{REPO}/releases/latest">Semua unduhan</a> <a class="btn ghost" href="{DISCORD}">Tanya di Discord</a></p>

<h2>D9 saya yang mana?</h2>
<div class="split"><div>
<ol>
<li><strong>Kabel pita pipih abu-abu</strong> menuju print head, <strong>probe silinder logam</strong>
di samping nozzle, tanpa penguat di sisi rangka: <a href="{p('mk1')}">MK1</a>.</li>
<li>Mesin generasi pertama yang sama, tetapi dengan <strong>probe BLTouch putih</strong> sebagai ganti probe logam:
MK1 yang dipasangi kit upgrade Wanhao, <a href="{p('mk1u2')}">MK1 + kit MK2</a>.</li>
<li><strong>Rusuk penguat miring</strong> di kedua sisi rangka, <strong>kabel bulat hitam</strong> ke head,
dan BLTouch: MK2 atau MK3. Lihat ke bawah bed, pada <strong>motor Y</strong>, yaitu motor yang menggerakkan bed:
kalau ada di belakang, itu <a href="{p('mk2')}">MK2</a>; kalau di depan, di sisi layar sentuh, itu
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Angka setelah D9 menunjukkan ukurannya: D9/300, D9/400, atau D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 dengan rusuk penguat di sisinya">
<figcaption>D9 MK2: rusuk samping, kabel bulat</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Probe induktif, kabel pita. Firmware, Wanhao V0.15 sampai V0.164(B), manual.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + kit MK2</h3><p>MK1 yang di-upgrade dengan kit BLTouch. Firmware dan Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware kit →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, rusuk samping. Firmware, Wanhao V1.1.2, panduan.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Motor Y di depan, sensor filamen. Firmware dan Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>Apa yang dibawa firmware ini</h2>
<ul>
<li><strong>Marlin 2.1</strong> yang dikompilasi dari konfigurasi Duplicator 9 yang diterbitkan di
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
dengan perubahan yang diusulkan di sana: probe MK1 dibaca dengan arah yang benar, arah Y pada MK3, pemulihan saat listrik padam,
filter noise endstop.</li>
<li><strong>Setelan pabrik Wanhao</strong>, diambil dari firmware dan kode sumber Wanhao sendiri untuk tiap model: steps/mm,
kecepatan, akselerasi, PID hotend, offset probe dan margin probing, homing, batas termal, jerk, dan arah sumbu.</li>
<li><strong>Pemulihan saat listrik padam</strong>: saat mencetak dari kartu SD, progres disimpan setiap ganti layer, dan setelah listrik padam layar menawarkan untuk melanjutkan dari titik itu.</li>
<li><strong>Sensor filamen</strong>: sakelar filamen habis di D8, aktif secara default di semua model (tidak berpengaruh jika sakelarnya tidak ada), dan BTT Smart Filament Sensor V2.0, yang juga bisa mendeteksi filamen macet. Lihat <a href="{p('sensor')}">Sensor filamen</a>.</li>
<li><strong>Head kembali ke tengah setelah leveling bed</strong>, jadi bed tidak lagi menutupi layar.</li>
<li><strong>Antarmuka layar sentuh baru dalam 16 bahasa</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, dengan halaman untuk mengatur sensor filamen.</li>
</ul>

<h2>Flash dalam tiga langkah</h2>
<ol>
<li>Unduh file <strong>.hex</strong> untuk model dan ukuran printer Anda dari halamannya.</li>
<li>Flash lewat USB dengan AVRDUDESS atau avrdude: <a href="{p('flash')}">panduan flash</a>.</li>
<li>Flash layar sentuh dari kartu microSD: <a href="{p('screen')}">panduan layar</a>.</li>
</ol>
<p>Firmware asli Wanhao tetap tersedia di setiap halaman model, jadi mesin selalu bisa dikembalikan ke kondisi pabriknya.</p>
""")

    if page == "mk1":
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 untuk Wanhao D9 MK1 dengan probe induktif, firmware asli Wanhao V0.15 sampai V0.164(B), "
                "file layar, dan manual pengguna MK1.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">Duplicator 9 generasi pertama: probe induktif logam di samping nozzle, kabel pita abu-abu ke
print head, dan rangka tanpa rusuk samping.</p>
<p>Build ini membaca probe induktif dengan arah yang benar (terpicu saat LOW) dan memakai setelan firmware MK1
terakhir dari Wanhao, V0.164(B), termasuk offset probe (X 15, Y 0). Motor Y ada di belakang, seperti rakitan Wanhao.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Probe induktif dan kabel pita pada print head Wanhao D9 MK1">
<figcaption>MK1: probe induktif, kabel pita</figcaption></figure></div>

<h2>Unduh</h2>
{dl("MK1")}
<p>Ambil file untuk ukuran printer Anda, lalu flash layar dengan
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumen Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Manual pengguna D9 MK1</a> (Juni 2018, dalam bahasa Inggris): perakitan, pengkabelan, menu, leveling, pemecahan masalah.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Panduan memulai D9 MK1</a>.</li>
</ul>

<h2>Firmware asli Wanhao</h2>
<p>Untuk mengembalikan mesin ke kondisi pabriknya. Setiap firmware mainboard hanya bekerja dengan firmware layar
dari versi yang sama.</p>
<div class="table"><table><thead><tr><th>Versi</th><th>Ukuran</th><th>Mainboard</th><th>Layar</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Setelan tiap versi (steps/mm, kecepatan, PID, arah sumbu) tercantum di
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, dibaca langsung dari file biner Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware Wanhao Duplicator 9 MK1 dengan kit upgrade MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 untuk Wanhao D9 MK1 yang di-upgrade dengan kit BLTouch MK2 dari Wanhao, dan firmware kit asli Wanhao V1.1.31.",
                f"""
<h1>Wanhao D9 MK1 dengan kit upgrade MK2</h1>
<div class="split"><div>
<p class="lead">D9 generasi pertama yang dipasangi kit upgrade MK2 dari Wanhao: rangka MK1, dengan probe BLTouch
sebagai ganti probe induktif logam.</p>
<p>Wanhao merilis firmware tersendiri untuk kombinasi ini, karena posisi BLTouch dari kit tidak sama dengan
BLTouch pada MK2 bawaan pabrik: offset Y probe-nya berbeda. Build ini memakai geometri kit. Motor Y ada di
belakang.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Probe BLTouch pada print head Wanhao D9">
<figcaption>Probe BLTouch</figcaption></figure></div>

<h2>Unduh</h2>
{dl("MK1u2")}
<p>Ambil file untuk ukuran printer Anda, lalu flash layar dengan
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Build ini memakai offset probe dari firmware kit, Y −10. Hanya baris ini yang berbeda antara kode sumber
kit Wanhao dan kode sumber MK2 pabrik (Y 0): BLTouch dari kit terpasang lebih ke belakang. Jika mesh bed Anda tampak
bergeser dari depan ke belakang, ukur offset Anda sendiri dengan <a href="{REPO}/blob/main/Offset.md">panduan offset</a>.</div>

<h2>Firmware asli Wanhao</h2>
<p>Firmware kit V1.1.31 dari Wanhao (Desember 2018), dipakai bersama firmware layar MK2.</p>
<div class="table"><table><thead><tr><th>Ukuran</th><th>Mainboard</th><th>Layar</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Setelan yang dibaca dari file biner Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 untuk Wanhao D9 MK2 dengan BLTouch, firmware dan file layar asli Wanhao V1.1.2, serta panduan MK2 dari Wanhao.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">Duplicator 9 generasi kedua: rusuk penguat miring di kedua sisi, kabel data bulat hitam ke
print head, probe BLTouch, dan dudukan spool di atas.</p>
<p>Wanhao juga mengganti carriage menjadi empat roda, memasang sumbu Y rel ganda dan belt yang lebih tebal pada 400
dan 500, serta bed dua sisi pada 300 dan 400. Motor Y ada di belakang; build ini memutar sumbu Y dengan arah yang
sama seperti firmware V1.1.2 dari Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Unduh</h2>
{dl("MK2")}
<p>Ambil file untuk ukuran printer Anda. MK2 yang head-nya juga sudah di-upgrade ke MK3 sebaiknya
memakai <a href="{p('mk3')}">firmware MK3</a>. Lalu flash layar dengan <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumen Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Panduan memulai D9 MK2</a> (dalam bahasa Inggris).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">12 peningkatan dari MK1 ke MK2</a>, dari Wanhao.</li>
</ul>

<h2>Firmware asli Wanhao</h2>
<p>V1.1.2 dari Wanhao (Oktober 2018; versi 500 dikompilasi ulang sebagai V1.1.2.1 pada Juli 2019), dengan firmware layar MK2 dari Wanhao.</p>
<div class="table"><table><thead><tr><th>Ukuran</th><th>Mainboard</th><th>Layar</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Setelan yang dibaca dari file biner Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 untuk Wanhao D9 MK3 (motor Y di depan, sensor filamen) dan firmware asli Wanhao V1.1.3.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK3</h1>
<p class="lead">Duplicator 9 terakhir tetap memakai rangka dan BLTouch dari MK2, menambahkan sensor filamen habis, dan memindahkan
motor Y ke depan, di sisi layar sentuh.</p>
<p>Pemindahan motor membalik arah sumbu Y: firmware V1.1.3 dari Wanhao sendiri membalik Y, dan build ini juga. Sensor
filamen habis aktif secara default. Wanhao tidak pernah merilis offset probe untuk MK3, jadi build ini memakai offset
milik MK2.</p>

<h2>Unduh</h2>
{dl("MK3")}
<p>Ambil file untuk ukuran printer Anda, lalu flash layar dengan
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Jika sensor filamen menghentikan cetakan secara acak, matikan dengan <code>M412 S0</code> lalu
<code>M500</code>. Wanhao Europe pernah merilis firmware MK3 “ReverseMode” untuk masalah itu; firmware tersebut sudah
dihapus dan tidak bisa ditemukan lagi.</div>

<h2>Firmware asli Wanhao</h2>
<p>V1.1.3 dari Wanhao (Agustus 2019). Wanhao tidak pernah merilis firmware layar MK3: unduhan MK3 mereka memakai firmware layar MK2.</p>
<div class="table"><table><thead><tr><th>Ukuran</th><th>Mainboard</th><th>Layar</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Setelan yang dibaca dari file biner Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Cara flash firmware mainboard Wanhao Duplicator 9 (D9)",
                "Panduan langkah demi langkah untuk flash Marlin ke Wanhao D9 lewat USB dengan AVRDUDESS atau avrdude, mengatasi "
                "masalah homing, dan kembali ke firmware Wanhao.",
                f"""
<h1>Flash mainboard Duplicator 9</h1>
<p class="lead">Mainboard D9 memakai ATmega2560 dengan bootloader USB: tanpa programmer, tanpa membongkar base,
cukup kabel USB.</p>

<h2>Yang dibutuhkan</h2>
<ul>
<li>Kabel USB antara printer dan komputer, dan printer dalam keadaan <strong>menyala</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, grafis, paling mudah) atau
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (command line, semua sistem operasi).</li>
<li>File <strong>.hex</strong> untuk model dan ukuran printer Anda: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Sebelum flash</h2>
<div class="note">Kirim <code>M503</code> dan simpan balasannya. Sejak v2.0.3, update mempertahankan setelan yang tersimpan di
printer, tetapi update <strong>ke</strong> v2.0.3 akan dimulai sekali dari nilai default firmware ini (cara penyimpanan
setelan berubah), begitu juga jika berasal dari firmware Wanhao. Setelah itu atur ulang Z offset probe Anda dengan <code>M851 Z…</code>
dan <code>M500</code>.</div>
<p>Tutup semua program yang mungkin sedang memakai port printer: Cura, PrusaSlicer, OctoPrint, Pronterface, terminal serial.</p>

<h2>Flash dengan AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: port COM printer Anda (misalnya <code>COM3</code>). Biarkan baud rate pada nilai default.</li>
<li>Flash: pilih file .hex, lalu klik <strong>Program!</strong>. Prosesnya 30 sampai 60 detik.</li>
</ol>

<h2>Flash dengan avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Ganti port dan nama file dengan milik Anda. Protokol <code>wiring</code> memilih sendiri kecepatan bootloader.</p>

<h2>Boot pertama</h2>
<ol>
<li>Cabut kabel USB, matikan lalu nyalakan lagi printer, pasang kembali kabelnya.</li>
<li>Sambungkan pada <strong>250000 baud</strong> (firmware Wanhao memakai 115200) dan kirim <code>M115</code>: balasannya menunjukkan firmware baru.</li>
<li>Lakukan homing semua sumbu, lalu leveling bed dari layar atau dengan <code>G29</code>, dan simpan dengan <code>M500</code>.</li>
</ol>

<h2 id="reset">Kembali ke setelan default firmware ini</h2>
<p>Sejak v2.0.3, update firmware <strong>mempertahankan</strong> setelan yang tersimpan di printer (Z offset probe, steps/mm,
PID, mesh…). Karena itu nilai default baru dalam sebuah rilis tidak menggantikan nilai yang sudah tersimpan. Lakukan reset
sekali jika Anda update dari v2.0.2 atau lebih lama sambil mempertahankan nilai yang disimpan manual, jika printer
berperilaku aneh setelah mencoba firmware lain, atau kapan pun Anda ingin mulai dari awal:</p>
<ul>
<li><strong>Di layar:</strong> <em>Pengaturan</em> → <em>Lainnya</em> → <em>Atur ulang</em> → ✓.</li>
<li><strong>Lewat USB:</strong> kirim <code>M502</code> (memuat nilai default firmware ini) lalu <code>M500</code> (menyimpannya).</li>
</ul>
<p>Setelah itu atur lagi Z offset probe Anda (<code>M851 Z…</code> lalu <code>M500</code>) dan lakukan leveling bed. Periksa
hasilnya dengan <code>M503</code>.</p>

<h2>Listrik padam dan sensor filamen</h2>
<ul>
<li>Pemulihan saat listrik padam aktif: progres disimpan setiap ganti layer. Untuk mematikannya: <code>M413 S0</code> lalu <code>M500</code>.</li>
<li>Cetakan langsung berhenti dengan pesan <em>power outage</em> begitu mulai memanaskan: update ke v2.0.4 atau yang lebih baru. Build sebelumnya memantau input deteksi listrik padam pada board, yang terbaca low begitu heater mulai menyala.</li>
<li>Deteksi filamen habis aktif secara default di semua model sejak v2.0.8, dan tidak melakukan apa pun jika tidak ada sensor. Setelah update dari rilis sebelumnya, aktifkan dengan <code>M412 S1</code> lalu <code>M500</code>, atau di layar lewat <em>Pengaturan</em> → <em>Filamen</em> → <em>Sensor filamen</em>. Pengkabelan dan BTT Smart Filament Sensor: <a href="{p('sensor')}">Sensor filamen</a>.</li>
</ul>

<h2>Pemecahan masalah</h2>
<div class="table"><table><thead><tr><th>Masalah</th><th>Solusi</th></tr></thead><tbody>
<tr><td>Port sedang dipakai</td><td>Tutup semua program yang memakai port printer.</td></tr>
<tr><td>Perangkat tidak ditemukan</td><td>Pasang driver USB CH340, coba kabel atau port USB lain, pastikan printer menyala.</td></tr>
<tr><td>Karakter tidak terbaca setelah flash</td><td>Gunakan 250000 baud dengan firmware ini, 115200 dengan firmware Wanhao.</td></tr>
<tr><td>Suhu di layar tampil ×10 (236 untuk 23,6 °C)</td><td>Layar masih memakai file lama: flash <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>Layar kembali ke bahasa Inggris setiap dinyalakan, atau halaman <em>Sensor filamen</em> tidak berfungsi</td><td>Firmware mainboard lebih lama dari v2.0.9: update firmware tersebut.</td></tr>
<tr><td>Homing berhenti beberapa milimeter sebelum sakelar, lalu muncul <em>Homing Failed</em></td><td>Noise listrik pada jalur endstop. Firmware ini sudah menyaringnya sejak v2.0.1: lakukan update.</td></tr>
<tr><td>Nozzle menabrak klip bed saat leveling</td><td>Update ke v2.0.2 atau yang lebih baru: kolom probing pertama berada 10 mm dari tepi, seperti di firmware Wanhao.</td></tr>
<tr><td>Bed bergerak menjauhi sakelar Y</td><td>Pastikan Anda mengambil firmware untuk model Anda: motor Y ada di belakang pada MK1, MK1 + kit, dan MK2, dan di depan pada MK3.</td></tr>
</tbody></table></div>

<h2>Kembali ke firmware Wanhao</h2>
<p>Setiap halaman model menyediakan tautan ke firmware mainboard dan layar asli Wanhao. Flash dengan cara yang sama; firmware
mainboard Wanhao membutuhkan firmware layar Wanhao dari generasi yang sama.</p>
<p>Pertanyaan: <a href="{DISCORD}">Discord</a> atau <a href="{REPO}/issues">issue di GitHub</a>.</p>
""")

    if page == "screen":
        return ("Firmware layar sentuh Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 dalam 16 bahasa",
                "Cara flash layar sentuh DWIN Wanhao D9 dengan DGUS Reloaded 2.0 dari kartu microSD: antarmuka baru dalam 16 "
                "bahasa, halaman sensor filamen, untuk Marlin 2.1. Serta cara kembali ke firmware layar Wanhao.",
                f"""
<h1>Flash layar sentuh Duplicator 9</h1>
<p class="lead">Semua D9, dari MK1 sampai MK3, memakai layar sentuh DWIN T5 yang sama (480 × 272). Dengan firmware ini, layar
menjalankan DGUS Reloaded 2.0, antarmuka baru kami dalam 16 bahasa, yang di-flash dari kartu microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Unduh DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Apa yang dibawa DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 bahasa</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Ketuk bendera di samping nama printer pada layar beranda
untuk mengganti bahasa; printer akan mengingat pilihan Anda.</li>
<li><strong>Halaman sensor filamen</strong>: <em>Pengaturan</em> → <em>Filamen</em> → <em>Sensor filamen</em>. Lihat
<a href="{p('sensor')}#screen">Sensor filamen</a>.</li>
<li><strong>Baris status yang tetap tampil</strong>: pesan terakhir, misalnya <em>Ready</em>, tetap ada di layar alih-alih
hilang setelah 30 detik.</li>
<li><strong>Indikator suhu</strong> untuk nozzle dan bed, dengan tanda suhu target.</li>
<li>Tampilan baru untuk semua halaman: tema gelap, tombol lebih besar, piktogram pada jendela pop-up.</li>
</ul>
</div><figure><img src="{img}screen/id-home.png" width="480" height="272" alt="Layar beranda DGUS Reloaded 2.0 pada Wanhao D9: suhu nozzle dan bed dengan indikator, baris status, tombol Cetak, Suhu, dan Pengaturan">
<figcaption>Layar beranda</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 membutuhkan <strong>v2.0.9 atau yang lebih baru</strong> di mainboard. Dengan v2.0.8 atau yang lebih lama,
bahasa kembali ke bahasa Inggris setiap kali dinyalakan dan halaman sensor filamen tidak berfungsi: <a href="{p('flash')}">flash
mainboard</a> terlebih dahulu.</div>

<h2>1. Format kartu microSD</h2>
<div class="note">FAT32 dengan allocation unit size <strong>4096 byte</strong>. Dengan ukuran lain, layar akan mengabaikan kartu.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 sering tidak mau memformat FAT32; gunakan <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
dan atur allocation unit size ke 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (periksa dulu perangkatnya dengan <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (periksa dengan <code>diskutil list</code>).</li>
</ul>

<h2>2. Salin file</h2>
<p>Ekstrak <code>DWIN_SET.zip</code> dan salin seluruh folder <code>DWIN_SET</code> ke root kartu.</p>

<h2>3. Flash</h2>
<ol>
<li>Matikan printer dan cabut kabel listriknya.</li>
<li>Buka bagian depan base untuk menjangkau bagian belakang layar, tempat slot microSD-nya berada.</li>
<li>Masukkan kartu lalu nyalakan printer. Layar menampilkan proses update dalam 10 sampai 30 detik; tunggu sampai layar
restart normal, total 1 sampai 3 menit.</li>
<li>Matikan printer, cabut kartu, tutup kembali base.</li>
</ol>
<p><a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">Video update layar D9</a> dari Wanhao menunjukkan letak slotnya.</p>

<h2>Asal-usulnya</h2>
<p>DGUS Reloaded 2.0 menggambar ulang <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(karya Desuuuu, lalu Neo2003) halaman demi halaman. Kode sumbernya, program yang menghasilkan file layar, dan terjemahannya ada
di <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Ada kata yang salah atau janggal dalam bahasa Anda? Beri tahu kami di
<a href="{DISCORD}">Discord</a> atau buka issue di sana.</p>
<p>Untuk kembali ke DGUS Reloaded 1.0.3, misalnya dengan firmware yang lebih lama dari v2.0.9, flash
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> dengan cara yang sama.</p>

<h2>Kembali ke layar Wanhao</h2>
<p>Firmware layar Wanhao hanya bekerja dengan firmware mainboard Wanhao. MK1: file layar dengan versi yang sesuai
di <a href="{p('mk1')}">halaman MK1</a>. MK1 + kit, MK2, dan MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Prosedurnya sama.</p>
""")

    if page == "sensor":
        return ("Sensor filamen pada Wanhao Duplicator 9: sakelar filamen habis dan pengkabelan BTT Smart Filament Sensor",
                "Tempat memasang sensor filamen di mainboard Wanhao D9 (D8, D9, GND, 5V), cara menyambungkan BTT Smart "
                "Filament Sensor V2.0, dan mengaktifkan deteksi filamen habis dan filamen macet dengan M412.",
                f"""
<h1>Sensor filamen</h1>
<p class="lead">Sejak v2.0.5, firmware ini membaca dua jenis sensor: sakelar filamen habis dari Wanhao, dan
BTT Smart Filament Sensor V2.0, yang juga mendeteksi saat filamen berhenti bergerak (spool kusut, macet, filamen
terkikis gear). <strong>Deteksi filamen habis aktif secara default di semua model</strong>, sedangkan deteksi macet nonaktif.</p>

<h2>Soket sensor</h2>
<figure><img src="{img}d9-sensor-plug-id.svg" width="760" height="440" alt="Mainboard Wanhao D9: soket sensor 4 pin di sebelah kiri POWER-DET, pin D9, D8, GND, dan 5V, tersambung ke BTT Smart Filament Sensor V2.0"></figure>
<p>Soket 4 pin di sebelah kiri <strong>POWER-DET</strong>, di bawah soket endstop, membawa <strong>D9, D8, GND, dan 5V</strong>,
dengan urutan tersebut. Nama pin berasal dari diagram pengkabelan Wanhao yang ditemukan dustovich dan dibagikan di
<a href="{DISCORD}">Discord</a>; di bagian belakang board, keempat pin yang sama tertulis CTRL, BTN, GND, dan VCC.</p>
<ul>
<li><strong>D8</strong> adalah input filamen habis yang dibaca firmware Wanhao sendiri.</li>
<li><strong>D9</strong> tidak dipakai oleh firmware Wanhao: build ini membaca sinyal gerakan sensor BTT di pin tersebut.</li>
</ul>
<div class="note">Printer harus dalam keadaan <strong>mati</strong> saat Anda memasang atau mencabut apa pun di board.</div>

<h2 id="screen">Di layar</h2>
<div class="split"><div>
<p>Dengan DGUS Reloaded 2.0 di layar (firmware v2.0.9 atau yang lebih baru): <em>Pengaturan</em> → <em>Filamen</em> →
<em>Sensor filamen</em>.</p>
<ul>
<li><strong>Filamen habis</strong> menyalakan atau mematikan semua deteksi, seperti <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Deteksi macet</strong> menyalakan deteksi macet dengan panjang di bawahnya, atau mematikannya (<code>L0</code>).</li>
<li><strong>Panjang macet</strong>: − dan + mengubahnya per 1 mm; ketuk angkanya untuk mengetik nilai.</li>
<li>Titik <strong>Filamen</strong> berwarna hijau saat sakelar filamen habis mendeteksi filamen, merah jika tidak.</li>
<li>Perubahan langsung berlaku. <strong>Simpan</strong> menyimpannya, seperti <code>M500</code>. Panah kembali keluar tanpa
menyimpan: setelan yang tersimpan akan kembali saat printer dinyalakan berikutnya.</li>
</ul>
</div><figure><img src="{img}screen/id-sensor.png" width="480" height="272" alt="Halaman sensor filamen DGUS Reloaded 2.0: sakelar deteksi filamen habis dan macet, panjang macet dengan tombol minus dan plus, indikator filamen, dan tombol Simpan">
<figcaption>Pengaturan → Filamen → Sensor filamen</figcaption></figure></div>

<h2>Perintah M412</h2>
<p>Semuanya diatur lewat USB dari terminal serial (Pronterface, terminal di slicer Anda atau di OctoPrint,
250000 baud). Parameter bisa digabung dalam satu perintah, misalnya <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Perintah</th><th>Fungsinya</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Menampilkan status, misalnya <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Menyalakan deteksi</strong>: sakelar filamen habis, dan juga deteksi macet jika panjang macet bukan 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Mematikan semua deteksi</strong>, sakelar maupun macet.</td></tr>
<tr><td><code>M412 D5</code></td><td>Setelah sakelar tidak lagi mendeteksi filamen, printer tetap mencetak <strong>5 mm</strong> sebelum pause, untuk memakai sisa filamen di antara sensor dan nozzle. Default 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Menyalakan deteksi macet</strong> (khusus sensor BTT): pause jika <strong>10 mm</strong> filamen melewati extruder tanpa roda sensor bergerak.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Mematikan deteksi macet</strong> dan membiarkan sakelar filamen habis apa adanya. Ini setelan default.</td></tr>
<tr><td><code>M500</code></td><td>Menyimpan setelan. Tanpa perintah ini, perubahan hilang saat printer dimatikan.</td></tr>
<tr><td><code>M119</code></td><td>Baris <em>filament</em> menampilkan <code>TRIGGERED</code> saat filamen terpasang, <code>open</code> jika tidak.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, dan <code>L</code> yang dipakai sendirian, berasal dari perubahan kami pada Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), yang sudah disertakan dalam firmware ini. Di Marlin tanpa perubahan itu, <code>L</code>
sendirian diabaikan dan <code>L0</code> langsung mem-pause cetakan karena dianggap macet.</p>

<h2>Sakelar filamen habis dari Wanhao</h2>
<p>Sakelar ini memberi tahu firmware apakah filamen ada. Saat filamen habis, cetakan di-pause setelah 5 mm filamen lagi
dan layar memulai proses ganti filamen.</p>
<p><strong>Sakelar ini aktif secara default di semua model, sejak v2.0.8.</strong> Jika tidak ada yang terpasang di D8, pull-up
pada board menahan pin di 5 V, yang terbaca sebagai “filamen ada”: deteksi tidak pernah terpicu, jadi fitur ini bisa
tetap aktif baik ada sensor maupun tidak. Pasang sakelar filamen habis ke D8 dan langsung berfungsi.</p>
<ul>
<li>Deteksi macet tetap nonaktif (<code>L0</code>): sakelar ini tidak bisa melihat filamen bergerak.</li>
<li>Untuk mematikan sakelar: <code>M412 S0</code> lalu <code>M500</code>.</li>
<li>Setelan yang disimpan oleh rilis sebelumnya mempertahankan status aktif/nonaktifnya. Untuk mengaktifkan: <code>M412 S1</code> lalu
<code>M500</code>, atau reset ke default (<code>M502</code> lalu <code>M500</code>, yang juga menghapus Z offset probe
dan mesh Anda).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Sensor ini punya dua output, dan firmware membacanya dengan cara berbeda:</p>
<ul>
<li><strong>Sakelar filamen habis</strong> (ke D8) berupa level: 5 V selama filamen ada, 0 V setelah filamen habis.</li>
<li><strong>Output gerakan</strong> (ke D9) berasal dari roda kecil yang diputar filamen saat lewat. Setiap beberapa
milimeter filamen, output berganti antara 0 V dan 5 V. Firmware hanya memantau perubahan itu: jika extruder mendorong
filamen sepanjang panjang macet tanpa satu pun perubahan, berarti filamen tidak ikut bergerak (spool kusut, macet, filamen
terkikis gear), dan cetakan di-pause. Sakelar filamen habis tidak bisa mendeteksi hal ini: saat macet, filamen masih ada.</li>
</ul>
<h3>Pengkabelan</h3>
<p><strong>5V</strong> ke 5V, <strong>GND</strong> ke GND, sinyal <strong>sakelar filamen habis</strong> ke <strong>D8</strong>
dan sinyal <strong>gerakan</strong> ke <strong>D9</strong>. Nama yang tercetak di kabel sensor bisa berbeda.</p>
<h3>Mengaktifkannya</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Jika cetakan pause tanpa alasan, naikkan panjang macet: <code>M412 L15</code> lalu <code>M500</code>. Untuk hanya memakai
sakelar filamen habis: <code>M412 L0</code> lalu <code>M500</code>.</p>
<h3>Memeriksanya</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> dengan filamen terpasang: <em>filament: TRIGGERED</em>. Jika baris itu berubah saat Anda mendorong filamen
dengan tangan, bukan saat memasukkan atau mencabutnya, berarti dua kabel sinyal tertukar: tukar D8 dan D9.</li>
</ul>
<div class="note">Deteksi macet sudah diuji pada MK2 300 tanpa sensor (panjang macet 2 mm memicu pause, <code>L0</code> tidak pernah),
tetapi belum diuji dengan sensor BTT itu sendiri. Jika sakelar terbaca terbalik (<em>open</em> saat filamen
terpasang), beri tahu kami di <a href="{DISCORD}">Discord</a>.</div>

<h2>Update dari v2.0.5 atau v2.0.6</h2>
<p>Rilis tersebut tidak punya cara untuk mematikan deteksi macet, jadi memakai panjang macet yang terlalu panjang untuk bisa tercapai: 100 m di
v2.0.5 (sebenarnya terlalu pendek: sekitar sepertiga spool 1 kg, setelah itu printer yang dibiarkan menyala bisa pause tanpa alasan) dan
10 km di v2.0.6. Saat printer dinyalakan, v2.0.7 memuat kedua nilai itu sebagai <code>L0</code>. Panjang sungguhan yang Anda atur
untuk sensor BTT, seperti <code>L10</code>, tetap dipertahankan. Dari v2.0.4 atau yang lebih lama, jarak filamen habis 5 mm dimuat
sebagai ganti nilai 0 yang disimpan versi-versi tersebut.</p>
""")

    if page == "slicer":
        return ("Profil Cura, OrcaSlicer dan Simplify3D untuk Wanhao Duplicator 9, dan cara mengatur Z offset",
                "Profil UltiMaker Cura, OrcaSlicer dan Simplify3D siap pakai untuk semua Wanhao D9, PLA, PETG dan ABS, cara "
                "mengatur Z offset probe, menjalankan probing bed dan mencetak 3DBenchy percobaan.",
                f"""
<h1>Slicing untuk Duplicator 9</h1>
<p class="lead">Satu profil untuk masing-masing dari dua belas printer, untuk
<strong>UltiMaker Cura</strong> dan <strong>OrcaSlicer</strong>, keduanya gratis dan tersedia di Windows, macOS dan
Linux, serta untuk <strong>Simplify3D</strong> kalau Anda sudah punya. Masing-masing sudah memuat volume cetak,
akselerasi dan suhu bed tertinggi dari firmware-nya sendiri.</p>

<h2>Unduhan</h2>
{h.slicer}
<p>Profil ini dibuat untuk firmware di situs ini, <a href="{p('flash')}">v2.0.9 atau yang lebih baru</a>.</p>

<h2>Cara memasangnya</h2>
<p><strong>OrcaSlicer</strong>: <em>File</em> → <em>Import</em> → <em>Import Configs…</em>, lalu pilih file
<code>.orca_printer</code>. Printer, tiga kualitasnya (0,12 / 0,20 / 0,28 mm) dan filamen PLA, PETG dan ABS akan
muncul di preset Anda.</p>
<p><strong>Cura</strong>: <em>Help</em> → <em>Show Configuration Folder</em>, tutup Cura, ekstrak file itu ke dalam
folder tersebut, jalankan Cura lagi, lalu <em>Settings</em> → <em>Printer</em> → <em>Add Printer…</em> → <em>Add a
non-networked printer</em> → <em>Wanhao</em> → model Anda. <em>Wanhao Duplicator 9</em> bawaan Cura adalah profil lama:
hanya ukuran 300, dengan raft dan support aktif secara default.</p>
<p><strong>Simplify3D</strong> (versi 5, berbayar): <em>File</em> → <em>Import Printer Profiles…</em>, lalu
pilih file <code>.fff</code>. Printer datang dengan tiga kualitasnya (0,30 / 0,20 / 0,10 mm) dan bahan PLA, PETG dan
ABS, di daftar <em>Auto-Configure</em> di atas pengaturan.</p>

<h2 id="first-print">Sebelum cetakan pertama: Z offset, lalu probing</h2>
<p>Probe memicu sedikit di atas bed, dan firmware harus tahu berapa selisihnya. Itulah <strong>Z offset</strong>.
Terlalu tinggi, layer pertama tidak menempel; terlalu rendah, nozzle menggores bed. Diatur sekali saja, dan inilah
setelan yang menentukan cetakan Anda menempel atau tidak.</p>
<div class="note">Semua yang ada di bawah ini tersimpan di memori printer, bukan di slicer. Nilainya bertahan setelah
update firmware (sejak v2.0.3).</div>

<h3>1. Panaskan dulu</h3>
<p>Nozzle yang panas beberapa perseratus milimeter lebih panjang. Panaskan seperti saat mencetak: di layar,
<em>Suhu</em> → <em>Panaskan</em> → <em>PLA</em> (200 °C dan 60 °C), lalu tunggu dua menit.</p>

<h3>2. Home-kan sumbunya</h3>
<p>Di layar: <em>Pengaturan</em> → <em>Gerak</em> → <em>Home</em>. Lewat USB: <code>G28</code>.</p>

<h3>3. Atur Z offset</h3>
<p><strong>Cara termudah, sambil mencetak.</strong> Mulai satu cetakan, dan selama <strong>layer pertama</strong> buka
<em>Sesuaikan</em> → <em>Offset Z</em> di layar. Turunkan per 0,01 mm selagi garisnya ditarik, sampai garisnya rata dan
menempel pada garis sebelahnya tanpa celah. Terlalu tinggi, garisnya tetap bulat dan terpisah; terlalu rendah,
permukaannya kasar dan gepeng, dan terlihat nozzle mengeruk bed. Nilainya tersimpan dengan sendirinya.</p>
<p><strong>Cara kertas, tanpa mencetak.</strong> Lewat USB, pada suhu cetak:</p>
<pre><code>M851 Z0     ; lupakan offset yang sekarang
M500
G28         ; home lagi supaya ikut diperhitungkan
M420 S0     ; abaikan mesh selama pengukuran
M211 S0     ; izinkan turun di bawah Z0: batas lunak yang menahan nozzle di situ
G1 Z0 F300  ; nozzle turun ke titik yang dianggap nol oleh firmware</code></pre>
<p>Selipkan selembar kertas di bawah nozzle, lalu turunkan sedikit demi sedikit dengan <code>G91</code> lalu
<code>G1 Z-0.05 F60</code>, berulang kali, sampai kertasnya baru mulai terasa seret. Baca nilainya dengan
<code>M114</code>: nilainya negatif, misalnya −1,30. Lalu:</p>
<pre><code>G90
M851 Z-1.30 ; nilai Anda
M500
M211 S1     ; pasang lagi batas lunaknya, itu yang melindungi bed</code></pre>
<p>Mulai v2.1.1, dua baris <code>M211</code> bisa dilewati: firmware sudah mengizinkan nozel turun 3 mm di bawah nol.</p>

<h3>4. Probing bed</h3>
<p>Di layar: <em>Pengaturan</em> → <em>Perataan</em> → <em>Otomatis</em> → <em>Probe</em>. Printer mengukur 25 titik
dan <strong>menyimpan mesh-nya sendiri</strong> (menjalankan <code>G29</code> lalu <code>M500</code>). Butuh beberapa
menit. Lewat USB: <code>G29</code> lalu <code>M500</code>.</p>
<p>Profil kami tidak melakukan probing sebelum setiap cetakan: profilnya menyalakan kembali mesh yang tersimpan dengan
<code>M420 S1</code>, tepat setelah homing. Jadi lakukan probing lagi kalau printer dipindahkan, kalau permukaan atau
nozzle diganti, atau kalau layer pertama bagus di satu sisi bed tetapi tidak di sisi lainnya.</p>

<h3>5. Periksa</h3>
<p><code>M503</code> menampilkan apa yang tersimpan: baris <code>M851</code> adalah Z offset Anda, dan
<code>M420 S1</code> menunjukkan mesh-nya aktif. Di layar, halaman <em>Otomatis</em> menampilkan 25 titik yang
terukur.</p>

<h2>Cetakan percobaan</h2>
<p>Sebuah 3DBenchy yang sudah di-slice untuk <strong>D9 MK2 300</strong>, untuk membandingkan kedua slicer atau
memeriksa satu setelan tanpa memasang apa pun:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Masing-masing sekitar satu setengah jam dan 4 m filamen. Untuk model atau ukuran lain, slice sendiri
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> dengan profil Anda.</p>
<h3>Tes all-in-one</h3>
<p>Batang overhang, sebuah jembatan, menara stringing, lubang toleransi dan skala kehalusan dalam satu benda 65 mm,
sekitar 2 jam 30 menit. Ini adalah <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a>
karya <strong>majda107</strong> (CC BY 4.0), di-slice untuk <strong>semua printer</strong> dan kedua slicer, dalam
ketiga materialnya. Berkas pada <a href="{REPO}/releases/latest">rilis terbaru</a> diberi nama
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, misalnya
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy yang dicetak dengan profil OrcaSlicer pada Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy yang dicetak dengan profil Cura pada Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="3DBenchy dicetak dengan PETG di Wanhao D9, oleh dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Mulai dari yang mana:</strong> pada D9 MK2 300 dengan PLA, Benchy yang sama memakan <strong>1 h 14 dengan
OrcaSlicer</strong> dan <strong>1 h 22 dengan Cura</strong>, dan dinding hasil OrcaSlicer keluar sedikit lebih bersih.
Keduanya bagus; OrcaSlicer yang akan kami pilih untuk memulai, dan perkakas kalibrasinya (flow, pressure advance,
menara suhu) membantu begitu Anda ingin lebih jauh.</p>
<div class="note">D9 adalah printer terbuka: ABS setidaknya butuh ruangan tanpa angin, dan suhu bed-nya diturunkan ke
angka yang diterima model Anda (80 °C di MK3 500).</div>

<h2>Isi profilnya</h2>
<ul>
<li><strong>Layer</strong> 0,20 mm, <strong>3 dinding</strong>, 4 layer atas dan 3 layer bawah, infill gyroid 15 %,
skirt 2 garis, tanpa support.</li>
<li><strong>Kecepatan</strong>: 40 mm/s di dinding luar, 60 di dalam, 70 untuk infill, 20 di layer pertama, 150 untuk
travel. Wanhao menyebut 70 mm/s sebagai kecepatan cetak tertinggi D9.</li>
<li><strong>Retraksi</strong> 1,5 mm pada 25 mm/s: semua D9 memakai ekstruder MK10 direct drive, dan firmware
membatasi ekstruder di 25 mm/s.</li>
<li><strong>Suhu</strong>: PLA 210 °C lalu 205, bed 65 lalu 60. PETG 240 / 80 lalu 235 / 75. ABS 245 / 105 lalu
245 / 100.</li>
<li><strong>Garis priming</strong> 15 mm dari tepi kiri, di luar klip bed, supaya nozzle sampai ke model dalam keadaan
bersih.</li>
<li>Di akhir cetakan, nozzle naik dan bed maju ke depan.</li>
</ul>
<p>Semua setelan dan cara mengubahnya: <a href="{REPO}/tree/main/Slicer">folder Slicer</a> di GitHub.</p>
""")

    if page == "quiet":
        return ("Membuat Wanhao Duplicator 9 lebih senyap: kipas mana saja, dan kipas board dengan termistor NTC",
                "Kipas Wanhao D9 mana yang bisa dibuat lebih senyap: kipas hotend harus tetap, kipas power supply sudah "
                "mengatur dirinya sendiri, dan kipas board bisa dicabut atau dijalankan lewat termistor NTC.",
                f"""
<h1>Membuat Duplicator 9 lebih senyap</h1>
<p class="lead">Saat diam, suara bising D9 berasal dari kipas-kipasnya. Berikut kipas mana yang bisa dibuat lebih senyap, dan caranya.</p>
<div class="note">Kerjakan dengan printer dalam keadaan <strong>dicabut dari listrik</strong>. Jauhkan semua kabel dari bagian 230 V.</div>

<h2>Kipas-kipasnya</h2>
<div class="table"><table class="stack"><thead><tr><th>Kipas</th><th>Dikendalikan oleh</th><th>Bisa dibuat lebih senyap?</th></tr></thead><tbody>
<tr><td><strong>Kipas heatsink hotend</strong> (print head)</td><td>tidak ada: 24 V selalu menyala</td><td><strong>tidak</strong>: biasanya paling bising, tetapi jika diperlambat, panas merambat naik ke hotend dan membuat filamen macet (heat creep)</td></tr>
<tr><td><strong>Kipas part cooling</strong> (print head)</td><td>firmware, pin D5 (PWM)</td><td>sudah bisa diatur: diatur oleh slicer dan <code>M106</code></td></tr>
<tr><td><strong>Kipas power supply</strong></td><td>power supply itu sendiri</td><td>tidak perlu diapa-apakan: pada unit yang diperiksa di sini (Chuanglian A-350FAK-24), kipas ini sudah mengikuti suhu power supply</td></tr>
<tr><td><strong>Kipas board</strong> (kotak kontrol)</td><td>tidak ada: 24 V selalu menyala</td><td><strong>ya</strong>, lihat di bawah</td></tr>
</tbody></table></div>
<p>Firmware Wanhao tidak mengendalikan kipas board maupun kipas hotend (<code>CONTROLLER_FAN_PIN</code> dan
<code>E0_AUTO_FAN_PIN</code> sama-sama <code>-1</code>), dan board tidak punya output switched yang tersisa. Itulah sebabnya
kedua kipas ini disambungkan ke konektor “24V OUT” yang selalu menyala, dan tidak ada firmware yang bisa memperlambatnya.</p>

<h2>Kipas board</h2>
<p>Pada unit yang diukur di sini: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, maks. 0,10 A, sleeve bearing</strong>.</p>
<p><strong>Banyak pemilik yang langsung mencabutnya saja.</strong> Board-nya tidak panas: letaknya di dasar kotak kontrol, di bawah
heated bed, dan panas bed naik menjauhinya. Jika Anda melakukannya, perhatikan beberapa cetakan panjang pertama Anda: driver stepper
yang kepanasan akan mati sebentar, yang terlihat sebagai <strong>layer bergeser</strong>, bukan sebagai pesan error.</p>
<h3>Tetap memakainya, tetapi hanya saat driver panas</h3>
<p>Dua termistor NTC daya yang dipasang seri membuat kipas mulai berputar sekitar 45–50 °C dan makin cepat seiring driver memanas:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), direkatkan ke heatsink driver dengan lem
termal, kakinya diisolasi.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── kipas (+)
                                    kipas (−) ── 0V</code></pre>
<ul>
<li>Ini hasil perhitungan, <strong>belum diuji pada printer</strong>: toleransi MF72 ±20 %, dan kipas kecil bisa mulai
berputar pada suhu lebih rendah dari perkiraan. Periksa suhu mulainya di meja kerja (NTC dalam kantong plastik kecil di air panas,
dengan termometer dapur); tambahkan satu lagi 200 Ω jika mulai terlalu cepat, lepas yang 200 Ω jika terlalu lambat.</li>
<li>NTC harus direkatkan ke heatsink: di udara terbuka, arus kipas (hingga sekitar 0,6 W di NTC) memanaskannya
hingga puluhan derajat.</li>
<li>Dengan cara ini kipas tidak pernah mencapai kecepatan penuh (sekitar 75 % pada 80 °C), dan NTC yang rusak menjadi open: kipas
pun berhenti untuk seterusnya.</li>
</ul>
<p>Sumber: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">datasheet MF72</a>.</p>
""")
    raise KeyError(page)
