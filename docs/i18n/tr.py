"""Türkçe: translation of en.py."""

META = {"name": "Türkçe", "locale": "tr_TR", "dir": "ltr"}

UI = {
    "nav": {"index": "Ana sayfa", "mk1": "MK1", "mk1u2": "MK1 + MK2 kiti", "mk2": "MK2", "mk3": "MK3",
            "flash": "Yükleme rehberi", "screen": "Ekran", "sensor": "Filament sensörü", "slicer": "Dilimleyici",
            "quiet": "Sessizleştirme"},
    "language": "Dil",
    "model": "Model",
    "size": "Boyut", "volume": "Baskı hacmi", "file": "Firmware",
    "footer_src": "Kaynak kod ve sorun kayıtları GitHub'da", "footer_chat": "Discord",
    "footer_note": "Firmware GNU GPL v3 lisanslıdır. Wanhao'nun kılavuzları ve firmware'leri Wanhao'ya aittir.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Wanhao D9 anakartı (üstten görünüş)",
    "plug": "sensör soketi",
    "switch": "filament bitti anahtarı",
    "motion": "hareket",
    "level": "seviye: filament var / yok",
    "pulses": "filament ilerledikçe darbeler",
    "names": "sensörünüzdeki adlar farklı olabilir",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Wanhao Duplicator 9 firmware'i (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Tüm Wanhao Duplicator 9 modelleri (D9/300, D9/400, D9/500; MK1, MK2, MK3) için güncel Marlin firmware, "
                "ekran dosyaları, Wanhao'nun orijinal firmware'leri ve kılavuzları, ve bunların nasıl yükleneceği.",
                f"""
<h1>Wanhao Duplicator 9 firmware'i</h1>
<p class="lead">Wanhao'nun Duplicator 9 indirme sitesi artık yok. Bir D9 sahibinin ihtiyaç duyduğu her şey artık burada:
her model ve boyut için güncel Marlin 2.1 firmware, uyumlu dokunmatik ekran dosyaları, Wanhao'nun orijinal
firmware'leri, Wanhao'nun kılavuzları ve adım adım yükleme rehberleri.</p>
<p><a class="btn" href="{REPO}/releases/latest">Tüm indirmeler</a> <a class="btn ghost" href="{DISCORD}">Discord'da sorun</a></p>

<h2>Hangi D9'a sahibim?</h2>
<div class="split"><div>
<ol>
<li>Baskı kafasına giden <strong>gri yassı şerit kablo</strong>, nozulun yanında <strong>metal silindir bir prob</strong>,
gövdenin yanlarında takviye yok: <a href="{p('mk1')}">MK1</a>.</li>
<li>Aynı ilk nesil makine, metal prob yerine <strong>beyaz bir BLTouch probuyla</strong>:
Wanhao'nun yükseltme kiti takılmış bir MK1, <a href="{p('mk1u2')}">MK1 + MK2 kiti</a>.</li>
<li>Gövdenin iki yanında <strong>açılı takviye kolları</strong>, kafaya giden <strong>yuvarlak siyah kablo</strong>
ve BLTouch: bir MK2 ya da MK3. Tablanın altındaki <strong>Y motoruna</strong>, yani tablayı hareket ettiren motora
bakın: arkadaysa bir <a href="{p('mk2')}">MK2</a>; önde, dokunmatik ekran tarafındaysa bir
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>D9'dan sonraki sayı boyutu gösterir: D9/300, D9/400 veya D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Yan takviye kollarıyla Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2: yan takviyeler, yuvarlak kablo</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Endüktif prob, şerit kablo. Firmware, Wanhao V0.15 ile V0.164(B) arası, kılavuz.</p><a class="more" href="{p('mk1')}">MK1 firmware'i →</a></div>
<div class="card"><h3>D9 MK1 + MK2 kiti</h3><p>BLTouch kitiyle yükseltilmiş MK1. Firmware ve Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Kit firmware'i →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, yan takviyeler. Firmware, Wanhao V1.1.2, rehberler.</p><a class="more" href="{p('mk2')}">MK2 firmware'i →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y motoru önde, filament sensörü. Firmware ve Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3 firmware'i →</a></div>
</div>

<h2>Bu firmware'ler neler getiriyor</h2>
<ul>
<li><strong>Marlin 2.1</strong>, <a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>
içinde yayımlanan Duplicator 9 yapılandırmalarından, orada önerilen değişikliklerle derlendi: MK1 probunun doğru
yönde okunması, MK3'ün Y yönü, elektrik kesintisinden kurtarma, endstop parazit filtresi.</li>
<li><strong>Wanhao'nun fabrika ayarları</strong>, her model için Wanhao'nun kendi firmware'inden ve kaynak kodundan alındı: steps/mm,
hızlar, hızlanmalar, hotend PID'i, prob ofsetleri ve ölçüm kenar payları, homing, termal sınırlar, jerk ve eksen yönleri.</li>
<li><strong>Elektrik kesintisinden kurtarma</strong>: SD karttan baskı sırasında iş her katman değişiminde kaydedilir ve bir kesintiden sonra ekran kaldığı yerden devam etmeyi önerir.</li>
<li><strong>Filament sensörleri</strong>: D8 üzerinde bir filament bitti anahtarı, her modelde varsayılan olarak açık (anahtar yoksa etkisi yok), ve tıkanmaları da yakalayan BTT Smart Filament Sensor V2.0. Bkz. <a href="{p('sensor')}">Filament sensörü</a>.</li>
<li><strong>Tabla seviyelemesinden sonra kafa ortaya döner</strong>, böylece tabla artık ekranı kapatmaz.</li>
<li><strong>16 dilde yeni bir dokunmatik ekran arayüzü</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, filament sensörünü ayarlamak için bir sayfayla.</li>
</ul>

<h2>Üç adımda yükleme</h2>
<ol>
<li>Modelinize ve boyutunuza uygun <strong>.hex</strong> dosyasını modelin sayfasından indirin.</li>
<li>AVRDUDESS veya avrdude ile USB üzerinden yükleyin: <a href="{p('flash')}">yükleme rehberi</a>.</li>
<li>Dokunmatik ekranın firmware'ini bir microSD karttan yükleyin: <a href="{p('screen')}">ekran rehberi</a>.</li>
</ol>
<p>Wanhao'nun orijinal firmware'leri her model sayfasında durmaya devam ediyor; böylece bir makine her zaman fabrikadan çıktığı hâline geri döndürülebilir.</p>
""")

    if page == "mk1":
        return ("Wanhao Duplicator 9 MK1 firmware'i (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Endüktif problu Wanhao D9 MK1 için Marlin 2.1 firmware, Wanhao'nun orijinal V0.15 – V0.164(B) firmware'leri, "
                "ekran dosyaları ve MK1 kullanım kılavuzu.",
                f"""
<h1>Wanhao Duplicator 9 MK1 firmware'i</h1>
<div class="split"><div>
<p class="lead">İlk Duplicator 9: nozulun yanında metal endüktif bir prob, baskı kafasına giden gri şerit kablo ve
yan takviyesi olmayan bir gövde.</p>
<p>Bu derlemeler endüktif probu doğru yönde okur (LOW seviyede tetiklenir) ve Wanhao'nun son MK1 firmware'i olan
V0.164(B) sürümünün ayarlarını, prob ofsetleri dahil (X 15, Y 0), kullanır. Y motoru, Wanhao'nun yaptığı gibi arkadadır.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Wanhao D9 MK1 baskı kafasında endüktif prob ve şerit kablo">
<figcaption>MK1: endüktif prob, şerit kablo</figcaption></figure></div>

<h2>İndirme</h2>
{dl("MK1")}
<p>Boyutunuza uygun dosyayı alın, ardından ekrana
<a href="{p('screen')}">DGUS Reloaded</a> yükleyin.</p>

<h2>Wanhao'nun belgeleri</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 kullanım kılavuzu</a> (Haziran 2018, İngilizce): montaj, kablolama, menüler, seviyeleme, sorun giderme.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 başlangıç rehberi</a>.</li>
</ul>

<h2>Wanhao'nun orijinal firmware'leri</h2>
<p>Bir makineyi fabrikadan çıktığı hâline döndürmek için. Her anakart firmware'i yalnızca aynı sürümdeki ekran
firmware'iyle çalışır.</p>
<div class="table"><table><thead><tr><th>Sürüm</th><th>Boyut</th><th>Anakart</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Her sürümün ayarları (steps/mm, hızlar, PID, eksen yönleri), Wanhao'nun binary dosyalarından okunarak
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a> içinde listelenmiştir.</p>
""")

    if page == "mk1u2":
        return ("MK2 yükseltme kitli (BLTouch) Wanhao Duplicator 9 MK1 firmware'i – Marlin 2.1",
                "Wanhao'nun MK2 BLTouch kitiyle yükseltilmiş Wanhao D9 MK1 için Marlin 2.1 firmware ve Wanhao'nun orijinal V1.1.31 kit firmware'i.",
                f"""
<h1>MK2 yükseltme kitli Wanhao D9 MK1</h1>
<div class="split"><div>
<p class="lead">Wanhao'nun MK2 yükseltme kiti takılmış ilk nesil bir D9: MK1 gövdesi, metal endüktif prob yerine
bir BLTouch probuyla.</p>
<p>Wanhao bu kombinasyon için ayrı bir firmware yayımlamıştı, çünkü kitin BLTouch'ı fabrika çıkışı MK2'dekiyle aynı
yerde durmaz: probun Y ofseti farklıdır. Bu derlemeler kitin geometrisini kullanır. Y motoru arkadadır.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Wanhao D9 baskı kafasında BLTouch probu">
<figcaption>BLTouch probu</figcaption></figure></div>

<h2>İndirme</h2>
{dl("MK1u2")}
<p>Boyutunuza uygun dosyayı alın, ardından ekrana
<a href="{p('screen')}">DGUS Reloaded</a> yükleyin.</p>
<div class="note">Bu derlemeler kit firmware'indeki prob ofsetini kullanır: Y −10. Wanhao'nun kit kaynak kodunun fabrika
MK2'sininkinden (Y 0) farklı olduğu tek satır budur: kitin BLTouch'ı daha arkada durur. Tabla mesh'iniz önden arkaya
kaymış görünüyorsa, kendi ofsetinizi <a href="{REPO}/blob/main/Offset.md">ofset rehberi</a> ile ölçün.</div>

<h2>Wanhao'nun orijinal firmware'leri</h2>
<p>Wanhao'nun V1.1.31 kit firmware'i (Aralık 2018), MK2 ekran firmware'iyle birlikte kullanılır.</p>
<div class="table"><table><thead><tr><th>Boyut</th><th>Anakart</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao'nun binary dosyalarından okunan ayarlar: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Wanhao Duplicator 9 MK2 firmware'i (D9/300, D9/400, D9/500) – Marlin 2.1",
                "BLTouch'lı Wanhao D9 MK2 için Marlin 2.1 firmware, Wanhao'nun orijinal V1.1.2 firmware'i ve ekran dosyaları, ve Wanhao'nun MK2 rehberleri.",
                f"""
<h1>Wanhao Duplicator 9 MK2 firmware'i</h1>
<div class="split"><div>
<p class="lead">İkinci Duplicator 9: iki yanda açılı takviye kolları, baskı kafasına giden yuvarlak siyah veri kablosu,
bir BLTouch probu ve üstte bir makara tutucu.</p>
<p>Wanhao ayrıca taşıyıcıları dört tekerlekli yaptı; 400 ve 500'de çift raylı Y ekseni ile daha kalın bir kayış,
300 ve 400'de ise çift yüzlü tabla kullandı. Y motoru arkadadır; bu derlemeler Y eksenini Wanhao'nun V1.1.2
firmware'iyle aynı yönde döndürür.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>İndirme</h2>
{dl("MK2")}
<p>Boyutunuza uygun dosyayı alın. Kafası da MK3'e yükseltilmiş bir MK2,
<a href="{p('mk3')}">MK3 firmware'ini</a> kullanmalıdır. Ardından ekrana <a href="{p('screen')}">DGUS Reloaded</a> yükleyin.</p>

<h2>Wanhao'nun belgeleri</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 başlangıç rehberi</a> (İngilizce).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">MK1'den MK2'ye 12 iyileştirme</a>, Wanhao'dan.</li>
</ul>

<h2>Wanhao'nun orijinal firmware'leri</h2>
<p>Wanhao'nun V1.1.2 sürümü (Ekim 2018; 500 modeli Temmuz 2019'da V1.1.2.1 olarak yeniden derlendi), Wanhao'nun MK2 ekran firmware'iyle birlikte.</p>
<div class="table"><table><thead><tr><th>Boyut</th><th>Anakart</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao'nun binary dosyalarından okunan ayarlar: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Wanhao Duplicator 9 MK3 firmware'i (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Wanhao D9 MK3 (Y motoru önde, filament sensörü) için Marlin 2.1 firmware ve Wanhao'nun orijinal V1.1.3 firmware'i.",
                f"""
<h1>Wanhao Duplicator 9 MK3 firmware'i</h1>
<p class="lead">Son Duplicator 9, MK2'nin gövdesini ve BLTouch'ını korur, bir filament bitti sensörü ekler ve Y motorunu
öne, dokunmatik ekran tarafına taşır.</p>
<p>Motorun yer değiştirmesi Y eksenini ters çevirir: Wanhao'nun kendi V1.1.3 firmware'i Y'yi ters çevirir, bu derlemeler
de öyle. Filament bitti sensörü varsayılan olarak açıktır. Wanhao MK3 için prob ofseti yayımlamadı, bu yüzden bu
derlemeler MK2'ninkileri kullanır.</p>

<h2>İndirme</h2>
{dl("MK3")}
<p>Boyutunuza uygun dosyayı alın, ardından ekrana
<a href="{p('screen')}">DGUS Reloaded</a> yükleyin.</p>
<div class="note">Filament sensörü baskıları rastgele durduruyorsa, <code>M412 S0</code> ve ardından
<code>M500</code> ile kapatın. Wanhao Europe bu sorun için “ReverseMode” adlı bir MK3 firmware'i yayımlamıştı; bu
firmware sonradan silindi ve bulunamadı.</div>

<h2>Wanhao'nun orijinal firmware'leri</h2>
<p>Wanhao'nun V1.1.3 sürümü (Ağustos 2019). Wanhao hiç MK3 ekran firmware'i yayımlamadı: MK3 indirmeleri MK2'ninkine dayanıyordu.</p>
<div class="table"><table><thead><tr><th>Boyut</th><th>Anakart</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao'nun binary dosyalarından okunan ayarlar: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Wanhao Duplicator 9 (D9) anakart firmware'i nasıl yüklenir",
                "Wanhao D9'a AVRDUDESS veya avrdude ile USB üzerinden Marlin yükleme, homing sorunlarını çözme ve "
                "Wanhao'nun firmware'ine geri dönme için adım adım rehber.",
                f"""
<h1>Duplicator 9 anakartına firmware yükleme</h1>
<p class="lead">D9'un anakartı USB bootloader'lı bir ATmega2560'tır: programlayıcı yok, tabanı açmak yok,
sadece bir USB kablosu.</p>

<h2>Gerekenler</h2>
<ul>
<li>Yazıcı ile bilgisayar arasında bir USB kablosu ve <strong>açık</strong> bir yazıcı.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, grafik arayüz, en kolayı) veya
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (komut satırı, tüm sistemler).</li>
<li>Modelinize ve boyutunuza uygun <strong>.hex</strong>: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Yüklemeden önce</h2>
<div class="note"><code>M503</code> gönderin ve yanıtı saklayın. v2.0.3'ten beri bir güncelleme yazıcıda kayıtlı ayarları
korur, ama <strong>v2.0.3'e</strong> güncelleme bir kereliğine bu firmware'in varsayılan değerleriyle başlar (ayarların
saklanma şekli değişti); Wanhao'nun firmware'inden geçişte de durum aynıdır. Sonrasında prob Z ofsetinizi
<code>M851 Z…</code> ve <code>M500</code> ile yeniden ayarlayın.</div>
<p>Yazıcının portunu kullanıyor olabilecek tüm programları kapatın: Cura, PrusaSlicer, OctoPrint, Pronterface, seri terminaller.</p>

