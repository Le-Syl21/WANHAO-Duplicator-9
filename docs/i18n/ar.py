"""العربية: translation of en.py."""

META = {"name": "العربية", "locale": "ar_AR", "dir": "rtl"}

UI = {
    "nav": {"index": "الرئيسية", "mk1": "MK1", "mk1u2": "MK1 + طقم MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "دليل التثبيت", "screen": "الشاشة", "sensor": "حساس الخيط", "slicer": "التقطيع", "quiet": "تقليل الضجيج"},
    "language": "اللغة",
    "model": "الطراز",
    "size": "المقاس", "volume": "حجم الطباعة", "file": "البرنامج الثابت",
    "footer_src": "المصدر والبلاغات على GitHub", "footer_chat": "Discord",
    "footer_note": "البرنامج الثابت مرخّص بموجب GNU GPL v3. تبقى أدلة Wanhao وبرامجها الثابتة ملكًا لـ Wanhao.",
}

# Labels of the sensor wiring diagram (img/d9-sensor-plug-<lang>.svg).
SVG = {
    "board": "اللوحة الأم لـ Wanhao D9 (منظر علوي)",
    "plug": "منفذ الحساس",
    "switch": "مفتاح نفاد الخيط",
    "motion": "الحركة",
    "level": "مستوى: الخيط موجود / غير موجود",
    "pulses": "نبضات أثناء حركة الخيط",
    "names": "قد تختلف الأسماء على حساسك",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("البرنامج الثابت (firmware) لطابعة Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "برنامج ثابت Marlin محدَّث لكل طرازات Wanhao Duplicator 9 (D9/300 وD9/400 وD9/500؛ MK1 وMK2 وMK3)، "
                "مع ملفات الشاشة والبرامج الثابتة الأصلية من Wanhao وأدلتها، وشرح طريقة تثبيتها.",
                f"""
<h1>البرنامج الثابت لطابعة Wanhao Duplicator 9</h1>
<p class="lead">اختفى موقع التنزيل الذي خصّصته Wanhao لطابعة Duplicator 9. تجد هنا بدلًا منه كل ما يحتاجه مالك D9:
برنامج Marlin 2.1 الثابت الحالي لكل طراز ومقاس، وملفات الشاشة اللمسية المطابقة له، والبرامج الثابتة الأصلية من Wanhao،
وأدلة Wanhao، وشروحات تثبيت خطوة بخطوة.</p>
<p><a class="btn" href="{REPO}/releases/latest">كل التنزيلات</a> <a class="btn ghost" href="{DISCORD}">اسأل على Discord</a></p>

<h2>ما طراز D9 الذي أملكه؟</h2>
<div class="split"><div>
<ol>
<li><strong>كابل شريطي رمادي مسطّح</strong> يصل إلى رأس الطباعة، و<strong>مجس معدني أسطواني</strong>
بجانب الفوهة، ولا توجد دعامات جانبية على الإطار: <a href="{p('mk1')}">MK1</a>.</li>
<li>الآلة نفسها من الجيل الأول ولكن مع <strong>مجس BLTouch أبيض</strong> بدل المجس المعدني:
إنها MK1 مركّب عليها طقم الترقية من Wanhao، <a href="{p('mk1u2')}">MK1 + طقم MK2</a>.</li>
<li><strong>دعامات تقوية مائلة</strong> على جانبي الإطار، و<strong>كابل أسود دائري</strong>
إلى الرأس، ومجس BLTouch: إنها MK2 أو MK3. انظر تحت السرير إلى <strong>محرك Y</strong>، وهو الذي
يحرّك السرير: إن كان في الخلف فهي <a href="{p('mk2')}">MK2</a>؛ وإن كان في الأمام، من جهة الشاشة اللمسية، فهي
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>الرقم بعد D9 هو المقاس: D9/300 أو D9/400 أو D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="طابعة Wanhao Duplicator 9 MK2 بدعامات التقوية الجانبية">
<figcaption>D9 MK2: دعامات جانبية، كابل دائري</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>مجس حثّي، كابل شريطي. البرنامج الثابت، وبرامج Wanhao من V0.15 إلى V0.164(B)، والدليل.</p><a class="more" href="{p('mk1')}">البرنامج الثابت لـ MK1 ←</a></div>
<div class="card"><h3>D9 MK1 + طقم MK2</h3><p>MK1 مُرقّاة بطقم BLTouch. البرنامج الثابت وبرنامج Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">البرنامج الثابت للطقم ←</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch، دعامات جانبية. البرنامج الثابت، وبرنامج Wanhao V1.1.2، والأدلة.</p><a class="more" href="{p('mk2')}">البرنامج الثابت لـ MK2 ←</a></div>
<div class="card"><h3>D9 MK3</h3><p>محرك Y في الأمام، حساس الخيط. البرنامج الثابت وبرنامج Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">البرنامج الثابت لـ MK3 ←</a></div>
</div>

<h2>ما الذي تضيفه هذه البرامج الثابتة</h2>
<ul>
<li><strong>Marlin 2.1</strong> مبني من إعدادات Duplicator 9 المنشورة في
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>،
مع التعديلات المقترحة هناك: قراءة مجس MK1 بالاتجاه الصحيح، واتجاه Y في MK3، والاستئناف بعد انقطاع الكهرباء،
ومرشّح التشويش لمفاتيح نهاية المسار.</li>
<li><strong>إعدادات المصنع من Wanhao</strong>، مأخوذة من البرنامج الثابت والكود المصدري من Wanhao لكل طراز: الخطوات/مم،
والسرعات، والتسارعات، وPID لرأس التسخين، وإزاحات المجس وهوامش القياس، والعودة إلى نقطة الأصل، والحدود الحرارية، وjerk، واتجاهات المحاور.</li>
<li><strong>الاستئناف بعد انقطاع الكهرباء</strong>: أثناء الطباعة من بطاقة SD تُحفظ المهمة عند كل تغيير للطبقة، وبعد الانقطاع تعرض الشاشة متابعة الطباعة من تلك النقطة.</li>
<li><strong>حساسات الخيط</strong>: مفتاح نفاد الخيط على D8، مفعّل افتراضيًا في كل الطرازات (ولا أثر له إن لم يكن موجودًا)، وحساس BTT Smart Filament Sensor V2.0 الذي يكتشف الانسداد أيضًا. راجع <a href="{p('sensor')}">حساس الخيط</a>.</li>
<li><strong>يعود الرأس إلى المنتصف بعد تسوية السرير</strong>، فلا يحجب السرير الشاشة بعد الآن.</li>
<li><strong>واجهة جديدة للشاشة اللمسية بـ 16 لغة</strong>، <a href="{p('screen')}">DGUS Reloaded 2.0</a>، مع صفحة لضبط حساس الخيط.</li>
</ul>

<h2>التثبيت في ثلاث خطوات</h2>
<ol>
<li>نزّل ملف <strong>.hex</strong> الخاص بطرازك ومقاسك من صفحته.</li>
<li>ثبّته عبر USB باستخدام AVRDUDESS أو avrdude: <a href="{p('flash')}">دليل التثبيت</a>.</li>
<li>ثبّت برنامج الشاشة اللمسية من بطاقة microSD: <a href="{p('screen')}">دليل الشاشة</a>.</li>
</ol>
<p>تبقى البرامج الثابتة الأصلية من Wanhao متاحة في صفحة كل طراز، لذا يمكن دائمًا إعادة الآلة إلى حالتها عند خروجها من المصنع.</p>
""")

    if page == "mk1":
        return ("البرنامج الثابت (firmware) لطابعة Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "برنامج Marlin 2.1 الثابت لطابعة Wanhao D9 MK1 ذات المجس الحثّي، والبرامج الثابتة الأصلية من Wanhao من V0.15 إلى V0.164(B)، "
                "وملفات الشاشة ودليل المستخدم لـ MK1.",
                f"""
<h1>البرنامج الثابت لطابعة Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">أول Duplicator 9: مجس حثّي معدني بجانب الفوهة، وكابل شريطي رمادي إلى
رأس الطباعة، وإطار بلا دعامات جانبية.</p>
<p>تقرأ هذه النسخ المجس الحثّي بالاتجاه الصحيح (ينطلق عند المستوى المنخفض LOW) وتعتمد إعدادات آخر برنامج
ثابت من Wanhao لطراز MK1، وهو V0.164(B)، بما في ذلك إزاحات المجس (X 15, Y 0). محرك Y في الخلف، كما ركّبته Wanhao.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="المجس الحثّي والكابل الشريطي على رأس الطباعة في Wanhao D9 MK1">
<figcaption>MK1: مجس حثّي، كابل شريطي</figcaption></figure></div>

<h2>التنزيل</h2>
{dl("MK1")}
<p>خذ الملف الخاص بمقاسك، ثم ثبّت برنامج الشاشة
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>مستندات Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">دليل المستخدم لـ D9 MK1</a> (يونيو 2018، بالإنجليزية): التجميع، والتوصيلات، والقوائم، والتسوية، وحل المشكلات.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">دليل البدء السريع لـ D9 MK1</a> (بالإنجليزية).</li>
</ul>

<h2>البرامج الثابتة الأصلية من Wanhao</h2>
<p>لإعادة الآلة إلى حالتها عند خروجها من المصنع. كل برنامج ثابت للوحة الأم لا يعمل إلا مع برنامج الشاشة
من الإصدار نفسه.</p>
<div class="table"><table><thead><tr><th>الإصدار</th><th>المقاس</th><th>اللوحة الأم</th><th>الشاشة</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>إعدادات كل إصدار (الخطوات/مم، والسرعات، وPID، واتجاهات المحاور) مدرجة في
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>، وقد قُرئت من الملفات الثنائية لـ Wanhao.</p>
""")

    if page == "mk1u2":
        return ("البرنامج الثابت (firmware) لطابعة Wanhao Duplicator 9 MK1 مع طقم الترقية MK2 (BLTouch) – Marlin 2.1",
                "برنامج Marlin 2.1 الثابت لطابعة Wanhao D9 MK1 مُرقّاة بطقم BLTouch من Wanhao لطراز MK2، والبرنامج الثابت الأصلي للطقم V1.1.31 من Wanhao.",
                f"""
<h1>Wanhao D9 MK1 مع طقم الترقية MK2</h1>
<div class="split"><div>
<p class="lead">طابعة D9 من الجيل الأول مركّب عليها طقم الترقية MK2 من Wanhao: إطار MK1، مع مجس BLTouch
بدل المجس الحثّي المعدني.</p>
<p>أصدرت Wanhao برنامجًا ثابتًا منفصلًا لهذه التركيبة، لأن BLTouch الخاص بالطقم لا يقع في المكان نفسه الذي يقع فيه
في MK2 الأصلية من المصنع: إزاحة Y للمجس مختلفة. تستخدم هذه النسخ أبعاد الطقم. محرك Y في
الخلف.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="مجس BLTouch على رأس طباعة Wanhao D9">
<figcaption>مجس BLTouch</figcaption></figure></div>

<h2>التنزيل</h2>
{dl("MK1u2")}
<p>خذ الملف الخاص بمقاسك، ثم ثبّت برنامج الشاشة
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">تستخدم هذه النسخ إزاحة المجس الموجودة في البرنامج الثابت للطقم، Y −10. وهو السطر الوحيد الذي يختلف فيه
مصدر الطقم لدى Wanhao عن مصدر MK2 الأصلية (Y 0): فمجس BLTouch في الطقم يقع أبعد إلى الخلف. إن بدت شبكة تسوية السرير
مزاحة من الأمام إلى الخلف، فقِس الإزاحة الخاصة بك باستخدام <a href="{REPO}/blob/main/Offset.md">دليل الإزاحة</a>.</div>

<h2>البرامج الثابتة الأصلية من Wanhao</h2>
<p>البرنامج الثابت V1.1.31 لطقم Wanhao (ديسمبر 2018)، ويُستخدم مع برنامج شاشة MK2.</p>
<div class="table"><table><thead><tr><th>المقاس</th><th>اللوحة الأم</th><th>الشاشة</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>الإعدادات المقروءة من الملفات الثنائية لـ Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("البرنامج الثابت (firmware) لطابعة Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "برنامج Marlin 2.1 الثابت لطابعة Wanhao D9 MK2 ذات BLTouch، والبرنامج الثابت الأصلي V1.1.2 وملفات الشاشة من Wanhao، وأدلة Wanhao لطراز MK2.",
                f"""
<h1>البرنامج الثابت لطابعة Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">الجيل الثاني من Duplicator 9: دعامات تقوية مائلة على الجانبين، وكابل بيانات أسود دائري إلى
رأس الطباعة، ومجس BLTouch، وحامل بكرة في الأعلى.</p>
<p>غيّرت Wanhao أيضًا العربات لتصبح بأربع عجلات، وركّبت محور Y بسكّتين وحزامًا أعرض في مقاسي 400
و500، وسريرًا بوجهين في مقاسي 300 و400. محرك Y في الخلف؛ وتدير هذه النسخ محور Y
بالاتجاه نفسه الذي يعتمده البرنامج الثابت V1.1.2 من Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="طابعة Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>التنزيل</h2>
{dl("MK2")}
<p>خذ الملف الخاص بمقاسك. أما طابعة MK2 التي رُقّي رأسها أيضًا إلى MK3 فعليها
استخدام <a href="{p('mk3')}">البرنامج الثابت لـ MK3</a>. بعد ذلك ثبّت برنامج الشاشة <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>مستندات Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">دليل البدء السريع لـ D9 MK2</a> (بالإنجليزية).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">التحسينات الاثنا عشر من MK1 إلى MK2</a>، من Wanhao (بالإنجليزية).</li>
</ul>

<h2>البرامج الثابتة الأصلية من Wanhao</h2>
<p>الإصدار V1.1.2 من Wanhao (أكتوبر 2018؛ وأُعيد بناء نسخة المقاس 500 بإصدار V1.1.2.1 في يوليو 2019)، مع برنامج شاشة MK2 من Wanhao.</p>
<div class="table"><table><thead><tr><th>المقاس</th><th>اللوحة الأم</th><th>الشاشة</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>الإعدادات المقروءة من الملفات الثنائية لـ Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("البرنامج الثابت (firmware) لطابعة Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "برنامج Marlin 2.1 الثابت لطابعة Wanhao D9 MK3 (محرك Y في الأمام، حساس الخيط) والبرنامج الثابت الأصلي V1.1.3 من Wanhao.",
                f"""
<h1>البرنامج الثابت لطابعة Wanhao Duplicator 9 MK3</h1>
<p class="lead">آخر إصدارات Duplicator 9 تحتفظ بإطار MK2 ومجس BLTouch، وتضيف حساسًا لنفاد الخيط، وتنقل
محرك Y إلى الأمام، من جهة الشاشة اللمسية.</p>
<p>نقل المحرك يعكس اتجاه محور Y: البرنامج الثابت V1.1.3 من Wanhao يعكس Y، وكذلك تفعل هذه النسخ.
حساس نفاد الخيط مفعّل افتراضيًا. لم تنشر Wanhao أي إزاحات للمجس خاصة بـ MK3، لذا تستخدم هذه النسخ
إزاحات MK2.</p>

<h2>التنزيل</h2>
{dl("MK3")}
<p>خذ الملف الخاص بمقاسك، ثم ثبّت برنامج الشاشة
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">إن كان حساس الخيط يوقف الطباعة بشكل عشوائي، فعطّله بالأمر <code>M412 S0</code> ثم
<code>M500</code>. كانت Wanhao Europe قد نشرت برنامجًا ثابتًا لـ MK3 باسم «ReverseMode» لحل هذه المشكلة؛ لكنه
حُذف منذ ذلك الحين ولم يُعثر عليه.</div>

<h2>البرامج الثابتة الأصلية من Wanhao</h2>
<p>الإصدار V1.1.3 من Wanhao (أغسطس 2019). لم تنشر Wanhao أي برنامج شاشة لـ MK3: كانت تنزيلاتها لـ MK3 تعتمد على برنامج MK2.</p>
<div class="table"><table><thead><tr><th>المقاس</th><th>اللوحة الأم</th><th>الشاشة</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>الإعدادات المقروءة من الملفات الثنائية لـ Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("كيفية تثبيت البرنامج الثابت (firmware) على اللوحة الأم لطابعة Wanhao Duplicator 9 (D9)",
                "دليل خطوة بخطوة لتثبيت Marlin على Wanhao D9 عبر USB باستخدام AVRDUDESS أو avrdude، وحل مشكلات "
                "العودة إلى نقطة الأصل، والرجوع إلى البرنامج الثابت من Wanhao.",
                f"""
<h1>تثبيت البرنامج الثابت على اللوحة الأم لطابعة Duplicator 9</h1>
<p class="lead">اللوحة الأم في D9 مبنية على ATmega2560 مع محمّل إقلاع (bootloader) عبر USB: لا حاجة إلى مبرمجة، ولا إلى فتح القاعدة،
يكفي كابل USB.</p>

<h2>ما تحتاج إليه</h2>
<ul>
<li>كابل USB بين الطابعة والحاسوب، والطابعة <strong>مُشغَّلة</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows، بواجهة رسومية، الأسهل) أو
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (سطر الأوامر، لكل الأنظمة).</li>
<li>ملف <strong>.hex</strong> الخاص بطرازك ومقاسك: <a href="{p('mk1')}">MK1</a>، <a href="{p('mk1u2')}">MK1 + الطقم</a>،
<a href="{p('mk2')}">MK2</a>، <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>قبل التثبيت</h2>
<div class="note">أرسل الأمر <code>M503</code> واحتفظ بالرد. منذ v2.0.3 يحتفظ التحديث بالإعدادات المخزّنة في
الطابعة، لكن التحديث <strong>إلى</strong> v2.0.3 يبدأ مرة واحدة من القيم الافتراضية لهذا البرنامج الثابت (لأن طريقة تخزين الإعدادات
تغيّرت)، وكذلك الأمر عند القدوم من البرنامج الثابت لـ Wanhao. بعد ذلك اضبط إزاحة Z للمجس من جديد بالأمر <code>M851 Z…</code>
ثم <code>M500</code>.</div>
<p>أغلق كل البرامج التي قد تشغل منفذ الطابعة: Cura وPrusaSlicer وOctoPrint وPronterface وطرفيات الاتصال التسلسلي.</p>

<h2>التثبيت باستخدام AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: منفذ COM الخاص بطابعتك (مثلًا <code>COM3</code>). اترك سرعة الباود على قيمتها الافتراضية.</li>
<li>Flash: اختر ملف .hex، ثم انقر <strong>Program!</strong>. يستغرق ذلك من 30 إلى 60 ثانية.</li>
</ol>

<h2>التثبيت باستخدام avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>استبدل المنفذ واسم الملف بما يخصّك. بروتوكول <code>wiring</code> يختار سرعة محمّل الإقلاع تلقائيًا.</p>

<h2>التشغيل الأول</h2>
<ol>
<li>افصل كابل USB، وأطفئ الطابعة ثم شغّلها، وأعد توصيل الكابل.</li>
<li>اتصل بسرعة <strong>250000 باود</strong> (كانت برامج Wanhao الثابتة تستخدم 115200) وأرسل <code>M115</code>: يُظهر الرد البرنامج الثابت الجديد.</li>
<li>أعد كل المحاور إلى نقطة الأصل، ثم نفّذ تسوية السرير من الشاشة أو بالأمر <code>G29</code>، واحفظ بالأمر <code>M500</code>.</li>
</ol>

<h2 id="reset">العودة إلى الإعدادات الافتراضية لهذا البرنامج الثابت</h2>
<p>منذ v2.0.3، <strong>يحتفظ</strong> تحديث البرنامج الثابت بالإعدادات المخزّنة في الطابعة (إزاحة Z للمجس، والخطوات/مم،
وPID، وشبكة التسوية…). لذلك لا تحلّ القيم الافتراضية الجديدة في أي إصدار محلّ القيم المخزّنة مسبقًا. أعد الضبط مرة واحدة عند
التحديث من v2.0.2 أو ما قبلها مع الاحتفاظ بقيم حفظتها يدويًا، أو عندما تتصرف الطابعة بشكل غريب بعد تجربة برامج
ثابتة أخرى، أو متى أردت البدء من جديد:</p>
<ul>
<li><strong>من الشاشة:</strong> <em>الإعدادات</em> ← <em>المزيد</em> ← <em>إعادة الضبط</em> ← ✓.</li>
<li><strong>عبر USB:</strong> أرسل <code>M502</code> (تحميل القيم الافتراضية لهذا البرنامج الثابت) ثم <code>M500</code> (حفظها).</li>
</ul>
<p>بعد ذلك اضبط إزاحة Z للمجس من جديد (<code>M851 Z…</code> ثم <code>M500</code>) ونفّذ تسوية السرير. تحقّق من
النتيجة بالأمر <code>M503</code>.</p>

<h2>انقطاع الكهرباء وحساس الخيط</h2>
<ul>
<li>الاستئناف بعد انقطاع الكهرباء مفعّل: تُحفظ المهمة عند كل تغيير للطبقة. لتعطيله: <code>M413 S0</code> ثم <code>M500</code>.</li>
<li>طباعة تتوقف فورًا برسالة <em>power outage</em> بمجرد بدء التسخين: حدّث إلى v2.0.4 أو أحدث. كانت النسخ السابقة تراقب مدخل اكتشاف انقطاع الكهرباء في اللوحة، وهو يقرأ مستوى منخفضًا بمجرد تشغيل السخانات.</li>
<li>اكتشاف نفاد الخيط مفعّل افتراضيًا في كل الطرازات منذ v2.0.8، ولا يفعل شيئًا من دون حساس. بعد التحديث من إصدار سابق، فعّله بالأمر <code>M412 S1</code> ثم <code>M500</code>، أو من الشاشة عبر <em>الإعدادات</em> ← <em>الخيط</em> ← <em>حساس الخيط</em>. التوصيل وحساس BTT Smart Filament Sensor: <a href="{p('sensor')}">حساس الخيط</a>.</li>
</ul>

<h2>حل المشكلات</h2>
<div class="table"><table><thead><tr><th>المشكلة</th><th>الحل</th></tr></thead><tbody>
<tr><td>المنفذ مشغول</td><td>أغلق كل البرامج التي تستخدم منفذ الطابعة.</td></tr>
<tr><td>لم يُعثر على الجهاز</td><td>ثبّت تعريف USB الخاص بـ CH340، وجرّب كابلًا أو منفذ USB آخر، وتأكّد من أن الطابعة مُشغَّلة.</td></tr>
<tr><td>رموز غير مقروءة بعد التثبيت</td><td>استخدم 250000 باود مع هذه البرامج الثابتة، و115200 مع برامج Wanhao.</td></tr>
<tr><td>درجات الحرارة تظهر مضروبة في 10 على الشاشة (236 بدل 23.6 °C)</td><td>ما زالت الشاشة تحمل ملفات قديمة: ثبّت <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>تعود الشاشة إلى الإنجليزية عند كل تشغيل، أو لا تعمل صفحة <em>حساس الخيط</em> فيها</td><td>البرنامج الثابت للوحة الأم أقدم من v2.0.9: حدّثه.</td></tr>
<tr><td>تتوقف العودة إلى نقطة الأصل قبل المفتاح ببضعة مليمترات، ثم تظهر <em>Homing Failed</em></td><td>تشويش كهربائي على خط مفتاح نهاية المسار. تُرشّحه هذه البرامج الثابتة منذ v2.0.1: حدّث.</td></tr>
<tr><td>تصطدم الفوهة بمشبك السرير أثناء التسوية</td><td>حدّث إلى v2.0.2 أو أحدث: أول عمود قياس يبعد 10 مم عن الحافة، كما في البرنامج الثابت من Wanhao.</td></tr>
<tr><td>يتحرك السرير مبتعدًا عن مفتاح Y</td><td>تأكّد من أنك أخذت البرنامج الثابت لطرازك: محرك Y في الخلف في MK1 وMK1 + الطقم وMK2، وفي الأمام في MK3.</td></tr>
</tbody></table></div>

<h2>الرجوع إلى البرنامج الثابت من Wanhao</h2>
<p>تحتوي صفحة كل طراز على روابط البرامج الثابتة الأصلية من Wanhao للوحة الأم وللشاشة. ثبّتها بالطريقة نفسها؛ فالبرنامج الثابت
للوحة الأم من Wanhao يحتاج إلى برنامج شاشة Wanhao من الجيل نفسه.</p>
<p>للأسئلة: <a href="{DISCORD}">Discord</a> أو <a href="{REPO}/issues">بلاغات GitHub</a>.</p>
""")

    if page == "screen":
        return ("البرنامج الثابت للشاشة اللمسية في Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 بـ 16 لغة",
                "كيفية تثبيت DGUS Reloaded 2.0 على شاشة DWIN اللمسية في Wanhao D9 من بطاقة microSD: واجهة جديدة بـ 16 "
                "لغة، وصفحة لحساس الخيط، لـ Marlin 2.1. وكيفية الرجوع إلى برنامج الشاشة من Wanhao.",
                f"""
<h1>تثبيت برنامج الشاشة اللمسية في Duplicator 9</h1>
<p class="lead">كل طرازات D9، من MK1 إلى MK3، تستخدم الشاشة اللمسية نفسها DWIN T5 (480 × 272). مع هذه البرامج الثابتة تعمل الشاشة
بـ DGUS Reloaded 2.0، واجهتنا الجديدة بـ 16 لغة، وتُثبَّت من بطاقة microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">تنزيل DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>ما الذي يضيفه DGUS Reloaded 2.0</h2>
<ul>
<li><strong>16 لغة</strong>: English، Français، Deutsch، Español، Italiano، Português، Nederlands، Polski، Türkçe،
Русский، العربية، हिन्दी، 中文، 日本語، 한국어، Bahasa Indonesia. المس العلم بجانب اسم الطابعة في الشاشة الرئيسية
لتغيير اللغة؛ وتتذكر الطابعة اختيارك.</li>
<li><strong>صفحة لحساس الخيط</strong>: <em>الإعدادات</em> ← <em>الخيط</em> ← <em>حساس الخيط</em>. راجع
<a href="{p('sensor')}#screen">حساس الخيط</a>.</li>
<li><strong>سطر حالة يبقى ظاهرًا</strong>: آخر رسالة، <em>Ready</em> مثلًا، تبقى على الشاشة بدل
أن تختفي بعد 30 ثانية.</li>
<li><strong>مؤشرات لدرجة الحرارة</strong> للفوهة والسرير، مع تحديد درجة الحرارة المستهدفة.</li>
<li>مظهر جديد لكل الصفحات: سمة داكنة، وأزرار أكبر، ورموز مصوّرة في النوافذ المنبثقة.</li>
</ul>
</div><figure><img src="{img}screen/ar-home.png" width="480" height="272" alt="الشاشة الرئيسية لـ DGUS Reloaded 2.0 على Wanhao D9: درجتا حرارة الفوهة والسرير مع المؤشرات، وسطر الحالة، وأزرار طباعة والحرارة والإعدادات">
<figcaption>الشاشة الرئيسية</figcaption></figure></div>
<div class="note">يحتاج DGUS Reloaded 2.0 إلى <strong>v2.0.9 أو أحدث</strong> على اللوحة الأم. مع v2.0.8 أو ما قبلها،
تعود اللغة إلى الإنجليزية عند كل تشغيل ولا تعمل صفحة حساس الخيط: <a href="{p('flash')}">ثبّت البرنامج الثابت على
اللوحة الأم</a> أولًا.</div>

<h2>1. تهيئة بطاقة microSD</h2>
<div class="note">FAT32 بحجم وحدة تخصيص <strong>4096 بايت</strong>. مع أي حجم آخر تتجاهل الشاشة البطاقة.</div>
<ul>
<li><strong>Windows</strong>: كثيرًا ما يرفض Windows 11 التهيئة بنظام FAT32؛ استخدم <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
واضبط حجم وحدة التخصيص على 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (تحقّق من اسم الجهاز أولًا بالأمر <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (تحقّق بالأمر <code>diskutil list</code>).</li>
</ul>

<h2>2. نسخ الملفات</h2>
<p>فكّ ضغط <code>DWIN_SET.zip</code> وانسخ مجلد <code>DWIN_SET</code> بالكامل إلى جذر البطاقة.</p>

<h2>3. التثبيت</h2>
<ol>
<li>أطفئ الطابعة وافصلها عن الكهرباء.</li>
<li>افتح واجهة القاعدة الأمامية للوصول إلى الجهة الخلفية للشاشة، حيث يوجد منفذ microSD الخاص بها.</li>
<li>أدخل البطاقة وشغّل الطابعة. تُظهر الشاشة التحديث خلال 10 إلى 30 ثانية؛ انتظر حتى تُعيد التشغيل
بشكل طبيعي، أي من 1 إلى 3 دقائق في المجمل.</li>
<li>أطفئ الطابعة، وأخرج البطاقة، وأغلق القاعدة.</li>
</ol>
<p>يُظهر <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">فيديو Wanhao لتحديث شاشة D9</a> مكان المنفذ.</p>

<h2>من أين أتت</h2>
<p>يعيد DGUS Reloaded 2.0 رسم <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(من تطوير Desuuuu، ثم Neo2003) صفحةً صفحة. الكود المصدري، والبرنامج الذي يولّد ملفات الشاشة، والترجمات
موجودة على <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. هل وجدت كلمة خاطئة أو غير موفّقة بلغتك؟ أخبرنا على
<a href="{DISCORD}">Discord</a> أو افتح بلاغًا هناك.</p>
<p>للرجوع إلى DGUS Reloaded 1.0.3، مثلًا مع برنامج ثابت أقدم من v2.0.9، ثبّت
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> بالطريقة نفسها.</p>

<h2>الرجوع إلى شاشة Wanhao</h2>
<p>لا يعمل برنامج الشاشة من Wanhao إلا مع البرنامج الثابت للوحة الأم من Wanhao. لطراز MK1: ملف الشاشة من الإصدار
المطابق في <a href="{p('mk1')}">صفحة MK1</a>. لـ MK1 + الطقم وMK2 وMK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. الإجراء نفسه.</p>
""")

    if page == "sensor":
        return ("حساسات الخيط في Wanhao Duplicator 9: توصيل مفتاح نفاد الخيط وحساس BTT Smart Filament Sensor",
                "أين يُوصَل حساس الخيط على اللوحة الأم لـ Wanhao D9 (D8 وD9 وGND و5V)، وكيف يُوصَل حساس BTT Smart "
                "Filament Sensor V2.0، وكيف يُفعَّل اكتشاف نفاد الخيط والانسداد بالأمر M412.",
                f"""
<h1>حساسات الخيط</h1>
<p class="lead">منذ v2.0.5 تقرأ هذه البرامج الثابتة نوعين من الحساسات: مفتاح نفاد الخيط من Wanhao، و
BTT Smart Filament Sensor V2.0 الذي يلاحظ أيضًا توقف الخيط عن الحركة (بكرة متشابكة، انسداد، خيط
متآكل). <strong>اكتشاف نفاد الخيط مفعّل افتراضيًا في كل الطرازات</strong>، أما اكتشاف الانسداد فمعطّل.</p>

<h2>منفذ الحساس</h2>
<figure><img src="{img}d9-sensor-plug-ar.svg" width="760" height="440" alt="اللوحة الأم لـ Wanhao D9: منفذ الحساس ذو الأطراف الأربعة على يسار POWER-DET، بالأطراف D9 وD8 وGND و5V، موصول بحساس BTT Smart Filament Sensor V2.0"></figure>
<p>المنفذ ذو الأطراف الأربعة على يسار <strong>POWER-DET</strong>، أسفل منافذ مفاتيح نهاية المسار، يحمل <strong>D9 وD8 وGND و5V</strong>،
بهذا الترتيب. أسماء الأطراف مأخوذة من مخطط توصيل من Wanhao عثر عليه dustovich وشاركه على
<a href="{DISCORD}">Discord</a>؛ والجهة الخلفية للوحة تطبع الأطراف الأربعة نفسها بالأسماء CTRL وBTN وGND وVCC.</p>
<ul>
<li><strong>D8</strong> هو مدخل نفاد الخيط الذي يقرؤه البرنامج الثابت من Wanhao نفسه.</li>
<li><strong>D9</strong> لا يستخدمه البرنامج الثابت من Wanhao: تقرأ هذه النسخ عليه إشارة الحركة من حساس BTT.</li>
</ul>
<div class="note">يجب أن تكون الطابعة <strong>مُطفأة</strong> أثناء توصيل أي شيء باللوحة أو فصله عنها.</div>

<h2 id="screen">على الشاشة</h2>
<div class="split"><div>
<p>مع DGUS Reloaded 2.0 على الشاشة (البرنامج الثابت v2.0.9 أو أحدث): <em>الإعدادات</em> ← <em>الخيط</em> ←
<em>حساس الخيط</em>.</p>
<ul>
<li><strong>نفاد الخيط</strong> يفعّل كل أنواع الاكتشاف أو يعطّلها، مثل <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>كشف الانسداد</strong> يفعّل اكتشاف الانسداد بالطول المحدد أدناه، أو يعطّله (<code>L0</code>).</li>
<li><strong>طول الانسداد</strong>: الزرّان − و+ يغيّرانه بمقدار 1 مم؛ المس الرقم لكتابته.</li>
<li>تكون نقطة <strong>الخيط</strong> خضراء ما دام مفتاح نفاد الخيط يرى الخيط، وحمراء عندما لا يراه.</li>
<li>تُطبَّق التغييرات فورًا. الزر <strong>حفظ</strong> يخزّنها، مثل <code>M500</code>. سهم الرجوع يخرج من دون
حفظ: تعود الإعدادات المخزّنة عند التشغيل التالي.</li>
</ul>
</div><figure><img src="{img}screen/ar-sensor.png" width="480" height="272" alt="صفحة حساس الخيط في DGUS Reloaded 2.0: مفتاحا اكتشاف نفاد الخيط والانسداد، وطول الانسداد مع زرّي الناقص والزائد، ومؤشر الخيط، وزر حفظ">
<figcaption>الإعدادات ← الخيط ← حساس الخيط</figcaption></figure></div>

<h2>أوامر M412</h2>
<p>يُضبط كل شيء عبر USB من طرفية تسلسلية (Pronterface، أو طرفية برنامج التقطيع أو OctoPrint،
بسرعة 250000 باود). يمكن جمع عدة معاملات في أمر واحد، مثل <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>الأمر</th><th>ما الذي يفعله</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>يعرض الحالة، مثلًا <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>يفعّل الاكتشاف</strong>: مفتاح نفاد الخيط، واكتشاف الانسداد أيضًا إن لم يكن طول الانسداد 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>يعطّل كل أنواع الاكتشاف</strong>، المفتاح والانسداد.</td></tr>
<tr><td><code>M412 D5</code></td><td>بعد أن يتوقف المفتاح عن رؤية الخيط، تستمر الطباعة <strong>5 مم</strong> قبل الإيقاف المؤقت، لاستهلاك الخيط المتبقي بين الحساس والفوهة. القيمة الافتراضية 5 مم.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>يفعّل اكتشاف الانسداد</strong> (لحساس BTT فقط): يوقف الطباعة مؤقتًا عندما تمر <strong>10 مم</strong> من الخيط عبر الطارد (extruder) من دون أن تدور عجلة الحساس.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>يعطّل اكتشاف الانسداد</strong> ويترك مفتاح نفاد الخيط على حاله. هذه هي القيمة الافتراضية.</td></tr>
<tr><td><code>M500</code></td><td>يحفظ الإعدادات. من دونه يضيع أي تغيير عند إطفاء الطابعة.</td></tr>
<tr><td><code>M119</code></td><td>يُظهر سطر <em>filament</em> القيمة <code>TRIGGERED</code> عند وجود الخيط، و<code>open</code> عند غيابه.</td></tr>
</tbody></table></div>
<p>الأمر <code>M412 L0</code>، واستخدام <code>L</code> وحده، مصدرهما تعديلنا على Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>)، وهو مدمج في هذه البرامج الثابتة. في Marlin من دون هذا التعديل، يُتجاهل <code>L</code>
وحده، ويوقف <code>L0</code> الطباعة فورًا على أنها انسداد.</p>

<h2>مفتاح نفاد الخيط من Wanhao</h2>
<p>يُخبر البرنامج الثابت بوجود الخيط أو عدمه. عندما ينفد الخيط، تتوقف الطباعة مؤقتًا بعد 5 مم إضافية من
الخيط وتبدأ الشاشة عملية تغيير الخيط.</p>
<p><strong>وهو مفعّل افتراضيًا في كل الطرازات منذ v2.0.8.</strong> عندما لا يكون أي شيء موصولًا بـ D8، تُبقي مقاومة
الرفع (pull-up) في اللوحة الطرف على 5 V، وهذا يُقرأ على أنه «الخيط موجود»: لذلك لا ينطلق الاكتشاف أبدًا، ويمكن تركه مفعّلًا
سواء رُكّب حساس أم لا. صِل مفتاح نفاد الخيط بـ D8 وسيعمل فورًا.</p>
<ul>
<li>يبقى اكتشاف الانسداد معطّلًا (<code>L0</code>): هذا المفتاح لا يستطيع رؤية حركة الخيط.</li>
<li>لتعطيل المفتاح: <code>M412 S0</code> ثم <code>M500</code>.</li>
<li>الإعدادات المحفوظة بإصدار سابق تحتفظ بحالة التفعيل أو التعطيل. لتفعيله: <code>M412 S1</code> ثم
<code>M500</code>، أو أعد الإعدادات الافتراضية (<code>M502</code> ثم <code>M500</code>، وهذا يمسح أيضًا إزاحة Z للمجس
وشبكة التسوية).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>لهذا الحساس مخرجان، ويقرؤهما البرنامج الثابت بطريقتين مختلفتين:</p>
<ul>
<li><strong>مفتاح نفاد الخيط</strong> (إلى D8) يعطي مستوى ثابتًا: 5 V ما دام الخيط موجودًا، و0 V بعد نفاده.</li>
<li><strong>مخرج الحركة</strong> (إلى D9) يأتي من عجلة صغيرة يُديرها الخيط أثناء مروره. كل بضعة
مليمترات من الخيط، يتبدّل المخرج بين 0 V و5 V. لا يراقب البرنامج الثابت إلا هذه التبدّلات: فإذا دفع
الطارد طولَ الانسداد من الخيط من دون أي تبدّل، فهذا يعني أن الخيط لا يتحرك (بكرة متشابكة، انسداد،
خيط متآكل)، فتتوقف الطباعة مؤقتًا. مفتاح نفاد الخيط لا يستطيع رؤية ذلك: أثناء الانسداد يبقى الخيط موجودًا.</li>
</ul>
<h3>التوصيل</h3>
<p><strong>5V</strong> إلى 5V، و<strong>GND</strong> إلى GND، وإشارة <strong>مفتاح نفاد الخيط</strong> إلى <strong>D8</strong>
وإشارة <strong>الحركة</strong> إلى <strong>D9</strong>. قد تختلف الأسماء المطبوعة على كابل الحساس.</p>
<h3>تفعيله</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>إن توقفت الطباعة مؤقتًا بلا سبب، فارفع طول الانسداد: <code>M412 L15</code> ثم <code>M500</code>. للإبقاء على
مفتاح نفاد الخيط وحده: <code>M412 L0</code> ثم <code>M500</code>.</p>
<h3>التحقق منه</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> مع وجود الخيط: <em>filament: TRIGGERED</em>. إذا تغيّر هذا السطر عندما تدفع الخيط
بيدك بدلًا من أن يتغير عند إدخاله أو إخراجه، فسلكا الإشارة معكوسان: بدّل بين D8 وD9.</li>
</ul>
<div class="note">جُرّب اكتشاف الانسداد على MK2 300 من دون الحساس (طول انسداد 2 مم ينطلق، و<code>L0</code> لا ينطلق
أبدًا)، لكن لم يُجرَّب بعد مع حساس BTT نفسه. إذا قُرئ المفتاح بالاتجاه المعكوس (<em>open</em> مع وجود
الخيط)، فأخبرنا على <a href="{DISCORD}">Discord</a>.</div>

<h2>التحديث من v2.0.5 أو v2.0.6</h2>
<p>لم يكن في هذين الإصدارين أي طريقة لتعطيل اكتشاف الانسداد، لذا استخدما طول انسداد أكبر من أن يُبلغ: 100 متر في
v2.0.5 (وهو في الواقع قصير جدًا: نحو ثلث بكرة وزنها 1 كغ، وبعده قد تتوقف طابعة تُركت مُشغَّلة مؤقتًا بلا سبب) و
10 كم في v2.0.6. عند تشغيل الطابعة، يحمّل v2.0.7 هاتين القيمتين على أنهما <code>L0</code>. أما الطول الحقيقي الذي ضبطته
لحساس BTT، مثل <code>L10</code>، فيُحتفظ به. وعند التحديث من v2.0.4 أو ما قبلها، تُحمَّل مسافة نفاد الخيط 5 مم
بدل القيمة 0 التي كانت تحفظها تلك الإصدارات.</p>
""")

    if page == "slicer":
        return ("ملفات تعريف Cura وOrcaSlicer لطابعة Wanhao Duplicator 9، وضبط إزاحة Z",
                "ملفات تعريف جاهزة لبرنامجي UltiMaker Cura وOrcaSlicer لكل طرازات Wanhao D9، مع PLA وPETG وABS، "
                "وكيف تضبط إزاحة Z للمجس، وتقيس السرير، وتطبع نموذج 3DBenchy للاختبار.",
                f"""
<h1>تقطيع النماذج لطابعة Duplicator 9</h1>
<p class="lead">ملف تعريف لكل واحدة من الطابعات الاثنتي عشرة، لبرنامجي <strong>UltiMaker Cura</strong> و
<strong>OrcaSlicer</strong>، وكلاهما مجاني ومتوفر على Windows وmacOS وLinux. يحمل كل ملف حجم الطباعة والتسارعات
وأقصى حرارة سرير في البرنامج الثابت الخاص به.</p>

<h2>التنزيل</h2>
{h.slicer}
<p>هي مصنوعة للبرنامج الثابت الموجود في هذا الموقع، <a href="{p('flash')}">v2.0.9 أو أحدث</a>.</p>

<h2>تثبيتها</h2>
<p><strong>OrcaSlicer</strong>: <em>File</em> ← <em>Import</em> ← <em>Import Configs…</em>، ثم اختر ملف
<code>.orca_printer</code>. ستظهر الطابعة، وجوداتها الثلاث (0.12 و0.20 و0.28 مم)، وخيوط PLA وPETG وABS ضمن
إعداداتك المسبقة.</p>
<p><strong>Cura</strong>: <em>Help</em> ← <em>Show Configuration Folder</em>، ثم أغلق Cura، وفكّ ضغط الملف داخل ذلك
المجلد، وأعد تشغيل Cura، ثم <em>Settings</em> ← <em>Printer</em> ← <em>Add Printer…</em> ←
<em>Add a non-networked printer</em> ← <em>Wanhao</em> ← طرازك. أما <em>Wanhao Duplicator 9</em> التي تأتي مع Cura
فهي ملف تعريف أقدم: 300 فقط، مع تفعيل الطوف والدعامات افتراضيًا.</p>

<h2 id="first-print">قبل أول طباعة: إزاحة Z، ثم قياس السرير</h2>
<p>ينطلق المجس على ارتفاع بسيط فوق السرير، وعلى البرنامج الثابت أن يعرف مقدار هذا الفارق. هذه هي
<strong>إزاحة Z</strong>. إن كانت كبيرة جدًا لم تلتصق الطبقة الأولى، وإن كانت صغيرة جدًا كشطت الفوهة السرير. تُضبط
مرة واحدة، وهي الإعداد الذي يقرّر ما إذا كانت مطبوعاتك ستلتصق أم لا.</p>
<div class="note">كل ما يلي يُحفظ في ذاكرة الطابعة، لا في برنامج التقطيع. ويبقى بعد تحديث البرنامج الثابت
(منذ v2.0.3).</div>

<h3>1. سخّن أولًا</h3>
<p>تزداد الفوهة الساخنة طولًا بأجزاء من مئة من المليمتر. سخّن كما لو كنت ستطبع: من الشاشة، <em>الحرارة</em> ←
<em>تسخين مسبق</em> ← <em>PLA</em> (200 °C و60 °C)، وانتظر دقيقتين.</p>

<h3>2. أعد المحاور إلى نقطة الأصل</h3>
<p>من الشاشة: <em>الإعدادات</em> ← <em>تحريك</em> ← <em>الأصل</em>. عبر USB: <code>G28</code>.</p>

<h3>3. اضبط إزاحة Z</h3>
<p><strong>الطريقة الأسهل، أثناء الطباعة.</strong> ابدأ طباعة، وأثناء <strong>الطبقة الأولى</strong> اذهب إلى
<em>ضبط</em> ← <em>إزاحة Z</em> على الشاشة. انزل بخطوات 0.01 مم بينما يُرسم الخط، حتى يصير مسطّحًا ويلامس الخط
المجاور من دون فراغ. إن كانت الإزاحة كبيرة جدًا بقيت الخيوط مستديرة ومنفصلة، وإن كانت صغيرة جدًا صار السطح خشنًا
وبدت الفوهة تحفر فيه. تُحفظ القيمة من تلقاء نفسها.</p>
<p><strong>طريقة الورقة، من دون طباعة.</strong> عبر USB، على حرارة الطباعة:</p>
<pre><code>M851 Z0     ; forget the current offset
M500
G28         ; home again so it is taken into account
M420 S0     ; ignore the mesh while measuring
M211 S0     ; allow going below Z0: the soft limits stop the nozzle there
G1 Z0 F300  ; the nozzle comes down to what the firmware thinks is zero</code></pre>
<p>مرّر ورقة تحت الفوهة، ثم انزل بخطوات صغيرة باستخدام <code>G91</code> ثم <code>G1 Z-0.05 F60</code>، مرة بعد
مرة، حتى تبدأ الورقة بالاحتكاك بالكاد. اقرأ القيمة بالأمر <code>M114</code>: هي سالبة، مثلًا −1.30. ثم:</p>
<pre><code>G90
M851 Z-1.30 ; your value
M500
M211 S1     ; put the soft limits back, they protect the bed</code></pre>
<p>بدءًا من الإصدار v2.1.0 يمكن الاستغناء عن سطرَي <code>M211</code>: فالبرنامج الثابت يسمح أصلًا بنزول الفوهة 3 مم تحت الصفر.</p>

<h3>4. قِس السرير</h3>
<p>من الشاشة: <em>الإعدادات</em> ← <em>تسوية السرير</em> ← <em>تلقائي</em> ← <em>قياس</em>. تقيس الطابعة 25 نقطة
و<strong>تحفظ الشبكة بنفسها</strong> (تنفّذ <code>G29</code> ثم <code>M500</code>). يستغرق ذلك بضع دقائق. عبر USB:
<code>G29</code> ثم <code>M500</code>.</p>
<p>لا تقيس ملفات التعريف لدينا السرير قبل كل طباعة: بل تعيد تفعيل الشبكة المحفوظة بالأمر <code>M420 S1</code> مباشرة
بعد العودة إلى نقطة الأصل. لذا أعد القياس عندما تنقل الطابعة، أو تغيّر سطح الطباعة أو الفوهة، أو عندما تكون الطبقة
الأولى جيدة في جهة من السرير وسيئة في الجهة الأخرى.</p>

<h3>5. تحقّق</h3>
<p>يعرض <code>M503</code> ما هو محفوظ: سطر <code>M851</code> هو إزاحة Z، و<code>M420 S1</code> يعني أن الشبكة
مفعّلة. وعلى الشاشة، تعرض صفحة <em>تلقائي</em> النقاط الـ25 المقيسة.</p>

<h2>طباعات اختبار</h2>
<p>نموذج 3DBenchy مقطَّع مسبقًا لطابعة <strong>D9 MK2 300</strong>، لمقارنة البرنامجين أو للتحقق من إعداد من دون
تثبيت أي شيء:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>يستغرق كل واحد نحو ساعة ونصف ويستهلك 4 أمتار من الخيط. لطراز آخر أو مقاس آخر، قطّع
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> بنفسك بملف التعريف الخاص بك.</p>
<h3>اختبار الكل في واحد</h3>
<p>قضبان بارزة، وجسر، وأبراج لاختبار الخيوط، وثقوب للتفاوتات، وسلّم للدقة، كلها في قطعة واحدة بطول 65 مم، نحو ساعتين
و30 دقيقة. إنه <a href="https://www.thingiverse.com/thing:2656594">All In One 3D printer test</a> من إعداد
<strong>majda107</strong> (CC BY 4.0)، مقطَّع لكل <strong>الطابعات</strong> وللبرنامجين معًا، وبالمواد الثلاث. تحمل ملفات
<a href="{REPO}/releases/latest">أحدث إصدار</a> أسماء مثل
<code>Test_D9_&lt;model&gt;_&lt;size&gt;_&lt;slicer&gt;_&lt;material&gt;.gcode</code>، مثل
<code>Test_D9_MK2_300_Orca_PLA.gcode</code>.</p>
<div class="cards">
<figure><img src="{img}benchy-orca.webp" width="760" height="621" alt="نموذج 3DBenchy مطبوع بملف تعريف OrcaSlicer على طابعة Wanhao D9 MK2 300"><figcaption>OrcaSlicer، ساعة و14 دقيقة</figcaption></figure>
<figure><img src="{img}benchy-cura.webp" width="760" height="685" alt="نموذج 3DBenchy مطبوع بملف تعريف Cura على طابعة Wanhao D9 MK2 300"><figcaption>Cura، ساعة و22 دقيقة</figcaption></figure>
<figure><img src="{img}benchy-petg-dustovich.webp" width="760" height="594" alt="نموذج 3DBenchy مطبوع بخيط PETG على طابعة Wanhao D9، من dustovich"><figcaption>PETG · dustovich</figcaption></figure>
</div>
<p><strong>بأيّهما تبدأ:</strong> على طابعة D9 MK2 300 وبخيط PLA، استغرق النموذج Benchy نفسه <strong>ساعة و14 دقيقة مع
OrcaSlicer</strong> و<strong>ساعة و22 دقيقة مع Cura</strong>، وخرجت جدران OrcaSlicer أنظف قليلًا. كلاهما جيد، ونحن
نبدأ بـOrcaSlicer، كما تنفع أدوات المعايرة فيه (التدفق، pressure advance، أبراج الحرارة) متى أردت الذهاب أبعد.</p>
<div class="note">الـD9 مفتوحة: يحتاج ABS على الأقل إلى غرفة بلا تيارات هواء، وحرارة سريره مخفَّضة إلى ما يقبله
طرازك (80 °C على MK3 500).</div>

<h2>ما في ملفات التعريف</h2>
<ul>
<li><strong>طبقات</strong> بسماكة 0.20 مم، و<strong>3 جدران</strong>، و4 طبقات مصمتة في الأعلى و3 في الأسفل، وحشو
gyroid بنسبة 15 %، وتنورة من سطرين، وبلا دعامات.</li>
<li><strong>السرعات</strong>: 40 مم/ث على الجدار الخارجي، و60 في الداخل، و70 للحشو، و20 في الطبقة الأولى، و150 في
التنقّل. تذكر Wanhao أن 70 مم/ث هي أقصى سرعة طباعة لـ D9.</li>
<li><strong>الارتداد</strong> 1.5 مم بسرعة 25 مم/ث: كل طابعات D9 فيها طارد MK10 مباشر، والبرنامج الثابت يحدّ سرعة
الطارد بـ25 مم/ث.</li>
<li><strong>الحرارات</strong>: PLA عند 210 °C ثم 205، والسرير عند 65 ثم 60. PETG عند 240 / 80 ثم 235 / 75. ABS
عند 245 / 105 ثم 245 / 100.</li>
<li><strong>خط تمهيد</strong> على بعد 15 مم من الحافة اليسرى، بعيدًا عن مشابك السرير، لتصل الفوهة نظيفة إلى
القطعة.</li>
<li>في النهاية ترتفع الفوهة ويتقدّم السرير إلى الأمام.</li>
</ul>
<p>كل الإعدادات وكيفية تعديلها: <a href="{REPO}/tree/main/Slicer">مجلد Slicer</a> على GitHub.</p>
""")

    if page == "quiet":
        return ("تقليل ضجيج Wanhao Duplicator 9: أي المراوح، ومروحة اللوحة مع ثرمستورات NTC",
                "أيّ مراوح Wanhao D9 يمكن تقليل ضجيجها: مروحة رأس التسخين يجب أن تبقى، ومروحة مزوّد الطاقة "
                "تنظّم نفسها أصلًا، ومروحة اللوحة يمكن فصلها أو تشغيلها عبر ثرمستورات NTC.",
                f"""
<h1>تقليل ضجيج Duplicator 9</h1>
<p class="lead">في وضع الخمول، يأتي ضجيج D9 من مراوحها. إليك أيها يمكن تقليل ضجيجه، وكيف.</p>
<div class="note">اعمل والطابعة <strong>مفصولة عن الكهرباء</strong>. أبعِد كل الأسلاك عن جهة 230 V.</div>

<h2>المراوح</h2>
<div class="table"><table class="stack"><thead><tr><th>المروحة</th><th>يتحكم بها</th><th>هل يمكن تقليل ضجيجها؟</th></tr></thead><tbody>
<tr><td><strong>مروحة مشتت حرارة رأس التسخين</strong> (رأس الطباعة)</td><td>لا شيء: 24 V تعمل دائمًا</td><td><strong>لا</strong>: هي عادةً الأعلى صوتًا، لكن إبطاءها يسمح للحرارة بالصعود في رأس التسخين فيسدّ الخيط (heat creep)</td></tr>
<tr><td><strong>مروحة تبريد القطعة</strong> (رأس الطباعة)</td><td>البرنامج الثابت، الطرف D5 (PWM)</td><td>متغيرة السرعة أصلًا: يضبطها برنامج التقطيع و<code>M106</code></td></tr>
<tr><td><strong>مروحة مزوّد الطاقة</strong></td><td>مزوّد الطاقة نفسه</td><td>لا حاجة لأي شيء: في الوحدة التي فُحصت هنا (Chuanglian A-350FAK-24) تتبع أصلًا درجة حرارة المزوّد</td></tr>
<tr><td><strong>مروحة اللوحة</strong> (صندوق التحكم)</td><td>لا شيء: 24 V تعمل دائمًا</td><td><strong>نعم</strong>، انظر أدناه</td></tr>
</tbody></table></div>
<p>البرنامج الثابت من Wanhao لا يتحكم بأي مروحة للوحة ولا بمروحة رأس التسخين (<code>CONTROLLER_FAN_PIN</code> و
<code>E0_AUTO_FAN_PIN</code> كلاهما <code>-1</code>)، وليس في اللوحة أي مخرج مُتحكَّم به متاح. لهذا تعمل هاتان
المروحتان من موصلات «24V OUT» الدائمة التشغيل، ولهذا لا يستطيع أي برنامج ثابت إبطاءهما.</p>

<h2>مروحة اللوحة</h2>
<p>في الوحدة التي قيست هنا: <strong>HZ-D 4010MS، 40 × 10 مم، 24 V، 0.10 A كحد أقصى، محمل انزلاقي (sleeve)</strong>.</p>
<p><strong>كثير من المالكين يفصلونها ببساطة.</strong> حرارة اللوحة منخفضة: فهي في أسفل صندوق التحكم، تحت
السرير الساخن، وحرارة السرير تصعد بعيدًا عنها. إن فعلت ذلك، فراقب أولى طباعاتك الطويلة: مشغّل المحرك (driver)
الذي ترتفع حرارته ينقطع لحظيًا، ويظهر ذلك على شكل <strong>طبقات مُزاحة</strong>، لا على شكل رسالة خطأ.</p>
<h3>الإبقاء عليها، ولكن فقط عندما تسخن المشغّلات</h3>
<p>ثرمستوران NTC للقدرة موصولان على التوالي يجعلان المروحة تبدأ الدوران عند نحو 45–50 °C وتتسارع كلما سخنت المشغّلات:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω)، مُلصقان على مشتت حرارة أحد المشغّلات بلاصق
حراري، مع عزل أطرافهما.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── fan (+)
                                    fan (−) ── 0V</code></pre>
<ul>
<li>هذا حساب نظري، <strong>ولم يُجرَّب على طابعة بعد</strong>: تفاوت MF72 هو ±20 %، وقد تبدأ مروحة صغيرة
الدوران عند درجة أقل من المتوقع. تحقّق من درجة بدء الدوران على طاولة العمل (ثرمستورات NTC في كيس صغير داخل ماء ساخن، مع
ميزان حرارة للمطبخ)؛ أضف ثرمستورًا ثانيًا بقيمة 200 Ω إن بدأت مبكرًا جدًا، واحذف ثرمستور 200 Ω إن بدأت متأخرة جدًا.</li>
<li>يجب لصق ثرمستورات NTC على مشتت حرارة: في الهواء الطلق، يسخّنها تيار المروحة (حتى نحو 0.6 W في ثرمستورات NTC) بعشرات
الدرجات.</li>
<li>لا تبلغ المروحة سرعتها القصوى بهذه الطريقة أبدًا (نحو 75 % عند 80 °C)، وثرمستور NTC الذي يتعطل يصبح دائرة مفتوحة: فتتوقف المروحة
نهائيًا.</li>
</ul>
<p>المصادر: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">ورقة بيانات MF72</a> (بالإنجليزية).</p>
""")
    raise KeyError(page)
