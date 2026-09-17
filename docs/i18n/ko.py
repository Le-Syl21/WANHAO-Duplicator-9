"""한국어: translation of en.py."""

META = {"name": "한국어", "locale": "ko_KR", "dir": "ltr"}

UI = {
    "nav": {"index": "홈", "mk1": "MK1", "mk1u2": "MK1 + MK2 키트", "mk2": "MK2", "mk3": "MK3",
            "flash": "플래싱 가이드", "screen": "화면", "sensor": "필라멘트 센서", "quiet": "소음 줄이기"},
    "language": "언어",
    "size": "크기", "volume": "출력 크기", "file": "펌웨어",
    "footer_src": "GitHub의 소스와 이슈", "footer_chat": "Discord",
    "footer_note": "펌웨어는 GNU GPL v3 라이선스입니다. Wanhao의 매뉴얼과 펌웨어의 권리는 Wanhao에 있습니다.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "Wanhao D9 메인보드 (위에서 본 모습)",
    "plug": "센서 커넥터",
    "switch": "필라멘트 소진 스위치",
    "motion": "움직임",
    "level": "레벨: 필라멘트 있음 / 없음",
    "pulses": "필라멘트가 움직이는 동안 펄스",
    "names": "센서에 적힌 이름은 다를 수 있음",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Wanhao Duplicator 9 펌웨어 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "모든 Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3)용 최신 Marlin 펌웨어, "
                "화면 파일, Wanhao 순정 펌웨어와 매뉴얼, 그리고 플래싱 방법.",
                f"""
<h1>Wanhao Duplicator 9 펌웨어</h1>
<p class="lead">Wanhao의 Duplicator 9 다운로드 사이트는 사라졌습니다. 대신 D9 사용자에게 필요한 모든 것을 여기에 모았습니다.
모든 모델과 크기에 맞는 최신 Marlin 2.1 펌웨어, 그에 맞는 터치스크린 파일, Wanhao 순정
펌웨어, Wanhao 매뉴얼, 그리고 단계별 플래싱 가이드입니다.</p>
<p><a class="btn" href="{REPO}/releases/latest">전체 다운로드</a> <a class="btn ghost" href="{DISCORD}">Discord에서 질문하기</a></p>

<h2>내 D9는 어떤 모델인가요?</h2>
<div class="split"><div>
<ol>
<li>프린트 헤드까지 이어지는 <strong>회색 납작한 리본 케이블</strong>, 노즐 옆의 <strong>금속 원통형 프로브</strong>가
있고 프레임 옆면에 보강대가 없다면: <a href="{p('mk1')}">MK1</a>.</li>
<li>같은 1세대 기계인데 금속 프로브 대신 <strong>흰색 BLTouch 프로브</strong>가 달려 있다면:
Wanhao 업그레이드 키트를 단 MK1, <a href="{p('mk1u2')}">MK1 + MK2 키트</a>입니다.</li>
<li>프레임 양옆에 <strong>비스듬한 보강대</strong>가 있고, 헤드까지 <strong>둥근 검은색 케이블</strong>이
이어지며 BLTouch가 달려 있다면: MK2 또는 MK3입니다. 베드 아래에서 베드를 움직이는 <strong>Y 모터</strong>를
확인하세요. 뒤쪽에 있으면 <a href="{p('mk2')}">MK2</a>, 앞쪽(터치스크린 쪽)에 있으면
<a href="{p('mk3')}">MK3</a>입니다.</li>
</ol>
<p>D9 뒤의 숫자는 크기입니다: D9/300, D9/400 또는 D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="옆면 보강대가 있는 Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2: 옆면 보강대, 둥근 케이블</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>인덕티브 프로브, 리본 케이블. 펌웨어, Wanhao V0.15~V0.164(B), 매뉴얼.</p><a class="more" href="{p('mk1')}">MK1 펌웨어 →</a></div>
<div class="card"><h3>D9 MK1 + MK2 키트</h3><p>BLTouch 키트로 업그레이드한 MK1. 펌웨어와 Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">키트 펌웨어 →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, 옆면 보강대. 펌웨어, Wanhao V1.1.2, 가이드.</p><a class="more" href="{p('mk2')}">MK2 펌웨어 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>앞쪽 Y 모터, 필라멘트 센서. 펌웨어와 Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">MK3 펌웨어 →</a></div>
</div>

<h2>이 펌웨어가 제공하는 것</h2>
<ul>
<li><a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>에
공개된 Duplicator 9 설정으로 빌드한 <strong>Marlin 2.1</strong>. 그곳에 제안한 변경 사항도 들어 있습니다: MK1 프로브를 올바른 방향으로 읽기, MK3 Y 방향, 정전 복구,
엔드스톱 노이즈 필터.</li>
<li><strong>Wanhao 공장 설정</strong>: 모델별 Wanhao 펌웨어와 소스에서 가져온 steps/mm,
속도, 가속도, 핫엔드 PID, 프로브 오프셋과 프로빙 여백, 원점 복귀, 온도 한계, jerk, 축 방향.</li>
<li><strong>정전 복구</strong>: SD 카드로 출력하는 동안 레이어가 바뀔 때마다 작업을 저장하고, 정전 후에는 화면에서 그 지점부터 이어서 출력할지 묻습니다.</li>
<li><strong>필라멘트 센서</strong>: D8의 필라멘트 소진 스위치(모든 모델에서 기본으로 켜져 있으며, 스위치가 없으면 아무 영향이 없음)와 막힘도 감지하는 BTT Smart Filament Sensor V2.0. <a href="{p('sensor')}">필라멘트 센서</a>를 참고하세요.</li>
<li><strong>베드 레벨링이 끝나면 헤드가 가운데로 돌아와</strong> 베드가 더 이상 화면을 가리지 않습니다.</li>
<li><strong>16개 언어를 지원하는 새 터치스크린 인터페이스</strong> <a href="{p('screen')}">DGUS Reloaded 2.0</a>, 필라멘트 센서 설정 페이지 포함.</li>
</ul>

<h2>세 단계로 플래싱하기</h2>
<ol>
<li>모델 페이지에서 내 모델과 크기에 맞는 <strong>.hex</strong> 파일을 내려받습니다.</li>
<li>AVRDUDESS나 avrdude로 USB를 통해 플래싱합니다: <a href="{p('flash')}">플래싱 가이드</a>.</li>
<li>microSD 카드로 터치스크린을 플래싱합니다: <a href="{p('screen')}">화면 가이드</a>.</li>
</ol>
<p>Wanhao 순정 펌웨어는 각 모델 페이지에 계속 남아 있으므로, 언제든 출고 상태로 되돌릴 수 있습니다.</p>
""")

    if page == "mk1":
        return ("Wanhao Duplicator 9 MK1 펌웨어 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "인덕티브 프로브를 쓰는 Wanhao D9 MK1용 Marlin 2.1 펌웨어, Wanhao 순정 펌웨어 V0.15~V0.164(B), "
                "화면 파일과 MK1 사용자 매뉴얼.",
                f"""
<h1>Wanhao Duplicator 9 MK1 펌웨어</h1>
<div class="split"><div>
<p class="lead">첫 번째 Duplicator 9입니다. 노즐 옆의 금속 인덕티브 프로브, 프린트 헤드까지 이어지는
회색 리본 케이블, 옆면 보강대가 없는 프레임이 특징입니다.</p>
<p>이 빌드는 인덕티브 프로브를 올바른 방향으로 읽고(LOW에서 트리거됨) Wanhao의
마지막 MK1 펌웨어인 V0.164(B)의 설정을 프로브 오프셋(X 15, Y 0)까지 그대로 가져왔습니다. Y 모터는 Wanhao가 만든 대로 뒤쪽에 있습니다.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Wanhao D9 MK1 프린트 헤드의 인덕티브 프로브와 리본 케이블">
<figcaption>MK1: 인덕티브 프로브, 리본 케이블</figcaption></figure></div>

<h2>다운로드</h2>
{dl("MK1")}
<p>내 크기에 맞는 파일을 받은 뒤, 화면은
<a href="{p('screen')}">DGUS Reloaded</a>로 플래싱하세요.</p>

<h2>Wanhao 문서</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 사용자 매뉴얼</a> (2018년 6월, 영어): 조립, 배선, 메뉴, 레벨링, 문제 해결.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 시작 가이드</a> (영어).</li>
</ul>

<h2>Wanhao 순정 펌웨어</h2>
<p>기계를 출고 상태로 되돌릴 때 사용합니다. 각 메인보드 펌웨어는 같은 버전의 화면 펌웨어와만
작동합니다.</p>
<div class="table"><table><thead><tr><th>버전</th><th>크기</th><th>메인보드</th><th>화면</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>버전별 설정(steps/mm, 속도, PID, 축 방향)은 Wanhao 바이너리에서 읽어 낸 것으로,
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>에 정리되어 있습니다.</p>
""")

    if page == "mk1u2":
        return ("MK2 업그레이드 키트(BLTouch)를 단 Wanhao Duplicator 9 MK1 펌웨어 – Marlin 2.1",
                "Wanhao MK2 BLTouch 키트로 업그레이드한 Wanhao D9 MK1용 Marlin 2.1 펌웨어와 Wanhao 순정 V1.1.31 키트 펌웨어.",
                f"""
<h1>MK2 업그레이드 키트를 단 Wanhao D9 MK1</h1>
<div class="split"><div>
<p class="lead">Wanhao MK2 업그레이드 키트를 단 1세대 D9입니다. 프레임은 MK1 그대로이고, 금속 인덕티브 프로브
대신 BLTouch 프로브가 달려 있습니다.</p>
<p>키트의 BLTouch는 공장 출고 MK2의 BLTouch와 위치가 달라 프로브의 Y 오프셋이 다르기 때문에, Wanhao는 이 조합을 위한
별도 펌웨어를 배포했습니다. 이 빌드는 키트의 치수를 사용합니다. Y 모터는
뒤쪽에 있습니다.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Wanhao D9 프린트 헤드의 BLTouch 프로브">
<figcaption>BLTouch 프로브</figcaption></figure></div>

<h2>다운로드</h2>
{dl("MK1u2")}
<p>내 크기에 맞는 파일을 받은 뒤, 화면은
<a href="{p('screen')}">DGUS Reloaded</a>로 플래싱하세요.</p>
<div class="note">이 빌드는 키트 펌웨어의 프로브 오프셋인 Y −10을 사용합니다. Wanhao 키트 소스가 공장 출고 MK2 소스(Y 0)와
다른 유일한 줄로, 키트의 BLTouch가 더 뒤쪽에 달리기 때문입니다. 베드 메시가 앞뒤로 밀린 것처럼
보이면 <a href="{REPO}/blob/main/Offset.md">오프셋 가이드</a>를 따라 직접 오프셋을 측정하세요.</div>

<h2>Wanhao 순정 펌웨어</h2>
<p>Wanhao V1.1.31 키트 펌웨어(2018년 12월)로, MK2 화면 펌웨어와 함께 사용합니다.</p>
<div class="table"><table><thead><tr><th>크기</th><th>메인보드</th><th>화면</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao 바이너리에서 읽어 낸 설정: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Wanhao Duplicator 9 MK2 펌웨어 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "BLTouch를 쓰는 Wanhao D9 MK2용 Marlin 2.1 펌웨어, Wanhao 순정 V1.1.2 펌웨어와 화면 파일, Wanhao MK2 가이드.",
                f"""
<h1>Wanhao Duplicator 9 MK2 펌웨어</h1>
<div class="split"><div>
<p class="lead">두 번째 Duplicator 9입니다. 양옆의 비스듬한 보강대, 프린트 헤드까지 이어지는 둥근 검은색 데이터 케이블,
BLTouch 프로브, 윗면의 스풀 홀더가 특징입니다.</p>
<p>Wanhao는 캐리지를 롤러 4개짜리로 바꾸고, 400과 500에는 레일 2개짜리 Y축과 더 두꺼운 벨트를,
300과 400에는 양면 베드를 달았습니다. Y 모터는 뒤쪽에 있으며, 이 빌드는 Wanhao V1.1.2 펌웨어와 같은 방향으로
Y축을 돌립니다.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>다운로드</h2>
{dl("MK2")}
<p>내 크기에 맞는 파일을 받으세요. 헤드까지 MK3로 업그레이드한 MK2라면
<a href="{p('mk3')}">MK3 펌웨어</a>를 사용해야 합니다. 그다음 화면은 <a href="{p('screen')}">DGUS Reloaded</a>로 플래싱하세요.</p>

<h2>Wanhao 문서</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 시작 가이드</a> (영어).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">MK1에서 MK2로 바뀐 12가지 개선점</a>, Wanhao 작성 (영어).</li>
</ul>

<h2>Wanhao 순정 펌웨어</h2>
<p>Wanhao V1.1.2(2018년 10월; 500은 2019년 7월에 V1.1.2.1로 다시 빌드됨)와 Wanhao MK2 화면 펌웨어.</p>
<div class="table"><table><thead><tr><th>크기</th><th>메인보드</th><th>화면</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao 바이너리에서 읽어 낸 설정: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Wanhao Duplicator 9 MK3 펌웨어 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Wanhao D9 MK3(앞쪽 Y 모터, 필라멘트 센서)용 Marlin 2.1 펌웨어와 Wanhao 순정 V1.1.3 펌웨어.",
                f"""
<h1>Wanhao Duplicator 9 MK3 펌웨어</h1>
<p class="lead">마지막 Duplicator 9는 MK2의 프레임과 BLTouch를 그대로 쓰면서 필라멘트 소진 센서를 추가하고,
Y 모터를 앞쪽(터치스크린 쪽)으로 옮겼습니다.</p>
<p>모터를 옮기면 Y축 방향이 반대가 됩니다. Wanhao의 V1.1.3 펌웨어도 Y를 반전하며, 이 빌드도 마찬가지입니다.
필라멘트 소진 센서는 기본으로 켜져 있습니다. Wanhao는 MK3용 프로브 오프셋을 공개하지 않았으므로, 이 빌드는
MK2의 오프셋을 사용합니다.</p>

<h2>다운로드</h2>
{dl("MK3")}
<p>내 크기에 맞는 파일을 받은 뒤, 화면은
<a href="{p('screen')}">DGUS Reloaded</a>로 플래싱하세요.</p>
<div class="note">필라멘트 센서가 아무 때나 출력을 멈춘다면 <code>M412 S0</code>, 이어서
<code>M500</code>으로 끄세요. Wanhao Europe이 이 문제를 위해 "ReverseMode" MK3 펌웨어를 공개한 적이 있지만, 이후
삭제되어 찾을 수 없습니다.</div>

<h2>Wanhao 순정 펌웨어</h2>
<p>Wanhao V1.1.3(2019년 8월). Wanhao는 MK3 화면 펌웨어를 따로 공개하지 않았고, MK3 다운로드는 MK2 화면 펌웨어를 사용했습니다.</p>
<div class="table"><table><thead><tr><th>크기</th><th>메인보드</th><th>화면</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao 바이너리에서 읽어 낸 설정: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Wanhao Duplicator 9 (D9) 메인보드 펌웨어 플래싱 방법",
                "AVRDUDESS나 avrdude로 USB를 통해 Wanhao D9에 Marlin을 플래싱하고, 원점 복귀(homing) "
                "문제를 해결하고, Wanhao 펌웨어로 복구하는 단계별 가이드.",
                f"""
<h1>Duplicator 9 메인보드 플래싱</h1>
<p class="lead">D9 메인보드는 USB 부트로더가 들어 있는 ATmega2560입니다. 프로그래머도 필요 없고 베이스를 열 필요도 없으며,
USB 케이블 하나면 됩니다.</p>

<h2>준비물</h2>
<ul>
<li>프린터와 컴퓨터를 잇는 USB 케이블, 그리고 <strong>전원이 켜진</strong> 프린터.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a>(Windows, 그래픽 화면, 가장 쉬움) 또는
<a href="https://github.com/avrdudes/avrdude">avrdude</a>(명령줄, 모든 운영체제).</li>
<li>내 모델과 크기에 맞는 <strong>.hex</strong> 파일: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + 키트</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>플래싱 전에</h2>
<div class="note"><code>M503</code>을 보내고 응답을 저장해 두세요. v2.0.3부터는 업데이트해도 프린터에 저장된
설정이 유지되지만, v2.0.3<strong>으로</strong> 업데이트할 때는 한 번 이 펌웨어의 기본값에서 다시 시작합니다(설정 저장 방식이
바뀌었기 때문). Wanhao 펌웨어에서 넘어올 때도 마찬가지입니다. 그다음 <code>M851 Z…</code>와
<code>M500</code>으로 프로브 Z 오프셋을 다시 설정하세요.</div>
<p>프린터 포트를 점유할 수 있는 프로그램을 모두 닫으세요: Cura, PrusaSlicer, OctoPrint, Pronterface, 시리얼 터미널.</p>

<h2>AVRDUDESS로 플래싱</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: 프린터의 COM 포트(예: <code>COM3</code>). 보드레이트는 기본값 그대로 두세요.</li>
<li>Flash: .hex 파일을 고른 뒤 <strong>Program!</strong>을 클릭합니다. 30~60초 정도 걸립니다.</li>
</ol>

<h2>avrdude로 플래싱</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>포트와 파일 이름을 내 것으로 바꾸세요. <code>wiring</code> 프로토콜이 부트로더 속도를 알아서 맞춥니다.</p>

<h2>첫 부팅</h2>
<ol>
<li>USB 케이블을 뽑고, 프린터를 껐다 켠 뒤 케이블을 다시 꽂습니다.</li>
<li><strong>250000 baud</strong>로 연결하고(Wanhao 펌웨어는 115200을 사용했음) <code>M115</code>를 보냅니다. 응답에 새 펌웨어가 표시됩니다.</li>
<li>모든 축을 원점 복귀한 뒤 화면에서 또는 <code>G29</code>로 베드 레벨링을 하고, <code>M500</code>으로 저장합니다.</li>
</ol>

<h2 id="reset">이 펌웨어의 기본 설정으로 되돌리기</h2>
<p>v2.0.3부터는 펌웨어를 업데이트해도 프린터에 저장된 설정(프로브 Z 오프셋, steps/mm,
PID, 메시…)이 <strong>유지됩니다</strong>. 따라서 새 릴리스의 기본값이 이미 저장된 값을 대체하지 않습니다. 직접 저장한 값이
남아 있는 상태에서 v2.0.2 이하에서 업데이트할 때, 다른 펌웨어를 써 본 뒤 프린터가 이상하게 동작할 때, 또는
깨끗하게 새로 시작하고 싶을 때는 한 번 초기화하세요:</p>
<ul>
<li><strong>화면에서:</strong> <em>설정</em> → <em>더보기</em> → <em>초기화</em> → ✓.</li>
<li><strong>USB로:</strong> <code>M502</code>(이 펌웨어의 기본값 불러오기)를 보낸 다음 <code>M500</code>(저장)을 보냅니다.</li>
</ul>
<p>그다음 프로브 Z 오프셋을 다시 설정하고(<code>M851 Z…</code> 후 <code>M500</code>) 베드 레벨링을 하세요.
<code>M503</code>으로 결과를 확인하세요.</p>

<h2>정전과 필라멘트 센서</h2>
<ul>
<li>정전 복구가 켜져 있어 레이어가 바뀔 때마다 작업을 저장합니다. 끄려면 <code>M413 S0</code> 후 <code>M500</code>.</li>
<li>가열을 시작하자마자 <em>power outage</em>와 함께 출력이 바로 멈춘다면 v2.0.4 이상으로 업데이트하세요. 이전 빌드는 보드의 정전 감지 입력을 감시했는데, 이 입력은 히터가 켜지는 순간 LOW로 읽힙니다.</li>
<li>필라멘트 소진 감지는 v2.0.8부터 모든 모델에서 기본으로 켜져 있으며, 센서가 없으면 아무 일도 하지 않습니다. 이전 릴리스에서 업데이트했다면 <code>M412 S1</code> 후 <code>M500</code>으로, 또는 화면의 <em>설정</em> → <em>필라멘트</em> → <em>필라멘트 센서</em>에서 켜세요. 배선과 BTT Smart Filament Sensor: <a href="{p('sensor')}">필라멘트 센서</a>.</li>
</ul>

<h2>문제 해결</h2>
<div class="table"><table><thead><tr><th>문제</th><th>해결</th></tr></thead><tbody>
<tr><td>포트가 사용 중</td><td>프린터 포트를 쓰는 프로그램을 모두 닫으세요.</td></tr>
<tr><td>장치를 찾을 수 없음</td><td>CH340 USB 드라이버를 설치하고, 다른 케이블이나 USB 포트를 써 보고, 프린터 전원이 켜져 있는지 확인하세요.</td></tr>
<tr><td>플래싱 후 글자가 깨져 보임</td><td>이 펌웨어는 250000 baud, Wanhao 펌웨어는 115200 baud를 사용하세요.</td></tr>
<tr><td>화면의 온도가 10배로 표시됨(23.6 °C가 236으로)</td><td>화면에 아직 옛 파일이 남아 있습니다: <a href="{p('screen')}">DGUS Reloaded 2.0</a>을 플래싱하세요.</td></tr>
<tr><td>켤 때마다 화면이 영어로 돌아가거나, <em>필라멘트 센서</em> 페이지가 작동하지 않음</td><td>메인보드 펌웨어가 v2.0.9보다 오래되었습니다: 업데이트하세요.</td></tr>
<tr><td>원점 복귀가 스위치 몇 mm 앞에서 멈추고 <em>Homing Failed</em>가 뜸</td><td>엔드스톱 선의 전기 노이즈입니다. 이 펌웨어는 v2.0.1부터 노이즈를 걸러 냅니다: 업데이트하세요.</td></tr>
<tr><td>레벨링 중 노즐이 베드 클립에 부딪힘</td><td>v2.0.2 이상으로 업데이트하세요. Wanhao 펌웨어처럼 첫 프로빙 열이 가장자리에서 10 mm 안쪽에 있습니다.</td></tr>
<tr><td>베드가 Y 스위치에서 멀어지는 방향으로 움직임</td><td>내 모델의 펌웨어를 받았는지 확인하세요. Y 모터는 MK1, MK1 + 키트, MK2에서는 뒤쪽, MK3에서는 앞쪽에 있습니다.</td></tr>
</tbody></table></div>

<h2>Wanhao 펌웨어로 되돌리기</h2>
<p>각 모델 페이지에 Wanhao 순정 메인보드 펌웨어와 화면 펌웨어 링크가 있습니다. 같은 방법으로 플래싱하면 됩니다. Wanhao
메인보드 펌웨어에는 같은 세대의 Wanhao 화면 펌웨어가 필요합니다.</p>
<p>질문: <a href="{DISCORD}">Discord</a> 또는 <a href="{REPO}/issues">GitHub 이슈</a>.</p>
""")

    if page == "screen":
        return ("Wanhao Duplicator 9 터치스크린 펌웨어 (DWIN DGUS) – 16개 언어의 DGUS Reloaded 2.0",
                "microSD 카드로 Wanhao D9 DWIN 터치스크린에 DGUS Reloaded 2.0을 플래싱하는 방법: 16개 언어의 새 "
                "인터페이스, 필라멘트 센서 페이지, Marlin 2.1용. 그리고 Wanhao 화면 펌웨어로 되돌리는 방법.",
                f"""
<h1>Duplicator 9 터치스크린 플래싱</h1>
<p class="lead">MK1부터 MK3까지 모든 D9에는 같은 DWIN T5 터치스크린(480 × 272)이 달려 있습니다. 이 펌웨어와 함께 화면은
microSD 카드로 플래싱하는 16개 언어의 새 인터페이스 DGUS Reloaded 2.0으로 작동합니다.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">DWIN_SET.zip 다운로드 (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>DGUS Reloaded 2.0의 새로운 점</h2>
<ul>
<li><strong>16개 언어</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. 홈 화면에서 프린터 이름 옆의 국기를 누르면
언어가 바뀌고, 프린터가 선택을 기억합니다.</li>
<li><strong>필라멘트 센서 페이지</strong>: <em>설정</em> → <em>필라멘트</em> → <em>필라멘트 센서</em>.
<a href="{p('sensor')}#screen">필라멘트 센서</a>를 참고하세요.</li>
<li><strong>사라지지 않는 상태 표시줄</strong>: 마지막 메시지(예: <em>Ready</em>)가 30초 뒤에 사라지지 않고
화면에 계속 남아 있습니다.</li>
<li>노즐과 베드의 <strong>온도 게이지</strong>, 목표 온도 표시 포함.</li>
<li>모든 페이지의 새로운 디자인: 어두운 테마, 더 큰 버튼, 팝업의 그림 아이콘.</li>
</ul>
</div><figure><img src="{img}screen/ko-home.png" width="480" height="272" alt="Wanhao D9의 DGUS Reloaded 2.0 홈 화면: 게이지가 있는 노즐과 베드 온도, 상태 표시줄, 인쇄·온도·설정 버튼">
<figcaption>홈 화면</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0을 쓰려면 메인보드에 <strong>v2.0.9 이상</strong>이 필요합니다. v2.0.8 이하에서는
켤 때마다 언어가 영어로 돌아가고 필라멘트 센서 페이지가 작동하지 않습니다. 먼저 <a href="{p('flash')}">메인보드를
플래싱</a>하세요.</div>

<h2>1. microSD 카드 포맷</h2>
<div class="note">할당 단위 크기 <strong>4096바이트</strong>의 FAT32로 포맷하세요. 다른 크기로 포맷하면 화면이 카드를 무시합니다.</div>
<ul>
<li><strong>Windows</strong>: Windows 11은 FAT32 포맷을 거부하는 경우가 많습니다. <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>을 사용하고
할당 단위 크기를 4096으로 설정하세요.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (먼저 <code>lsblk</code>로 장치를 확인하세요).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (<code>diskutil list</code>로 확인하세요).</li>
</ul>

<h2>2. 파일 복사</h2>
<p><code>DWIN_SET.zip</code>의 압축을 풀고 <code>DWIN_SET</code> 폴더 전체를 카드의 최상위에 복사하세요.</p>

<h2>3. 플래싱</h2>
<ol>
<li>프린터를 끄고 전원 플러그를 뽑습니다.</li>
<li>베이스 앞쪽을 열어 화면 뒷면에 손이 닿게 합니다. microSD 슬롯이 그곳에 있습니다.</li>
<li>카드를 넣고 전원을 켭니다. 10~30초 안에 화면에 업데이트가 표시됩니다. 화면이 정상적으로 다시 시작될 때까지
기다리세요. 전체 1~3분 걸립니다.</li>
<li>전원을 끄고 카드를 빼낸 뒤 베이스를 닫습니다.</li>
</ol>
<p>Wanhao의 <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">D9 화면 업데이트 영상</a>에서 슬롯 위치를 볼 수 있습니다.</p>

<h2>어디에서 왔나요</h2>
<p>DGUS Reloaded 2.0은 <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(Desuuuu, 이후 Neo2003 제작)을 한 페이지씩 새로 그린 것입니다. 소스, 화면 파일을 생성하는 프로그램, 번역은
<a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>에 있습니다. 한국어 표현이 틀렸거나 어색한가요?
<a href="{DISCORD}">Discord</a>에서 알려 주시거나 그곳에 이슈를 열어 주세요.</p>
<p>DGUS Reloaded 1.0.3으로 되돌리려면(예: v2.0.9보다 오래된 펌웨어를 쓸 때)
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a>을 같은 방법으로 플래싱하세요.</p>

<h2>Wanhao 화면으로 되돌리기</h2>
<p>Wanhao 화면 펌웨어는 Wanhao 메인보드 펌웨어와만 작동합니다. MK1: <a href="{p('mk1')}">MK1 페이지</a>에서
버전이 맞는 화면 파일. MK1 + 키트, MK2, MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. 절차는 같습니다.</p>
""")

    if page == "sensor":
        return ("Wanhao Duplicator 9 필라멘트 센서: 필라멘트 소진 스위치와 BTT Smart Filament Sensor 배선",
                "Wanhao D9 메인보드에서 필라멘트 센서를 꽂는 위치(D8, D9, GND, 5V), BTT Smart "
                "Filament Sensor V2.0 배선 방법, M412로 필라멘트 소진 감지와 막힘 감지를 켜는 방법.",
                f"""
<h1>필라멘트 센서</h1>
<p class="lead">v2.0.5부터 이 펌웨어는 두 종류의 센서를 읽습니다. Wanhao의 필라멘트 소진 스위치, 그리고 필라멘트가
움직이지 않을 때(엉킨 스풀, 막힘, 갈려 나간 필라멘트)도 알아차리는 BTT Smart Filament Sensor V2.0입니다.
<strong>필라멘트 소진 감지는 모든 모델에서 기본으로 켜져 있고</strong>, 막힘 감지는 꺼져 있습니다.</p>

<h2>센서 커넥터</h2>
<figure><img src="{img}d9-sensor-plug-ko.svg" width="760" height="440" alt="Wanhao D9 메인보드: POWER-DET 왼쪽의 4핀 센서 커넥터(핀 D9, D8, GND, 5V)와 BTT Smart Filament Sensor V2.0 배선"></figure>
<p><strong>POWER-DET</strong> 왼쪽, 엔드스톱 커넥터 아래에 있는 4핀 커넥터에는 <strong>D9, D8, GND, 5V</strong>가
이 순서대로 있습니다. 핀 이름은 dustovich가 찾아내
<a href="{DISCORD}">Discord</a>에 공유한 Wanhao 배선도에서 가져왔습니다. 보드 뒷면에는 같은 네 핀이 CTRL, BTN, GND, VCC로 인쇄되어 있습니다.</p>
<ul>
<li><strong>D8</strong>은 Wanhao 순정 펌웨어가 읽는 필라멘트 소진 입력입니다.</li>
<li><strong>D9</strong>는 Wanhao 펌웨어가 사용하지 않습니다. 이 빌드는 여기서 BTT 센서의 움직임 신호를 읽습니다.</li>
</ul>
<div class="note">보드에 무엇이든 꽂거나 뽑을 때는 프린터 <strong>전원을 끄세요</strong>.</div>

<h2 id="screen">화면에서</h2>
<div class="split"><div>
<p>화면에 DGUS Reloaded 2.0이 설치되어 있다면(펌웨어 v2.0.9 이상): <em>설정</em> → <em>필라멘트</em> →
<em>필라멘트 센서</em>.</p>
<ul>
<li><strong>필라멘트 소진</strong>: 모든 감지를 켜거나 끕니다. <code>M412 S1</code> / <code>M412 S0</code>과 같습니다.</li>
<li><strong>막힘 감지</strong>: 아래 길이로 막힘 감지를 켜거나 끕니다(<code>L0</code>).</li>
<li><strong>막힘 길이</strong>: −와 +로 1 mm씩 바꿉니다. 숫자를 누르면 직접 입력할 수 있습니다.</li>
<li><strong>필라멘트</strong> 표시등은 소진 스위치가 필라멘트를 감지하면 초록색, 감지하지 못하면 빨간색입니다.</li>
<li>변경 사항은 바로 적용됩니다. <strong>저장</strong>을 누르면 <code>M500</code>처럼 저장됩니다. 뒤로 화살표로 나가면
저장되지 않고, 다음 부팅 때 저장된 설정으로 돌아갑니다.</li>
</ul>
</div><figure><img src="{img}screen/ko-sensor.png" width="480" height="272" alt="DGUS Reloaded 2.0의 필라멘트 센서 페이지: 필라멘트 소진·막힘 감지 스위치, 빼기·더하기 버튼이 있는 막힘 길이, 필라멘트 표시등, 저장 버튼">
<figcaption>설정 → 필라멘트 → 필라멘트 센서</figcaption></figure></div>

<h2>M412 명령</h2>
<p>모든 설정은 시리얼 터미널(Pronterface, 슬라이서나 OctoPrint의 터미널,
250000 baud)에서 USB로 합니다. 여러 파라미터를 한 명령에 함께 쓸 수 있습니다. 예: <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>명령</th><th>동작</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>상태를 표시합니다. 예: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>감지를 켭니다</strong>: 필라멘트 소진 스위치, 그리고 막힘 길이가 0이 아니면 막힘 감지도 켭니다.</td></tr>
<tr><td><code>M412 S0</code></td><td>스위치와 막힘을 포함한 <strong>모든 감지를 끕니다</strong>.</td></tr>
<tr><td><code>M412 D5</code></td><td>스위치가 필라멘트 없음을 감지한 뒤, 센서와 노즐 사이에 남은 필라멘트를 쓰기 위해 <strong>5 mm</strong> 더 출력한 다음 일시 정지합니다. 기본값 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>막힘 감지를 켭니다</strong>(BTT 센서 전용): 센서 바퀴가 돌지 않은 채 필라멘트 <strong>10 mm</strong>가 익스트루더를 지나가면 일시 정지합니다.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>막힘 감지를 끄고</strong> 필라멘트 소진 스위치는 그대로 둡니다. 이것이 기본값입니다.</td></tr>
<tr><td><code>M500</code></td><td>설정을 저장합니다. 저장하지 않으면 프린터를 끌 때 변경 사항이 사라집니다.</td></tr>
<tr><td><code>M119</code></td><td><em>filament</em> 줄이 필라멘트가 있으면 <code>TRIGGERED</code>, 없으면 <code>open</code>으로 표시됩니다.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>과 단독으로 쓰는 <code>L</code>은 저희가 Marlin에 제안한 변경
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>)에서 온 것으로, 이 펌웨어에 포함되어 있습니다. 이 변경이 없는 Marlin에서는 <code>L</code>
단독 사용은 무시되고, <code>L0</code>은 곧바로 막힘으로 판단해 출력을 일시 정지합니다.</p>