<h2>AVRDUDESS ile yükleme</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: yazıcınızın COM portu (örneğin <code>COM3</code>). Baud hızını varsayılan değerinde bırakın.</li>
<li>Flash: .hex dosyasını seçin, ardından <strong>Program!</strong> düğmesine tıklayın. İşlem 30 ile 60 saniye sürer.</li>
</ol>

<h2>avrdude ile yükleme</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Portu ve dosya adını kendinizinkilerle değiştirin. <code>wiring</code> protokolü bootloader'ın hızını kendisi seçer.</p>

<h2>İlk açılış</h2>
<ol>
<li>USB kablosunu çıkarın, yazıcıyı kapatıp açın, kabloyu yeniden takın.</li>
<li><strong>250000 baud</strong> ile bağlanın (Wanhao'nun firmware'leri 115200 kullanıyordu) ve <code>M115</code> gönderin: yanıtta yeni firmware görünür.</li>
<li>Tüm eksenlerde homing yapın, ardından ekrandan veya <code>G29</code> ile tabla seviyelemesi yapın ve <code>M500</code> ile kaydedin.</li>
</ol>

<h2 id="reset">Bu firmware'in varsayılan ayarlarına dönmek</h2>
<p>v2.0.3'ten beri bir firmware güncellemesi yazıcıda kayıtlı ayarları <strong>korur</strong> (prob Z ofseti, steps/mm,
PID, mesh…). Bu yüzden bir sürümdeki yeni varsayılan değerler, zaten kayıtlı olanların yerine geçmez. Elle kaydedilmiş
değerleri koruyarak v2.0.2 veya daha eski bir sürümden güncelliyorsanız, başka firmware'ler denedikten sonra yazıcı tuhaf
davranıyorsa ya da temiz bir başlangıç yapmak istediğiniz her durumda bir kez sıfırlama yapın:</p>
<ul>
<li><strong>Ekrandan:</strong> <em>Ayarlar</em> → <em>Diğer</em> → <em>Sıfırla</em> → ✓.</li>
<li><strong>USB üzerinden:</strong> <code>M502</code> (bu firmware'in varsayılanlarını yükler) ve ardından <code>M500</code> (bunları kaydeder) gönderin.</li>
</ul>
<p>Ardından prob Z ofsetinizi yeniden ayarlayın (<code>M851 Z…</code> ve ardından <code>M500</code>) ve bir tabla
seviyelemesi yapın. Sonucu <code>M503</code> ile kontrol edin.</p>

<h2>Elektrik kesintisi ve filament sensörü</h2>
<ul>
<li>Elektrik kesintisinden kurtarma açıktır: iş her katman değişiminde kaydedilir. Kapatmak için: <code>M413 S0</code> ve ardından <code>M500</code>.</li>
<li>Isınmaya başlar başlamaz <em>power outage</em> mesajıyla hemen duran bir baskı: v2.0.4 veya daha yeni bir sürüme güncelleyin. Önceki derlemeler kartın elektrik kesintisi girişini izliyordu; bu giriş ısıtıcılar çalışmaya başlar başlamaz düşük okunur.</li>
<li>Filament bitti algılama v2.0.8'den beri her modelde varsayılan olarak açıktır ve sensör yoksa hiçbir şey yapmaz. Daha eski bir sürümden güncelledikten sonra <code>M412 S1</code> ve ardından <code>M500</code> ile ya da ekranda <em>Ayarlar</em> → <em>Filament</em> → <em>Filament sensörü</em> altından açın. Kablolama ve BTT Smart Filament Sensor: <a href="{p('sensor')}">Filament sensörü</a>.</li>
</ul>

<h2>Sorun giderme</h2>
<div class="table"><table><thead><tr><th>Sorun</th><th>Çözüm</th></tr></thead><tbody>
<tr><td>Port kullanımda</td><td>Yazıcının portunu kullanan tüm programları kapatın.</td></tr>
<tr><td>Cihaz bulunamadı</td><td>CH340 USB sürücüsünü kurun, başka bir kablo veya USB portu deneyin, yazıcının açık olduğunu kontrol edin.</td></tr>
<tr><td>Yüklemeden sonra okunamayan karakterler</td><td>Bu firmware'lerle 250000 baud, Wanhao'nunkilerle 115200 kullanın.</td></tr>
<tr><td>Ekranda sıcaklıklar ×10 gösteriliyor (23,6 °C için 236)</td><td>Ekranda hâlâ eski dosyalar var: <a href="{p('screen')}">DGUS Reloaded 2.0</a> yükleyin.</td></tr>
<tr><td>Ekran her açılışta İngilizceye dönüyor ya da <em>Filament sensörü</em> sayfası hiçbir şey yapmıyor</td><td>Anakart firmware'i v2.0.9'dan eski: güncelleyin.</td></tr>
<tr><td>Homing, anahtara birkaç milimetre kala duruyor, ardından <em>Homing Failed</em></td><td>Endstop hattında elektriksel parazit. Bu firmware'ler v2.0.1'den beri bunu filtreliyor: güncelleyin.</td></tr>
<tr><td>Seviyeleme sırasında nozul bir tabla klipsine çarpıyor</td><td>v2.0.2 veya daha yeni bir sürüme güncelleyin: ilk ölçüm sütunu, Wanhao'nun firmware'inde olduğu gibi kenardan 10 mm içeridedir.</td></tr>
<tr><td>Tabla Y anahtarından uzağa gidiyor</td><td>Modelinize ait firmware'i aldığınızı kontrol edin: Y motoru MK1, MK1 + kit ve MK2'de arkada, MK3'te öndedir.</td></tr>
</tbody></table></div>

<h2>Wanhao'nun firmware'ine geri dönmek</h2>
<p>Her model sayfası Wanhao'nun orijinal anakart ve ekran firmware'lerine bağlantı verir. Bunları aynı şekilde yükleyin;
Wanhao'nun anakart firmware'i, aynı nesilden Wanhao ekran firmware'ine ihtiyaç duyar.</p>
<p>Sorular için: <a href="{DISCORD}">Discord</a> veya <a href="{REPO}/issues">GitHub sorun kayıtları</a>.</p>
""")

    if page == "screen":
        return ("Wanhao Duplicator 9 dokunmatik ekran firmware'i (DWIN DGUS) – 16 dilde DGUS Reloaded 2.0",
                "Wanhao D9'un DWIN dokunmatik ekranına microSD karttan DGUS Reloaded 2.0 yükleme: 16 dilde yeni arayüz, "
                "filament sensörü sayfası, Marlin 2.1 için. Ve Wanhao'nun ekran firmware'ine nasıl geri dönülür.",
                f"""
<h1>Duplicator 9 dokunmatik ekranına firmware yükleme</h1>
<p class="lead">MK1'den MK3'e her D9'da aynı DWIN T5 dokunmatik ekran (480 × 272) bulunur. Bu firmware'lerle ekranda,
microSD karttan yüklenen, 16 dilli yeni arayüzümüz DGUS Reloaded 2.0 çalışır.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">DWIN_SET.zip dosyasını indir (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>DGUS Reloaded 2.0 neler getiriyor</h2>
<ul>
<li><strong>16 dil</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Dili değiştirmek için ana ekranda yazıcı adının yanındaki
bayrağa dokunun; yazıcı seçiminizi hatırlar.</li>
<li><strong>Filament sensörü sayfası</strong>: <em>Ayarlar</em> → <em>Filament</em> → <em>Filament sensörü</em>. Bkz.
<a href="{p('sensor')}#screen">Filament sensörü</a>.</li>
<li><strong>Kalıcı bir durum satırı</strong>: son mesaj, örneğin <em>Ready</em>, 30 saniye sonra kaybolmak yerine
ekranda kalır.</li>
<li>Nozul ve tabla için, hedef değeri işaretli <strong>sıcaklık göstergeleri</strong>.</li>
<li>Tüm sayfalara yeni bir görünüm: koyu tema, daha büyük düğmeler, açılır pencerelerde piktogramlar.</li>
</ul>
</div><figure><img src="{img}screen/tr-home.png" width="480" height="272" alt="Wanhao D9 üzerinde DGUS Reloaded 2.0 ana ekranı: göstergeli nozul ve tabla sıcaklıkları, durum satırı, Yazdır, Sıcaklık ve Ayarlar düğmeleri">
<figcaption>Ana ekran</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0, anakartta <strong>v2.0.9 veya daha yeni</strong> bir sürüm gerektirir. v2.0.8 veya daha eski
bir sürümle dil her açılışta İngilizceye döner ve filament sensörü sayfası çalışmaz: önce <a href="{p('flash')}">anakarta
firmware yükleyin</a>.</div>

<h2>1. microSD kartı biçimlendirin</h2>
<div class="note"><strong>4096 bayt</strong> ayırma birimi boyutuyla FAT32. Başka herhangi bir boyutta ekran kartı yok sayar.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 çoğu zaman FAT32 biçimlendirmez; <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
kullanın ve ayırma birimi boyutunu 4096 yapın.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (önce aygıtı <code>lsblk</code> ile kontrol edin).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (<code>diskutil list</code> ile kontrol edin).</li>
</ul>

<h2>2. Dosyaları kopyalayın</h2>
<p><code>DWIN_SET.zip</code> arşivini açın ve <code>DWIN_SET</code> klasörünün tamamını kartın kök dizinine kopyalayın.</p>

<h2>3. Yükleyin</h2>
<ol>
<li>Yazıcıyı kapatın ve fişini çekin.</li>
<li>Ekranın arkasına, microSD yuvasının bulunduğu yere ulaşmak için tabanın ön kısmını açın.</li>
<li>Kartı takın ve yazıcıyı açın. Ekran 10 ile 30 saniye içinde güncellemeyi gösterir; normal şekilde yeniden başlayana
kadar bekleyin, toplamda 1 ile 3 dakika.</li>
<li>Yazıcıyı kapatın, kartı çıkarın, tabanı kapatın.</li>
</ol>
<p>Wanhao'nun <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">D9 ekran güncelleme videosu</a> yuvanın yerini gösteriyor.</p>

<h2>Nereden geliyor</h2>
<p>DGUS Reloaded 2.0, <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
arayüzünü (önce Desuuuu, sonra Neo2003 tarafından geliştirildi) sayfa sayfa yeniden çizer. Kaynak kodu, ekran dosyalarını
üreten program ve çeviriler <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a> üzerinde. Dilinizde yanlış
ya da kulağa garip gelen bir kelime mi var? Bize <a href="{DISCORD}">Discord</a> üzerinden söyleyin ya da GitHub'da bir sorun kaydı açın.</p>
<p>DGUS Reloaded 1.0.3'e dönmek için, örneğin v2.0.9'dan eski bir firmware ile,
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> dosyasını aynı şekilde yükleyin.</p>

<h2>Wanhao'nun ekranına geri dönmek</h2>
<p>Wanhao'nun ekran firmware'i yalnızca Wanhao'nun anakart firmware'iyle çalışır. MK1: <a href="{p('mk1')}">MK1 sayfasındaki</a>
ilgili sürümün ekran dosyası. MK1 + kit, MK2 ve MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Prosedür aynıdır.</p>
""")

    if page == "sensor":
        return ("Wanhao Duplicator 9'da filament sensörleri: filament bitti anahtarı ve BTT Smart Filament Sensor bağlantısı",
                "Wanhao D9 anakartında filament sensörü nereye takılır (D8, D9, GND, 5V), BTT Smart Filament Sensor V2.0 nasıl "
                "bağlanır ve M412 ile filament bitti ve tıkanma algılama nasıl açılır.",
                f"""
<h1>Filament sensörleri</h1>
<p class="lead">v2.0.5'ten itibaren bu firmware'ler iki tür sensör okur: Wanhao'nun filament bitti anahtarı ve
filamentin ilerlemeyi bıraktığını da fark eden (dolaşmış makara, tıkanma, dişlinin yediği filament) BTT Smart Filament
Sensor V2.0. <strong>Filament bitti algılama her modelde varsayılan olarak açıktır</strong>, tıkanma algılama ise kapalıdır.</p>

<h2>Sensör soketi</h2>
<figure><img src="{img}d9-sensor-plug-tr.svg" width="760" height="440" alt="Wanhao D9 anakartı: POWER-DET'in solundaki 4 pinli sensör soketi, D9, D8, GND ve 5V pinleri, bir BTT Smart Filament Sensor V2.0'a bağlı"></figure>
<p>Endstop soketlerinin altında, <strong>POWER-DET</strong> yazısının solundaki 4 pinli soket, bu sırayla <strong>D9, D8, GND ve 5V</strong>
pinlerini taşır. Pin adları, dustovich'in bulup <a href="{DISCORD}">Discord</a> sunucusunda paylaştığı bir Wanhao kablolama
şemasından geliyor; kartın arka yüzünde aynı dört pin CTRL, BTN, GND ve VCC olarak yazılıdır.</p>
<ul>
<li><strong>D8</strong>, Wanhao'nun kendi firmware'inin okuduğu filament bitti girişidir.</li>
<li><strong>D9</strong> Wanhao'nun firmware'i tarafından kullanılmaz: bu derlemeler BTT sensörünün hareket sinyalini bu pinden okur.</li>
</ul>
<div class="note">Kart üzerinde herhangi bir şeyi takıp çıkarırken yazıcı <strong>kapalı</strong> olmalıdır.</div>

<h2 id="screen">Ekranda</h2>
<div class="split"><div>
<p>Ekranda DGUS Reloaded 2.0 varken (firmware v2.0.9 veya daha yeni): <em>Ayarlar</em> → <em>Filament</em> →
<em>Filament sensörü</em>.</p>
<ul>
<li><strong>Filament bitti</strong> tüm algılamayı açar veya kapatır, <code>M412 S1</code> / <code>M412 S0</code> gibi.</li>
<li><strong>Tıkanma algılama</strong>, tıkanma algılamayı alttaki uzunlukla açar ya da kapatır (<code>L0</code>).</li>
<li><strong>Tıkanma uzunluğu</strong>: − ve + değeri 1 mm değiştirir; elle yazmak için sayıya dokunun.</li>
<li><strong>Filament</strong> noktası, filament bitti anahtarı filamenti gördüğü sürece yeşil, görmediğinde kırmızıdır.</li>
<li>Değişiklikler hemen uygulanır. <strong>Kaydet</strong> onları saklar, <code>M500</code> gibi. Geri oku kaydetmeden
çıkar: kayıtlı ayarlar bir sonraki açılışta geri gelir.</li>
</ul>
</div><figure><img src="{img}screen/tr-sensor.png" width="480" height="272" alt="DGUS Reloaded 2.0 filament sensörü sayfası: filament bitti ve tıkanma algılama anahtarları, eksi ve artı düğmeli tıkanma uzunluğu, filament göstergesi ve Kaydet düğmesi">
<figcaption>Ayarlar → Filament → Filament sensörü</figcaption></figure></div>

<h2>M412 komutları</h2>
<p>Her şey USB üzerinden bir seri terminalden ayarlanır (Pronterface, dilimleyicinizin ya da OctoPrint'in terminali,
250000 baud). Parametreler tek bir komutta birleştirilebilir, örneğin <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Komut</th><th>Ne yapar</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Durumu gösterir, örneğin <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Algılamayı açar</strong>: filament bitti anahtarını, tıkanma uzunluğu 0 değilse tıkanma algılamayı da.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Tüm algılamayı kapatır</strong>: anahtar ve tıkanma.</td></tr>
<tr><td><code>M412 D5</code></td><td>Anahtar filament görmediğinde, sensör ile nozul arasında kalan filamenti kullanmak için duraklatmadan önce <strong>5 mm</strong> daha baskıya devam eder. Varsayılan 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Tıkanma algılamayı açar</strong> (yalnızca BTT sensörü): sensörün tekerleği dönmeden ekstrüderden <strong>10 mm</strong> filament geçtiğinde baskıyı duraklatır.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Tıkanma algılamayı kapatır</strong>, filament bitti anahtarına dokunmaz. Varsayılan budur.</td></tr>
<tr><td><code>M500</code></td><td>Ayarları kaydeder. Bu komut olmadan, yazıcı kapatılınca değişiklik kaybolur.</td></tr>
<tr><td><code>M119</code></td><td><em>filament</em> satırı filament takılıyken <code>TRIGGERED</code>, takılı değilken <code>open</code> gösterir.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code> ve tek başına kullanılan <code>L</code>, bu firmware'lere dahil edilen Marlin değişikliğimizden
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>) gelir. Bu değişiklik olmayan Marlin'de tek başına <code>L</code>
yok sayılır ve <code>L0</code> baskıyı hemen tıkanma varmış gibi duraklatır.</p>

