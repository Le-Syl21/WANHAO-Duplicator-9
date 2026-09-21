"""Polski: translation of en.py."""

META = {"name": "Polski", "locale": "pl_PL", "dir": "ltr"}

UI = {
    "nav": {"index": "Strona główna", "mk1": "MK1", "mk1u2": "MK1 + zestaw MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Wgrywanie firmware'u", "screen": "Ekran", "sensor": "Czujnik filamentu", "slicer": "Slicer",
            "quiet": "Wyciszanie"},
    "language": "Język",
    "model": "Model",
    "size": "Rozmiar", "volume": "Pole robocze", "file": "Firmware",
    "footer_src": "Kod źródłowy i zgłoszenia na GitHubie", "footer_chat": "Discord",
    "footer_note": "Firmware na licencji GNU GPL v3. Instrukcje i firmware Wanhao pozostają własnością Wanhao.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Płyta główna Wanhao D9 (widok z góry)",
    "plug": "złącze czujnika",
    "switch": "koniec filamentu",
    "motion": "ruch",
    "level": "poziom: filament jest / brak",
    "pulses": "impulsy, gdy filament się przesuwa",
    "names": "nazwy na Twoim czujniku mogą być inne",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Aktualny firmware Marlin dla każdej drukarki Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "pliki ekranu, oryginalny firmware i instrukcje Wanhao oraz sposób ich wgrania.",
                f"""
<h1>Firmware do Wanhao Duplicator 9</h1>
<p class="lead">Strona Wanhao z plikami do pobrania dla Duplicatora 9 już nie istnieje. Wszystko, czego potrzebuje właściciel D9,
jest teraz tutaj: aktualny firmware Marlin 2.1 dla każdego modelu i rozmiaru, pasujące pliki ekranu dotykowego, oryginalny
firmware Wanhao, instrukcje Wanhao oraz poradniki wgrywania krok po kroku.</p>
<p><a class="btn" href="{REPO}/releases/latest">Wszystkie pliki do pobrania</a> <a class="btn ghost" href="{DISCORD}">Zapytaj na Discordzie</a></p>

<h2>Którą wersję D9 mam?</h2>
<div class="split"><div>
<ol>
<li><strong>Szara płaska taśma</strong> biegnąca do głowicy drukującej i <strong>metalowy cylindryczny czujnik</strong>
obok dyszy, brak bocznych wzmocnień ramy: <a href="{p('mk1')}">MK1</a>.</li>
<li>Ta sama maszyna pierwszej generacji z <strong>białym czujnikiem BLTouch</strong> zamiast metalowego:
MK1 z zestawem modernizacyjnym Wanhao, <a href="{p('mk1u2')}">MK1 + zestaw MK2</a>.</li>
<li><strong>Skośne żebra wzmacniające</strong> po obu stronach ramy, <strong>okrągły czarny kabel</strong>
do głowicy i BLTouch: MK2 albo MK3. Zajrzyj pod stół i znajdź <strong>silnik osi Y</strong>, czyli ten, który
przesuwa stół: jeśli jest z tyłu, to <a href="{p('mk2')}">MK2</a>; jeśli z przodu, od strony ekranu dotykowego, to
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>Liczba po D9 oznacza rozmiar: D9/300, D9/400 lub D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 z bocznymi żebrami wzmacniającymi">
<figcaption>D9 MK2: boczne żebra, okrągły kabel</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Czujnik indukcyjny, taśma. Firmware, Wanhao od V0.15 do V0.164(B), instrukcja.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + zestaw MK2</h3><p>MK1 zmodernizowana zestawem BLTouch. Firmware i Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware do zestawu →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, boczne żebra. Firmware, Wanhao V1.1.2, poradniki.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Silnik Y z przodu, czujnik filamentu. Firmware i Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>Co daje ten firmware</h2>
<ul>
<li><strong>Marlin 2.1</strong> zbudowany z konfiguracji dla Duplicatora 9 opublikowanych w
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
z zaproponowanymi tam zmianami: czujnik MK1 odczytywany we właściwą stronę, kierunek osi Y w MK3, wznawianie po zaniku zasilania,
filtr zakłóceń krańcówek.</li>
<li><strong>Fabryczne ustawienia Wanhao</strong>, wzięte z firmware'u i kodu źródłowego Wanhao dla każdego modelu: kroki/mm,
prędkości, przyspieszenia, PID hotendu, offsety czujnika i marginesy sondowania, bazowanie, limity temperatur, jerk i kierunki osi.</li>
<li><strong>Wznawianie po zaniku zasilania</strong>: podczas druku z karty SD zadanie jest zapisywane przy każdej zmianie warstwy, a po zaniku prądu ekran proponuje wznowienie od tego miejsca.</li>
<li><strong>Czujniki filamentu</strong>: czujnik końca filamentu na D8, domyślnie włączony w każdym modelu (bez czujnika nic nie robi), oraz BTT Smart Filament Sensor V2.0, który wykrywa też zatory. Zobacz <a href="{p('sensor')}">Czujnik filamentu</a>.</li>
<li><strong>Głowica wraca na środek po poziomowaniu stołu</strong>, więc stół nie zasłania już ekranu.</li>
<li><strong>Nowy interfejs ekranu dotykowego w 16 językach</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, ze stroną do ustawiania czujnika filamentu.</li>
</ul>

<h2>Wgrywanie w trzech krokach</h2>
<ol>
<li>Pobierz plik <strong>.hex</strong> dla swojego modelu i rozmiaru z jego strony.</li>
<li>Wgraj go przez USB za pomocą AVRDUDESS lub avrdude: <a href="{p('flash')}">poradnik wgrywania</a>.</li>
<li>Wgraj pliki ekranu dotykowego z karty microSD: <a href="{p('screen')}">poradnik ekranu</a>.</li>
</ol>
<p>Oryginalny firmware Wanhao pozostaje dostępny na stronie każdego modelu, więc maszynę zawsze można przywrócić do stanu fabrycznego.</p>
""")

    if page == "mk1":
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 do Wanhao D9 MK1 z czujnikiem indukcyjnym, oryginalny firmware Wanhao od V0.15 do V0.164(B), "
                "pliki ekranu i instrukcja obsługi MK1.",
                f"""
<h1>Firmware do Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">Pierwszy Duplicator 9: metalowy czujnik indukcyjny obok dyszy, szara taśma do głowicy
drukującej i rama bez bocznych żeber.</p>
<p>Te wersje odczytują czujnik indukcyjny we właściwą stronę (zadziałanie to stan LOW) i przejmują ustawienia
ostatniego firmware'u Wanhao dla MK1, V0.164(B), łącznie z offsetami czujnika (X 15, Y 0). Silnik osi Y jest z tyłu, tak jak zamontował go Wanhao.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Czujnik indukcyjny i taśma na głowicy drukującej Wanhao D9 MK1">
<figcaption>MK1: czujnik indukcyjny, taśma</figcaption></figure></div>

<h2>Pobieranie</h2>
{dl("MK1")}
<p>Wybierz plik dla swojego rozmiaru, a potem wgraj pliki ekranu z
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumenty Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Instrukcja obsługi D9 MK1</a> (czerwiec 2018, po angielsku): montaż, okablowanie, menu, poziomowanie, rozwiązywanie problemów.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Skrócony przewodnik D9 MK1</a>.</li>
</ul>

<h2>Oryginalny firmware Wanhao</h2>
<p>Pozwala przywrócić maszynę do stanu fabrycznego. Każda wersja firmware'u płyty głównej działa tylko z firmware'em ekranu
w tej samej wersji.</p>
<div class="table"><table><thead><tr><th>Wersja</th><th>Rozmiar</th><th>Płyta główna</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ustawienia każdej wersji (kroki/mm, prędkości, PID, kierunki osi) są wypisane w
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, odczytane z plików binarnych Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware Wanhao Duplicator 9 MK1 z zestawem modernizacyjnym MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 do Wanhao D9 MK1 zmodernizowanej zestawem BLTouch MK2 od Wanhao oraz oryginalny firmware Wanhao V1.1.31 do zestawu.",
                f"""