<h2>Wanhao 필라멘트 소진 스위치</h2>
<p>필라멘트가 있는지 없는지를 펌웨어에 알려 줍니다. 필라멘트가 없어지면 필라멘트 5 mm를 더 출력한 뒤
일시 정지하고, 화면에서 필라멘트 교체가 시작됩니다.</p>
<p><strong>v2.0.8부터 모든 모델에서 기본으로 켜져 있습니다.</strong> D8에 아무것도 꽂혀 있지 않으면 보드의
풀업 저항이 핀을 5 V로 유지하고, 이는 "필라멘트 있음"으로 읽힙니다. 그래서 감지가 절대 트리거되지 않으므로,
센서 장착 여부와 상관없이 켜 두어도 됩니다. D8에 소진 스위치를 꽂으면 바로 작동합니다.</p>
<ul>
<li>막힘 감지는 꺼진 상태(<code>L0</code>)로 유지됩니다. 이 스위치는 필라멘트의 움직임을 볼 수 없습니다.</li>
<li>스위치를 끄려면: <code>M412 S0</code> 후 <code>M500</code>.</li>
<li>이전 릴리스에서 저장한 설정은 켜짐/꺼짐 상태를 그대로 유지합니다. 켜려면: <code>M412 S1</code> 후
<code>M500</code>, 또는 기본값으로 초기화하세요(<code>M502</code> 후 <code>M500</code>. 프로브 Z
오프셋과 메시도 지워집니다).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>이 센서에는 출력이 두 개 있고, 펌웨어는 두 출력을 서로 다르게 읽습니다.</p>
<ul>
<li><strong>필라멘트 소진 스위치</strong>(D8로)는 레벨 신호입니다. 필라멘트가 있는 동안 5 V, 없어지면 0 V입니다.</li>
<li><strong>움직임 출력</strong>(D9로)은 필라멘트가 지나가면서 돌리는 작은 바퀴에서 나옵니다. 필라멘트가 몇
mm 움직일 때마다 출력이 0 V와 5 V 사이에서 바뀝니다. 펌웨어는 이 변화만 지켜봅니다. 익스트루더가
막힘 길이만큼 필라멘트를 밀어내는 동안 변화가 한 번도 없으면 필라멘트가 따라오지 않는 것이므로(엉킨 스풀, 막힘,
갈려 나간 필라멘트) 출력을 일시 정지합니다. 소진 스위치는 이를 알 수 없습니다. 막혀 있어도 필라멘트는 그대로 있기 때문입니다.</li>
</ul>
<h3>배선</h3>
<p><strong>5V</strong>는 5V에, <strong>GND</strong>는 GND에, <strong>필라멘트 소진 스위치</strong> 신호는 <strong>D8</strong>에,
<strong>움직임</strong> 신호는 <strong>D9</strong>에 연결합니다. 센서 케이블에 인쇄된 이름은 다를 수 있습니다.</p>
<h3>켜기</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>이유 없이 출력이 일시 정지되면 막힘 길이를 늘리세요: <code>M412 L15</code> 후 <code>M500</code>. 필라멘트 소진
스위치만 쓰려면: <code>M412 L0</code> 후 <code>M500</code>.</p>
<h3>확인하기</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li>필라멘트를 넣은 상태에서 <code>M119</code>: <em>filament: TRIGGERED</em>. 필라멘트를 넣거나 뺄 때가 아니라
손으로 밀어 넣을 때 이 줄이 바뀐다면 두 신호선이 뒤바뀐 것입니다: D8과 D9를 서로 바꾸세요.</li>
</ul>
<div class="note">막힘 감지는 센서 없이 MK2 300에서 테스트했지만(막힘 길이 2 mm는 트리거되고, <code>L0</code>은 절대
트리거되지 않음), BTT 센서 자체로는 아직 테스트하지 않았습니다. 스위치가 반대로 읽힌다면(필라멘트를 넣었는데
<em>open</em>) <a href="{DISCORD}">Discord</a>에서 알려 주세요.</div>