<h2>Wanhao'nun filament bitti anahtarı</h2>
<p>Firmware'e filamentin olup olmadığını bildirir. Filament bittiğinde baskı 5 mm daha filament kullandıktan sonra
duraklar ve ekran bir filament değişimi başlatır.</p>
<p><strong>v2.0.8'den beri her modelde varsayılan olarak açıktır.</strong> D8'e hiçbir şey takılı değilken kartın pull-up
direnci pini 5 V'ta tutar ve bu “filament var” olarak okunur: algılama bu durumda hiç tetiklenmez, bu yüzden sensör
takılı olsun ya da olmasın açık kalabilir. D8'e bir filament bitti anahtarı takın, hemen çalışır.</p>
<ul>
<li>Tıkanma algılama kapalı kalır (<code>L0</code>): bu anahtar filamentin hareket ettiğini göremez.</li>
<li>Anahtarı kapatmak için: <code>M412 S0</code> ve ardından <code>M500</code>.</li>
<li>Önceki bir sürümün kaydettiği ayarlar açık/kapalı durumunu korur. Açmak için: <code>M412 S1</code> ve ardından
<code>M500</code>, ya da varsayılanlara sıfırlayın (<code>M502</code> ve ardından <code>M500</code>; bu, prob Z
ofsetinizi ve mesh'inizi de siler).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Bu sensörün iki çıkışı vardır ve firmware bunları farklı şekilde okur:</p>
<ul>
<li><strong>Filament bitti anahtarı</strong> (D8'e) bir seviye verir: filament varken 5 V, filament bitince 0 V.</li>
<li><strong>Hareket çıkışı</strong> (D9'a), filament geçerken döndürdüğü küçük bir tekerlekten gelir. Her birkaç
milimetre filamentte çıkış 0 V ile 5 V arasında değişir. Firmware yalnızca bu değişimleri izler: ekstrüder tek bir
değişim olmadan tıkanma uzunluğu kadar filament iterse filament takip etmiyordur (dolaşmış makara, tıkanma, dişlinin
yediği filament) ve baskı duraklar. Filament bitti anahtarı bunu göremez: tıkanma sırasında filament hâlâ oradadır.</li>
</ul>
<h3>Kablolama</h3>
<p><strong>5V</strong> ucunu 5V'a, <strong>GND</strong> ucunu GND'ye, <strong>filament bitti anahtarı</strong> sinyalini <strong>D8</strong>
pinine ve <strong>hareket</strong> sinyalini <strong>D9</strong> pinine bağlayın. Sensörün kablosunda yazan adlar farklı olabilir.</p>
<h3>Açmak</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Baskılar sebepsiz yere duraklıyorsa tıkanma uzunluğunu artırın: <code>M412 L15</code> ve ardından <code>M500</code>. Yalnızca
filament bitti anahtarını kullanmak için: <code>M412 L0</code> ve ardından <code>M500</code>.</p>
<h3>Kontrol etmek</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li>Filament takılıyken <code>M119</code>: <em>filament: TRIGGERED</em>. Bu satır filamenti takıp çıkardığınızda değil de
elle ittiğinizde değişiyorsa, iki sinyal kablosu yer değiştirmiştir: D8 ile D9'u yer değiştirin.</li>
</ul>
<div class="note">Tıkanma algılama, sensör olmadan bir MK2 300 üzerinde test edildi (2 mm'lik tıkanma uzunluğu tetikler, <code>L0</code> hiç
tetiklemez), ama henüz BTT sensörünün kendisiyle test edilmedi. Anahtar ters okuyorsa (filament takılıyken <em>open</em>),
bize <a href="{DISCORD}">Discord</a> üzerinden bildirin.</div>

<h2>v2.0.5 veya v2.0.6'dan güncelleme</h2>
<p>Bu sürümlerde tıkanma algılamayı kapatmanın bir yolu yoktu, bu yüzden asla ulaşılamayacak kadar uzun bir tıkanma
uzunluğu kullanıyorlardı: v2.0.5'te 100 m (aslında fazla kısa: 1 kg'lık bir makaranın yaklaşık üçte biri; bu miktardan
sonra açık bırakılmış bir yazıcı boş yere duraklayabiliyordu) ve v2.0.6'da 10 km. Yazıcı açılırken v2.0.7 bu iki değeri
<code>L0</code> olarak yükler. BTT sensörü için ayarladığınız gerçek bir uzunluk, örneğin <code>L10</code>, korunur. v2.0.4
veya daha eski bir sürümden gelindiğinde, bu sürümlerin kaydettiği 0 yerine 5 mm'lik filament bitti mesafesi yüklenir.</p>
""")

    if page == "slicer":
        return ("Wanhao Duplicator 9 için Cura, OrcaSlicer ve Simplify3D profilleri ve Z ofseti ayarı",
                "Her Wanhao D9 için hazır UltiMaker Cura, OrcaSlicer ve Simplify3D profilleri, PLA, PETG ve ABS, probun Z ofseti "
                "nasıl ayarlanır, tabla nasıl ölçülür ve test için 3DBenchy nasıl basılır.",
                f"""
<h1>Duplicator 9 için dilimleme</h1>
<p class="lead">On iki yazıcının her biri için bir profil, <strong>UltiMaker Cura</strong> ve
<strong>OrcaSlicer</strong> için; ikisi de ücretsiz ve Windows, macOS ve Linux'ta çalışıyor. Zaten sahipseniz
<strong>Simplify3D</strong> için de var. Her profil kendi firmware'inin baskı hacmini, ivmelerini ve en yüksek tabla
sıcaklığını içerir.</p>

<h2>İndirme</h2>
{h.slicer}
<p>Bu sitedeki firmware için hazırlandılar: <a href="{p('flash')}">v2.0.9 veya daha yeni</a>.</p>

<h2>Kurulum</h2>
<p><strong>OrcaSlicer</strong>: <em>Dosya</em> → <em>İçe aktar</em> → <em>Yapılandırmaları içe aktar…</em>, ardından
<code>.orca_printer</code> dosyasını seçin. Yazıcı, üç kalitesi (0,12 / 0,20 / 0,28 mm) ve PLA, PETG ve ABS
filamentleri ön ayarlarınızın arasında görünür.</p>
<p><strong>Cura</strong>: <em>Yardım</em> → <em>Yapılandırma klasörünü göster</em>, Cura'yı kapatın, dosyayı bu klasörün
içine açın, Cura'yı yeniden başlatın, sonra <em>Ayarlar</em> → <em>Yazıcı</em> → <em>Yazıcı ekle…</em> → <em>Ağa bağlı
olmayan bir yazıcı ekle</em> → <em>Wanhao</em> → modeliniz. Cura ile birlikte gelen <em>Wanhao Duplicator 9</em> daha
eski bir profildir: yalnızca 300 boyutu, radye ve destekler varsayılan olarak açık.</p>
<p><strong>Simplify3D</strong> (sürüm 5, ücretli): <em>File</em> → <em>Import Printer Profiles…</em>,
ardından <code>.fff</code> dosyasını seçin. Yazıcı, üç kalitesi (0,30 / 0,20 / 0,10 mm) ve PLA, PETG ve ABS
malzemeleriyle birlikte, ayarların üstündeki <em>Auto-Configure</em> listelerinde görünür.</p>

<h2 id="first-print">İlk baskıdan önce: Z ofseti, sonra bir ölçüm</h2>
<p>Prob tablanın biraz üstünde tetiklenir ve firmware'in bunun ne kadar olduğunu bilmesi gerekir. İşte bu
<strong>Z ofsetidir</strong>. Çok yüksek olursa ilk katman tutmaz; çok alçak olursa nozul tablayı çizer. Bir kez
ayarlanır ve baskılarınızın yapışıp yapışmayacağına karar veren ayar odur.</p>
<div class="note">Aşağıdakilerin tamamı dilimleyicide değil, yazıcının belleğinde saklanır. Firmware güncellemesinden
sonra da orada kalır (v2.0.3'ten beri).</div>

<h3>1. Önce ısıtın</h3>
<p>Sıcak bir nozul, birkaç yüzde milimetre daha uzundur. Baskıdaki gibi ısıtın: ekranda <em>Sıcaklık</em> →
<em>Ön ısıtma</em> → <em>PLA</em> (200 °C ve 60 °C) ve birkaç dakika bekleyin.</p>

<h3>2. Eksenleri sıfırlayın</h3>
<p>Ekranda: <em>Ayarlar</em> → <em>Hareket</em> → <em>Sıfırla</em>. USB üzerinden: <code>G28</code>.</p>

<h3>3. Z ofsetini ayarlayın</h3>
<p><strong>En kolayı, baskı sırasında.</strong> Bir baskı başlatın ve <strong>ilk katman</strong> basılırken ekranda
<em>Ayarla</em> → <em>Z ofseti</em> sayfasına gidin. Çizgi çizilirken 0,01 mm'lik adımlarla indirin; çizgi yassılaşıp
komşusuna boşluk bırakmadan değene kadar. Çok yüksekse çizgiler yuvarlak ve ayrı kalır; çok alçaksa yüzey pürüzlü ve
ezik olur, nozulun kazıdığı görülür. Değer kendiliğinden kaydedilir.</p>
<p><strong>Kâğıt yöntemi, baskı yapmadan.</strong> USB üzerinden, baskı sıcaklığında:</p>
<pre><code>M851 Z0     ; mevcut ofseti unut
M500
G28         ; hesaba katılması için yeniden sıfırla
M420 S0     ; ölçüm sırasında ağı yok say
M211 S0     ; Z0 altına inmeye izin ver: nozulu orada yazılım sınırları durdurur
G1 Z0 F300  ; nozul, firmware'in sıfır sandığı yere iner</code></pre>
<p>Nozulun altına bir kâğıt sürün, sonra <code>G91</code> ve ardından <code>G1 Z-0.05 F60</code> ile küçük adımlarla,
kâğıt ancak sürtmeye başlayana kadar tekrar tekrar indirin. Değeri <code>M114</code> ile okuyun: negatiftir, örneğin
−1,30. Sonra:</p>
<pre><code>G90
M851 Z-1.30 ; sizin değeriniz
M500
M211 S1     ; yazılım sınırlarını geri koy, tablayı onlar korur</code></pre>
<p>v2.1.1 ve sonrasında iki <code>M211</code> satırını atlayabilirsiniz: yazılım nozülün sıfırın 3 mm altına inmesine zaten izin verir.</p>

<h3>4. Tablayı ölçün</h3>
<p>Ekranda: <em>Ayarlar</em> → <em>Tabla ayarı</em> → <em>Otomatik</em> → <em>Ölç</em>. Yazıcı 25 nokta ölçer ve
<strong>ağı kendisi kaydeder</strong> (<code>G29</code> ve ardından <code>M500</code> çalıştırır). Birkaç dakika sürer.
USB üzerinden: <code>G29</code> sonra <code>M500</code>.</p>
<p>Profillerimiz her baskıdan önce ölçüm yapmaz: sıfırlamanın hemen ardından <code>M420 S1</code> ile kayıtlı ağı geri
açarlar. Bu yüzden yazıcıyı yerinden oynattığınızda, yüzeyi ya da nozulu değiştirdiğinizde veya ilk katman tablanın bir
tarafında iyi, öbür tarafında kötü olduğunda yeniden ölçüm yapın.</p>

<h3>5. Kontrol edin</h3>
<p><code>M503</code> kayıtlı olanları listeler: <code>M851</code> satırı sizin Z ofsetinizdir, <code>M420 S1</code> ise
ağın açık olduğunu gösterir. Ekranda <em>Otomatik</em> sayfası ölçülen 25 noktayı gösterir.</p>

<h2>Test baskıları</h2>
<p>İki dilimleyiciyi karşılaştırmak ya da hiçbir şey kurmadan bir ayarı denemek için, <strong>D9 MK2 300</strong> için
hazır dilimlenmiş bir 3DBenchy:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Her biri yaklaşık bir buçuk saat ve 4 m filament. Başka bir model ya da boyut için
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a>'yi kendi profilinizle kendiniz dilimleyin.</p>
<h3>Hepsi bir arada test</h3>
<p>Çıkıntı çubukları, bir köprü, stringing kuleleri, tolerans delikleri ve bir incelik ölçeği; hepsi 65 mm'lik tek bir
parçada, yaklaşık 2 h 30. Bu, <strong>majda107</strong> tarafından hazırlanan
<a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> (CC BY 4.0); <strong>her yazıcı</strong>
ve iki dilimleyici için, üç malzemede dilimlendi. <a href="{REPO}/releases/latest">En son sürümdeki</a> dosyaların adı
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code> biçimindedir, örneğin
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="Wanhao D9 MK2 300'de OrcaSlicer profiliyle basılmış 3DBenchy"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="Wanhao D9 MK2 300'de Cura profiliyle basılmış 3DBenchy"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="dustovich tarafından Wanhao D9'da PETG ile basılmış 3DBenchy"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Hangisiyle başlamalı:</strong> PLA ile bir D9 MK2 300'de aynı Benchy <strong>OrcaSlicer ile 1 h 14</strong>,
<strong>Cura ile 1 h 22</strong> sürdü ve OrcaSlicer'ın duvarları biraz daha temiz çıktı. İkisi de iyi; biz
OrcaSlicer ile başlardık, ayrıca kalibrasyon araçları (akış, pressure advance, sıcaklık kuleleri) daha fazlasını
istediğinizde işinize yarar.</p>
<div class="note">D9 açık bir yazıcıdır: ABS en azından hava akımı olmayan bir oda ister ve tabla sıcaklığı,
modelinizin kabul ettiği değere düşürülür (MK3 500'de 80 °C).</div>

<h2>Profillerin içinde ne var</h2>
<ul>
<li><strong>Katmanlar</strong> 0,20 mm, <strong>3 duvar</strong>, üstte 4, altta 3 dolu katman, %15 gyroid dolgu,
2 hatlık etek, destek yok.</li>
<li><strong>Hızlar</strong>: dış duvarda 40 mm/s, içeride 60, dolguda 70, ilk katmanda 20, boş harekette 150. Wanhao,
D9'un en yüksek baskı hızını 70 mm/s olarak veriyor.</li>
<li><strong>Geri çekme</strong> 25 mm/s'de 1,5 mm: her D9'da doğrudan tahrikli MK10 ekstrüder vardır ve firmware
ekstrüderi 25 mm/s ile sınırlar.</li>
<li><strong>Sıcaklıklar</strong>: PLA 210 °C sonra 205, tabla 65 sonra 60. PETG 240 / 80 sonra 235 / 75. ABS 245 / 105
sonra 245 / 100.</li>
<li><strong>Bir hazırlık çizgisi</strong>, sol kenardan 15 mm içeride ve tabla klipslerinin dışında: nozul parçaya
temiz gelir.</li>
<li>Sonunda nozul yükselir ve tabla öne gelir.</li>
</ul>
<p>Tüm ayarlar ve nasıl değiştirilecekleri: GitHub'da <a href="{REPO}/tree/main/Slicer">Slicer klasörü</a>.</p>
""")

    if page == "quiet":
        return ("Wanhao Duplicator 9'u sessizleştirmek: hangi fanlar ve NTC termistörlü anakart fanı",
                "Wanhao D9'un hangi fanları sessizleştirilebilir: hotend fanı kalmalı, güç kaynağı fanı zaten kendini "
                "ayarlıyor, anakart fanının ise fişi çekilebilir ya da NTC termistörlerle çalıştırılabilir.",
                f"""
<h1>Duplicator 9'u daha sessiz hale getirmek</h1>
<p class="lead">Boştayken D9'un gürültüsü fanlarından gelir. Hangisinin sessizleştirilebileceği ve nasıl yapılacağı aşağıda.</p>
<div class="note">Yazıcının <strong>fişi çekiliyken</strong> çalışın. Tüm kabloları 230 V tarafından uzak tutun.</div>

<h2>Fanlar</h2>
<div class="table"><table class="stack"><thead><tr><th>Fan</th><th>Kontrol eden</th><th>Sessizleştirilebilir mi?</th></tr></thead><tbody>
<tr><td><strong>Hotend soğutucu fanı</strong> (baskı kafası)</td><td>hiçbir şey: 24 V, sürekli açık</td><td><strong>hayır</strong>: genellikle en gürültülüsüdür, ama yavaşlatılırsa ısı hotend boyunca yukarı çıkar ve filamenti tıkar (heat creep)</td></tr>
<tr><td><strong>Parça soğutma fanı</strong> (baskı kafası)</td><td>firmware, D5 pini (PWM)</td><td>zaten değişken hızlı: dilimleyici ve <code>M106</code> ile ayarlanır</td></tr>
<tr><td><strong>Güç kaynağı fanı</strong></td><td>güç kaynağının kendisi</td><td>yapılacak bir şey yok: burada incelenen ünitede (Chuanglian A-350FAK-24) zaten güç kaynağının sıcaklığını takip ediyor</td></tr>
<tr><td><strong>Anakart fanı</strong> (kontrol kutusu)</td><td>hiçbir şey: 24 V, sürekli açık</td><td><strong>evet</strong>, aşağıya bakın</td></tr>
</tbody></table></div>
<p>Wanhao'nun firmware'i ne anakart fanını ne de hotend fanını kontrol eder (<code>CONTROLLER_FAN_PIN</code> ve
<code>E0_AUTO_FAN_PIN</code> ikisi de <code>-1</code>) ve kartta boşta anahtarlamalı bir çıkış yoktur. Bu ikisinin sürekli
açık “24V OUT” konnektörlerinden beslenmesinin ve hiçbir firmware'in onları yavaşlatamamasının nedeni budur.</p>

<h2>Anakart fanı</h2>
<p>Burada ölçülen ünitede: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, en fazla 0,10 A, kaymalı yatak</strong>.</p>
<p><strong>Birçok kullanıcı bu fanın fişini düpedüz çekiyor.</strong> Kart serin çalışır: kontrol kutusunun en altında, ısıtmalı
tablanın altında durur ve tablanın ısısı ondan uzağa, yukarı doğru yükselir. Bunu yaparsanız ilk uzun baskılarınızı
yakından izleyin: aşırı ısınan bir step motor sürücüsü kısa süreliğine devre dışı kalır; bu da bir hata mesajı olarak
değil, <strong>katman kayması</strong> olarak ortaya çıkar.</p>
<h3>Fanı tutmak, ama yalnızca sürücüler ısındığında çalıştırmak</h3>
<p>Seri bağlı iki güç NTC termistörü, fanın 45–50 °C civarında çalışmaya başlamasını ve sürücüler ısındıkça hızlanmasını
sağlar: <strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), termal yapıştırıcıyla bir sürücü
soğutucusuna yapıştırılmış, bacakları yalıtılmış.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V</code></pre>
<ul>
<li>Bu bir hesaplamadır, <strong>henüz bir yazıcıda test edilmedi</strong>: MF72 toleransı ±%20'dir ve küçük bir fan
beklenenden düşük sıcaklıkta çalışmaya başlayabilir. Başlama sıcaklığını tezgâhta kontrol edin (NTC'ler küçük bir poşet
içinde sıcak suda, yanında bir mutfak termometresiyle); çok erken başlarsa ikinci bir 200 Ω ekleyin, çok geç başlarsa
200 Ω'u çıkarın.</li>
<li>NTC'ler bir soğutucuya yapıştırılmalıdır: açık havada fan akımı (NTC'lerde yaklaşık 0,6 W'a kadar) onları onlarca
derece ısıtır.</li>
<li>Fan bu şekilde hiçbir zaman tam hıza ulaşmaz (80 °C'de yaklaşık %75) ve arızalanan bir NTC açık devre olur: fan da
kalıcı olarak durur.</li>
</ul>
<p>Kaynaklar: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 veri sayfası</a>.</p>
""")
    raise KeyError(page)
