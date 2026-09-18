"""中文: translation of en.py."""

META = {"name": "中文", "locale": "zh_CN", "dir": "ltr"}

UI = {
    "nav": {"index": "首页", "mk1": "MK1", "mk1u2": "MK1 + MK2 套件", "mk2": "MK2", "mk3": "MK3",
            "flash": "刷写指南", "screen": "触摸屏", "sensor": "耗材传感器", "slicer": "切片", "quiet": "降噪"},
    "language": "语言",
    "model": "型号",
    "size": "尺寸", "volume": "打印尺寸", "file": "固件",
    "footer_src": "GitHub 上的源代码和 issue", "footer_chat": "Discord",
    "footer_note": "固件采用 GNU GPL v3 许可。Wanhao 的说明书和固件版权仍归 Wanhao 所有。",
}

# 传感器接线图的标签（img/d9-sensor-plug-<语言>.svg）。
SVG = {
    "board": "Wanhao D9 主板（俯视图）",
    "plug": "传感器插座",
    "switch": "断料开关",
    "motion": "运动",
    "level": "电平：有耗材 / 无耗材",
    "pulses": "耗材移动时输出脉冲",
    "names": "你的传感器上的名称可能不同",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Wanhao Duplicator 9 固件（D9 MK1、MK2、MK3）– Marlin 2.1",
                "适用于所有 Wanhao Duplicator 9（D9/300、D9/400、D9/500；MK1、MK2、MK3）的最新 Marlin 固件、"
                "屏幕文件、Wanhao 原厂固件和说明书，以及刷写方法。",
                f"""
<h1>Wanhao Duplicator 9 固件</h1>
<p class="lead">Wanhao 为 Duplicator 9 提供的下载站点已经关闭。D9 用户需要的一切都可以在这里找到：适用于所有型号和尺寸的最新 Marlin 2.1 固件、配套的触摸屏文件、Wanhao 原厂固件、Wanhao 说明书，以及分步刷写指南。</p>
<p><a class="btn" href="{REPO}/releases/latest">全部下载</a> <a class="btn ghost" href="{DISCORD}">在 Discord 上提问</a></p>

<h2>我的 D9 是哪一款？</h2>
<div class="split"><div>
<ol>
<li>通往打印头的是<strong>灰色扁平排线</strong>，喷嘴旁边是<strong>金属圆柱形探针</strong>，机架两侧没有加强筋：<a href="{p('mk1')}">MK1</a>。</li>
<li>同样是第一代机器，但装的是<strong>白色 BLTouch 探针</strong>，而不是金属探针：这是加装了 Wanhao 升级套件的 MK1，<a href="{p('mk1u2')}">MK1 + MK2 套件</a>。</li>
<li>机架两侧有<strong>斜向加强筋</strong>，通往打印头的是<strong>黑色圆形线缆</strong>，并配有 BLTouch：这是 MK2 或 MK3。看看热床下方的 <strong>Y 轴电机</strong>，也就是带动热床移动的那个：在后面的是 <a href="{p('mk2')}">MK2</a>；在前面（触摸屏一侧）的是
<a href="{p('mk3')}">MK3</a>。</li>
</ol>
<p>D9 后面的数字表示尺寸：D9/300、D9/400 或 D9/500。</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="带侧面加强筋的 Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2：侧面加强筋，圆形线缆</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>电感式探针，扁平排线。固件、Wanhao V0.15 至 V0.164(B)、说明书。</p><a class="more" href="{p('mk1')}">MK1 固件 →</a></div>
<div class="card"><h3>D9 MK1 + MK2 套件</h3><p>加装 BLTouch 套件的 MK1。固件及 Wanhao V1.1.31。</p><a class="more" href="{p('mk1u2')}">套件固件 →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch，侧面加强筋。固件、Wanhao V1.1.2、指南。</p><a class="more" href="{p('mk2')}">MK2 固件 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Y 轴电机在前，带耗材传感器。固件及 Wanhao V1.1.3。</p><a class="more" href="{p('mk3')}">MK3 固件 →</a></div>
</div>

<h2>这些固件带来了什么</h2>
<ul>
<li><strong>Marlin 2.1</strong>，基于
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>
中发布的 Duplicator 9 配置编译，并包含在那里提交的修改：MK1 探针信号按正确方向读取、MK3 的 Y 轴方向、断电续打、限位开关抗干扰滤波。</li>
<li><strong>Wanhao 出厂设置</strong>，取自 Wanhao 针对各型号的固件和源代码：步数/mm、速度、加速度、热端 PID、探针偏移和探测边距、归零、温度限制、jerk 以及各轴方向。</li>
<li><strong>断电续打</strong>：从 SD 卡打印时，每换一层都会保存打印进度；断电恢复后，屏幕会提示从该处继续打印。</li>
<li><strong>耗材传感器</strong>：D8 上的断料开关，所有型号默认开启（未安装时不起作用），以及 BTT Smart Filament Sensor V2.0，它还能检测堵料。参见<a href="{p('sensor')}">耗材传感器</a>。</li>
<li><strong>调平结束后打印头回到中间</strong>，热床不会再挡住屏幕。</li>
<li><strong>全新的 16 种语言触摸屏界面</strong>：<a href="{p('screen')}">DGUS Reloaded 2.0</a>，带有耗材传感器设置页面。</li>
</ul>

<h2>三步完成刷写</h2>
<ol>
<li>在型号页面下载适合你的型号和尺寸的 <strong>.hex</strong> 文件。</li>
<li>通过 USB 用 AVRDUDESS 或 avrdude 刷写：<a href="{p('flash')}">刷写指南</a>。</li>
<li>用 microSD 卡刷写触摸屏：<a href="{p('screen')}">触摸屏指南</a>。</li>
</ol>
<p>每个型号页面都保留了 Wanhao 原厂固件，机器随时可以恢复到出厂状态。</p>
""")

    if page == "mk1":
        return ("Wanhao Duplicator 9 MK1 固件（D9/300、D9/400、D9/500）– Marlin 2.1",
                "适用于配备电感式探针的 Wanhao D9 MK1 的 Marlin 2.1 固件，Wanhao 原厂 V0.15 至 V0.164(B) 固件、"
                "屏幕文件及 MK1 用户手册。",
                f"""
<h1>Wanhao Duplicator 9 MK1 固件</h1>
<div class="split"><div>
<p class="lead">第一代 Duplicator 9：喷嘴旁有金属电感式探针，灰色扁平排线连到打印头，机架两侧没有加强筋。</p>
<p>这些固件按正确方向读取电感式探针（低电平触发），并采用 Wanhao 最后一版 MK1 固件 V0.164(B) 的设置，包括探针偏移（X 15，Y 0）。Y 轴电机在后面，与 Wanhao 的原始设计一致。</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Wanhao D9 MK1 打印头上的电感式探针和扁平排线">
<figcaption>MK1：电感式探针，扁平排线</figcaption></figure></div>

<h2>下载</h2>
{dl("MK1")}
<p>选择与你的尺寸对应的文件，然后用
<a href="{p('screen')}">DGUS Reloaded</a> 刷写触摸屏。</p>

<h2>Wanhao 文档</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">D9 MK1 用户手册</a>（2018 年 6 月，英文）：组装、接线、菜单、调平、故障排除。</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">D9 MK1 入门指南</a>。</li>
</ul>

<h2>Wanhao 原厂固件</h2>
<p>用于把机器恢复到出厂状态。每个主板固件只能与同一版本的屏幕固件配合使用。</p>
<div class="table"><table><thead><tr><th>版本</th><th>尺寸</th><th>主板</th><th>屏幕</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>各版本的设置（步数/mm、速度、PID、轴方向）列在
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a> 中，均从 Wanhao 的二进制文件中读出。</p>
""")

    if page == "mk1u2":
        return ("Wanhao Duplicator 9 MK1 加装 MK2 升级套件（BLTouch）固件 – Marlin 2.1",
                "适用于加装 Wanhao MK2 BLTouch 套件的 Wanhao D9 MK1 的 Marlin 2.1 固件，以及 Wanhao 原厂 V1.1.31 套件固件。",
                f"""
<h1>加装 MK2 升级套件的 Wanhao D9 MK1</h1>
<div class="split"><div>
<p class="lead">加装了 Wanhao MK2 升级套件的第一代 D9：MK1 的机架，用 BLTouch 探针取代了金属电感式探针。</p>
<p>Wanhao 为这种组合单独发布了固件，因为套件中 BLTouch 的安装位置与出厂 MK2 不同：探针的 Y 偏移不一样。这些固件使用套件的几何参数。Y 轴电机在后面。</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Wanhao D9 打印头上的 BLTouch 探针">
<figcaption>BLTouch 探针</figcaption></figure></div>

<h2>下载</h2>
{dl("MK1u2")}
<p>选择与你的尺寸对应的文件，然后用
<a href="{p('screen')}">DGUS Reloaded</a> 刷写触摸屏。</p>
<div class="note">这些固件使用套件固件中的探针偏移 Y −10。这是 Wanhao 套件源代码与出厂 MK2（Y 0）唯一不同的一行：套件的 BLTouch 装得更靠后。如果热床网格看起来前后错位，请按照<a href="{REPO}/blob/main/Offset.md">偏移指南</a>测量你自己的偏移。</div>

<h2>Wanhao 原厂固件</h2>
<p>Wanhao V1.1.31 套件固件（2018 年 12 月），配合 MK2 屏幕固件使用。</p>
<div class="table"><table><thead><tr><th>尺寸</th><th>主板</th><th>屏幕</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>从 Wanhao 二进制文件中读出的设置：<a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "mk2":
        return ("Wanhao Duplicator 9 MK2 固件（D9/300、D9/400、D9/500）– Marlin 2.1",
                "适用于配备 BLTouch 的 Wanhao D9 MK2 的 Marlin 2.1 固件，Wanhao 原厂 V1.1.2 固件和屏幕文件，以及 Wanhao 的 MK2 指南。",
                f"""
<h1>Wanhao Duplicator 9 MK2 固件</h1>
<div class="split"><div>
<p class="lead">第二代 Duplicator 9：两侧有斜向加强筋，黑色圆形数据线连到打印头，配有 BLTouch 探针，顶部有料盘架。</p>
<p>Wanhao 还把滑车改为四轮，在 400 和 500 上采用双导轨 Y 轴和更粗的同步带，在 300 和 400 上采用双面热床。Y 轴电机在后面；这些固件的 Y 轴转动方向与 Wanhao V1.1.2 固件一致。</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>下载</h2>
{dl("MK2")}
<p>选择与你的尺寸对应的文件。如果 MK2 的打印头也升级成了 MK3 的，请使用 <a href="{p('mk3')}">MK3 固件</a>。然后用 <a href="{p('screen')}">DGUS Reloaded</a> 刷写触摸屏。</p>

<h2>Wanhao 文档</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">D9 MK2 入门指南</a>（英文）。</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">从 MK1 到 MK2 的 12 项改进</a>，由 Wanhao 编写。</li>
</ul>

<h2>Wanhao 原厂固件</h2>
<p>Wanhao V1.1.2（2018 年 10 月；500 型号于 2019 年 7 月重新编译为 V1.1.2.1），配合 Wanhao 的 MK2 屏幕固件。</p>
<div class="table"><table><thead><tr><th>尺寸</th><th>主板</th><th>屏幕</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>从 Wanhao 二进制文件中读出的设置：<a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "mk3":
        return ("Wanhao Duplicator 9 MK3 固件（D9/300、D9/400、D9/500）– Marlin 2.1",
                "适用于 Wanhao D9 MK3（Y 轴电机在前、带耗材传感器）的 Marlin 2.1 固件，以及 Wanhao 原厂 V1.1.3 固件。",
                f"""
<h1>Wanhao Duplicator 9 MK3 固件</h1>
<p class="lead">最后一代 Duplicator 9 沿用了 MK2 的机架和 BLTouch，增加了断料传感器，并把 Y 轴电机移到了前面（触摸屏一侧）。</p>
<p>电机换位后 Y 轴方向随之反转：Wanhao 自己的 V1.1.3 固件反转了 Y 轴，这些固件也一样。断料传感器默认开启。Wanhao 没有公布 MK3 的探针偏移，因此这些固件沿用 MK2 的数值。</p>

<h2>下载</h2>
{dl("MK3")}
<p>选择与你的尺寸对应的文件，然后用
<a href="{p('screen')}">DGUS Reloaded</a> 刷写触摸屏。</p>
<div class="note">如果耗材传感器随机中断打印，请发送 <code>M412 S0</code>，再发送
<code>M500</code> 将其关闭。Wanhao 欧洲曾为此问题发布过一个“ReverseMode”MK3 固件；该固件后来被删除，已无处可寻。</div>

<h2>Wanhao 原厂固件</h2>
<p>Wanhao V1.1.3（2019 年 8 月）。Wanhao 没有发布 MK3 屏幕固件：其 MK3 下载使用的是 MK2 的屏幕固件。</p>
<div class="table"><table><thead><tr><th>尺寸</th><th>主板</th><th>屏幕</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>从 Wanhao 二进制文件中读出的设置：<a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>。</p>
""")

    if page == "flash":
        return ("如何刷写 Wanhao Duplicator 9（D9）主板固件",
                "分步指南：通过 USB 用 AVRDUDESS 或 avrdude 为 Wanhao D9 刷写 Marlin，解决归零问题，"
                "以及刷回 Wanhao 固件进行恢复。",
                f"""
<h1>刷写 Duplicator 9 主板</h1>
<p class="lead">D9 的主板是带 USB 引导程序（bootloader）的 ATmega2560：不需要编程器，也不用打开底座，只要一根 USB 线。</p>

<h2>准备工作</h2>
<ul>
<li>一根连接打印机和电脑的 USB 线，并且打印机<strong>已开机</strong>。</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a>（Windows，图形界面，最简单）或
<a href="https://github.com/avrdudes/avrdude">avrdude</a>（命令行，适用于所有系统）。</li>
<li>适用于你的型号和尺寸的 <strong>.hex</strong> 文件：<a href="{p('mk1')}">MK1</a>、<a href="{p('mk1u2')}">MK1 + 套件</a>、<a href="{p('mk2')}">MK2</a>、<a href="{p('mk3')}">MK3</a>。</li>
</ul>

<h2>刷写之前</h2>
<div class="note">发送 <code>M503</code> 并保存返回的内容。从 v2.0.3 起，更新固件会保留打印机中已保存的设置，但升级<strong>到</strong> v2.0.3 时会先恢复一次本固件的默认值（设置的存储方式变了），从 Wanhao 固件切换过来时也是如此。之后请用 <code>M851 Z…</code>
和 <code>M500</code> 重新设置探针 Z 偏移。</div>
<p>关闭所有可能占用打印机端口的程序：Cura、PrusaSlicer、OctoPrint、Pronterface、串口终端。</p>

<h2>用 AVRDUDESS 刷写</h2>
<ol>
<li>Programmer：<code>wiring</code>。MCU：<code>ATmega2560</code>。</li>
<li>Port：打印机的 COM 端口（例如 <code>COM3</code>）。波特率保持默认。</li>
<li>Flash：选择 .hex 文件，然后点击 <strong>Program!</strong>。大约需要 30 到 60 秒。</li>
</ol>

<h2>用 avrdude 刷写</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>把端口和文件名换成你自己的。<code>wiring</code> 协议会自动选择引导程序的通信速率。</p>

<h2>首次启动</h2>
<ol>
<li>拔下 USB 线，关闭并重新打开打印机，再插回 USB 线。</li>
<li>以 <strong>250000 波特率</strong>连接（Wanhao 固件使用 115200），发送 <code>M115</code>：返回内容会显示新固件。</li>
<li>所有轴归零，然后在屏幕上或用 <code>G29</code> 进行热床调平，再用 <code>M500</code> 保存。</li>
</ol>

<h2 id="reset">恢复本固件的默认设置</h2>
<p>从 v2.0.3 起，固件更新会<strong>保留</strong>打印机中已保存的设置（探针 Z 偏移、步数/mm、PID、网格……）。因此新版本中的新默认值不会覆盖已经保存的值。以下情况请重置一次：从 v2.0.2 或更早版本更新，并且保留着手动保存的值；试过其他固件后打印机表现异常；或者任何你想从头开始的时候：</p>
<ul>
<li><strong>在屏幕上：</strong><em>设置</em> → <em>更多</em> → <em>恢复默认</em> → ✓。</li>
<li><strong>通过 USB：</strong>发送 <code>M502</code>（载入本固件的默认值），然后发送 <code>M500</code>（保存）。</li>
</ul>
<p>然后重新设置探针 Z 偏移（<code>M851 Z…</code> 然后 <code>M500</code>），并进行热床调平。用 <code>M503</code> 检查结果。</p>

<h2>断电与耗材传感器</h2>
<ul>
<li>断电续打已开启：每换一层都会保存打印进度。关闭方法：<code>M413 S0</code> 然后 <code>M500</code>。</li>
<li>打印一开始加热就立即停止并显示 <em>power outage</em>：请更新到 v2.0.4 或更高版本。早期版本会监测主板的断电检测输入，而加热器一启动，该输入就会变为低电平。</li>
<li>从 v2.0.8 起，所有型号默认开启断料检测，未安装传感器时不起作用。从更早的版本更新后，请用 <code>M412 S1</code> 然后 <code>M500</code> 开启，或在屏幕上进入 <em>设置</em> → <em>耗材</em> → <em>耗材传感器</em> 开启。接线方法及 BTT Smart Filament Sensor：参见<a href="{p('sensor')}">耗材传感器</a>。</li>
</ul>

<h2>故障排除</h2>
<div class="table"><table><thead><tr><th>问题</th><th>解决方法</th></tr></thead><tbody>
<tr><td>端口被占用</td><td>关闭所有正在使用打印机端口的程序。</td></tr>
<tr><td>找不到设备</td><td>安装 CH340 USB 驱动，换一根线或换一个 USB 口，确认打印机已开机。</td></tr>
<tr><td>刷写后出现乱码</td><td>这些固件使用 250000 波特率，Wanhao 固件使用 115200。</td></tr>
<tr><td>屏幕上温度显示为实际的 10 倍（23.6 °C 显示为 236）</td><td>屏幕里仍是旧文件：刷写 <a href="{p('screen')}">DGUS Reloaded 2.0</a>。</td></tr>
<tr><td>每次开机屏幕都变回英文，或其 <em>耗材传感器</em> 页面不起作用</td><td>主板固件早于 v2.0.9：请更新。</td></tr>
<tr><td>归零时在碰到限位开关前几毫米就停下，然后显示 <em>Homing Failed</em></td><td>限位开关线路上有电气干扰。这些固件从 v2.0.1 起会过滤这种干扰：请更新。</td></tr>
<tr><td>调平时喷嘴撞到热床夹子</td><td>请更新到 v2.0.2 或更高版本：第一列探测点距边缘 10 mm，与 Wanhao 固件相同。</td></tr>
<tr><td>热床朝远离 Y 轴限位开关的方向移动</td><td>检查你下载的是否是自己型号的固件：MK1、MK1 + 套件和 MK2 的 Y 轴电机在后面，MK3 的在前面。</td></tr>
</tbody></table></div>

<h2>刷回 Wanhao 固件</h2>
<p>每个型号页面都提供 Wanhao 原厂主板固件和屏幕固件的链接。刷写方法相同；Wanhao 主板固件需要配合同一代的 Wanhao 屏幕固件。</p>
<p>有问题？请到 <a href="{DISCORD}">Discord</a> 或 <a href="{REPO}/issues">GitHub issues</a>。</p>
""")

    if page == "screen":
        return ("Wanhao Duplicator 9 触摸屏固件（DWIN DGUS）– DGUS Reloaded 2.0，支持 16 种语言",
                "如何用 microSD 卡为 Wanhao D9 的 DWIN 触摸屏刷写 DGUS Reloaded 2.0：16 种语言的新界面、"
                "耗材传感器页面，适用于 Marlin 2.1。以及如何刷回 Wanhao 屏幕固件。",
                f"""
<h1>刷写 Duplicator 9 触摸屏</h1>
<p class="lead">从 MK1 到 MK3，所有 D9 都使用同一款 DWIN T5 触摸屏（480 × 272）。配合这些固件，它运行
DGUS Reloaded 2.0——我们推出的 16 种语言新界面，通过 microSD 卡刷写。</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">下载 DWIN_SET.zip（DGUS Reloaded 2.0）</a></p>
<div class="split"><div>
<h2>DGUS Reloaded 2.0 带来了什么</h2>
<ul>
<li><strong>16 种语言</strong>：English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia。在主屏幕上点击打印机名称旁边的国旗即可切换；打印机会记住你的选择。</li>
<li><strong>耗材传感器页面</strong>：<em>设置</em> → <em>耗材</em> → <em>耗材传感器</em>。参见<a href="{p('sensor')}#screen">耗材传感器</a>。</li>
<li><strong>常驻的状态栏</strong>：最后一条消息（例如 <em>Ready</em>）会一直显示在屏幕上，不会在 30 秒后消失。</li>
<li>喷嘴和热床的<strong>温度仪表</strong>，并标出目标温度。</li>
<li>所有页面焕然一新：深色主题、更大的按钮、弹窗配有图标。</li>
</ul>
</div><figure><img src="{img}screen/zh-home.png" width="480" height="272" alt="Wanhao D9 上的 DGUS Reloaded 2.0 主屏幕：带仪表的喷嘴和热床温度、状态栏，以及“打印”“温度”“设置”按钮">
<figcaption>主屏幕</figcaption></figure></div>
<div class="note">DGUS Reloaded 2.0 要求主板固件为 <strong>v2.0.9 或更高版本</strong>。使用 v2.0.8 或更早版本时，每次开机语言都会变回英文，耗材传感器页面也无法使用：请先<a href="{p('flash')}">刷写主板</a>。</div>

<h2>1. 格式化 microSD 卡</h2>
<div class="note">FAT32，分配单元大小为 <strong>4096 字节</strong>。使用其他大小时，屏幕会忽略这张卡。</div>
<ul>
<li><strong>Windows</strong>：Windows 11 经常无法格式化为 FAT32；请使用 <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>，并把分配单元大小设为 4096。</li>
<li><strong>Linux</strong>：<code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code>（先用 <code>lsblk</code> 确认设备）。</li>
<li><strong>macOS</strong>：<code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code>（用 <code>diskutil list</code> 确认）。</li>
</ul>

<h2>2. 复制文件</h2>
<p>解压 <code>DWIN_SET.zip</code>，把整个 <code>DWIN_SET</code> 文件夹复制到卡的根目录。</p>

<h2>3. 刷写</h2>
<ol>
<li>关闭打印机并拔掉电源线。</li>
<li>打开底座前部，就能接触到屏幕背面，microSD 卡槽就在那里。</li>
<li>插入卡片并开机。屏幕会在 10 到 30 秒内显示更新过程；等待它正常重启，整个过程需要 1 到 3 分钟。</li>
<li>关机，取出卡片，合上底座。</li>
</ol>
<p>Wanhao 的 <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">D9 屏幕更新视频</a> 展示了卡槽的位置。</p>

<h2>项目来源</h2>
<p>DGUS Reloaded 2.0 逐页重绘了 <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
（作者 Desuuuu，后由 Neo2003 接手）。它的源代码、生成屏幕文件的程序以及各语言翻译都在
<a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a> 上。发现你的语言里有错误或别扭的用词？请在
<a href="{DISCORD}">Discord</a> 上告诉我们，或在 GitHub 上提交 issue。</p>
<p>如需回到 DGUS Reloaded 1.0.3（例如使用早于 v2.0.9 的固件时），用同样的方法刷写
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a>。</p>

<h2>刷回 Wanhao 屏幕固件</h2>
<p>Wanhao 屏幕固件只能配合 Wanhao 主板固件使用。MK1：使用 <a href="{p('mk1')}">MK1 页面</a>上对应版本的屏幕文件。MK1 + 套件、MK2 和 MK3：<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>。步骤相同。</p>
""")

    if page == "sensor":
        return ("Wanhao Duplicator 9 耗材传感器：断料开关与 BTT Smart Filament Sensor 接线",
                "在 Wanhao D9 主板上的哪里连接耗材传感器（D8、D9、GND、5V），如何为 BTT Smart "
                "Filament Sensor V2.0 接线，以及如何用 M412 开启断料检测和堵料检测。",
                f"""
<h1>耗材传感器</h1>
<p class="lead">从 v2.0.5 起，这些固件支持两种传感器：Wanhao 的断料开关，以及
BTT Smart Filament Sensor V2.0，后者还能发现耗材停止移动（料盘缠绕、堵料、耗材被挤出齿轮啃坏）。<strong>所有型号默认开启断料检测</strong>，堵料检测默认关闭。</p>

<h2>传感器插座</h2>
<figure><img src="{img}d9-sensor-plug-zh.svg" width="760" height="440" alt="Wanhao D9 主板：POWER-DET 左侧的 4 针传感器插座，针脚为 D9、D8、GND 和 5V，连接到 BTT Smart Filament Sensor V2.0"></figure>
<p><strong>POWER-DET</strong> 左侧、限位开关插座下方的 4 针插座，依次为 <strong>D9、D8、GND 和 5V</strong>。针脚名称来自 dustovich 找到并分享在
<a href="{DISCORD}">Discord</a> 上的一份 Wanhao 接线图；主板背面把这四个针脚分别标为 CTRL、BTN、GND 和 VCC。</p>
<ul>
<li><strong>D8</strong> 是 Wanhao 原厂固件读取的断料输入。</li>
<li><strong>D9</strong> 在 Wanhao 固件中未使用：这些固件在这里读取 BTT 传感器的运动信号。</li>
</ul>
<div class="note">在主板上插拔任何东西时，打印机都必须<strong>关机</strong>。</div>

<h2 id="screen">在屏幕上设置</h2>
<div class="split"><div>
<p>屏幕刷入 DGUS Reloaded 2.0 后（主板固件 v2.0.9 或更高版本）：<em>设置</em> → <em>耗材</em> →
<em>耗材传感器</em>。</p>
<ul>
<li><strong>断料检测</strong>开启或关闭全部检测，相当于 <code>M412 S1</code> / <code>M412 S0</code>。</li>
<li><strong>堵料检测</strong>按下方设置的长度开启堵料检测，或将其关闭（<code>L0</code>）。</li>
<li><strong>堵料长度</strong>：− 和 + 每次调整 1 mm；点击数字可直接输入。</li>
<li>断料开关检测到耗材时，<strong>耗材</strong>指示点为绿色，检测不到时为红色。</li>
<li>更改会立即生效。<strong>保存</strong>会保存这些更改，相当于 <code>M500</code>。点返回箭头则不保存直接离开：下次开机时会恢复已保存的设置。</li>
</ul>
</div><figure><img src="{img}screen/zh-sensor.png" width="480" height="272" alt="DGUS Reloaded 2.0 的耗材传感器页面：断料检测和堵料检测开关、带减号和加号按钮的堵料长度、耗材指示灯和保存按钮">
<figcaption>设置 → 耗材 → 耗材传感器</figcaption></figure></div>

<h2>M412 命令</h2>
<p>所有设置都可以通过 USB 在串口终端中完成（Pronterface、切片软件或 OctoPrint 自带的终端，250000 波特率）。多个参数可以合并在一条命令中，例如 <code>M412 S1 L10</code>。</p>
<div class="table"><table class="stack"><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>显示当前状态，例如 <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>。</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>开启检测</strong>：开启断料开关；如果堵料长度不为 0，也同时开启堵料检测。</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>关闭全部检测</strong>，包括断料开关和堵料检测。</td></tr>
<tr><td><code>M412 D5</code></td><td>断料开关检测不到耗材后，继续打印 <strong>5 mm</strong> 再暂停，以用完传感器和喷嘴之间剩余的耗材。默认 5 mm。</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>开启堵料检测</strong>（仅限 BTT 传感器）：当 <strong>10 mm</strong> 耗材经过挤出机而传感器的滚轮没有转动时暂停。</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>关闭堵料检测</strong>，断料开关保持不变。这是默认设置。</td></tr>
<tr><td><code>M500</code></td><td>保存设置。不保存的话，关机后更改就会丢失。</td></tr>
<tr><td><code>M119</code></td><td>装有耗材时 <em>filament</em> 一行显示 <code>TRIGGERED</code>，没有耗材时显示 <code>open</code>。</td></tr>
</tbody></table></div>
<p><code>M412 L0</code> 以及单独使用 <code>L</code> 的功能，来自我们对 Marlin 的修改（<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>），已集成到这些固件中。在没有这项修改的 Marlin 中，单独的 <code>L</code>
会被忽略，而 <code>L0</code> 会立即判定为堵料并暂停打印。</p>

<h2>Wanhao 断料开关</h2>
<p>它告诉固件耗材是否存在。耗材用完时，再走 5 mm 耗材后打印暂停，屏幕开始换料流程。</p>
<p><strong>从 v2.0.8 起，所有型号默认开启。</strong>D8 上什么都没接时，主板的上拉电阻会把该针脚保持在 5 V，读作“有耗材”：检测永远不会触发，所以无论是否安装了传感器，都可以保持开启。把断料开关接到 D8 上，就能直接工作。</p>
<ul>
<li>堵料检测保持关闭（<code>L0</code>）：这种开关无法看出耗材是否在移动。</li>
<li>关闭开关：<code>M412 S0</code> 然后 <code>M500</code>。</li>
<li>由早期版本保存的设置会保留其开/关状态。要开启：<code>M412 S1</code> 然后
<code>M500</code>，或恢复默认值（<code>M502</code> 然后 <code>M500</code>，这也会清除你的探针 Z
偏移和网格）。</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>这款传感器有两个输出，固件以不同方式读取它们：</p>
<ul>
<li><strong>断料开关</strong>（接 D8）是电平信号：有耗材时为 5 V，耗材用完后为 0 V。</li>
<li><strong>运动输出</strong>（接 D9）来自一个由经过的耗材带动旋转的小滚轮。耗材每前进几毫米，输出就在 0 V 和 5 V 之间翻转一次。固件只关注这些变化：如果挤出机推送了堵料长度的耗材，却一次变化都没有，说明耗材没有跟着走（料盘缠绕、堵料、耗材被啃坏），打印就会暂停。断料开关无法发现这种情况：堵料时耗材仍然在。</li>
</ul>
<h3>接线</h3>
<p><strong>5V</strong> 接 5V，<strong>GND</strong> 接 GND，<strong>断料开关</strong>信号接 <strong>D8</strong>，<strong>运动</strong>信号接 <strong>D9</strong>。传感器线缆上印的名称可能不同。</p>
<h3>开启</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>如果打印无故暂停，请加大堵料长度：<code>M412 L15</code> 然后 <code>M500</code>。如果只想保留断料开关：<code>M412 L0</code> 然后 <code>M500</code>。</p>
<h3>检查</h3>
<ul>
<li><code>M412</code>：<em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>。</li>
<li>装有耗材时 <code>M119</code>：<em>filament: TRIGGERED</em>。如果这一行是在你用手推动耗材时变化，而不是在插入或取出耗材时变化，说明两根信号线接反了：对调 D8 和 D9。</li>
</ul>
<div class="note">堵料检测已在一台未装传感器的 MK2 300 上测试过（堵料长度设为 2 mm 时会触发，<code>L0</code> 则从不触发），但尚未用 BTT 传感器本身测试。如果开关读数反了（装有耗材时显示 <em>open</em>），请在 <a href="{DISCORD}">Discord</a> 上告诉我们。</div>

<h2>从 v2.0.5 或 v2.0.6 更新</h2>
<p>这两个版本无法关闭堵料检测，因此使用了一个长到永远达不到的堵料长度：v2.0.5 中为 100 m
（实际上太短了：约为 1 kg 料盘的三分之一，超过之后，一直开着的打印机可能会无故暂停），v2.0.6 中为 10 km。打印机启动时，v2.0.7 会把这两个值载入为 <code>L0</code>。你为 BTT 传感器设置的实际长度（如 <code>L10</code>）会被保留。从 v2.0.4 或更早版本更新时，会载入 5 mm 的断料距离，而不是这些版本保存的 0。</p>
""")

    if page == "slicer":
        return ("Wanhao Duplicator 9 的 Cura 和 OrcaSlicer 配置，以及 Z 偏移的设置方法",
                "适用于所有 Wanhao D9 的现成 UltiMaker Cura 和 OrcaSlicer 配置，涵盖 PLA、PETG 和 ABS，"
                "以及如何设置探针的 Z 偏移、探测热床和打印一个测试用 3DBenchy。",
                f"""
<h1>为 Duplicator 9 切片</h1>
<p class="lead">十二台打印机各有一套配置，分别用于 <strong>UltiMaker Cura</strong> 和
<strong>OrcaSlicer</strong>，两者都免费，并且支持 Windows、macOS 和 Linux。每一套都带有对应固件自己的打印尺寸、加速度和最高热床温度。</p>

<h2>下载</h2>
{h.slicer}
<p>它们是为本站的固件制作的，<a href="{p('flash')}">v2.0.9 或更高版本</a>。</p>

<h2>安装方法</h2>
<p><strong>OrcaSlicer</strong>：<em>文件</em> → <em>导入</em> → <em>导入配置…</em>，然后选择
<code>.orca_printer</code> 文件。这台打印机、它的三种质量（0.12、0.20 和 0.28 mm）以及 PLA、PETG 和 ABS 耗材就会出现在你的预设中。</p>
<p><strong>Cura</strong>：<em>帮助</em> → <em>显示配置文件夹</em>，关闭 Cura，把文件解压到该文件夹，再启动 Cura，然后 <em>设置</em> → <em>打印机</em> → <em>添加打印机…</em> → <em>添加非联网打印机</em> →
<em>Wanhao</em> → 你的型号。Cura 自带的 <em>Wanhao Duplicator 9</em> 是一个较旧的配置：只有 300，而且默认开启了 raft 和支撑。</p>

<h2 id="first-print">第一次打印之前：先设 Z 偏移，再探测一次</h2>
<p>探针会在略高于热床的位置触发，固件必须知道高出多少。这就是 <strong>Z 偏移</strong>。太高，第一层粘不住；太低，喷嘴会刮到热床。它只需设置一次，而且正是这个设置决定了打印件粘不粘得住。</p>
<div class="note">下面这些内容都保存在打印机的存储器里，而不是切片软件里。固件更新之后依然保留（从 v2.0.3 起）。</div>

<h3>1. 先加热</h3>
<p>热的喷嘴会伸长几百分之一毫米。像打印时那样加热——在屏幕上：<em>温度</em> → <em>预热</em> → <em>PLA</em>（200 °C 和 60 °C），然后等上两分钟。</p>

<h3>2. 让各轴归零</h3>
<p>在屏幕上：<em>设置</em> → <em>移动</em> → <em>归零</em>。通过 USB：<code>G28</code>。</p>

<h3>3. 设置 Z 偏移</h3>
<p><strong>最简单的办法：边打印边调。</strong>开始一次打印，在打印<strong>第一层</strong>时进入屏幕上的
<em>调整</em> → <em>Z 偏移</em>。一边看着线条被挤出，一边以 0.01 mm 为步长往下调，直到线条变平、和旁边的线条紧挨着不留缝隙。太高时线条是圆的、彼此分开；太低时表面粗糙、被压扁，还能看到喷嘴在刮。数值会自动保存。</p>
<p><strong>用纸片的办法，不用打印。</strong>通过 USB，在打印温度下：</p>
<pre><code>M851 Z0     ; 忘掉当前的偏移
M500
G28         ; 重新归零，让它生效
M420 S0     ; 测量时忽略网格
M211 S0     ; 允许下降到 Z0 以下：软件限位会把喷嘴挡在那里
G1 Z0 F300  ; 喷嘴下降到固件认为的零点</code></pre>
<p>把一张纸塞到喷嘴下面，然后用 <code>G91</code> 再配合 <code>G1 Z-0.05 F60</code> 一小步一小步地往下调，反复进行，直到纸刚好开始有阻力。用 <code>M114</code> 读出数值：它是负数，例如 −1.30。然后：</p>
<pre><code>G90
M851 Z-1.30 ; 你的数值
M500
M211 S1     ; 恢复软件限位，它们保护着热床</code></pre>

<h3>4. 探测热床</h3>
<p>在屏幕上：<em>设置</em> → <em>调平</em> → <em>自动</em> → <em>探测</em>。打印机会测量 25 个点并<strong>自动保存网格</strong>（它会执行 <code>G29</code> 然后 <code>M500</code>）。需要几分钟。通过 USB：<code>G29</code> 然后 <code>M500</code>。</p>
<p>我们的配置不会在每次打印前探测：它们在归零之后立即用 <code>M420 S1</code> 重新启用已保存的网格。所以当你搬动打印机、更换打印表面或喷嘴，或者第一层在热床一侧好、另一侧不好时，请重新探测一次。</p>

<h3>5. 检查</h3>
<p><code>M503</code> 会列出已保存的内容：<code>M851</code> 那一行就是你的 Z 偏移，<code>M420 S1</code>
表示网格已启用。在屏幕上，<em>自动</em> 页面会显示测得的 25 个点。</p>

<h2>测试打印</h2>
<p>一个已经为 <strong>D9 MK2 300</strong> 切好片的 3DBenchy，可以用来比较两款切片软件，或者不安装任何东西就检查某个设置：</p>
<ul>
<li>Cura：<a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer：<a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>每个大约需要一个半小时和 4 m 耗材。换别的型号或尺寸时，请用你自己的配置来切片
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a>。</p>
<h3>全能测试件</h3>
<p>悬垂横杆、一段桥接、拉丝塔、公差孔和一条精细度标尺，全都集中在一个 65 mm 的模型里，约 2 小时 30 分。它是 <strong>majda107</strong> 的 <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a>（CC BY 4.0），已经为<strong>每一台打印机</strong>、两款切片软件和三种材料切好片。<a href="{REPO}/releases/latest">最新发布</a>里的文件名形如 <code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>，例如 <code>Test_D9_MK2_300_Orca_PLA.gcode</code>。</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="用 OrcaSlicer 配置在 Wanhao D9 MK2 300 上打印的 3DBenchy"><figcaption>OrcaSlicer，1 小时 14 分</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="用 Cura 配置在 Wanhao D9 MK2 300 上打印的 3DBenchy"><figcaption>Cura，1 小时 22 分</figcaption></figure>
</div>
<p><strong>先从哪一个开始：</strong>在一台 D9 MK2 300 上用 PLA 打印，同一个 Benchy 在 <strong>OrcaSlicer 里用了 1 小时 14 分</strong>，在 <strong>Cura 里用了 1 小时 22 分</strong>，而且 OrcaSlicer 打出来的外壁略微更干净一些。两款都很好；我们会从 OrcaSlicer 开始，等你想更进一步时，它的校准工具（流量、pressure advance、温度塔）就派得上用场。</p>
<div class="note">D9 是开放式的：打印 ABS 至少需要一个没有穿堂风的房间，而它的热床温度会被降到你的型号所能接受的数值（MK3 500 上为 80 °C）。</div>

<h2>配置里有什么</h2>
<ul>
<li><strong>层高</strong> 0.20 mm，<strong>3 层墙</strong>，顶部 4 层、底部 3 层，15 % 的螺旋二十四面体（gyroid）填充，2 圈裙边，不加支撑。</li>
<li><strong>速度</strong>：外墙 40 mm/s，内墙 60，填充 70，第一层 20，空驶 150。Wanhao 给出的 D9 最高打印速度是 70 mm/s。</li>
<li><strong>回抽</strong> 1.5 mm，速度 25 mm/s：所有 D9 都是 MK10 近程直驱挤出机，而固件把挤出机限制在 25 mm/s。</li>
<li><strong>温度</strong>：PLA 210 °C 然后 205，热床 65 然后 60。PETG 240 / 80 然后 235 / 75。ABS 245 / 105 然后 245 / 100。</li>
<li><strong>一条起始擦料线</strong>，距左边缘 15 mm，避开热床夹子，让喷嘴干干净净地开始打印模型。</li>
<li>打印结束时，喷嘴升起，热床移到前面。</li>
</ul>
<p>全部设置以及修改方法：GitHub 上的 <a href="{REPO}/tree/main/Slicer">Slicer 文件夹</a>。</p>
""")

    if page == "quiet":
        return ("让 Wanhao Duplicator 9 更安静：哪些风扇可以降噪，以及用 NTC 热敏电阻控制主板风扇",
                "Wanhao D9 的哪些风扇可以降噪：热端风扇必须保留，电源风扇本身已经会自动调速，"
                "主板风扇可以拔掉，或改用 NTC 热敏电阻控制。",
                f"""
<h1>让 Duplicator 9 更安静</h1>
<p class="lead">待机时，D9 的噪音来自它的风扇。下面介绍哪个风扇可以降噪，以及具体怎么做。</p>
<div class="note">操作时请<strong>拔掉</strong>打印机电源。所有导线都要远离 230 V 一侧。</div>

<h2>风扇</h2>
<div class="table"><table class="stack"><thead><tr><th>风扇</th><th>控制方式</th><th>能否降噪？</th></tr></thead><tbody>
<tr><td><strong>热端散热风扇</strong>（打印头）</td><td>无：24 V 常开</td><td><strong>不能</strong>：通常是最吵的一个，但降低转速会让热量沿热端向上蔓延，导致耗材堵塞（heat creep）</td></tr>
<tr><td><strong>模型冷却风扇</strong>（打印头）</td><td>固件，D5 针脚（PWM）</td><td>本来就可调速：由切片软件和 <code>M106</code> 设定</td></tr>
<tr><td><strong>电源风扇</strong></td><td>电源自身</td><td>无需处理：在这里检查的这台电源（Chuanglian A-350FAK-24）上，它已经会根据电源温度调速</td></tr>
<tr><td><strong>主板风扇</strong>（控制盒）</td><td>无：24 V 常开</td><td><strong>能</strong>，见下文</td></tr>
</tbody></table></div>
<p>Wanhao 固件既不控制主板风扇，也不控制热端风扇（<code>CONTROLLER_FAN_PIN</code> 和
<code>E0_AUTO_FAN_PIN</code> 都是 <code>-1</code>），主板上也没有空闲的可开关输出。所以这两个风扇接在常开的“24V OUT”接口上，任何固件都无法降低它们的转速。</p>

<h2>主板风扇</h2>
<p>在这里实测的这台机器上：<strong>HZ-D 4010MS，40 × 10 mm，24 V，最大 0.10 A，含油轴承</strong>。</p>
<p><strong>很多用户干脆把它拔掉。</strong>主板温度并不高：它位于控制盒底部、热床下方，热床的热量向上散发，不会传到它那里。如果你这么做，请留意最初几次长时间打印：步进电机驱动过热时会短暂断开，表现为<strong>层错位</strong>，而不是报错信息。</p>
<h3>保留风扇，但只在驱动变热时运转</h3>
<p>将两个功率型 NTC 热敏电阻串联，可以让风扇在约 45–50 °C 时启动，并随驱动升温而加速：<strong>MF72-400D9</strong>（400 Ω）+ <strong>MF72-200D9</strong>（200 Ω），用导热胶粘在驱动散热片上，引脚做好绝缘。</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── 风扇 (+)
                                    风扇 (−) ── 0V</code></pre>
<ul>
<li>这是计算结果，<strong>尚未在打印机上实测</strong>：MF72 的公差为 ±20 %，小风扇的启动温度可能比预期低。请先在工作台上检查启动温度（把 NTC 装进小袋子泡在热水里，配合厨房温度计）；如果启动太早就再串一个 200 Ω，太晚就去掉那个 200 Ω。</li>
<li>NTC 必须粘在散热片上：悬空时，风扇电流（NTC 上最多约 0.6 W）会让它们升温几十度。</li>
<li>用这种方式，风扇永远达不到全速（80 °C 时约为 75 %），而且 NTC 损坏时会开路：风扇就会彻底停转。</li>
</ul>
<p>资料来源：<a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">MF72 数据手册</a>。</p>
""")
    raise KeyError(page)