<h1>Wanhao D9 MK1 z zestawem modernizacyjnym MK2</h1>
<div class="split"><div>
<p class="lead">D9 pierwszej generacji z zestawem modernizacyjnym MK2 od Wanhao: rama MK1, a zamiast metalowego czujnika
indukcyjnego czujnik BLTouch.</p>
<p>Wanhao wydał osobny firmware dla tego połączenia, bo BLTouch z zestawu nie jest zamontowany w tym samym miejscu co
w fabrycznej MK2: offset Y czujnika jest inny. Te wersje używają geometrii zestawu. Silnik osi Y jest
z tyłu.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Czujnik BLTouch na głowicy drukującej Wanhao D9">
<figcaption>Czujnik BLTouch</figcaption></figure></div>

<h2>Pobieranie</h2>
{dl("MK1u2")}
<p>Wybierz plik dla swojego rozmiaru, a potem wgraj pliki ekranu z
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Te wersje używają offsetu czujnika z firmware'u zestawu, Y −10. To jedyna linia, w której kod źródłowy
zestawu Wanhao różni się od fabrycznej MK2 (Y 0): BLTouch z zestawu jest przesunięty bardziej do tyłu. Jeśli siatka stołu wygląda
na przesuniętą w osi przód–tył, zmierz własny offset według <a href="{REPO}/blob/main/Offset.md">poradnika offsetu</a>.</div>

<h2>Oryginalny firmware Wanhao</h2>
<p>Firmware Wanhao V1.1.31 do zestawu (grudzień 2018), używany z firmware'em ekranu MK2.</p>
<div class="table"><table><thead><tr><th>Rozmiar</th><th>Płyta główna</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ustawienia odczytane z plików binarnych Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 do Wanhao D9 MK2 z BLTouch, oryginalny firmware Wanhao V1.1.2 z plikami ekranu oraz poradniki Wanhao do MK2.",
                f"""
<h1>Firmware do Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">Drugi Duplicator 9: skośne żebra wzmacniające po obu stronach, okrągły czarny kabel danych do
głowicy drukującej, czujnik BLTouch i uchwyt na szpulę na górze.</p>
<p>Wanhao zmienił też wózki na czterokołowe, a w wersjach 400 i 500 zamontował oś Y na podwójnej prowadnicy i grubszy pasek,
w wersjach 300 i 400 zaś dwustronny stół. Silnik osi Y jest z tyłu; te wersje obracają oś Y
tak samo jak firmware Wanhao V1.1.2.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Pobieranie</h2>
{dl("MK2")}
<p>Wybierz plik dla swojego rozmiaru. MK2, w której głowicę zmodernizowano także do MK3, powinna
używać <a href="{p('mk3')}">firmware'u MK3</a>. Następnie wgraj pliki ekranu z <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Dokumenty Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Skrócony przewodnik D9 MK2</a> (po angielsku).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">12 ulepszeń od MK1 do MK2</a>, opracowanie Wanhao.</li>
</ul>

<h2>Oryginalny firmware Wanhao</h2>
<p>Wersja V1.1.2 od Wanhao (październik 2018; dla modelu 500 przebudowana jako V1.1.2.1 w lipcu 2019), z firmware'em ekranu MK2 od Wanhao.</p>
<div class="table"><table><thead><tr><th>Rozmiar</th><th>Płyta główna</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ustawienia odczytane z plików binarnych Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 do Wanhao D9 MK3 (silnik Y z przodu, czujnik filamentu) oraz oryginalny firmware Wanhao V1.1.3.",
                f"""
<h1>Firmware do Wanhao Duplicator 9 MK3</h1>
<p class="lead">Ostatni Duplicator 9 zachowuje ramę i BLTouch z MK2, dodaje czujnik końca filamentu i przenosi
silnik osi Y do przodu, na stronę ekranu dotykowego.</p>
<p>Przeniesienie silnika odwraca oś Y: firmware Wanhao V1.1.3 odwraca Y i te wersje robią to samo.
Czujnik końca filamentu jest domyślnie włączony. Wanhao nie opublikował offsetów czujnika dla MK3, więc te wersje używają
offsetów z MK2.</p>