<h2>v2.0.5 또는 v2.0.6에서 업데이트할 때</h2>
<p>이 릴리스들은 막힘 감지를 끌 방법이 없어서, 절대 도달하지 않을 만큼 긴 막힘 길이를 사용했습니다. v2.0.5는 100 m
(실제로는 너무 짧았습니다: 1 kg 스풀의 약 3분의 1 정도로, 그 뒤에는 켜 둔 프린터가 괜히 일시 정지할 수 있었습니다),
v2.0.6은 10 km였습니다. v2.0.7은 프린터가 시작될 때 이 두 값을 <code>L0</code>으로 불러옵니다. BTT 센서용으로 직접 설정한
실제 길이(예: <code>L10</code>)는 유지됩니다. v2.0.4 이하에서 업데이트하면, 그 버전들이 저장한 0 대신 5 mm 필라멘트 소진 거리를
불러옵니다.</p>
""")

    if page == "quiet":
        return ("Wanhao Duplicator 9 소음 줄이기: 어떤 팬을, 그리고 NTC 서미스터로 보드 팬 제어하기",
                "Wanhao D9의 어떤 팬을 조용하게 만들 수 있는지: 핫엔드 팬은 그대로 둬야 하고, 파워 서플라이 팬은 이미 "
                "스스로 조절하며, 보드 팬은 뽑거나 NTC 서미스터로 돌릴 수 있습니다.",
                f"""
