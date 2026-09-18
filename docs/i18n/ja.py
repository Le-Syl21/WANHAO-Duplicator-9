"""日本語: translation of en.py."""

META = {"name": "日本語", "locale": "ja_JP", "dir": "ltr"}

UI = {
    "nav": {"index": "ホーム", "mk1": "MK1", "mk1u2": "MK1 + MK2キット", "mk2": "MK2", "mk3": "MK3",
            "flash": "書き込みガイド", "screen": "タッチスクリーン", "sensor": "フィラメントセンサー", "slicer": "スライサー", "quiet": "静音化"},
    "language": "言語",
    "model": "モデル",
    "size": "サイズ", "volume": "造形サイズ", "file": "ファームウェア",
    "footer_src": "ソースコードと issue は GitHub で", "footer_chat": "Discord",
    "footer_note": "ファームウェアは GNU GPL v3 で提供しています。Wanhao のマニュアルとファームウェアの権利は Wanhao に帰属します。",
}

# センサー配線図のラベル（img/d9-sensor-plug-<言語>.svg）。
SVG = {
    "board": "Wanhao D9 メインボード（上面図）",
    "plug": "センサーコネクター",
    "switch": "フィラメント切れスイッチ",
    "motion": "動き検出",
    "level": "レベル：フィラメントあり／なし",
    "pulses": "フィラメントが動くとパルス",
    "names": "センサー側の名称は異なる場合があります",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Wanhao Duplicator 9 ファームウェア（D9 MK1・MK2・MK3）– Marlin 2.1",
                "すべての Wanhao Duplicator 9（D9/300、D9/400、D9/500、MK1・MK2・MK3）に対応した最新の Marlin ファームウェア、"
                "画面用ファイル、Wanhao 純正ファームウェアとマニュアル、そして書き込み方法。",
                f"""
<h1>Wanhao Duplicator 9 ファームウェア</h1>
<p class="lead">Wanhao の Duplicator 9 ダウンロードサイトはなくなってしまいました。D9 のオーナーに必要なものは、代わりにすべてここにあります。全モデル・全サイズ向けの最新 Marlin 2.1 ファームウェア、対応するタッチスクリーン用ファイル、Wanhao 純正ファームウェア、Wanhao のマニュアル、そして手順どおりに進められる書き込みガイドです。</p>
<p><a class="btn" href="{REPO}/releases/latest">すべてのダウンロード</a> <a class="btn ghost" href="{DISCORD}">Discord で質問する</a></p>

<h2>自分の D9 はどれ？</h2>
<div class="split"><div>
<ol>
<li>プリントヘッドまで<strong>灰色のフラットケーブル</strong>が伸びていて、ノズルの横に<strong>金属製の円筒形プローブ</strong>があり、フレームの側面に補強がない：<a href="{p('mk1')}">MK1</a>。</li>
<li>同じ第 1 世代の機体で、金属プローブの代わりに<strong>白い BLTouch プローブ</strong>が付いている：Wanhao のアップグレードキットを取り付けた MK1、<a href="{p('mk1u2')}">MK1 + MK2キット</a>。</li>
<li>フレームの両側に<strong>斜めの補強リブ</strong>があり、ヘッドまで<strong>黒い丸ケーブル</strong>が伸びていて、BLTouch が付いている：MK2 または MK3 です。ベッドの下にある <strong>Y 軸モーター</strong>（ベッドを動かすモーター）を見てください。背面にあれば <a href="{p('mk2')}">MK2</a>、前面（タッチスクリーン側）にあれば
<a href="{p('mk3')}">MK3</a> です。</li>
</ol>
<p>D9 の後ろの数字はサイズを表します：D9/300、D9/400、D9/500。</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="側面に補強リブのある Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2：側面リブ、丸ケーブル</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>誘導式プローブ、フラットケーブル。ファームウェア、Wanhao V0.15～V0.164(B)、マニュアル。</p><a class="more" href="{p('mk1')}">MK1 ファームウェア →</a></div>
<div class="card"><h3>D9 MK1 + MK2キット</h3><p>BLTouch キットでアップグレードした MK1。ファームウェアと Wanhao V1.1.31。</p><a class="more" href="{p('mk1u2')}">キット用ファームウェア →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch、側面リブ。ファームウェア、Wanhao V1.1.2、ガイド。</p><a class="more" href="{p('mk2')}">MK2 ファームウェア →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y 軸モーターが前面、フィラメントセンサー。ファームウェアと Wanhao V1.1.3。</p><a class="more" href="{p('mk3')}">MK3 ファームウェア →</a></div>
</div>

<h2>このファームウェアでできること</h2>
<ul>
<li><strong>Marlin 2.1</strong>：<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>
で公開されている Duplicator 9 用の設定からビルドし、そこで提案した変更を加えています。MK1 プローブを正しい向きで読み取る修正、MK3 の Y 軸方向、停電からの復帰、エンドストップのノイズフィルターです。</li>
<li><strong>Wanhao の工場出荷時設定</strong>：各モデルの Wanhao 純正ファームウェアとソースから取り出しています。steps/mm、速度、加速度、ホットエンドの PID、プローブオフセットとプロービングの余白、原点復帰、温度制限、ジャーク、各軸の方向です。</li>
<li><strong>停電からの復帰</strong>：SD カードから印刷しているときはレイヤーが変わるたびにジョブが保存され、停電のあとは画面にその位置から再開するかどうかが表示されます。</li>
<li><strong>フィラメントセンサー</strong>：D8 に接続するフィラメント切れスイッチ（全モデルでデフォルト有効、スイッチがなければ何も起きません）と、詰まりも検出できる BTT Smart Filament Sensor V2.0 に対応しています。<a href="{p('sensor')}">フィラメントセンサー</a>をご覧ください。</li>
<li><strong>ベッドのレベリング後、ヘッドが中央に戻ります</strong>。ベッドで画面が隠れることはもうありません。</li>
<li><strong>16 言語に対応した新しいタッチスクリーン UI</strong>、<a href="{p('screen')}">DGUS Reloaded 2.0</a>。フィラメントセンサーの設定ページもあります。</li>
</ul>

<h2>3 ステップで書き込み</h2>
<ol>
<li>各モデルのページから、モデルとサイズに合った <strong>.hex</strong> をダウンロードします。</li>
<li>AVRDUDESS または avrdude を使い、USB 経由で書き込みます：<a href="{p('flash')}">書き込みガイド</a>。</li>
<li>microSD カードからタッチスクリーンを書き換えます：<a href="{p('screen')}">タッチスクリーンガイド</a>。</li>
</ol>
<p>Wanhao 純正ファームウェアも各モデルのページで引き続き入手できるので、いつでも工場出荷時の状態に戻せます。</p>
""")

    if page == "mk1":
        return ("Wanhao Duplicator 9 MK1 ファームウェア（D9/300、D9/400、D9/500）– Marlin 2.1",
                "誘導式プローブを搭載した Wanhao D9 MK1 用の Marlin 2.1 ファームウェア、Wanhao 純正 V0.15～V0.164(B) ファームウェア、"
                "画面用ファイル、MK1 ユーザーマニュアル。",
                f"""
<h1>Wanhao Duplicator 9 MK1 ファームウェア</h1>
<div class="split"><div>
<p class="lead">最初の Duplicator 9 です。ノズルの横に金属製の誘導式プローブ、プリントヘッドまで灰色のフラットケーブル、側面リブのないフレームが特徴です。</p>
<p>このビルドは誘導式プローブを正しい向きで読み取り（LOW でトリガー）、Wanhao の最後の MK1 ファームウェア V0.164(B) の設定を、プローブオフセット（X 15、Y 0）も含めて引き継いでいます。Y 軸モーターは Wanhao の設計どおり背面にあります。</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Wanhao D9 MK1 のプリントヘッドにある誘導式プローブとフラットケーブル">
<figcaption>MK1：誘導式プローブ、フラットケーブル</figcaption></figure></div>

<h2>ダウンロード</h2>
{dl("MK1")}
<p>お使いのサイズのファイルを選び、そのあと
<a href="{p('screen')}">DGUS Reloaded</a> でタッチスクリーンを書き換えてください。</p>

<h2>Wanhao の資料</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 ユーザーマニュアル</a>（2018 年 6 月、英語）：組み立て、配線、メニュー、レベリング、トラブルシューティング。</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 スタートガイド</a>。</li>
</ul>

<h2>Wanhao 純正ファームウェア</h2>
<p>機体を工場出荷時の状態に戻すためのものです。メインボード用ファームウェアは、それぞれ同じバージョンの画面用ファームウェアとしか動作しません。</p>
<div class="table"><table><thead><tr><th>バージョン</th><th>サイズ</th><th>メインボード</th><th>画面</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>各バージョンの設定（steps/mm、速度、PID、軸の方向）は、Wanhao のバイナリから読み出して
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a> にまとめています。</p>
""")

    if page == "mk1u2":
        return ("Wanhao Duplicator 9 MK1 + MK2 アップグレードキット（BLTouch）用ファームウェア – Marlin 2.1",
                "Wanhao の MK2 BLTouch キットでアップグレードした Wanhao D9 MK1 用の Marlin 2.1 ファームウェアと、Wanhao 純正 V1.1.31 キット用ファームウェア。",
                f"""
<h1>MK2 アップグレードキットを付けた Wanhao D9 MK1</h1>
<div class="split"><div>
<p class="lead">Wanhao の MK2 アップグレードキットを取り付けた第 1 世代の D9 です。MK1 のフレームに、金属製の誘導式プローブの代わりに BLTouch プローブが付いています。</p>
<p>Wanhao はこの組み合わせ専用のファームウェアを出していました。キットの BLTouch は工場出荷の MK2 とは取り付け位置が違い、プローブの Y オフセットが異なるためです。このビルドはキットの寸法を使っています。Y 軸モーターは背面にあります。</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Wanhao D9 のプリントヘッドに付いた BLTouch プローブ">
<figcaption>BLTouch プローブ</figcaption></figure></div>

<h2>ダウンロード</h2>
{dl("MK1u2")}
<p>お使いのサイズのファイルを選び、そのあと
<a href="{p('screen')}">DGUS Reloaded</a> でタッチスクリーンを書き換えてください。</p>
<div class="note">このビルドは、キット用ファームウェアのプローブオフセット Y −10 を使っています。Wanhao のキット用ソースが工場出荷の MK2（Y 0）と異なるのはこの 1 行だけで、キットの BLTouch はより後ろに付いています。ベッドメッシュが前後にずれて見える場合は、<a href="{REPO}/blob/main/Offset.md">オフセットガイド</a>で実際のオフセットを測ってください。</div>

<h2>Wanhao 純正ファームウェア</h2>
<p>Wanhao の V1.1.31 キット用ファームウェア（2018 年 12 月）。MK2 の画面用ファームウェアと組み合わせて使います。</p>
<div class="table"><table><thead><tr><th>サイズ</th><th>メインボード</th><th>画面</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao のバイナリから読み出した設定：<a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "mk2":
        return ("Wanhao Duplicator 9 MK2 ファームウェア（D9/300、D9/400、D9/500）– Marlin 2.1",
                "BLTouch を搭載した Wanhao D9 MK2 用の Marlin 2.1 ファームウェア、Wanhao 純正 V1.1.2 ファームウェアと画面用ファイル、Wanhao の MK2 ガイド。",
                f"""
<h1>Wanhao Duplicator 9 MK2 ファームウェア</h1>
<div class="split"><div>
<p class="lead">2 代目の Duplicator 9 です。両側に斜めの補強リブ、プリントヘッドまで黒い丸型のデータケーブル、BLTouch プローブ、上部にスプールホルダーがあります。</p>
<p>Wanhao はさらに、キャリッジを 4 ローラーに変え、400 と 500 ではダブルレールの Y 軸とより太いベルトを、300 と 400 では両面ベッドを採用しました。Y 軸モーターは背面にあり、このビルドは Wanhao の V1.1.2 ファームウェアと同じ向きに Y 軸を回します。</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>ダウンロード</h2>
{dl("MK2")}
<p>お使いのサイズのファイルを選んでください。ヘッドも MK3 仕様にアップグレードした MK2 では、<a href="{p('mk3')}">MK3 ファームウェア</a>を使ってください。そのあと <a href="{p('screen')}">DGUS Reloaded</a> でタッチスクリーンを書き換えます。</p>

<h2>Wanhao の資料</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 スタートガイド</a>（英語）。</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">MK1 から MK2 への 12 の改良点</a>（Wanhao 作成）。</li>
</ul>

<h2>Wanhao 純正ファームウェア</h2>
<p>Wanhao の V1.1.2（2018 年 10 月。500 は 2019 年 7 月に V1.1.2.1 として再ビルド）と、Wanhao の MK2 画面用ファームウェア。</p>
<div class="table"><table><thead><tr><th>サイズ</th><th>メインボード</th><th>画面</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao のバイナリから読み出した設定：<a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "mk3":
        return ("Wanhao Duplicator 9 MK3 ファームウェア（D9/300、D9/400、D9/500）– Marlin 2.1",
                "Wanhao D9 MK3（Y 軸モーターが前面、フィラメントセンサー付き）用の Marlin 2.1 ファームウェアと、Wanhao 純正 V1.1.3 ファームウェア。",
                f"""
<h1>Wanhao Duplicator 9 MK3 ファームウェア</h1>
<p class="lead">最後の Duplicator 9 は、MK2 のフレームと BLTouch をそのまま使い、フィラメント切れセンサーを追加し、Y 軸モーターを前面（タッチスクリーン側）に移しました。</p>
<p>モーターを移したことで Y 軸の向きが逆になります。Wanhao 自身の V1.1.3 ファームウェアは Y を反転しており、このビルドも同様です。フィラメント切れセンサーはデフォルトで有効です。Wanhao は MK3 のプローブオフセットを公開していないため、このビルドは
MK2 の値を使っています。</p>

<h2>ダウンロード</h2>
{dl("MK3")}
<p>お使いのサイズのファイルを選び、そのあと
<a href="{p('screen')}">DGUS Reloaded</a> でタッチスクリーンを書き換えてください。</p>
<div class="note">フィラメントセンサーがランダムに印刷を止める場合は、<code>M412 S0</code> のあと
<code>M500</code> で無効にしてください。Wanhao Europe はこの問題向けに「ReverseMode」という MK3 ファームウェアを公開していましたが、その後削除され、見つけることはできませんでした。</div>

<h2>Wanhao 純正ファームウェア</h2>
<p>Wanhao の V1.1.3（2019 年 8 月）。Wanhao は MK3 用の画面ファームウェアを公開しておらず、MK3 のダウンロードでは MK2 用のものが使われていました。</p>
<div class="table"><table><thead><tr><th>サイズ</th><th>メインボード</th><th>画面</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Wanhao のバイナリから読み出した設定：<a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "flash":
        return ("Wanhao Duplicator 9（D9）のメインボードにファームウェアを書き込む方法",
                "AVRDUDESS または avrdude で USB 経由で Wanhao D9 に Marlin を書き込む手順、原点復帰トラブルの"
                "解決方法、Wanhao ファームウェアへの戻し方。",
                f"""
<h1>Duplicator 9 のメインボードに書き込む</h1>
<p class="lead">D9 のメインボードは USB ブートローダー付きの ATmega2560 です。書き込み器は不要で、ベースを開ける必要もなく、USB ケーブル 1 本だけで済みます。</p>

<h2>必要なもの</h2>
<ul>
<li>プリンターとパソコンをつなぐ USB ケーブル。プリンターは<strong>電源を入れた状態</strong>にしておきます。</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a>（Windows、GUI、いちばん簡単）または
<a href="https://github.com/avrdudes/avrdude">avrdude</a>（コマンドライン、すべての OS に対応）。</li>
<li>お使いのモデルとサイズに合った <strong>.hex</strong>：<a href="{p('mk1')}">MK1</a>、<a href="{p('mk1u2')}">MK1 + キット</a>、<a href="{p('mk2')}">MK2</a>、<a href="{p('mk3')}">MK3</a>。</li>
</ul>

<h2>書き込みの前に</h2>
<div class="note"><code>M503</code> を送信し、その応答を控えておいてください。v2.0.3 以降、アップデートしてもプリンターに保存された設定は保持されますが、v2.0.3 <strong>へ</strong>アップデートするときは一度だけこのファームウェアのデフォルト値から始まります（設定の保存方式が変わったため）。Wanhao のファームウェアから移行する場合も同様です。そのあと <code>M851 Z…</code>
と <code>M500</code> でプローブの Z オフセットを設定し直してください。</div>
<p>プリンターのポートを使う可能性のあるプログラムはすべて閉じてください：Cura、PrusaSlicer、OctoPrint、Pronterface、シリアルターミナル。</p>

<h2>AVRDUDESS で書き込む</h2>
<ol>
<li>Programmer：<code>wiring</code>。MCU：<code>ATmega2560</code>。</li>
<li>Port：プリンターの COM ポート（例：<code>COM3</code>）。ボーレートはデフォルトのままにします。</li>
<li>Flash：.hex ファイルを選び、<strong>Program!</strong> をクリックします。30～60 秒かかります。</li>
</ol>

<h2>avrdude で書き込む</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>ポートとファイル名はご自身の環境に合わせて置き換えてください。<code>wiring</code> プロトコルはブートローダーの通信速度を自動で選びます。</p>

<h2>初回起動</h2>
<ol>
<li>USB ケーブルを抜き、プリンターの電源を切ってから入れ直し、ケーブルを挿し直します。</li>
<li><strong>250000 bps</strong> で接続し（Wanhao のファームウェアは 115200 でした）、<code>M115</code> を送信します。応答に新しいファームウェアが表示されます。</li>
<li>全軸を原点復帰させてから、画面または <code>G29</code> でベッドのレベリングを行い、<code>M500</code> で保存します。</li>
</ol>

<h2 id="reset">このファームウェアのデフォルト設定に戻す</h2>
<p>v2.0.3 以降、ファームウェアをアップデートしても、プリンターに保存された設定（プローブの Z オフセット、steps/mm、PID、メッシュなど）は<strong>保持</strong>されます。そのため、新しいリリースでデフォルト値が変わっても、すでに保存されている値は置き換わりません。次のような場合は一度リセットしてください：手動で保存した値を残したまま v2.0.2 以前からアップデートするとき、ほかのファームウェアを試したあとプリンターの挙動がおかしいとき、あるいはまっさらな状態から始めたいとき。</p>
<ul>
<li><strong>画面から：</strong><em>設定</em> → <em>その他</em> → <em>リセット</em> → ✓。</li>
<li><strong>USB から：</strong><code>M502</code>（このファームウェアのデフォルト値を読み込む）を送信し、続けて <code>M500</code>（保存する）を送信します。</li>
</ul>
<p>そのあとプローブの Z オフセットを設定し直し（<code>M851 Z…</code> のあと <code>M500</code>）、ベッドのレベリングを行ってください。結果は <code>M503</code> で確認できます。</p>

<h2>停電とフィラメントセンサー</h2>
<ul>
<li>停電からの復帰は有効になっています。レイヤーが変わるたびにジョブが保存されます。無効にするには <code>M413 S0</code> のあと <code>M500</code> を送信します。</li>
<li>加熱が始まった途端に <em>power outage</em> で印刷が止まる場合：v2.0.4 以降にアップデートしてください。それより前のビルドはボードの停電検出入力を監視しており、この入力はヒーターが動き出すとすぐに LOW になってしまいます。</li>
<li>v2.0.8 以降、フィラメント切れ検出は全モデルでデフォルト有効で、センサーがなければ何もしません。それより前のリリースからアップデートした場合は、<code>M412 S1</code> のあと <code>M500</code> で有効にするか、画面の <em>設定</em> → <em>フィラメント</em> → <em>フィラメントセンサー</em> で有効にしてください。配線と BTT Smart Filament Sensor については<a href="{p('sensor')}">フィラメントセンサー</a>をご覧ください。</li>
</ul>

<h2>トラブルシューティング</h2>
<div class="table"><table><thead><tr><th>症状</th><th>対処法</th></tr></thead><tbody>
<tr><td>ポートが使用中</td><td>プリンターのポートを使っているプログラムをすべて閉じてください。</td></tr>
<tr><td>デバイスが見つからない</td><td>CH340 USB ドライバーをインストールし、別のケーブルや USB ポートを試し、プリンターの電源が入っているか確認してください。</td></tr>
<tr><td>書き込み後に文字化けする</td><td>このファームウェアでは 250000 bps、Wanhao のファームウェアでは 115200 bps を使ってください。</td></tr>
<tr><td>画面の温度が 10 倍で表示される（23.6 °C が 236）</td><td>画面に古いファイルが残っています：<a href="{p('screen')}">DGUS Reloaded 2.0</a> を書き込んでください。</td></tr>
<tr><td>起動するたびに画面が英語に戻る、または <em>フィラメントセンサー</em> ページが機能しない</td><td>メインボードのファームウェアが v2.0.9 より古いです：アップデートしてください。</td></tr>
<tr><td>原点復帰がスイッチの数ミリ手前で止まり、<em>Homing Failed</em> と表示される</td><td>エンドストップの信号線に電気ノイズが乗っています。このファームウェアは v2.0.1 からノイズを除去しています：アップデートしてください。</td></tr>
<tr><td>レベリング中にノズルがベッドのクリップに当たる</td><td>v2.0.2 以降にアップデートしてください：最初のプロービング列は、Wanhao のファームウェアと同じく端から 10 mm 内側になります。</td></tr>
<tr><td>ベッドが Y エンドストップから離れる方向に動く</td><td>お使いのモデル用のファームウェアか確認してください：Y 軸モーターは MK1、MK1 + キット、MK2 では背面、MK3 では前面にあります。</td></tr>
</tbody></table></div>

<h2>Wanhao のファームウェアに戻す</h2>
<p>各モデルのページに、Wanhao 純正のメインボード用・画面用ファームウェアへのリンクがあります。同じ方法で書き込めます。Wanhao のメインボード用ファームウェアには、同じ世代の Wanhao 画面用ファームウェアが必要です。</p>
<p>ご質問は <a href="{DISCORD}">Discord</a> または <a href="{REPO}/issues">GitHub issues</a> へどうぞ。</p>
""")

    if page == "screen":
        return ("Wanhao Duplicator 9 タッチスクリーン用ファームウェア（DWIN DGUS）– 16 言語対応の DGUS Reloaded 2.0",
                "Wanhao D9 の DWIN タッチスクリーンに microSD カードから DGUS Reloaded 2.0 を書き込む方法。16 言語対応の新しい"
                "UI、フィラメントセンサーのページ、Marlin 2.1 用。Wanhao の画面用ファームウェアへの戻し方も。",
                f"""
<h1>Duplicator 9 のタッチスクリーンを書き換える</h1>
<p class="lead">MK1 から MK3 まで、すべての D9 は同じ DWIN T5 タッチスクリーン（480 × 272）を搭載しています。このファームウェアでは、microSD カードから書き込む、私たちの 16 言語対応の新しい UI「DGUS Reloaded 2.0」で動作します。</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">DWIN_SET.zip をダウンロード（DGUS Reloaded 2.0）</a></p>
<div class="split"><div>
<h2>DGUS Reloaded 2.0 の特長</h2>
<ul>
<li><strong>16 言語</strong>：English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia。ホーム画面でプリンター名の横にある国旗をタップすると切り替わり、選んだ言語はプリンターが記憶します。</li>
<li><strong>フィラメントセンサーのページ</strong>：<em>設定</em> → <em>フィラメント</em> → <em>フィラメントセンサー</em>。<a href="{p('sensor')}#screen">フィラメントセンサー</a>をご覧ください。</li>
<li><strong>消えないステータス行</strong>：最後のメッセージ（たとえば <em>Ready</em>）が、30 秒後に消えずに画面に残ります。</li>
<li>ノズルとベッドの<strong>温度ゲージ</strong>（目標温度の目印付き）。</li>
<li>全ページが新しいデザインに：ダークテーマ、大きなボタン、ポップアップのアイコン。</li>
</ul>
</div><figure><img src="{img}screen/ja-home.png" width="480" height="272" alt="Wanhao D9 上の DGUS Reloaded 2.0 ホーム画面：ゲージ付きのノズルとベッドの温度、ステータス行、「印刷」「温度」「設定」ボタン">
<figcaption>ホーム画面</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 には、メインボードに <strong>v2.0.9 以降</strong>が必要です。v2.0.8 以前では、起動のたびに言語が英語に戻り、フィラメントセンサーのページも動作しません。先に<a href="{p('flash')}">メインボードを書き換えて</a>ください。</div>

<h2>1. microSD カードをフォーマットする</h2>
<div class="note">FAT32、アロケーションユニットサイズ <strong>4096 バイト</strong>でフォーマットします。ほかのサイズでは画面がカードを無視します。</div>
<ul>
<li><strong>Windows</strong>：Windows 11 では FAT32 でフォーマットできないことが多いので、<a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
を使い、アロケーションユニットサイズを 4096 に設定します。</li>
<li><strong>Linux</strong>：<code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code>（先に <code>lsblk</code> でデバイスを確認してください）。</li>
<li><strong>macOS</strong>：<code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code>（<code>diskutil list</code> で確認してください）。</li>
</ul>

<h2>2. ファイルをコピーする</h2>
<p><code>DWIN_SET.zip</code> を展開し、<code>DWIN_SET</code> フォルダーをまるごとカードのルートにコピーします。</p>

<h2>3. 書き込む</h2>
<ol>
<li>プリンターの電源を切り、電源コードを抜きます。</li>
<li>ベースの前面を開けて、画面の裏側に手が届くようにします。microSD スロットはそこにあります。</li>
<li>カードを挿して電源を入れます。10～30 秒で画面に更新が表示されます。正常に再起動するまで待ちます（全体で 1～3 分）。</li>
<li>電源を切り、カードを抜いて、ベースを閉じます。</li>
</ol>
<p>Wanhao の<a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">D9 画面アップデート動画</a>で、スロットの位置がわかります。</p>

<h2>このプロジェクトの由来</h2>
<p>DGUS Reloaded 2.0 は <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
（Desuuuu 作、のちに Neo2003 が引き継ぎ）をページごとに描き直したものです。ソースコード、画面用ファイルを生成するプログラム、翻訳は
<a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a> にあります。お使いの言語で間違った言葉や不自然な言葉を見つけましたか？<a href="{DISCORD}">Discord</a> で教えていただくか、GitHub で issue を作成してください。</p>
<p>DGUS Reloaded 1.0.3 に戻すには（たとえば v2.0.9 より古いファームウェアを使う場合）、<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> を同じ方法で書き込みます。</p>

<h2>Wanhao の画面に戻す</h2>
<p>Wanhao の画面用ファームウェアは、Wanhao のメインボード用ファームウェアでしか動作しません。MK1：<a href="{p('mk1')}">MK1 のページ</a>にある、対応するバージョンの画面用ファイル。MK1 + キット、MK2、MK3：<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>。手順は同じです。</p>
""")

    if page == "sensor":
        return ("Wanhao Duplicator 9 のフィラメントセンサー：フィラメント切れスイッチと BTT Smart Filament Sensor の配線",
                "Wanhao D9 のメインボードでフィラメントセンサーを接続する場所（D8、D9、GND、5V）、BTT Smart "
                "Filament Sensor V2.0 の配線、M412 でフィラメント切れ検出と詰まり検出を有効にする方法。",
                f"""
<h1>フィラメントセンサー</h1>
<p class="lead">v2.0.5 以降、このファームウェアは 2 種類のセンサーを読み取れます。Wanhao のフィラメント切れスイッチと、フィラメントが動かなくなったこと（スプールの絡まり、詰まり、フィラメントの削れ）も検知する BTT Smart Filament Sensor V2.0 です。<strong>フィラメント切れ検出は全モデルでデフォルト有効</strong>で、詰まり検出は無効です。</p>

<h2>センサーコネクター</h2>
<figure><img src="{img}d9-sensor-plug-ja.svg" width="760" height="440" alt="Wanhao D9 のメインボード：POWER-DET の左にある 4 ピンのセンサーコネクター（ピン D9、D8、GND、5V）と、BTT Smart Filament Sensor V2.0 への配線"></figure>
<p><strong>POWER-DET</strong> の左、エンドストップ用コネクターの下にある 4 ピンのコネクターには、<strong>D9、D8、GND、5V</strong> がこの順に並んでいます。ピン名は、dustovich さんが見つけて
<a href="{DISCORD}">Discord</a> で共有してくれた Wanhao の配線図によるものです。ボードの裏面には、同じ 4 本のピンが CTRL、BTN、GND、VCC と印字されています。</p>
<ul>
<li><strong>D8</strong> は、Wanhao 純正ファームウェアが読み取るフィラメント切れ入力です。</li>
<li><strong>D9</strong> は Wanhao のファームウェアでは使われていません。このビルドでは、ここで BTT センサーの動き検出信号を読み取ります。</li>
</ul>
<div class="note">ボードに何かを挿したり抜いたりするときは、必ずプリンターの<strong>電源を切って</strong>ください。</div>

<h2 id="screen">画面から設定する</h2>
<div class="split"><div>
<p>画面に DGUS Reloaded 2.0 を入れている場合（ファームウェア v2.0.9 以降）：<em>設定</em> → <em>フィラメント</em> →
<em>フィラメントセンサー</em>。</p>
<ul>
<li><strong>フィラメント切れ</strong>は、すべての検出をオン／オフします。<code>M412 S1</code> / <code>M412 S0</code> と同じです。</li>
<li><strong>詰まり検出</strong>は、下の長さで詰まり検出をオンにするか、オフ（<code>L0</code>）にします。</li>
<li><strong>詰まり長さ</strong>：− と + で 1 mm ずつ変更します。数値をタップすると直接入力できます。</li>
<li><strong>フィラメント</strong>の丸印は、フィラメント切れスイッチがフィラメントを検知しているときは緑、検知していないときは赤になります。</li>
<li>変更はすぐに反映されます。<strong>保存</strong>で保存されます（<code>M500</code> と同じ）。戻る矢印で抜けると保存されず、次回の起動時に保存済みの設定に戻ります。</li>
</ul>
</div><figure><img src="{img}screen/ja-sensor.png" width="480" height="272" alt="DGUS Reloaded 2.0 のフィラメントセンサーページ：フィラメント切れ検出と詰まり検出のスイッチ、マイナス・プラスボタン付きの詰まり長さ、フィラメント表示、保存ボタン">
<figcaption>設定 → フィラメント → フィラメントセンサー</figcaption></figure></div>

<h2>M412 コマンド</h2>
<p>設定はすべて、シリアルターミナル（Pronterface、スライサーや OctoPrint のターミナル、250000 bps）から USB 経由で行います。パラメーターは 1 つのコマンドにまとめられます。例：<code>M412 S1 L10</code>。</p>
<div class="table"><table class="stack"><thead><tr><th>コマンド</th><th>機能</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>状態を表示します。例：<em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>。</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>検出を有効にします</strong>：フィラメント切れスイッチと、詰まり長さが 0 でなければ詰まり検出も有効になります。</td></tr>
<tr><td><code>M412 S0</code></td><td>スイッチと詰まりの<strong>すべての検出を無効にします</strong>。</td></tr>
<tr><td><code>M412 D5</code></td><td>スイッチがフィラメントなしを検知してから <strong>5 mm</strong> 印刷を続けて一時停止し、センサーとノズルの間に残ったフィラメントを使い切ります。デフォルトは 5 mm。</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>詰まり検出を有効にします</strong>（BTT センサーのみ）：センサーのホイールが回らないまま <strong>10 mm</strong> のフィラメントがエクストルーダーを通過すると一時停止します。</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>詰まり検出を無効にします</strong>。フィラメント切れスイッチはそのままです。これがデフォルトです。</td></tr>
<tr><td><code>M500</code></td><td>設定を保存します。保存しないと、電源を切ったときに変更が失われます。</td></tr>
<tr><td><code>M119</code></td><td><em>filament</em> の行は、フィラメントが入っていると <code>TRIGGERED</code>、入っていないと <code>open</code> になります。</td></tr>
</tbody></table></div>
<p><code>M412 L0</code> と、<code>L</code> を単独で使う機能は、私たちが Marlin に加えた変更（<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>）によるもので、このファームウェアに組み込まれています。この変更のない Marlin では、単独の <code>L</code>
は無視され、<code>L0</code> はすぐに詰まりとして印刷を一時停止してしまいます。</p>

<h2>Wanhao のフィラメント切れスイッチ</h2>
<p>フィラメントがあるかどうかをファームウェアに伝えます。フィラメントがなくなると、さらに 5 mm 分のフィラメントを使ったところで印刷が一時停止し、画面でフィラメント交換が始まります。</p>
<p><strong>v2.0.8 以降、全モデルでデフォルト有効です。</strong>D8 に何も接続されていないときは、ボードのプルアップによってピンが 5 V に保たれ、「フィラメントあり」と読み取られます。そのため検出が作動することはなく、センサーの有無にかかわらず有効のままにしておけます。D8 にフィラメント切れスイッチを接続すれば、そのまま動作します。</p>
<ul>
<li>詰まり検出は無効のままです（<code>L0</code>）：このスイッチではフィラメントの動きを検知できません。</li>
<li>スイッチを無効にするには：<code>M412 S0</code> のあと <code>M500</code>。</li>
<li>以前のリリースで保存された設定は、オン／オフの状態がそのまま残ります。有効にするには：<code>M412 S1</code> のあと
<code>M500</code>、またはデフォルトに戻します（<code>M502</code> のあと <code>M500</code>。プローブの Z
オフセットとメッシュも消去されます）。</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>このセンサーには出力が 2 つあり、ファームウェアはそれぞれを異なる方法で読み取ります：</p>
<ul>
<li><strong>フィラメント切れスイッチ</strong>（D8 へ）はレベル信号です：フィラメントがある間は 5 V、なくなると 0 V になります。</li>
<li><strong>動き検出出力</strong>（D9 へ）は、通過するフィラメントによって回る小さなホイールから出ています。フィラメントが数ミリ進むごとに、出力が 0 V と 5 V の間で切り替わります。ファームウェアが見ているのはこの切り替わりだけです。エクストルーダーが詰まり長さ分のフィラメントを押し出しても一度も切り替わらなければ、フィラメントが付いてきていない（スプールの絡まり、詰まり、フィラメントの削れ）ということなので、印刷を一時停止します。フィラメント切れスイッチではこれを検知できません：詰まっている間もフィラメントはそこにあるからです。</li>
</ul>
<h3>配線</h3>
<p><strong>5V</strong> を 5V に、<strong>GND</strong> を GND に、<strong>フィラメント切れスイッチ</strong>の信号を <strong>D8</strong> に、<strong>動き検出</strong>の信号を <strong>D9</strong> に接続します。センサーのケーブルに印字された名前は異なる場合があります。</p>
<h3>有効にする</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>理由もなく印刷が一時停止する場合は、詰まり長さを大きくしてください：<code>M412 L15</code> のあと <code>M500</code>。フィラメント切れスイッチだけを使う場合：<code>M412 L0</code> のあと <code>M500</code>。</p>
<h3>動作確認</h3>
<ul>
<li><code>M412</code>：<em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>。</li>
<li>フィラメントを入れた状態で <code>M119</code>：<em>filament: TRIGGERED</em>。この行が、フィラメントを挿入・取り外したときではなく、手でフィラメントを押し込んだときに変わる場合は、2 本の信号線が逆になっています：D8 と D9 を入れ替えてください。</li>
</ul>
<div class="note">詰まり検出は、センサーなしの MK2 300 でテスト済みです（詰まり長さ 2 mm で作動し、<code>L0</code> では作動しない）が、BTT センサー本体ではまだテストしていません。スイッチの読み取りが逆（フィラメントが入っているのに <em>open</em>）の場合は、<a href="{DISCORD}">Discord</a> で教えてください。</div>

<h2>v2.0.5 または v2.0.6 からのアップデート</h2>
<p>これらのリリースには詰まり検出を無効にする手段がなかったため、決して到達しないはずの長い詰まり長さを使っていました。v2.0.5 では
100 m（実際には短すぎました：1 kg スプールの約 3 分の 1 で、それを超えると電源を入れたままのプリンターが意味もなく一時停止することがありました）、v2.0.6 では 10 km です。プリンターの起動時に、v2.0.7 はこの 2 つの値を <code>L0</code> として読み込みます。BTT センサー用に設定した実際の長さ（<code>L10</code> など）はそのまま保持されます。v2.0.4 以前からの場合は、それらのバージョンが保存した 0 の代わりに、5 mm のフィラメント切れ距離が読み込まれます。</p>
""")

    if page == "slicer":
        return ("Wanhao Duplicator 9 用の Cura と OrcaSlicer のプロファイル、そして Z オフセットの設定",
                "すべての Wanhao D9 向けにそのまま使える UltiMaker Cura と OrcaSlicer のプロファイル（PLA・PETG・ABS）、"
                "プローブの Z オフセットの設定方法、ベッドのプロービング、テスト用 3DBenchy の印刷。",
                f"""
<h1>Duplicator 9 のスライス</h1>
<p class="lead">12 機種それぞれに 1 つずつ、<strong>UltiMaker Cura</strong> と
<strong>OrcaSlicer</strong> 用のプロファイルを用意しました。どちらも無料で、Windows・macOS・Linux で使えます。それぞれのプロファイルには、その機種のファームウェアどおりの造形サイズ、加速度、ベッド最高温度が入っています。</p>

<h2>ダウンロード</h2>
{h.slicer}
<p>このサイトのファームウェア、<a href="{p('flash')}">v2.0.9 以降</a>に合わせて作られています。</p>

<h2>インストール</h2>
<p><strong>OrcaSlicer</strong>：<em>ファイル</em> → <em>インポート</em> → <em>設定をインポート…</em> と進み、
<code>.orca_printer</code> ファイルを選びます。プリンター、3 つの品質（0.12・0.20・0.28 mm）、そして PLA・PETG・ABS のフィラメントがプリセットに追加されます。</p>
<p><strong>Cura</strong>：<em>ヘルプ</em> → <em>設定フォルダーを表示</em>、Cura を終了し、ファイルをそのフォルダーに展開してから
Cura を起動し直して、<em>設定</em> → <em>プリンター</em> → <em>プリンターを追加…</em> →
<em>非ネットワークプリンターを追加</em> → <em>Wanhao</em> → お使いの機種を選びます。Cura に最初から入っている
<em>Wanhao Duplicator 9</em> は古いプロファイルです：300 のみで、ラフトとサポートが既定で有効になっています。</p>

<h2 id="first-print">最初の印刷の前に：Z オフセット、そしてプロービング</h2>
<p>プローブはベッドより少し上で反応するので、ファームウェアはその差を知っている必要があります。それが <strong>Z オフセット</strong>です。高すぎると 1 層目が定着せず、低すぎるとノズルがベッドを削ります。設定は一度だけで、印刷が定着するかどうかを決めるのはこの値です。</p>
<div class="note">以下の内容はすべてスライサーではなくプリンターのメモリーに保存されます。ファームウェアを更新しても残ります（v2.0.3 以降）。</div>

<h3>1. まず加熱する</h3>
<p>ノズルは熱くなると数百分の 1 mm 伸びます。印刷するときと同じように加熱してください。画面で <em>温度</em> →
<em>予熱</em> → <em>PLA</em>（200 °C と 60 °C）を選び、2 分ほど待ちます。</p>

<h3>2. 軸を原点復帰させる</h3>
<p>画面で：<em>設定</em> → <em>移動</em> → <em>原点</em>。USB からは <code>G28</code>。</p>

<h3>3. Z オフセットを設定する</h3>
<p><strong>かんたんな方法：印刷しながら。</strong>印刷を始めて、<strong>1 層目</strong>の間に画面の <em>調整</em> →
<em>Zオフセット</em> を開きます。線が引かれていくのを見ながら 0.01 mm ずつ下げていき、線が平らになって隣の線とすき間なくくっつくところで止めます。高すぎると線は丸いまま離れていて、低すぎると表面がざらついて押しつぶされ、ノズルが削っているのが分かります。値はひとりでに保存されます。</p>
<p><strong>紙を使う方法：印刷せずに。</strong>USB から、印刷時の温度で：</p>
<pre><code>M851 Z0     ; 今のオフセットを消す
M500
G28         ; 反映させるためにもう一度原点復帰
M420 S0     ; 測定中はメッシュを無視する
M211 S0     ; Z0 より下げられるようにする。ソフトリミットがノズルをそこで止めている
G1 Z0 F300  ; ファームウェアがゼロだと思っている高さまでノズルを下げる</code></pre>
<p>ノズルの下に紙を 1 枚すべり込ませ、<code>G91</code> のあと <code>G1 Z-0.05 F60</code> を何度も繰り返して少しずつ下げ、紙がやっと擦れるところまで来たら止めます。値は <code>M114</code> で読み取ります。値は負の数で、たとえば −1.30 です。そのあと：</p>
<pre><code>G90
M851 Z-1.30 ; あなたの値
M500
M211 S1     ; ソフトリミットを戻す。ベッドを守ってくれる</code></pre>

<h3>4. ベッドをプロービングする</h3>
<p>画面で：<em>設定</em> → <em>レベリング</em> → <em>自動</em> → <em>プローブ</em>。プリンターが 25 点を測定し、<strong>メッシュを自動で保存します</strong>（<code>G29</code> のあと <code>M500</code> を実行します）。数分かかります。USB からは <code>G29</code> のあと <code>M500</code>。</p>
<p>このプロファイルは毎回の印刷前にプロービングしません。原点復帰の直後に <code>M420 S1</code> で保存済みのメッシュを有効に戻すだけです。そのため、プリンターを移動したとき、印刷面やノズルを変えたとき、あるいはベッドの片側だけ 1 層目の調子が良いときは、もう一度プロービングしてください。</p>

<h3>5. 確認する</h3>
<p><code>M503</code> で保存されている内容が一覧表示されます。<code>M851</code> の行があなたの Z オフセットで、
<code>M420 S1</code> はメッシュが有効であることを示します。画面では <em>自動</em> のページに測定した 25 点が表示されます。</p>

<h2>テスト印刷</h2>
<p><strong>D9 MK2 300</strong> 用にスライス済みの 3DBenchy です。2 つのスライサーを比べたいときや、何もインストールせずに設定を確かめたいときにどうぞ：</p>
<ul>
<li>Cura：<a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer：<a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>どれも 1 時間半ほど、フィラメント 4 m ほどです。ほかの機種やサイズで印刷する場合は、
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> をご自分のプロファイルでスライスしてください。</p>
<h3>オールインワンのテスト</h3>
<p>オーバーハングのバー、ブリッジ、糸引きタワー、公差穴、細かさのスケールが 65 mm のひとつの造形物にまとまっていて、約 2 時間 30 分です。<strong>majda107</strong> さんの <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a>（CC BY 4.0）を、<strong>すべてのプリンター</strong>と 2 つのスライサー、3 種類の材料向けにスライスしたものです。<a href="{REPO}/releases/latest">最新リリース</a>のファイル名は <code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code> という形で、たとえば <code>Test_D9_MK2_300_Orca_PLA.gcode</code> です。</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="Wanhao D9 MK2 300 で OrcaSlicer のプロファイルを使って印刷した 3DBenchy"><figcaption>OrcaSlicer、1 時間 14 分</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="Wanhao D9 MK2 300 で Cura のプロファイルを使って印刷した 3DBenchy"><figcaption>Cura、1 時間 22 分</figcaption></figure>
</div>
<p><strong>どちらから始めるか：</strong>D9 MK2 300 で PLA を使うと、同じ Benchy が <strong>OrcaSlicer では 1 時間 14 分</strong>、<strong>Cura では 1 時間 22 分</strong>かかり、壁面は OrcaSlicer のほうがわずかにきれいでした。どちらも良いスライサーですが、私たちなら OrcaSlicer から始めます。もっと追い込みたくなったときは、そのキャリブレーション機能（フロー、pressure advance、温度タワー）が役に立ちます。</p>
<div class="note">D9 はオープンフレームです。ABS には最低でもすきま風のない部屋が必要で、ベッド温度はお使いの機種が許す値まで下げてあります（MK3 500 では 80 °C）。</div>

<h2>プロファイルの中身</h2>
<ul>
<li><strong>積層ピッチ</strong> 0.20 mm、<strong>ウォール 3 本</strong>、上面 4 層・底面 3 層、ジャイロイドインフィル 15 %、2 周のスカート、サポートなし。</li>
<li><strong>速度</strong>：外壁 40 mm/s、内壁 60、インフィル 70、1 層目 20、移動 150。Wanhao は D9 の最高印刷速度を 70 mm/s としています。</li>
<li><strong>リトラクト</strong> 1.5 mm を 25 mm/s で：D9 はどれも MK10 のダイレクトドライブエクストルーダーで、ファームウェアがエクストルーダーを 25 mm/s に制限しています。</li>
<li><strong>温度</strong>：PLA 210 °C のあと 205、ベッド 65 のあと 60。PETG 240 / 80 のあと 235 / 75。ABS 245 / 105 のあと 245 / 100。</li>
<li><strong>プライムライン</strong>を左端から 15 mm の位置に引きます。ベッドのクリップを避けた位置なので、ノズルはきれいな状態で造形物に入ります。</li>
<li>印刷が終わると、ノズルが上がってベッドが手前に出てきます。</li>
</ul>
<p>すべての設定と変更方法は GitHub の <a href="{REPO}/tree/main/Slicer">Slicer フォルダー</a>にあります。</p>
""")

    if page == "quiet":
        return ("Wanhao Duplicator 9 を静かにする：対象になるファンと、NTC サーミスターによるボードファン制御",
                "Wanhao D9 のどのファンを静かにできるか。ホットエンドファンは残す必要があり、電源ファンはすでに自動で"
                "回転を調整しており、ボードファンは外すか NTC サーミスターで制御できます。",
                f"""
<h1>Duplicator 9 を静かにする</h1>
<p class="lead">待機中の D9 の騒音はファンから出ています。どのファンを静かにできるか、その方法を説明します。</p>
<div class="note">作業はプリンターの<strong>電源プラグを抜いて</strong>行ってください。配線はすべて 230 V 側から離しておいてください。</div>

<h2>ファン</h2>
<div class="table"><table class="stack"><thead><tr><th>ファン</th><th>制御</th><th>静かにできる？</th></tr></thead><tbody>
<tr><td><strong>ホットエンドのヒートシンクファン</strong>（プリントヘッド）</td><td>なし：24 V 常時オン</td><td><strong>いいえ</strong>：たいてい一番うるさいファンですが、回転を落とすと熱がホットエンドを伝って上がり、フィラメントが詰まります（heat creep）</td></tr>
<tr><td><strong>パーツ冷却ファン</strong>（プリントヘッド）</td><td>ファームウェア、D5 ピン（PWM）</td><td>すでに可変：スライサーと <code>M106</code> で設定</td></tr>
<tr><td><strong>電源ファン</strong></td><td>電源ユニット自身</td><td>対処不要：ここで確認した個体（Chuanglian A-350FAK-24）では、すでに電源の温度に応じて回転します</td></tr>
<tr><td><strong>ボードファン</strong>（コントロールボックス）</td><td>なし：24 V 常時オン</td><td><strong>はい</strong>、下記参照</td></tr>
</tbody></table></div>
<p>Wanhao のファームウェアはボードファンもホットエンドファンも制御しておらず（<code>CONTROLLER_FAN_PIN</code> と
<code>E0_AUTO_FAN_PIN</code> はどちらも <code>-1</code>）、ボードには空いているスイッチ出力もありません。そのため、この
2 つは常時オンの「24V OUT」コネクターにつながっており、どのファームウェアでも回転を落とせません。</p>

<h2>ボードファン</h2>
<p>ここで測定した個体：<strong>HZ-D 4010MS、40 × 10 mm、24 V、最大 0.10 A、スリーブベアリング</strong>。</p>
<p><strong>多くのオーナーは単純に外しています。</strong>ボードはあまり熱くなりません。コントロールボックスの底、ヒートベッドの下にあり、ベッドの熱はボードから離れて上へ逃げていくからです。外す場合は、最初の何回かの長時間印刷に注意してください。ステッピングモータードライバーが過熱すると一瞬出力が止まり、それはエラーメッセージではなく<strong>レイヤーずれ</strong>として現れます。</p>
<h3>ファンは残し、ドライバーが温まったときだけ回す</h3>
<p>パワー用 NTC サーミスター 2 個を直列につなぐと、ファンは 45～50 °C あたりで回り始め、ドライバーが温まるにつれて速くなります。<strong>MF72-400D9</strong>（400 Ω）+ <strong>MF72-200D9</strong>（200 Ω）を熱伝導接着剤でドライバーのヒートシンクに貼り付け、リード線は絶縁します。</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ファン (+)
                                    ファン (−) ── 0V</code></pre>
<ul>
<li>これは計算によるもので、<strong>まだプリンターではテストしていません</strong>：MF72 の公差は ±20 % で、小型ファンは想定より低い温度で回り始めることがあります。作業台で回り始める温度を確認してください（NTC を小さな袋に入れてお湯に浸け、キッチン温度計で測る）。早すぎる場合は 200 Ω をもう 1 個追加し、遅すぎる場合は 200 Ω を外します。</li>
<li>NTC は必ずヒートシンクに貼り付けてください：空気中に浮かせたままだと、ファン電流（NTC で最大約 0.6 W）によって数十度も発熱します。</li>
<li>この方法ではファンが全速に達することはなく（80 °C で約 75 %）、NTC が故障すると開放状態になります。その場合、ファンは完全に止まったままになります。</li>
</ul>
<p>出典：<a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 データシート</a>。</p>
""")
    raise KeyError(page)