<h2>Pobieranie</h2>
{dl("MK3")}
<p>Wybierz plik dla swojego rozmiaru, a potem wgraj pliki ekranu z
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Jeśli czujnik filamentu przerywa wydruki losowo, wyłącz go poleceniem <code>M412 S0</code>, a potem
<code>M500</code>. Wanhao Europe opublikował kiedyś firmware MK3 „ReverseMode” na ten problem; później został
usunięty i nie udało się go odnaleźć.</div>

<h2>Oryginalny firmware Wanhao</h2>
<p>Wersja V1.1.3 od Wanhao (sierpień 2019). Wanhao nie opublikował firmware'u ekranu dla MK3: pliki do pobrania dla MK3 odsyłały do tego z MK2.</p>
<div class="table"><table><thead><tr><th>Rozmiar</th><th>Płyta główna</th><th>Ekran</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Ustawienia odczytane z plików binarnych Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Jak wgrać firmware płyty głównej do Wanhao Duplicator 9 (D9)",
                "Poradnik krok po kroku: wgrywanie Marlina do Wanhao D9 przez USB za pomocą AVRDUDESS lub avrdude, rozwiązywanie "
                "problemów z bazowaniem i powrót do firmware'u Wanhao.",
                f"""
<h1>Wgrywanie firmware'u płyty głównej Duplicatora 9</h1>
<p class="lead">Płyta główna D9 to ATmega2560 z bootloaderem USB: bez programatora, bez otwierania podstawy,
wystarczy kabel USB.</p>

<h2>Czego potrzebujesz</h2>
<ul>
<li>Kabla USB między drukarką a komputerem oraz <strong>włączonej</strong> drukarki.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, graficzny, najprostszy) lub
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (wiersz poleceń, każdy system).</li>
<li>Pliku <strong>.hex</strong> dla swojego modelu i rozmiaru: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + zestaw</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Przed wgraniem</h2>
<div class="note">Wyślij <code>M503</code> i zachowaj odpowiedź. Od v2.0.3 aktualizacja zachowuje ustawienia zapisane w
drukarce, ale aktualizacja <strong>do</strong> v2.0.3 jednorazowo startuje od domyślnych wartości tego firmware'u (zmienił się
sposób zapisu ustawień); tak samo przy przejściu z firmware'u Wanhao. Potem ustaw ponownie offset Z czujnika poleceniem <code>M851 Z…</code>
i <code>M500</code>.</div>
<p>Zamknij wszystkie programy, które mogą zajmować port drukarki: Cura, PrusaSlicer, OctoPrint, Pronterface, terminale szeregowe.</p>

<h2>Wgrywanie za pomocą AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: port COM drukarki (na przykład <code>COM3</code>). Prędkość (baud rate) zostaw domyślną.</li>
<li>Flash: wybierz plik .hex, a potem kliknij <strong>Program!</strong>. Trwa to od 30 do 60 sekund.</li>
</ol>

<h2>Wgrywanie za pomocą avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Zastąp port i nazwę pliku własnymi. Protokół <code>wiring</code> sam dobiera prędkość bootloadera.</p>

<h2>Pierwsze uruchomienie</h2>
<ol>
<li>Odłącz kabel USB, wyłącz i włącz drukarkę, podłącz kabel z powrotem.</li>
<li>Połącz się z prędkością <strong>250000 bodów</strong> (firmware Wanhao używał 115200) i wyślij <code>M115</code>: odpowiedź pokaże nowy firmware.</li>
<li>Zbazuj wszystkie osie, potem wykonaj poziomowanie stołu z ekranu lub poleceniem <code>G29</code> i zapisz przez <code>M500</code>.</li>
</ol>

<h2 id="reset">Powrót do domyślnych ustawień tego firmware'u</h2>
<p>Od v2.0.3 aktualizacja firmware'u <strong>zachowuje</strong> ustawienia zapisane w drukarce (offset Z czujnika, kroki/mm,
PID, siatkę…). Nowe wartości domyślne z danego wydania nie zastępują więc tych już zapisanych. Zresetuj ustawienia raz, gdy
aktualizujesz z v2.0.2 lub starszej i masz wartości zapisane ręcznie, gdy drukarka zachowuje się dziwnie po testowaniu innych
firmware'ów albo zawsze, gdy chcesz zacząć od czystej karty:</p>
<ul>
<li><strong>Na ekranie:</strong> <em>Ustawienia</em> → <em>Więcej</em> → <em>Resetuj</em> → ✓.</li>
<li><strong>Przez USB:</strong> wyślij <code>M502</code> (wczytuje domyślne wartości tego firmware'u), a potem <code>M500</code> (zapisuje je).</li>
</ul>
<p>Następnie ustaw ponownie offset Z czujnika (<code>M851 Z…</code>, potem <code>M500</code>) i wykonaj poziomowanie stołu. Sprawdź
wynik poleceniem <code>M503</code>.</p>

<h2>Zanik zasilania i czujnik filamentu</h2>
<ul>
<li>Wznawianie po zaniku zasilania jest włączone: zadanie jest zapisywane przy każdej zmianie warstwy. Wyłączysz je poleceniem <code>M413 S0</code>, a potem <code>M500</code>.</li>
<li>Wydruk zatrzymuje się od razu z komunikatem <em>power outage</em>, gdy tylko zaczyna grzać: zaktualizuj do v2.0.4 lub nowszej. Wcześniejsze wersje obserwowały wejście wykrywania zaniku zasilania na płycie, które pokazuje stan niski, gdy tylko włączą się grzałki.</li>
<li>Wykrywanie końca filamentu jest domyślnie włączone w każdym modelu od v2.0.8 i bez czujnika nic nie robi. Po aktualizacji z wcześniejszego wydania włącz je poleceniem <code>M412 S1</code>, a potem <code>M500</code>, albo na ekranie w <em>Ustawienia</em> → <em>Filament</em> → <em>Czujnik filamentu</em>. Podłączenie i BTT Smart Filament Sensor: <a href="{p('sensor')}">Czujnik filamentu</a>.</li>
</ul>

<h2>Rozwiązywanie problemów</h2>
<div class="table"><table><thead><tr><th>Problem</th><th>Rozwiązanie</th></tr></thead><tbody>
<tr><td>Port zajęty</td><td>Zamknij wszystkie programy używające portu drukarki.</td></tr>
<tr><td>Nie znaleziono urządzenia</td><td>Zainstaluj sterownik USB CH340, spróbuj innego kabla lub portu USB, sprawdź, czy drukarka jest włączona.</td></tr>
<tr><td>Nieczytelne znaki po wgraniu</td><td>Używaj 250000 bodów z tym firmware'em, 115200 z firmware'em Wanhao.</td></tr>
<tr><td>Temperatury na ekranie ×10 (236 zamiast 23,6 °C)</td><td>Ekran ma jeszcze stare pliki: wgraj <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>Ekran przy każdym uruchomieniu wraca do angielskiego albo jego strona <em>Czujnik filamentu</em> nic nie robi</td><td>Firmware płyty głównej jest starszy niż v2.0.9: zaktualizuj go.</td></tr>
<tr><td>Bazowanie zatrzymuje się kilka milimetrów przed krańcówką, a potem pojawia się <em>Homing Failed</em></td><td>Zakłócenia elektryczne na linii krańcówki. Ten firmware filtruje je od v2.0.1: zaktualizuj.</td></tr>
<tr><td>Dysza uderza w klips stołu podczas poziomowania</td><td>Zaktualizuj do v2.0.2 lub nowszej: pierwsza kolumna punktów pomiarowych jest 10 mm od krawędzi, jak w firmware'ze Wanhao.</td></tr>
<tr><td>Stół odjeżdża od krańcówki Y</td><td>Sprawdź, czy wgrałeś firmware dla swojego modelu: silnik osi Y jest z tyłu w MK1, MK1 + zestaw i MK2, a z przodu w MK3.</td></tr>
</tbody></table></div>

<h2>Powrót do firmware'u Wanhao</h2>
<p>Strona każdego modelu zawiera odnośniki do oryginalnego firmware'u Wanhao dla płyty głównej i ekranu. Wgrywa się go tak samo; firmware
płyty głównej Wanhao wymaga firmware'u ekranu Wanhao z tej samej generacji.</p>
<p>Pytania: <a href="{DISCORD}">Discord</a> lub <a href="{REPO}/issues">zgłoszenia na GitHubie</a>.</p>
""")

    if page == "screen":
        return ("Firmware ekranu dotykowego Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 w 16 językach",
                "Jak wgrać DGUS Reloaded 2.0 na ekran dotykowy DWIN w Wanhao D9 z karty microSD: nowy interfejs w 16 "
                "językach, strona czujnika filamentu, dla Marlina 2.1. Oraz jak wrócić do firmware'u ekranu Wanhao.",
                f"""
<h1>Wgrywanie firmware'u ekranu dotykowego Duplicatora 9</h1>
<p class="lead">Każdy D9, od MK1 do MK3, ma ten sam ekran dotykowy DWIN T5 (480 × 272). Z tym firmware'em działa na nim
DGUS Reloaded 2.0, nasz nowy interfejs w 16 językach, wgrywany z karty microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Pobierz DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>Co daje DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 języków</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Dotknij flagi obok nazwy drukarki na ekranie głównym,
aby zmienić język; drukarka zapamiętuje wybór.</li>
<li><strong>Strona czujnika filamentu</strong>: <em>Ustawienia</em> → <em>Filament</em> → <em>Czujnik filamentu</em>. Zobacz
<a href="{p('sensor')}#screen">Czujnik filamentu</a>.</li>
<li><strong>Pasek stanu, który nie znika</strong>: ostatni komunikat, na przykład <em>Ready</em>, zostaje na ekranie, zamiast
znikać po 30 sekundach.</li>
<li><strong>Wskaźniki temperatury</strong> dyszy i stołu z zaznaczoną temperaturą docelową.</li>
<li>Nowy wygląd wszystkich stron: ciemny motyw, większe przyciski, piktogramy w okienkach.</li>
</ul>
</div><figure><img src="{img}screen/pl-home.png" width="480" height="272" alt="Ekran główny DGUS Reloaded 2.0 na Wanhao D9: temperatury dyszy i stołu ze wskaźnikami, pasek stanu, przyciski Drukuj, Temperatura i Ustawienia">
<figcaption>Ekran główny</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 wymaga na płycie głównej firmware'u <strong>v2.0.9 lub nowszego</strong>. Z v2.0.8 lub starszym
język przy każdym uruchomieniu wraca do angielskiego, a strona czujnika filamentu nie działa: najpierw <a href="{p('flash')}">wgraj firmware
płyty głównej</a>.</div>

<h2>1. Sformatuj kartę microSD</h2>
<div class="note">FAT32 z rozmiarem jednostki alokacji <strong>4096 bajtów</strong>. Przy każdym innym rozmiarze ekran ignoruje kartę.</div>
<ul>
<li><strong>Windows</strong>: Windows 11 często nie chce formatować w FAT32; użyj <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
i ustaw rozmiar jednostki alokacji na 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (najpierw sprawdź urządzenie poleceniem <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (sprawdź poleceniem <code>diskutil list</code>).</li>
</ul>

<h2>2. Skopiuj pliki</h2>
<p>Rozpakuj <code>DWIN_SET.zip</code> i skopiuj cały folder <code>DWIN_SET</code> do katalogu głównego karty.</p>

<h2>3. Wgraj</h2>
<ol>
<li>Wyłącz drukarkę i odłącz ją od prądu.</li>
<li>Otwórz przód podstawy, aby dostać się do tyłu ekranu, gdzie jest jego gniazdo microSD.</li>
<li>Włóż kartę i włącz drukarkę. Po 10–30 sekundach ekran pokaże aktualizację; poczekaj, aż uruchomi się ponownie
normalnie, łącznie od 1 do 3 minut.</li>
<li>Wyłącz drukarkę, wyjmij kartę, zamknij podstawę.</li>
</ol>
<p><a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">Film Wanhao o aktualizacji ekranu D9</a> pokazuje, gdzie jest gniazdo.</p>

<h2>Skąd to się wzięło</h2>
<p>DGUS Reloaded 2.0 to strona po stronie przerysowany <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(autorstwa Desuuuu, a potem Neo2003). Kod źródłowy, program generujący pliki ekranu i tłumaczenia są
na <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHubie</a>. Błędne lub niezręczne słowo w Twoim języku? Napisz nam na
<a href="{DISCORD}">Discordzie</a> albo zgłoś problem (issue) na GitHubie.</p>
<p>Aby wrócić do DGUS Reloaded 1.0.3, na przykład z firmware'em starszym niż v2.0.9, wgraj w ten sam sposób
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a>.</p>

<h2>Powrót do ekranu Wanhao</h2>
<p>Firmware ekranu Wanhao działa tylko z firmware'em płyty głównej Wanhao. MK1: plik ekranu w odpowiedniej
wersji na <a href="{p('mk1')}">stronie MK1</a>. MK1 + zestaw, MK2 i MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Procedura jest taka sama.</p>
""")

    if page == "sensor":
        return ("Czujniki filamentu w Wanhao Duplicator 9: czujnik końca filamentu i podłączenie BTT Smart Filament Sensor",
                "Gdzie podłączyć czujnik filamentu na płycie głównej Wanhao D9 (D8, D9, GND, 5V), jak podłączyć BTT Smart "
                "Filament Sensor V2.0 i włączyć wykrywanie końca filamentu oraz zatorów poleceniem M412.",
                f"""
<h1>Czujniki filamentu</h1>
<p class="lead">Od v2.0.5 ten firmware obsługuje dwa rodzaje czujników: czujnik końca filamentu Wanhao oraz
BTT Smart Filament Sensor V2.0, który wykrywa też, gdy filament przestaje się przesuwać (splątana szpula, zator, filament
zmielony przez ekstruder). <strong>Wykrywanie końca filamentu jest domyślnie włączone w każdym modelu</strong>, a wykrywanie zatorów jest wyłączone.</p>

<h2>Złącze czujnika</h2>
<figure><img src="{img}d9-sensor-plug-pl.svg" width="760" height="440" alt="Płyta główna Wanhao D9: 4-pinowe złącze czujnika na lewo od POWER-DET, piny D9, D8, GND i 5V, podłączone do BTT Smart Filament Sensor V2.0"></figure>
<p>4-pinowe złącze na lewo od <strong>POWER-DET</strong>, pod złączami krańcówek, ma piny <strong>D9, D8, GND i 5V</strong>,
w tej kolejności. Nazwy pinów pochodzą ze schematu połączeń Wanhao, który znalazł i udostępnił dustovich na
<a href="{DISCORD}">Discordzie</a>; na spodzie płyty te same cztery piny są opisane jako CTRL, BTN, GND i VCC.</p>
<ul>
<li><strong>D8</strong> to wejście końca filamentu, które odczytuje firmware Wanhao.</li>
<li><strong>D9</strong> nie jest używany przez firmware Wanhao: nasze wersje odczytują na nim sygnał ruchu z czujnika BTT.</li>
</ul>
<div class="note">Drukarka musi być <strong>wyłączona</strong>, gdy cokolwiek podłączasz do płyty lub odłączasz.</div>

<h2 id="screen">Na ekranie</h2>
<div class="split"><div>
<p>Z DGUS Reloaded 2.0 na ekranie (firmware v2.0.9 lub nowszy): <em>Ustawienia</em> → <em>Filament</em> →
<em>Czujnik filamentu</em>.</p>
<ul>
<li><strong>Koniec filamentu</strong> włącza lub wyłącza całe wykrywanie, jak <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Wykrywanie zatoru</strong> włącza wykrywanie zatorów z długością ustawioną poniżej albo je wyłącza (<code>L0</code>).</li>
<li><strong>Długość zatoru</strong>: − i + zmieniają ją o 1 mm; dotknij liczby, aby ją wpisać.</li>
<li>Kropka <strong>Filament</strong> jest zielona, gdy czujnik końca filamentu wykrywa filament, i czerwona, gdy go nie wykrywa.</li>
<li>Zmiany działają od razu. <strong>Zapisz</strong> je zapamiętuje, jak <code>M500</code>. Strzałka wstecz wychodzi bez
zapisywania: przy następnym uruchomieniu wracają zapisane ustawienia.</li>
</ul>
</div><figure><img src="{img}screen/pl-sensor.png" width="480" height="272" alt="Strona czujnika filamentu w DGUS Reloaded 2.0: przełączniki wykrywania końca filamentu i zatoru, długość zatoru z przyciskami minus i plus, wskaźnik filamentu i przycisk Zapisz">
<figcaption>Ustawienia → Filament → Czujnik filamentu</figcaption></figure></div>

<h2>Polecenia M412</h2>
<p>Wszystko ustawia się przez USB z terminala szeregowego (Pronterface, terminal slicera lub OctoPrinta,
250000 bodów). Parametry można łączyć w jednym poleceniu, na przykład <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Polecenie</th><th>Co robi</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Pokazuje stan, na przykład <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Włącza wykrywanie</strong>: czujnik końca filamentu, a także wykrywanie zatorów, jeśli długość zatoru nie wynosi 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Wyłącza całe wykrywanie</strong>, końca filamentu i zatorów.</td></tr>
<tr><td><code>M412 D5</code></td><td>Gdy czujnik nie wykrywa już filamentu, drukuje jeszcze <strong>5 mm</strong> przed pauzą, aby zużyć filament pozostały między czujnikiem a dyszą. Domyślnie 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Włącza wykrywanie zatorów</strong> (tylko czujnik BTT): pauzuje, gdy przez ekstruder przejdzie <strong>10 mm</strong> filamentu, a kółko czujnika się nie poruszy.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Wyłącza wykrywanie zatorów</strong> i nie zmienia ustawienia czujnika końca filamentu. To ustawienie domyślne.</td></tr>
<tr><td><code>M500</code></td><td>Zapisuje ustawienia. Bez tego zmiana przepada po wyłączeniu drukarki.</td></tr>
<tr><td><code>M119</code></td><td>Linia <em>filament</em> pokazuje <code>TRIGGERED</code>, gdy filament jest załadowany, i <code>open</code>, gdy go nie ma.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code> oraz samo <code>L</code> pochodzą z naszej zmiany w Marlinie
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), wbudowanej w ten firmware. W Marlinie bez tej zmiany samo <code>L</code>
jest ignorowane, a <code>L0</code> od razu pauzuje wydruk jak przy zatorze.</p>

<h2>Czujnik końca filamentu Wanhao</h2>
<p>Informuje firmware, czy filament jest obecny. Gdy filamentu zabraknie, wydruk pauzuje po kolejnych 5 mm
filamentu, a ekran rozpoczyna wymianę filamentu.</p>
<p><strong>Od v2.0.8 jest domyślnie włączony w każdym modelu.</strong> Gdy do D8 nic nie jest podłączone, rezystor
podciągający na płycie utrzymuje pin na 5 V, co jest odczytywane jako „filament obecny”: wykrywanie nigdy wtedy nie zadziała, więc może pozostać włączone
niezależnie od tego, czy czujnik jest zamontowany. Podłącz czujnik końca filamentu do D8, a od razu zacznie działać.</p>
<ul>
<li>Wykrywanie zatorów pozostaje wyłączone (<code>L0</code>): ten czujnik nie widzi ruchu filamentu.</li>
<li>Aby wyłączyć czujnik: <code>M412 S0</code>, potem <code>M500</code>.</li>
<li>Ustawienia zapisane przez wcześniejsze wydanie zachowują swój stan (włączony lub wyłączony). Aby go włączyć: <code>M412 S1</code>, potem
<code>M500</code>, albo przywróć ustawienia domyślne (<code>M502</code>, potem <code>M500</code>, co kasuje też offset Z czujnika
i siatkę stołu).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Ten czujnik ma dwa wyjścia, a firmware odczytuje je na różne sposoby:</p>
<ul>
<li><strong>Czujnik końca filamentu</strong> (do D8) podaje poziom: 5 V, dopóki filament jest, 0 V, gdy go zabraknie.</li>
<li><strong>Wyjście ruchu</strong> (do D9) pochodzi z małego kółka, które obraca przesuwający się filament. Co kilka
milimetrów filamentu wyjście przełącza się między 0 V a 5 V. Firmware obserwuje tylko te zmiany: jeśli
ekstruder przepchnie długość zatoru bez ani jednej zmiany, filament nie nadąża (splątana szpula, zator,
filament zmielony przez ekstruder) i wydruk pauzuje. Czujnik końca filamentu tego nie wykryje: podczas zatoru filament wciąż jest na miejscu.</li>
</ul>
<h3>Podłączenie</h3>
<p><strong>5V</strong> do 5V, <strong>GND</strong> do GND, sygnał <strong>końca filamentu</strong> do <strong>D8</strong>,
a sygnał <strong>ruchu</strong> do <strong>D9</strong>. Nazwy nadrukowane na przewodzie czujnika mogą być inne.</p>
<h3>Włączanie</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Jeśli wydruki pauzują bez powodu, zwiększ długość zatoru: <code>M412 L15</code>, potem <code>M500</code>. Aby zostawić tylko
czujnik końca filamentu: <code>M412 L0</code>, potem <code>M500</code>.</p>
<h3>Sprawdzanie</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> z załadowanym filamentem: <em>filament: TRIGGERED</em>. Jeśli ta linia zmienia się, gdy przepychasz filament
ręką, a nie gdy go wkładasz lub wyjmujesz, dwa przewody sygnałowe są zamienione: zamień D8 z D9.</li>
</ul>
<div class="note">Wykrywanie zatorów przetestowano na MK2 300 bez czujnika (długość zatoru 2 mm wyzwala pauzę, <code>L0</code> nigdy),
ale jeszcze nie z samym czujnikiem BTT. Jeśli czujnik jest odczytywany odwrotnie (<em>open</em> z załadowanym
filamentem), daj nam znać na <a href="{DISCORD}">Discordzie</a>.</div>

<h2>Aktualizacja z v2.0.5 lub v2.0.6</h2>
<p>Te wydania nie pozwalały wyłączyć wykrywania zatorów, więc używały długości zatoru tak dużej, by nigdy nie została osiągnięta: 100 m w
v2.0.5 (w praktyce za mało: około jednej trzeciej szpuli 1 kg, po czym pozostawiona włączona drukarka mogła zapauzować bez powodu) i
10 km w v2.0.6. Przy uruchomieniu drukarki v2.0.7 wczytuje te dwie wartości jako <code>L0</code>. Rzeczywista długość ustawiona
dla czujnika BTT, taka jak <code>L10</code>, zostaje zachowana. Przy aktualizacji z v2.0.4 lub starszej wczytywana jest odległość końca filamentu 5 mm
zamiast 0 zapisanego przez tamte wersje.</p>
""")

    if page == "slicer":
        return ("Profile Cura i OrcaSlicer do Wanhao Duplicator 9 oraz ustawianie offsetu Z",
                "Gotowe profile UltiMaker Cura i OrcaSlicer do każdej Wanhao D9, PLA, PETG i ABS, jak ustawić offset Z "
                "czujnika, zrobić sondowanie stołu i wydrukować testowego 3DBenchy.",
                f"""
<h1>Slicing dla Duplicator 9</h1>
<p class="lead">Jeden profil na każdą z dwunastu drukarek, do <strong>UltiMaker Cura</strong> i
<strong>OrcaSlicer</strong> — oba darmowe i dostępne na Windows, macOS i Linux. Każdy ma pole robocze, przyspieszenia
i najwyższą temperaturę stołu z firmware'u swojej drukarki.</p>

<h2>Pobieranie</h2>
{h.slicer}
<p>Są przygotowane pod firmware z tej strony, <a href="{p('flash')}">v2.0.9 lub nowszy</a>.</p>

<h2>Instalacja</h2>
<p><strong>OrcaSlicer</strong>: <em>Plik</em> → <em>Importuj</em> → <em>Importuj konfiguracje…</em>, a potem wskaż plik
<code>.orca_printer</code>. Drukarka, jej trzy jakości (0,12, 0,20 i 0,28 mm) oraz filamenty PLA, PETG i ABS pojawią
się w Twoich profilach.</p>
<p><strong>Cura</strong>: <em>Pomoc</em> → <em>Pokaż folder konfiguracji</em>, zamknij Curę, rozpakuj plik do tego
folderu, uruchom Curę ponownie, a potem <em>Ustawienia</em> → <em>Drukarka</em> → <em>Dodaj drukarkę…</em> →
<em>Dodaj drukarkę niesieciową</em> → <em>Wanhao</em> → Twój model. <em>Wanhao Duplicator 9</em> dostarczana razem
z Curą to starszy profil: tylko 300, z raftem i podporami włączonymi domyślnie.</p>

<h2 id="first-print">Przed pierwszym wydrukiem: offset Z, a potem sondowanie</h2>
<p>Czujnik wyzwala się trochę nad stołem i firmware musi wiedzieć, o ile. To właśnie <strong>offset Z</strong>. Za
wysoko — pierwsza warstwa nie trzyma; za nisko — dysza szoruje po stole. Ustawia się go raz i to on decyduje, czy
wydruki się trzymają.</p>
<div class="note">Wszystko poniżej zapisuje się w pamięci drukarki, a nie w slicerze. Przetrwa aktualizację firmware'u
(od v2.0.3).</div>

<h3>1. Najpierw rozgrzej</h3>
<p>Gorąca dysza jest o kilka setnych milimetra dłuższa. Rozgrzej drukarkę jak do wydruku: na ekranie
<em>Temperatura</em> → <em>Podgrzej</em> → <em>PLA</em> (200 °C i 60 °C) i odczekaj dwie minuty.</p>

<h3>2. Wykonaj bazowanie osi</h3>
<p>Na ekranie: <em>Ustawienia</em> → <em>Ruch</em> → <em>Bazowanie</em>. Przez USB: <code>G28</code>.</p>

<h3>3. Ustaw offset Z</h3>
<p><strong>Najprościej, w trakcie druku.</strong> Zacznij wydruk i podczas <strong>pierwszej warstwy</strong> wejdź na
ekranie w <em>Dostosuj</em> → <em>Offset Z</em>. Schodź co 0,01 mm, gdy linia jest rysowana, aż będzie płaska i dotknie
sąsiedniej bez szczeliny. Za wysoko — zostają okrągłe, osobne nitki; za nisko — powierzchnia robi się szorstka
i zgnieciona, a dyszę widać, jak ryje. Wartość zapisuje się sama.</p>
<p><strong>Na kartkę papieru, bez drukowania.</strong> Przez USB, w temperaturze druku:</p>
<pre><code>M851 Z0     ; zapomnij bieżący offset
M500
G28         ; bazuj ponownie, żeby został uwzględniony
M420 S0     ; zignoruj siatkę na czas pomiaru
M211 S0     ; pozwól zejść poniżej Z0: blokady programowe zatrzymują tam dyszę
G1 Z0 F300  ; dysza zjeżdża do zera, w które wierzy firmware</code></pre>
<p>Wsuń pod dyszę kartkę papieru, a potem schodź małymi krokami: <code>G91</code>, a potem
<code>G1 Z-0.05 F60</code>, raz za razem, aż kartka zacznie ledwo ocierać. Odczytaj wartość poleceniem
<code>M114</code>: jest ujemna, na przykład −1,30. Następnie:</p>
<pre><code>G90
M851 Z-1.30 ; Twoja wartość
M500
M211 S1     ; przywróć blokady programowe, chronią stół</code></pre>
<p>Od wersji v2.1.1 obie linie <code>M211</code> są zbędne: firmware pozwala już dyszy zejść 3 mm poniżej zera.</p>

<h3>4. Zsonduj stół</h3>
<p>Na ekranie: <em>Ustawienia</em> → <em>Poziomowanie</em> → <em>Automatyczne</em> → <em>Sonduj</em>. Drukarka mierzy
25 punktów i <strong>sama zapisuje siatkę</strong> (wykonuje <code>G29</code>, a potem <code>M500</code>). Zajmuje to
kilka minut. Przez USB: <code>G29</code>, a potem <code>M500</code>.</p>
<p>Nasze profile nie sondują przed każdym wydrukiem: włączają zapisaną siatkę poleceniem <code>M420 S1</code>, zaraz
po bazowaniu. Powtórz więc sondowanie, gdy przestawisz drukarkę, zmienisz powierzchnię albo dyszę, albo gdy pierwsza
warstwa wychodzi dobrze z jednej strony stołu, a z drugiej nie.</p>

<h3>5. Sprawdź</h3>
<p><code>M503</code> wypisuje to, co jest zapisane: linia <code>M851</code> to Twój offset Z, a <code>M420 S1</code>
pokazuje, że siatka jest włączona. Na ekranie strona <em>Automatyczne</em> pokazuje 25 zmierzonych punktów.</p>

<h2>Wydruki testowe</h2>
<p>3DBenchy, już pocięty dla <strong>D9 MK2 300</strong>, żeby porównać oba slicery albo sprawdzić jakieś ustawienie
bez instalowania czegokolwiek:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Każdy to około półtorej godziny i 4 m filamentu. Dla innego modelu lub rozmiaru potnij
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> samodzielnie swoim profilem.</p>
<h3>Test wszystko w jednym</h3>
<p>Belki nawisów, mostek, wieżyczki do stringingu, otwory tolerancji i skala dokładności w jednym elemencie o wysokości
65 mm, około 2 h 30. To <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> autorstwa
<strong>majda107</strong> (CC BY 4.0), pocięty dla <strong>każdej drukarki</strong> i obu slicerów, w trzech
materiałach. Pliki z <a href="{REPO}/releases/latest">najnowszego wydania</a> nazywają się
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>, na przykład
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="3DBenchy wydrukowany z profilem OrcaSlicer na Wanhao D9 MK2 300"><figcaption>OrcaSlicer, 1 h 14</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="3DBenchy wydrukowany z profilem Cura na Wanhao D9 MK2 300"><figcaption>Cura, 1 h 22</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="3DBenchy wydrukowany z PETG na Wanhao D9, autor: dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>Od którego zacząć:</strong> na D9 MK2 300 w PLA ten sam Benchy zajął <strong>1 h 14 z OrcaSlicerem</strong>
i <strong>1 h 22 z Curą</strong>, a ścianki z OrcaSlicera wyszły odrobinę czystsze. Oba są dobre; my zaczęlibyśmy od
OrcaSlicera, a jego narzędzia do kalibracji (przepływ, pressure advance, wieże temperaturowe) przydają się, gdy
chcesz pójść dalej.</p>
<div class="note">D9 jest otwarta: ABS wymaga co najmniej pomieszczenia bez przeciągów, a jego temperatura stołu jest
obniżona do tego, co wytrzymuje Twój model (80 °C na MK3 500).</div>

<h2>Co jest w profilach</h2>
<ul>
<li><strong>Warstwy</strong> 0,20 mm, <strong>3 ściany</strong>, 4 warstwy pełne na górze i 3 na dole, wypełnienie
gyroid 15 %, skirt z 2 linii, bez podpór.</li>
<li><strong>Prędkości</strong>: 40 mm/s na ścianie zewnętrznej, 60 w środku, 70 dla wypełnienia, 20 na pierwszej
warstwie, 150 przy przelotach. Wanhao podaje 70 mm/s jako maksymalną prędkość druku D9.</li>
<li><strong>Retrakcja</strong> 1,5 mm przy 25 mm/s: każda D9 ma ekstruder MK10 w układzie direct drive, a firmware
ogranicza ekstruder do 25 mm/s.</li>
<li><strong>Temperatury</strong>: PLA 210 °C, potem 205, stół 65, potem 60. PETG 240 / 80, potem 235 / 75. ABS
245 / 105, potem 245 / 100.</li>
<li><strong>Linia zagruntowania</strong> 15 mm od lewej krawędzi, poza klipsami stołu, żeby dysza dojechała czysta do
modelu.</li>
<li>Na koniec dysza unosi się, a stół wyjeżdża do przodu.</li>
</ul>
<p>Wszystkie ustawienia i jak je zmienić: <a href="{REPO}/tree/main/Slicer">folder Slicer</a> na GitHubie.</p>
""")

    if page == "quiet":
        return ("Jak wyciszyć Wanhao Duplicator 9: które wentylatory, i wentylator płyty głównej na termistorach NTC",
                "Które wentylatory Wanhao D9 można wyciszyć: wentylator hotendu musi zostać, wentylator zasilacza już sam "
                "się reguluje, a wentylator płyty głównej można odłączyć lub zasilić przez termistory NTC.",
                f"""
<h1>Wyciszanie Duplicatora 9</h1>
<p class="lead">W spoczynku hałas D9 pochodzi z wentylatorów. Oto który można wyciszyć i jak.</p>
<div class="note">Pracuj przy drukarce <strong>odłączonej od prądu</strong>. Trzymaj wszystkie przewody z dala od części z napięciem 230 V.</div>

<h2>Wentylatory</h2>
<div class="table"><table class="stack"><thead><tr><th>Wentylator</th><th>Sterowany przez</th><th>Czy można go wyciszyć?</th></tr></thead><tbody>
<tr><td><strong>Wentylator radiatora hotendu</strong> (głowica)</td><td>nic: 24 V, zawsze włączony</td><td><strong>nie</strong>: zwykle najgłośniejszy, ale spowolnienie go pozwala ciepłu wędrować w górę hotendu i powoduje zatory filamentu (heat creep)</td></tr>
<tr><td><strong>Wentylator chłodzenia wydruku</strong> (głowica)</td><td>firmware, pin D5 (PWM)</td><td>już regulowany: ustawia go slicer i <code>M106</code></td></tr>
<tr><td><strong>Wentylator zasilacza</strong></td><td>sam zasilacz</td><td>nic do zrobienia: w sprawdzonym tu egzemplarzu (Chuanglian A-350FAK-24) już dostosowuje się do temperatury zasilacza</td></tr>
<tr><td><strong>Wentylator płyty głównej</strong> (skrzynka elektroniki)</td><td>nic: 24 V, zawsze włączony</td><td><strong>tak</strong>, patrz niżej</td></tr>
</tbody></table></div>
<p>Firmware Wanhao nie steruje ani wentylatorem płyty głównej, ani wentylatorem hotendu (<code>CONTROLLER_FAN_PIN</code> i
<code>E0_AUTO_FAN_PIN</code> mają wartość <code>-1</code>), a płyta nie ma wolnego wyjścia sterowanego. Dlatego te
dwa są zasilane ze stale aktywnych złączy „24V OUT” i żaden firmware nie może ich spowolnić.</p>

<h2>Wentylator płyty głównej</h2>
<p>W zmierzonym tu egzemplarzu: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, maks. 0,10 A, łożysko ślizgowe</strong>.</p>
<p><strong>Wielu właścicieli po prostu go odłącza.</strong> Płyta się nie nagrzewa: leży na dnie skrzynki elektroniki, pod
stołem grzewczym, a ciepło stołu unosi się w górę, z dala od niej. Jeśli to zrobisz, obserwuj pierwsze długie wydruki: przegrzany
sterownik silnika krokowego na chwilę się wyłącza, co widać jako <strong>przesunięte warstwy</strong>, a nie jako komunikat o błędzie.</p>
<h3>Zostawić go, ale tylko gdy sterowniki są ciepłe</h3>
<p>Dwa termistory mocy NTC połączone szeregowo sprawiają, że wentylator rusza przy około 45–50 °C i przyspiesza w miarę nagrzewania się sterowników:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), przyklejone do radiatora sterownika klejem
termoprzewodzącym, z zaizolowanymi wyprowadzeniami.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── wentylator (+)
                                    wentylator (−) ── 0V</code></pre>
<ul>
<li>To wynik obliczeń, <strong>jeszcze nie przetestowany na drukarce</strong>: tolerancja MF72 to ±20 %, a mały wentylator może
ruszyć niżej, niż zakładano. Sprawdź temperaturę startu na stole warsztatowym (termistory NTC w woreczku w gorącej wodzie, z termometrem
kuchennym); dodaj drugi termistor 200 Ω, jeśli rusza za wcześnie, usuń termistor 200 Ω, jeśli za późno.</li>
<li>Termistory NTC muszą być przyklejone do radiatora: na wolnym powietrzu prąd wentylatora (do około 0,6 W w termistorach) nagrzewa je o
kilkadziesiąt stopni.</li>
<li>W tym układzie wentylator nigdy nie osiąga pełnej prędkości (około 75 % przy 80 °C), a uszkodzony termistor NTC przerywa obwód: wentylator
zatrzymuje się wtedy na dobre.</li>
</ul>
<p>Źródła: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">karta katalogowa MF72</a>.</p>
""")
    raise KeyError(page)