<h1>Duplicator 9 소음 줄이기</h1>
<p class="lead">대기 중인 D9의 소음은 팬에서 나옵니다. 어떤 팬을 조용하게 만들 수 있는지, 그리고 그 방법을 소개합니다.</p>
<div class="note">프린터 <strong>전원 플러그를 뽑은 상태</strong>에서 작업하세요. 모든 전선을 230 V 쪽에서 멀리 두세요.</div>

<h2>팬 종류</h2>
<div class="table"><table class="stack"><thead><tr><th>팬</th><th>제어 주체</th><th>조용하게 만들 수 있나요?</th></tr></thead><tbody>
<tr><td><strong>핫엔드 방열판 팬</strong>(프린트 헤드)</td><td>없음: 24 V 상시 작동</td><td><strong>아니요</strong>: 보통 가장 시끄럽지만, 속도를 줄이면 열이 핫엔드 위로 올라가 필라멘트가 막힙니다(heat creep)</td></tr>
<tr><td><strong>출력물 냉각 팬</strong>(프린트 헤드)</td><td>펌웨어, 핀 D5(PWM)</td><td>이미 속도 조절됨: 슬라이서와 <code>M106</code>으로 설정</td></tr>
<tr><td><strong>파워 서플라이 팬</strong></td><td>파워 서플라이 자체</td><td>할 일 없음: 여기서 확인한 제품(Chuanglian A-350FAK-24)은 이미 파워 서플라이 온도에 따라 작동합니다</td></tr>
<tr><td><strong>보드 팬</strong>(컨트롤 박스)</td><td>없음: 24 V 상시 작동</td><td><strong>예</strong>, 아래 참고</td></tr>
</tbody></table></div>
<p>Wanhao 펌웨어는 보드 팬도 핫엔드 팬도 제어하지 않으며(<code>CONTROLLER_FAN_PIN</code>과
<code>E0_AUTO_FAN_PIN</code>이 모두 <code>-1</code>), 보드에는 남는 스위칭 출력이 없습니다. 그래서 이 두 팬은
상시 전원인 "24V OUT" 커넥터에 연결되어 있고, 어떤 펌웨어로도 속도를 줄일 수 없습니다.</p>

<h2>보드 팬</h2>
<p>여기서 측정한 제품: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 최대 0.10 A, 슬리브 베어링</strong>.</p>
<p><strong>많은 사용자가 그냥 뽑아 버립니다.</strong> 보드는 별로 뜨거워지지 않습니다. 컨트롤 박스 바닥, 히팅베드
아래에 있어서 베드의 열이 보드 반대쪽 위로 올라가기 때문입니다. 뽑는다면 처음 몇 번의 긴 출력을 잘 지켜보세요. 과열된
스테퍼 드라이버는 잠깐 꺼지는데, 이는 오류 메시지가 아니라 <strong>레이어 밀림</strong>으로 나타납니다.</p>
<h3>남겨 두되, 드라이버가 뜨거울 때만 돌리기</h3>
<p>전력용 NTC 서미스터 두 개를 직렬로 연결하면 팬이 약 45–50 °C에서 돌기 시작해 드라이버가 뜨거워질수록 빨라집니다.
<strong>MF72-400D9</strong>(400 Ω) + <strong>MF72-200D9</strong>(200 Ω)를 드라이버 방열판에 열전도
접착제로 붙이고, 리드선은 절연합니다.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── 팬 (+)
                                    팬 (−) ── 0V</code></pre>
<ul>
<li>계산으로 얻은 값이며 <strong>아직 프린터에서 테스트하지 않았습니다</strong>. MF72의 허용 오차는 ±20 %이고, 작은 팬은
예상보다 낮은 온도에서 돌기 시작할 수 있습니다. 작업대에서 시작 온도를 확인하세요(NTC를 작은 봉지에 넣어 뜨거운 물에 담그고
주방용 온도계로 측정). 너무 일찍 돌기 시작하면 200 Ω을 하나 더 추가하고, 너무 늦게 돌면 200 Ω을 빼세요.</li>
<li>NTC는 반드시 방열판에 붙여야 합니다. 공기 중에 두면 팬 전류(NTC에서 최대 약 0.6 W)로 인해 온도가
수십 도나 올라갑니다.</li>
<li>이 방식으로는 팬이 최고 속도에 도달하지 않으며(80 °C에서 약 75 %), NTC가 고장 나면 회로가 끊어져 팬이 완전히
멈춥니다.</li>
</ul>
<p>출처: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 데이터시트</a> (영어).</p>
""")
    raise KeyError(page)
