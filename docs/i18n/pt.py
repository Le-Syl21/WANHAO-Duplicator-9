"""Português: translation of en.py."""

META = {"name": "Português", "locale": "pt_BR", "dir": "ltr"}

UI = {
    "nav": {"index": "Início", "mk1": "MK1", "mk1u2": "MK1 + kit MK2", "mk2": "MK2", "mk3": "MK3",
            "flash": "Guia de gravação", "screen": "Tela", "sensor": "Sensor de filamento", "slicer": "Fatiador", "quiet": "Menos ruído"},
    "language": "Idioma",
    "model": "Modelo",
    "size": "Tamanho", "volume": "Volume de impressão", "file": "Firmware",
    "footer_src": "Código-fonte e issues no GitHub", "footer_chat": "Discord",
    "footer_note": "Firmware sob a licença GNU GPL v3. Os manuais e firmwares da Wanhao continuam sendo da Wanhao.",
}

# Rótulos do diagrama de ligação do sensor (img/d9-sensor-plug-<idioma>.svg).
SVG = {
    "board": "Placa-mãe Wanhao D9 (vista de cima)",
    "plug": "conector do sensor",
    "switch": "fim de filamento",
    "motion": "movimento",
    "level": "nível: com / sem filamento",
    "pulses": "pulsos enquanto o filamento avança",
    "names": "os nomes no seu sensor podem ser diferentes",
}


def content(page, h):
    p, img, dl, rows = h.p, h.img, h.dl, h.rows
    REPO, RAW, FW, DL, DISCORD = h.REPO, h.RAW, h.FW, h.DL, h.DISCORD

    if page == "index":
        return ("Firmware Wanhao Duplicator 9 (D9 MK1, MK2, MK3) – Marlin 2.1",
                "Firmware Marlin atualizado para todas as Wanhao Duplicator 9 (D9/300, D9/400, D9/500; MK1, MK2, MK3), "
                "arquivos da tela, firmwares originais e manuais da Wanhao, e como gravá-los.",
                f"""
<h1>Firmware Wanhao Duplicator 9</h1>
<p class="lead">O site de downloads da Wanhao para a Duplicator 9 saiu do ar. Tudo o que um dono de D9 precisa está
aqui: firmware Marlin 2.1 atualizado para cada modelo e tamanho, os arquivos correspondentes da tela touch, os firmwares
originais da Wanhao, os manuais da Wanhao e guias de gravação passo a passo.</p>
<p><a class="btn" href="{REPO}/releases/latest">Todos os downloads</a> <a class="btn ghost" href="{DISCORD}">Pergunte no Discord</a></p>

<h2>Qual D9 eu tenho?</h2>
<div class="split"><div>
<ol>
<li><strong>Cabo flat cinza</strong> indo até a cabeça de impressão, uma <strong>sonda cilíndrica de metal</strong>
ao lado do bico e nenhum reforço nas laterais da estrutura: <a href="{p('mk1')}">MK1</a>.</li>
<li>A mesma máquina de primeira geração com uma <strong>sonda BLTouch branca</strong> no lugar da de metal:
uma MK1 com o kit de upgrade da Wanhao, <a href="{p('mk1u2')}">MK1 + kit MK2</a>.</li>
<li><strong>Reforços inclinados</strong> nos dois lados da estrutura, um <strong>cabo preto redondo</strong>
até a cabeça e um BLTouch: uma MK2 ou uma MK3. Olhe embaixo da mesa o <strong>motor Y</strong>, o que
movimenta a mesa: se ele fica atrás, é uma <a href="{p('mk2')}">MK2</a>; se fica na frente, do lado da tela touch, uma
<a href="{p('mk3')}">MK3</a>.</li>
</ol>
<p>O número depois de D9 é o tamanho: D9/300, D9/400 ou D9/500.</p>
</div>
<figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2 com seus reforços laterais">
<figcaption>D9 MK2: reforços laterais, cabo redondo</figcaption></figure></div>

<div class="cards">
<div class="card"><h3>D9 MK1</h3><p>Sonda indutiva, cabo flat. Firmware, Wanhao V0.15 a V0.164(B), manual.</p><a class="more" href="{p('mk1')}">Firmware MK1 →</a></div>
<div class="card"><h3>D9 MK1 + kit MK2</h3><p>MK1 atualizada com o kit BLTouch. Firmware e Wanhao V1.1.31.</p><a class="more" href="{p('mk1u2')}">Firmware do kit →</a></div>
<div class="card"><h3>D9 MK2</h3><p>BLTouch, reforços laterais. Firmware, Wanhao V1.1.2, guias.</p><a class="more" href="{p('mk2')}">Firmware MK2 →</a></div>
<div class="card"><h3>D9 MK3</h3><p>Motor Y na frente, sensor de filamento. Firmware e Wanhao V1.1.3.</p><a class="more" href="{p('mk3')}">Firmware MK3 →</a></div>
</div>

<h2>O que estes firmwares trazem</h2>
<ul>
<li><strong>Marlin 2.1</strong> compilado a partir das configurações da Duplicator 9 publicadas em
<a href="https://github.com/MarlinFirmware/Configurations/tree/bugfix-2.1.x/config/examples/Wanhao/Duplicator%209">Marlin Configurations</a>,
com as mudanças propostas lá: sonda da MK1 lida do jeito certo, sentido do Y da MK3, recuperação após queda de energia,
filtro de ruído nos fins de curso.</li>
<li><strong>As configurações de fábrica da Wanhao</strong>, tiradas do firmware e do código-fonte da própria Wanhao para cada modelo: passos/mm,
velocidades, acelerações, PID do hotend, offsets e margens de sondagem da sonda, homing, limites térmicos, jerk e sentido dos eixos.</li>
<li><strong>Recuperação após queda de energia</strong>: durante uma impressão pelo cartão SD, o trabalho é salvo a cada troca de camada e, depois de uma queda, a tela oferece retomar a partir dali.</li>
<li><strong>Sensores de filamento</strong>: um interruptor de fim de filamento no D8, ativado por padrão em todos os modelos (sem efeito se não houver nenhum), e o BTT Smart Filament Sensor V2.0, que também detecta entupimentos. Veja <a href="{p('sensor')}">Sensor de filamento</a>.</li>
<li><strong>A cabeça volta para o centro depois do nivelamento da mesa</strong>, então a mesa não esconde mais a tela.</li>
<li><strong>Uma nova interface da tela touch em 16 idiomas</strong>, <a href="{p('screen')}">DGUS Reloaded 2.0</a>, com uma página para configurar o sensor de filamento.</li>
</ul>

<h2>Gravar em três passos</h2>
<ol>
<li>Baixe o <strong>.hex</strong> do seu modelo e tamanho na página dele.</li>
<li>Grave pelo USB com AVRDUDESS ou avrdude: <a href="{p('flash')}">guia de gravação</a>.</li>
<li>Grave a tela touch a partir de um cartão microSD: <a href="{p('screen')}">guia da tela</a>.</li>
</ol>
<p>Os firmwares originais da Wanhao continuam disponíveis na página de cada modelo, então uma máquina sempre pode voltar a ficar como saiu de fábrica.</p>
""")

    if page == "mk1":
        return ("Firmware Wanhao Duplicator 9 MK1 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para a Wanhao D9 MK1 com sonda indutiva, firmwares originais da Wanhao V0.15 a V0.164(B), "
                "arquivos da tela e manual do usuário da MK1.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK1</h1>
<div class="split"><div>
<p class="lead">A primeira Duplicator 9: uma sonda indutiva de metal ao lado do bico, um cabo flat cinza até a
cabeça de impressão e uma estrutura sem reforços laterais.</p>
<p>Estas versões leem a sonda indutiva do jeito certo (ela aciona em nível baixo) e usam as configurações do último
firmware MK1 da Wanhao, a V0.164(B), incluindo os offsets da sonda (X 15, Y 0). O motor Y fica atrás, como a Wanhao montou.</p>
</div><figure><img src="{img}d9-mk1-inductive-probe.webp" width="600" height="364" alt="Sonda indutiva e cabo flat na cabeça de impressão de uma Wanhao D9 MK1">
<figcaption>MK1: sonda indutiva, cabo flat</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1")}
<p>Pegue o arquivo do seu tamanho e depois grave a tela com
<a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documentos da Wanhao</h2>
<ul>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_User_Manual.pdf">Manual do usuário D9 MK1</a> (junho de 2018, em inglês): montagem, ligações, menus, nivelamento, solução de problemas.</li>
<li><a href="{RAW}MK1/WANHAO_D9_MK1_Getting_Started_Guide.pdf">Guia de primeiros passos D9 MK1</a> (em inglês).</li>
</ul>

<h2>Firmwares originais da Wanhao</h2>
<p>Para deixar uma máquina como saiu de fábrica. Cada firmware da placa-mãe só funciona com o firmware da tela
da mesma versão.</p>
<div class="table"><table><thead><tr><th>Versão</th><th>Tamanho</th><th>Placa-mãe</th><th>Tela</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>As configurações de cada versão (passos/mm, velocidades, PID, sentido dos eixos) estão listadas em
<a href="{FW}MK1/Wanhao_factory/extract.md">extract.md</a>, lidas dos binários da Wanhao.</p>
""")

    if page == "mk1u2":
        return ("Firmware Wanhao Duplicator 9 MK1 com kit de upgrade MK2 (BLTouch) – Marlin 2.1",
                "Firmware Marlin 2.1 para uma Wanhao D9 MK1 atualizada com o kit BLTouch MK2 da Wanhao, e o firmware original do kit Wanhao V1.1.31.",
                f"""
<h1>Wanhao D9 MK1 com o kit de upgrade MK2</h1>
<div class="split"><div>
<p class="lead">Uma D9 de primeira geração com o kit de upgrade MK2 da Wanhao: a estrutura da MK1, com uma sonda BLTouch
no lugar da sonda indutiva de metal.</p>
<p>A Wanhao lançou um firmware separado para essa combinação, porque o BLTouch do kit não fica na mesma posição que o
da MK2 de fábrica: o offset Y da sonda é diferente. Estas versões usam a geometria do kit. O motor Y fica
atrás.</p>
</div><figure><img src="{img}d9-mk2-bltouch.webp" width="500" height="427" alt="Sonda BLTouch na cabeça de impressão de uma Wanhao D9">
<figcaption>Sonda BLTouch</figcaption></figure></div>

<h2>Download</h2>
{dl("MK1u2")}
<p>Pegue o arquivo do seu tamanho e depois grave a tela com
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Estas versões usam o offset da sonda do firmware do kit, Y −10. É a única linha em que o código-fonte do
kit da Wanhao difere do da MK2 de fábrica (Y 0): o BLTouch do kit fica mais para trás. Se a malha da mesa parecer deslocada
da frente para trás, meça o seu próprio offset com o <a href="{REPO}/blob/main/Offset.md">guia de offset</a>.</div>

<h2>Firmwares originais da Wanhao</h2>
<p>O firmware V1.1.31 do kit da Wanhao (dezembro de 2018), usado com o firmware da tela da MK2.</p>
<div class="table"><table><thead><tr><th>Tamanho</th><th>Placa-mãe</th><th>Tela</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Configurações lidas dos binários da Wanhao: <a href="{FW}MK1u2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk2":
        return ("Firmware Wanhao Duplicator 9 MK2 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para a Wanhao D9 MK2 com BLTouch, firmware e arquivos da tela originais da Wanhao V1.1.2, e os guias da Wanhao para a MK2.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK2</h1>
<div class="split"><div>
<p class="lead">A segunda Duplicator 9: reforços inclinados nos dois lados, um cabo de dados preto e redondo até a
cabeça de impressão, uma sonda BLTouch e um suporte de carretel em cima.</p>
<p>A Wanhao também passou os carros para quatro rodinhas, colocou um eixo Y de trilho duplo e uma correia mais grossa nas 400
e 500, e uma mesa dupla face nas 300 e 400. O motor Y fica atrás; estas versões giram o eixo Y no mesmo sentido
que o firmware V1.1.2 da Wanhao.</p>
</div><figure><img src="{img}d9-mk2.webp" width="600" height="600" alt="Wanhao Duplicator 9 MK2">
<figcaption>D9 MK2</figcaption></figure></div>

<h2>Download</h2>
{dl("MK2")}
<p>Pegue o arquivo do seu tamanho. Uma MK2 cuja cabeça também recebeu o upgrade para MK3 deve
usar o <a href="{p('mk3')}">firmware MK3</a>. Depois grave a tela com <a href="{p('screen')}">DGUS Reloaded</a>.</p>

<h2>Documentos da Wanhao</h2>
<ul>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Getting_Started_Guide.pdf">Guia de primeiros passos D9 MK2</a> (em inglês).</li>
<li><a href="{RAW}MK2/WANHAO_D9_MK2_Improvements.pdf">As 12 melhorias da MK1 para a MK2</a>, pela Wanhao (em inglês).</li>
</ul>

<h2>Firmwares originais da Wanhao</h2>
<p>A V1.1.2 da Wanhao (outubro de 2018; a 500 foi recompilada como V1.1.2.1 em julho de 2019), com o firmware da tela MK2 da Wanhao.</p>
<div class="table"><table><thead><tr><th>Tamanho</th><th>Placa-mãe</th><th>Tela</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Configurações lidas dos binários da Wanhao: <a href="{FW}MK2/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "mk3":
        return ("Firmware Wanhao Duplicator 9 MK3 (D9/300, D9/400, D9/500) – Marlin 2.1",
                "Firmware Marlin 2.1 para a Wanhao D9 MK3 (motor Y na frente, sensor de filamento) e o firmware original da Wanhao V1.1.3.",
                f"""
<h1>Firmware Wanhao Duplicator 9 MK3</h1>
<p class="lead">A última Duplicator 9 mantém a estrutura e o BLTouch da MK2, ganha um sensor de fim de filamento e leva
o motor Y para a frente, do lado da tela touch.</p>
<p>Mudar o motor de lugar inverte o eixo Y: o próprio firmware V1.1.3 da Wanhao inverte o Y, e estas versões também. O
sensor de fim de filamento vem ativado por padrão. A Wanhao não publicou offsets da sonda para a MK3, então estas versões
usam os da MK2.</p>

<h2>Download</h2>
{dl("MK3")}
<p>Pegue o arquivo do seu tamanho e depois grave a tela com
<a href="{p('screen')}">DGUS Reloaded</a>.</p>
<div class="note">Se o sensor de filamento interromper impressões aleatoriamente, desative-o com <code>M412 S0</code> e depois
<code>M500</code>. A Wanhao Europe chegou a publicar um firmware MK3 “ReverseMode” para esse problema; ele foi
removido depois e não foi possível encontrá-lo.</div>

<h2>Firmwares originais da Wanhao</h2>
<p>A V1.1.3 da Wanhao (agosto de 2019). A Wanhao não publicou nenhum firmware da tela para a MK3: os downloads da MK3 usavam o da MK2.</p>
<div class="table"><table><thead><tr><th>Tamanho</th><th>Placa-mãe</th><th>Tela</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Configurações lidas dos binários da Wanhao: <a href="{FW}MK3/Wanhao_factory/extract.md">extract.md</a>.</p>
""")

    if page == "flash":
        return ("Como gravar o firmware da placa-mãe de uma Wanhao Duplicator 9 (D9)",
                "Guia passo a passo para gravar o Marlin em uma Wanhao D9 pelo USB com AVRDUDESS ou avrdude, resolver problemas "
                "de homing e voltar ao firmware da Wanhao.",
                f"""
<h1>Gravar a placa-mãe da Duplicator 9</h1>
<p class="lead">A placa-mãe da D9 é um ATmega2560 com bootloader USB: sem gravador, sem abrir a base,
só um cabo USB.</p>

<h2>O que você precisa</h2>
<ul>
<li>Um cabo USB entre a impressora e o computador, e a impressora <strong>ligada</strong>.</li>
<li><a href="https://github.com/zkemble/AVRDUDESS">AVRDUDESS</a> (Windows, interface gráfica, o mais fácil) ou
<a href="https://github.com/avrdudes/avrdude">avrdude</a> (linha de comando, qualquer sistema).</li>
<li>O <strong>.hex</strong> do seu modelo e tamanho: <a href="{p('mk1')}">MK1</a>, <a href="{p('mk1u2')}">MK1 + kit</a>,
<a href="{p('mk2')}">MK2</a>, <a href="{p('mk3')}">MK3</a>.</li>
</ul>

<h2>Antes de gravar</h2>
<div class="note">Envie <code>M503</code> e guarde a resposta. Desde a v2.0.3, uma atualização mantém as configurações salvas na
impressora, mas atualizar <strong>para</strong> a v2.0.3 começa uma vez com os valores padrão deste firmware (a forma de salvar as
configurações mudou), e o mesmo acontece vindo do firmware da Wanhao. Depois, ajuste de novo o offset Z da sonda com <code>M851 Z…</code>
e <code>M500</code>.</div>
<p>Feche todos os programas que possam estar usando a porta da impressora: Cura, PrusaSlicer, OctoPrint, Pronterface, terminais seriais.</p>

<h2>Gravar com AVRDUDESS</h2>
<ol>
<li>Programmer: <code>wiring</code>. MCU: <code>ATmega2560</code>.</li>
<li>Port: a porta COM da sua impressora (por exemplo <code>COM3</code>). Deixe a taxa de transmissão (baud rate) no padrão.</li>
<li>Flash: escolha o arquivo .hex e clique em <strong>Program!</strong>. Leva de 30 a 60 segundos.</li>
</ol>

<h2>Gravar com avrdude</h2>
<pre><code># Windows
avrdude -v -p atmega2560 -c wiring -P COM3 -D -U flash:w:D9_MK2_300.hex:i

# Linux / macOS
avrdude -v -p atmega2560 -c wiring -P /dev/ttyUSB0 -D -U flash:w:D9_MK2_300.hex:i</code></pre>
<p>Troque a porta e o nome do arquivo pelos seus. O protocolo <code>wiring</code> escolhe sozinho a velocidade do bootloader.</p>

<h2>Primeira inicialização</h2>
<ol>
<li>Desconecte o cabo USB, desligue e ligue a impressora, e conecte o cabo de novo.</li>
<li>Conecte a <strong>250000 baud</strong> (os firmwares da Wanhao usavam 115200) e envie <code>M115</code>: a resposta mostra o novo firmware.</li>
<li>Faça o home de todos os eixos, depois o nivelamento da mesa pela tela ou com <code>G29</code>, e salve com <code>M500</code>.</li>
</ol>

<h2 id="reset">Voltar às configurações padrão deste firmware</h2>
<p>Desde a v2.0.3, uma atualização de firmware <strong>mantém</strong> as configurações salvas na impressora (offset Z da sonda,
passos/mm, PID, malha…). Por isso, os novos valores padrão de uma versão não substituem os que já estão salvos. Redefina uma vez
se você atualizar a partir da v2.0.2 ou anterior e tiver valores salvos à mão, se a impressora se comportar de forma estranha
depois de testar outros firmwares, ou sempre que quiser começar do zero:</p>
<ul>
<li><strong>Na tela:</strong> <em>Configurações</em> → <em>Mais</em> → <em>Redefinir</em> → ✓.</li>
<li><strong>Pelo USB:</strong> envie <code>M502</code> (carrega os valores padrão deste firmware) e depois <code>M500</code> (salva).</li>
</ul>
<p>Depois ajuste de novo o offset Z da sonda (<code>M851 Z…</code> e depois <code>M500</code>) e faça o nivelamento da mesa. Confira o
resultado com <code>M503</code>.</p>

<h2>Queda de energia e sensor de filamento</h2>
<ul>
<li>A recuperação após queda de energia vem ativada: o trabalho é salvo a cada troca de camada. Desative com <code>M413 S0</code> e depois <code>M500</code>.</li>
<li>Uma impressão que para na hora com <em>power outage</em> assim que começa a aquecer: atualize para a v2.0.4 ou mais recente. As versões anteriores monitoravam a entrada de falha de energia da placa, que vai para nível baixo assim que os aquecedores ligam.</li>
<li>A detecção de fim de filamento vem ativada por padrão em todos os modelos desde a v2.0.8, e não faz nada sem sensor. Depois de atualizar a partir de uma versão anterior, ative com <code>M412 S1</code> e depois <code>M500</code>, ou na tela em <em>Configurações</em> → <em>Filamento</em> → <em>Sensor de filamento</em>. Ligação e BTT Smart Filament Sensor: <a href="{p('sensor')}">Sensor de filamento</a>.</li>
</ul>

<h2>Solução de problemas</h2>
<div class="table"><table><thead><tr><th>Problema</th><th>Solução</th></tr></thead><tbody>
<tr><td>Porta em uso</td><td>Feche todos os programas que usam a porta da impressora.</td></tr>
<tr><td>Dispositivo não encontrado</td><td>Instale o driver USB CH340, tente outro cabo ou outra porta USB, confira se a impressora está ligada.</td></tr>
<tr><td>Caracteres ilegíveis depois da gravação</td><td>Use 250000 baud com estes firmwares, 115200 com os da Wanhao.</td></tr>
<tr><td>Temperaturas multiplicadas por 10 na tela (236 para 23,6 °C)</td><td>A tela ainda está com arquivos antigos: grave o <a href="{p('screen')}">DGUS Reloaded 2.0</a>.</td></tr>
<tr><td>A tela volta para o inglês a cada inicialização, ou a página <em>Sensor de filamento</em> não faz nada</td><td>O firmware da placa-mãe é anterior à v2.0.9: atualize-o.</td></tr>
<tr><td>O homing para alguns milímetros antes da chave de fim de curso, e depois aparece <em>Homing Failed</em></td><td>Ruído elétrico na linha do fim de curso. Estes firmwares filtram isso desde a v2.0.1: atualize.</td></tr>
<tr><td>O bico bate em uma presilha da mesa durante o nivelamento</td><td>Atualize para a v2.0.2 ou mais recente: a primeira coluna de sondagem fica a 10 mm da borda, como no firmware da Wanhao.</td></tr>
<tr><td>A mesa se afasta da chave de fim de curso do Y</td><td>Confira se você pegou o firmware do seu modelo: o motor Y fica atrás na MK1, na MK1 + kit e na MK2, e na frente na MK3.</td></tr>
</tbody></table></div>

<h2>Voltar ao firmware da Wanhao</h2>
<p>A página de cada modelo tem os links para os firmwares originais da placa-mãe e da tela da Wanhao. Grave-os do mesmo jeito; o
firmware da placa-mãe da Wanhao precisa do firmware da tela da Wanhao da mesma geração.</p>
<p>Dúvidas: <a href="{DISCORD}">Discord</a> ou <a href="{REPO}/issues">issues no GitHub</a>.</p>
""")

    if page == "screen":
        return ("Firmware da tela touch Wanhao Duplicator 9 (DWIN DGUS) – DGUS Reloaded 2.0 em 16 idiomas",
                "Como gravar a tela touch DWIN da Wanhao D9 com DGUS Reloaded 2.0 a partir de um cartão microSD: nova interface em 16 "
                "idiomas, página do sensor de filamento, para Marlin 2.1. E como voltar ao firmware da tela da Wanhao.",
                f"""
<h1>Gravar a tela touch da Duplicator 9</h1>
<p class="lead">Todas as D9, da MK1 à MK3, têm a mesma tela touch DWIN T5 (480 × 272). Com estes firmwares ela usa o
DGUS Reloaded 2.0, a nossa nova interface em 16 idiomas, gravada a partir de um cartão microSD.</p>
<p><a class="btn" href="{DL}DWIN_SET.zip">Baixar DWIN_SET.zip (DGUS Reloaded 2.0)</a></p>
<div class="split"><div>
<h2>O que o DGUS Reloaded 2.0 traz</h2>
<ul>
<li><strong>16 idiomas</strong>: English, Français, Deutsch, Español, Italiano, Português, Nederlands, Polski, Türkçe,
Русский, العربية, हिन्दी, 中文, 日本語, 한국어, Bahasa Indonesia. Toque na bandeira ao lado do nome da impressora na tela inicial
para trocar; a impressora lembra da escolha.</li>
<li><strong>Uma página do sensor de filamento</strong>: <em>Configurações</em> → <em>Filamento</em> → <em>Sensor de filamento</em>. Veja
<a href="{p('sensor')}#screen">Sensor de filamento</a>.</li>
<li><strong>Uma linha de status que fica</strong>: a última mensagem, <em>Ready</em> por exemplo, continua na tela em vez
de sumir depois de 30 segundos.</li>
<li><strong>Medidores de temperatura</strong> para o bico e a mesa, com a temperatura alvo marcada.</li>
<li>Um visual novo em todas as páginas: tema escuro, botões maiores, pictogramas nas janelas pop-up.</li>
</ul>
</div><figure><img src="{img}screen/pt-home.png" width="480" height="272" alt="Tela inicial do DGUS Reloaded 2.0 em uma Wanhao D9: temperaturas do bico e da mesa com medidores, linha de status, botões Imprimir, Temperatura e Configurações">
<figcaption>A tela inicial</figcaption></figure></div>
<div class="note">O DGUS Reloaded 2.0 precisa da <strong>v2.0.9 ou mais recente</strong> na placa-mãe. Com a v2.0.8 ou anterior, o
idioma volta para o inglês a cada inicialização e a página do sensor de filamento não funciona: <a href="{p('flash')}">grave a
placa-mãe</a> primeiro.</div>

<h2>1. Formatar o cartão microSD</h2>
<div class="note">FAT32 com tamanho da unidade de alocação de <strong>4096 bytes</strong>. Com qualquer outro tamanho, a tela ignora o cartão.</div>
<ul>
<li><strong>Windows</strong>: o Windows 11 muitas vezes não formata em FAT32; use o <a href="http://ridgecrop.co.uk/index.htm?guiformat.htm">GUIFormat</a>
com o tamanho da unidade de alocação em 4096.</li>
<li><strong>Linux</strong>: <code>sudo mkfs.fat -F 32 -s 8 /dev/sdX1</code> (confira antes o dispositivo com <code>lsblk</code>).</li>
<li><strong>macOS</strong>: <code>sudo newfs_msdos -F 32 -c 8 /dev/diskN</code> (confira com <code>diskutil list</code>).</li>
</ul>

<h2>2. Copiar os arquivos</h2>
<p>Descompacte o <code>DWIN_SET.zip</code> e copie a pasta <code>DWIN_SET</code> inteira para a raiz do cartão.</p>

<h2>3. Gravar</h2>
<ol>
<li>Desligue a impressora e tire-a da tomada.</li>
<li>Abra a frente da base para chegar à parte de trás da tela, onde fica o slot microSD dela.</li>
<li>Coloque o cartão e ligue. A tela mostra a atualização em 10 a 30 segundos; espere até ela reiniciar
normalmente, de 1 a 3 minutos no total.</li>
<li>Desligue, tire o cartão e feche a base.</li>
</ol>
<p>O <a href="https://www.youtube.com/watch?v=VGvtMmlBVj8">vídeo da Wanhao de atualização da tela da D9</a> mostra onde fica o slot.</p>

<h2>De onde ela vem</h2>
<p>O DGUS Reloaded 2.0 redesenha página por página o <a href="https://github.com/Neo2003/DGUS-reloaded/releases/tag/1.0.3">DGUS Reloaded 1.0.3</a>
(de Desuuuu, e depois Neo2003). O código-fonte, o programa que gera os arquivos da tela e as traduções estão
no <a href="https://github.com/Le-Syl21/DGUS-Reloaded-2">GitHub</a>. Alguma palavra errada ou estranha no seu idioma? Avise a gente no
<a href="{DISCORD}">Discord</a> ou abra uma issue lá.</p>
<p>Para voltar ao DGUS Reloaded 1.0.3, por exemplo com um firmware anterior à v2.0.9, grave o
<a href="{RAW}LCD/DWIN_SET_1.0.3.zip">DWIN_SET_1.0.3.zip</a> do mesmo jeito.</p>

<h2>Voltar à tela da Wanhao</h2>
<p>O firmware da tela da Wanhao só funciona com o firmware da placa-mãe da Wanhao. MK1: o arquivo da tela da versão
correspondente na <a href="{p('mk1')}">página da MK1</a>. MK1 + kit, MK2 e MK3:
<a href="{RAW}MK2/Wanhao_factory/DWIN_SET_MK2.zip">DWIN_SET_MK2.zip</a>. Mesmo procedimento.</p>
""")

    if page == "sensor":
        return ("Sensores de filamento na Wanhao Duplicator 9: interruptor de fim de filamento e ligação do BTT Smart Filament Sensor",
                "Onde ligar um sensor de filamento na placa-mãe da Wanhao D9 (D8, D9, GND, 5V), como ligar um BTT Smart "
                "Filament Sensor V2.0 e ativar a detecção de fim de filamento e de entupimento com M412.",
                f"""
<h1>Sensores de filamento</h1>
<p class="lead">Desde a v2.0.5, estes firmwares leem dois tipos de sensor: o interruptor de fim de filamento da Wanhao e o
BTT Smart Filament Sensor V2.0, que também percebe quando o filamento para de andar (carretel embaraçado, entupimento, filamento
mordido pela engrenagem). <strong>A detecção de fim de filamento vem ativada por padrão em todos os modelos</strong>, e a detecção de entupimento vem desativada.</p>

<h2>O conector do sensor</h2>
<figure><img src="{img}d9-sensor-plug-pt.svg" width="760" height="440" alt="Placa-mãe da Wanhao D9: o conector de sensor de 4 pinos à esquerda do POWER-DET, pinos D9, D8, GND e 5V, ligado a um BTT Smart Filament Sensor V2.0"></figure>
<p>O conector de 4 pinos à esquerda do <strong>POWER-DET</strong>, abaixo dos conectores dos fins de curso, tem <strong>D9, D8, GND e 5V</strong>,
nessa ordem. Os nomes dos pinos vêm de um diagrama de ligação da Wanhao que o dustovich encontrou e compartilhou no
<a href="{DISCORD}">Discord</a>; no verso da placa, os mesmos quatro pinos aparecem como CTRL, BTN, GND e VCC.</p>
<ul>
<li><strong>D8</strong> é a entrada de fim de filamento que o próprio firmware da Wanhao lê.</li>
<li><strong>D9</strong> não é usado pelo firmware da Wanhao: estas versões leem nele o sinal de movimento do sensor BTT.</li>
</ul>
<div class="note">Impressora <strong>desligada</strong> sempre que for ligar ou desligar qualquer coisa na placa.</div>

<h2 id="screen">Na tela</h2>
<div class="split"><div>
<p>Com o DGUS Reloaded 2.0 na tela (firmware v2.0.9 ou mais recente): <em>Configurações</em> → <em>Filamento</em> →
<em>Sensor de filamento</em>.</p>
<ul>
<li><strong>Fim de filamento</strong> ativa ou desativa toda a detecção, como <code>M412 S1</code> / <code>M412 S0</code>.</li>
<li><strong>Detecção de entupimento</strong> ativa a detecção de entupimento com o comprimento logo abaixo, ou a desativa (<code>L0</code>).</li>
<li><strong>Comprimento de entupimento</strong>: − e + mudam o valor de 1 em 1 mm; toque no número para digitá-lo.</li>
<li>O ponto <strong>Filamento</strong> fica verde enquanto o interruptor detecta filamento, e vermelho quando não detecta.</li>
<li>As mudanças valem na hora. <strong>Salvar</strong> grava as mudanças, como <code>M500</code>. A seta de voltar sai sem
salvar: as configurações salvas voltam na próxima inicialização.</li>
</ul>
</div><figure><img src="{img}screen/pt-sensor.png" width="480" height="272" alt="Página do sensor de filamento do DGUS Reloaded 2.0: chaves de detecção de fim de filamento e de entupimento, comprimento de entupimento com botões de menos e mais, indicador de filamento e botão Salvar">
<figcaption>Configurações → Filamento → Sensor de filamento</figcaption></figure></div>

<h2>Os comandos M412</h2>
<p>Tudo é configurado pelo USB em um terminal serial (Pronterface, o terminal do seu fatiador ou do OctoPrint,
250000 baud). Os parâmetros podem ser combinados em um só comando, por exemplo <code>M412 S1 L10</code>.</p>
<div class="table"><table class="stack"><thead><tr><th>Comando</th><th>O que faz</th></tr></thead><tbody>
<tr><td><code>M412</code></td><td>Mostra o estado, por exemplo <em>Filament runout ON ; Distance 5.00mm ; Motion distance 0.00mm</em>.</td></tr>
<tr><td><code>M412 S1</code></td><td><strong>Ativa a detecção</strong>: o interruptor de fim de filamento, e também a detecção de entupimento se o comprimento de entupimento não for 0.</td></tr>
<tr><td><code>M412 S0</code></td><td><strong>Desativa toda a detecção</strong>, interruptor e entupimento.</td></tr>
<tr><td><code>M412 D5</code></td><td>Quando o interruptor deixa de detectar filamento, continua imprimindo <strong>5 mm</strong> antes de pausar, para aproveitar o filamento que sobra entre o sensor e o bico. Padrão: 5 mm.</td></tr>
<tr><td><code>M412 L10</code></td><td><strong>Ativa a detecção de entupimento</strong> (só com o sensor BTT): pausa quando <strong>10 mm</strong> de filamento passam pela extrusora sem que a roda do sensor se mova.</td></tr>
<tr><td><code>M412 L0</code></td><td><strong>Desativa a detecção de entupimento</strong> e deixa o interruptor de fim de filamento como está. É o padrão.</td></tr>
<tr><td><code>M500</code></td><td>Salva as configurações. Sem ele, a mudança se perde quando a impressora é desligada.</td></tr>
<tr><td><code>M119</code></td><td>A linha <em>filament</em> mostra <code>TRIGGERED</code> com filamento carregado e <code>open</code> sem filamento.</td></tr>
</tbody></table></div>
<p><code>M412 L0</code>, e o <code>L</code> usado sozinho, vêm da nossa modificação no Marlin
(<a href="https://github.com/MarlinFirmware/Marlin/pull/28585">MarlinFirmware/Marlin#28585</a>), incluída nestes firmwares. Em um Marlin sem ela, o <code>L</code>
sozinho é ignorado e o <code>L0</code> pausa a impressão na hora, como se fosse um entupimento.</p>

<h2>O interruptor de fim de filamento da Wanhao</h2>
<p>Ele informa ao firmware se há filamento. Quando o filamento acaba, a impressão pausa depois de mais 5 mm de
filamento e a tela inicia uma troca de filamento.</p>
<p><strong>Ele vem ativado por padrão em todos os modelos, desde a v2.0.8.</strong> Sem nada ligado no D8, o resistor de
pull-up da placa mantém o pino em 5 V, o que é lido como “filamento presente”: a detecção então nunca dispara, por isso ela
pode ficar ativada com ou sem sensor instalado. Ligue um interruptor de fim de filamento no D8 e ele funciona na hora.</p>
<ul>
<li>A detecção de entupimento continua desativada (<code>L0</code>): este interruptor não consegue ver o filamento andar.</li>
<li>Para desativar o interruptor: <code>M412 S0</code> e depois <code>M500</code>.</li>
<li>As configurações salvas por uma versão anterior mantêm o estado ativado ou desativado. Para ativar: <code>M412 S1</code> e depois
<code>M500</code>, ou volte aos valores padrão (<code>M502</code> e depois <code>M500</code>, o que também apaga o offset Z da
sonda e a malha).</li>
</ul>

<h2>BTT Smart Filament Sensor V2.0</h2>
<p>Este sensor tem duas saídas, e o firmware lê cada uma de um jeito:</p>
<ul>
<li><strong>O interruptor de fim de filamento</strong> (no D8) dá um nível: 5 V enquanto há filamento, 0 V quando ele acaba.</li>
<li><strong>A saída de movimento</strong> (no D9) vem de uma rodinha que o filamento faz girar ao passar. A cada poucos
milímetros de filamento, a saída alterna entre 0 V e 5 V. O firmware só observa essas mudanças: se a
extrusora empurrar o comprimento de entupimento sem nenhuma mudança, o filamento não está acompanhando (carretel embaraçado, entupimento,
filamento mordido pela engrenagem), e a impressão pausa. O interruptor de fim de filamento não consegue ver isso: durante um entupimento, o filamento continua lá.</li>
</ul>
<h3>Ligação</h3>
<p><strong>5V</strong> no 5V, <strong>GND</strong> no GND, o sinal do <strong>interruptor de fim de filamento</strong> no <strong>D8</strong>
e o sinal de <strong>movimento</strong> no <strong>D9</strong>. Os nomes impressos no cabo do sensor podem ser diferentes.</p>
<h3>Ativar</h3>
<pre><code>M412 S1 L10
M500</code></pre>
<p>Se as impressões pausarem sem motivo, aumente o comprimento de entupimento: <code>M412 L15</code> e depois <code>M500</code>. Para manter só
o interruptor de fim de filamento: <code>M412 L0</code> e depois <code>M500</code>.</p>
<h3>Conferir</h3>
<ul>
<li><code>M412</code>: <em>Filament runout ON ; Distance 5.00mm ; Motion distance 10.00mm</em>.</li>
<li><code>M119</code> com filamento carregado: <em>filament: TRIGGERED</em>. Se essa linha mudar quando você empurra o filamento
com a mão, e não quando você o coloca ou tira, os dois fios de sinal estão trocados: inverta D8 e D9.</li>
</ul>
<div class="note">A detecção de entupimento foi testada em uma MK2 300 sem o sensor (um comprimento de entupimento de 2 mm dispara, <code>L0</code> nunca
dispara), mas ainda não com o próprio sensor BTT. Se o interruptor for lido ao contrário (<em>open</em> com filamento
carregado), avise a gente no <a href="{DISCORD}">Discord</a>.</div>

<h2>Atualizando a partir da v2.0.5 ou da v2.0.6</h2>
<p>Essas versões não tinham como desativar a detecção de entupimento, então usavam um comprimento de entupimento longo demais para ser alcançado: 100 m na
v2.0.5 (na verdade curto demais: cerca de um terço de um carretel de 1 kg, depois do qual uma impressora deixada ligada podia pausar sem motivo) e
10 km na v2.0.6. Quando a impressora inicia, a v2.0.7 carrega esses dois valores como <code>L0</code>. Um comprimento real que você configurou
para um sensor BTT, como <code>L10</code>, é mantido. A partir da v2.0.4 ou anterior, a distância de fim de filamento de 5 mm é carregada
no lugar do 0 que essas versões salvavam.</p>
""")

    if page == "slicer":
        return ("Perfis Cura e OrcaSlicer para a Wanhao Duplicator 9, e como ajustar o offset Z",
                "Perfis UltiMaker Cura e OrcaSlicer prontos para usar para todas as Wanhao D9, PLA, PETG e ABS, como "
                "ajustar o offset Z da sonda, fazer uma sondagem da mesa e imprimir um 3DBenchy de teste.",
                f"""
<h1>Fatiar para a Duplicator 9</h1>
<p class="lead">Um perfil para cada uma das doze impressoras, para o <strong>UltiMaker Cura</strong> e o
<strong>OrcaSlicer</strong>, os dois gratuitos e disponíveis no Windows, no macOS e no Linux. Cada um já traz o volume
de impressão, as acelerações e a temperatura máxima de mesa do seu próprio firmware.</p>

<h2>Download</h2>
{h.slicer}
<p>Eles são feitos para o firmware deste site, <a href="{p('flash')}">v2.0.9 ou mais recente</a>.</p>

<h2>Instalar</h2>
<p><strong>OrcaSlicer</strong>: <em>Arquivo</em> → <em>Importar</em> → <em>Importar configurações…</em>, e então
escolha o arquivo <code>.orca_printer</code>. A impressora, suas três qualidades (0,12, 0,20 e 0,28 mm) e os filamentos
PLA, PETG e ABS aparecem nas suas predefinições.</p>
<p><strong>Cura</strong>: <em>Ajuda</em> → <em>Mostrar pasta de configuração</em>, feche o Cura, descompacte o arquivo
nessa pasta, abra o Cura de novo e depois <em>Configurações</em> → <em>Impressora</em> →
<em>Adicionar impressora…</em> → <em>Adicionar uma impressora fora da rede</em> → <em>Wanhao</em> → o seu modelo. A
<em>Wanhao Duplicator 9</em> que vem com o Cura é um perfil mais antigo: só a 300, com raft e suportes ligados por
padrão.</p>

<h2 id="first-print">Antes da primeira impressão: o offset Z, e depois uma sondagem</h2>
<p>A sonda dispara um pouco acima da mesa, e o firmware precisa saber de quanto. É o <strong>offset Z</strong>. Alto
demais, a primeira camada não gruda; baixo demais, o bico raspa a mesa. Ele é ajustado uma única vez, e é o ajuste que
decide se as suas impressões grudam ou não.</p>
<div class="note">Tudo o que vem a seguir fica guardado na memória da impressora, não no fatiador. Isso sobrevive a uma
atualização de firmware (desde a v2.0.3).</div>

<h3>1. Aqueça primeiro</h3>
<p>Um bico quente fica alguns centésimos de milímetro mais comprido. Aqueça como para imprimir: na tela,
<em>Temperatura</em> → <em>Pré-aquecer</em> → <em>PLA</em> (200 °C e 60 °C), e espere uns dois minutos.</p>

<h3>2. Faça a origem dos eixos</h3>
<p>Na tela: <em>Configurações</em> → <em>Mover</em> → <em>Origem</em>. Pelo USB: <code>G28</code>.</p>

<h3>3. Ajuste o offset Z</h3>
<p><strong>O jeito mais simples, imprimindo.</strong> Comece uma impressão e, durante a <strong>primeira camada</strong>,
vá em <em>Ajustar</em> → <em>Offset Z</em> na tela. Desça de 0,01 em 0,01 mm enquanto a linha está sendo traçada, até
ela ficar plana e encostar na vizinha sem deixar vão. Alto demais deixa cordões redondos e separados; baixo demais
deixa uma superfície áspera e esmagada, com o bico cavando. O valor é salvo sozinho.</p>
<p><strong>Com uma folha de papel, sem imprimir.</strong> Pelo USB, na temperatura de impressão:</p>
<pre><code>M851 Z0     ; esquece o offset atual
M500
G28         ; refaz a origem para que ele seja levado em conta
M420 S0     ; ignora a malha durante a medição
G1 Z0 F300  ; o bico desce até o zero que o firmware acha que existe</code></pre>
<p>Passe uma folha de papel embaixo do bico e desça em passos pequenos com <code>G91</code> e depois
<code>G1 Z-0.05 F60</code>, várias vezes, até a folha começar a raspar de leve. Leia o valor com <code>M114</code>: ele
é negativo, por exemplo −1,30. Em seguida:</p>
<pre><code>G90
M851 Z-1.30 ; o seu valor
M500</code></pre>

<h3>4. Sonde a mesa</h3>
<p>Na tela: <em>Configurações</em> → <em>Nivelamento</em> → <em>Automático</em> → <em>Sondar</em>. A impressora mede
25 pontos e <strong>salva a malha sozinha</strong> (ela roda <code>G29</code> e depois <code>M500</code>). Conte alguns
minutos. Pelo USB: <code>G29</code> e depois <code>M500</code>.</p>
<p>Nossos perfis não sondam antes de cada impressão: eles religam a malha salva com <code>M420 S1</code>, logo depois
da origem. Então sonde de novo quando mudar a impressora de lugar, trocar a superfície ou o bico, ou quando a primeira
camada sair boa de um lado da mesa e não do outro.</p>

<h3>5. Confira</h3>
<p><code>M503</code> mostra o que está guardado: a linha <code>M851</code> é o seu offset Z, e <code>M420 S1</code>
indica que a malha está ativa. Na tela, a página <em>Automático</em> mostra os 25 pontos medidos.</p>

<h2>Impressões de teste</h2>
<p>Um 3DBenchy já fatiado para uma <strong>D9 MK2 300</strong>, para comparar os dois fatiadores ou conferir um ajuste
sem instalar nada:</p>
<ul>
<li>Cura: <a href="{DL}Benchy_Cura_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Cura_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Cura_ABS.gcode">ABS</a></li>
<li>OrcaSlicer: <a href="{DL}Benchy_Orca_PLA.gcode">PLA</a> · <a href="{DL}Benchy_Orca_PETG.gcode">PETG</a> ·
<a href="{DL}Benchy_Orca_ABS.gcode">ABS</a></li>
</ul>
<p>Cerca de uma hora e meia e 4 m de filamento cada um. Para outro modelo ou outro tamanho, fatie você mesmo o
<a href="https://github.com/CreativeTools/3DBenchy">3DBenchy</a> com o seu perfil.</p>
<div class="note">A D9 é aberta: o ABS pede no mínimo um cômodo sem corrente de ar, e a temperatura de mesa dele é
reduzida ao que o seu modelo aceita (80 °C numa MK3 500).</div>

<h2>O que tem nos perfis</h2>
<ul>
<li><strong>Camadas</strong> de 0,20 mm, <strong>3 paredes</strong>, 4 camadas sólidas em cima e 3 embaixo,
preenchimento giroide a 15 %, uma saia de 2 linhas, sem suporte.</li>
<li><strong>Velocidades</strong>: 40 mm/s na parede externa, 60 por dentro, 70 no preenchimento, 20 na primeira camada,
150 no deslocamento. A Wanhao dá 70 mm/s como velocidade máxima de impressão da D9.</li>
<li><strong>Retração</strong> de 1,5 mm a 25 mm/s: todas as D9 têm um extrusor MK10 direct drive, e o firmware limita o
extrusor a 25 mm/s.</li>
<li><strong>Temperaturas</strong>: PLA 210 °C e depois 205, mesa 65 e depois 60. PETG 240 / 80 e depois 235 / 75. ABS
245 / 105 e depois 245 / 100.</li>
<li><strong>Uma linha de preparação</strong> a 15 mm da borda esquerda, longe das presilhas da mesa, para o bico chegar
limpo na peça.</li>
<li>No fim, o bico sobe e a mesa vem para a frente.</li>
</ul>
<p>Todos os ajustes e como mudá-los: <a href="{REPO}/tree/main/Slicer">pasta Slicer</a> no GitHub.</p>
""")

    if page == "quiet":
        return ("Deixar uma Wanhao Duplicator 9 mais silenciosa: quais ventoinhas, e a ventoinha da placa com termistores NTC",
                "Quais ventoinhas da Wanhao D9 podem ficar mais silenciosas: a do hotend precisa ficar, a da fonte de alimentação já "
                "se regula sozinha, e a da placa pode ser desconectada ou ligada através de termistores NTC.",
                f"""
<h1>Deixar a Duplicator 9 mais silenciosa</h1>
<p class="lead">Parada, o barulho da D9 vem das ventoinhas. Veja qual delas pode ficar mais silenciosa, e como.</p>
<div class="note">Trabalhe com a impressora <strong>fora da tomada</strong>. Mantenha todos os fios longe da parte de 230 V.</div>

<h2>As ventoinhas</h2>
<div class="table"><table class="stack"><thead><tr><th>Ventoinha</th><th>Controlada por</th><th>Dá para deixar mais silenciosa?</th></tr></thead><tbody>
<tr><td><strong>Ventoinha do dissipador do hotend</strong> (cabeça de impressão)</td><td>nada: 24 V sempre ligada</td><td><strong>não</strong>: costuma ser a mais barulhenta, mas desacelerá-la deixa o calor subir pelo hotend e entope o filamento (heat creep)</td></tr>
<tr><td><strong>Ventoinha de resfriamento da peça</strong> (cabeça de impressão)</td><td>firmware, pino D5 (PWM)</td><td>já é variável: controlada pelo fatiador e pelo <code>M106</code></td></tr>
<tr><td><strong>Ventoinha da fonte de alimentação</strong></td><td>a própria fonte</td><td>não precisa fazer nada: na unidade verificada aqui (Chuanglian A-350FAK-24), ela já acompanha a temperatura da fonte</td></tr>
<tr><td><strong>Ventoinha da placa</strong> (caixa de controle)</td><td>nada: 24 V sempre ligada</td><td><strong>sim</strong>, veja abaixo</td></tr>
</tbody></table></div>
<p>O firmware da Wanhao não controla nenhuma ventoinha da placa nem do hotend (<code>CONTROLLER_FAN_PIN</code> e
<code>E0_AUTO_FAN_PIN</code> valem os dois <code>-1</code>), e a placa não tem nenhuma saída chaveada livre. É por isso que essas
duas ficam nos conectores “24V OUT”, sempre ligados, e por isso nenhum firmware consegue desacelerá-las.</p>

<h2>Ventoinha da placa</h2>
<p>Na unidade medida aqui: <strong>HZ-D 4010MS, 40 × 10 mm, 24 V, 0,10 A máx., rolamento de bucha (sleeve bearing)</strong>.</p>
<p><strong>Muitos donos simplesmente a desconectam.</strong> A placa trabalha fria: ela fica no fundo da caixa de controle, abaixo
da mesa aquecida, e o calor da mesa sobe, para longe dela. Se fizer isso, fique de olho nas suas primeiras impressões longas: um driver
de motor superaquecido desliga por um instante, o que aparece como <strong>camadas deslocadas</strong>, e não como mensagem de erro.</p>
<h3>Manter a ventoinha, mas só quando os drivers esquentam</h3>
<p>Dois termistores NTC de potência em série fazem a ventoinha partir por volta de 45–50 °C e acelerar conforme os drivers esquentam:
<strong>MF72-400D9</strong> (400 Ω) + <strong>MF72-200D9</strong> (200 Ω), colados no dissipador de um driver com adesivo
térmico, com os terminais isolados.</p>
<pre><code>+24V ── MF72-400D9 ── MF72-200D9 ── ventoinha (+)
                                    ventoinha (−) ── 0V</code></pre>
<ul>
<li>Isto é um cálculo, <strong>ainda não testado em uma impressora</strong>: a tolerância dos MF72 é de ±20 %, e uma ventoinha pequena pode
partir numa temperatura mais baixa que o esperado. Confira a temperatura de partida na bancada (os NTC num saquinho dentro de água quente, com um
termômetro de cozinha); acrescente um segundo de 200 Ω se ela partir cedo demais, tire o de 200 Ω se partir tarde demais.</li>
<li>Os NTC precisam estar colados em um dissipador: ao ar livre, a corrente da ventoinha (até cerca de 0,6 W nos NTC) os aquece
em dezenas de graus.</li>
<li>Desse jeito a ventoinha nunca chega à velocidade máxima (cerca de 75 % a 80 °C), e um NTC que queima fica em circuito aberto: aí a ventoinha para
de vez.</li>
</ul>
<p>Fontes: <a href="https://www.cantherm.com/wp-content/uploads/2018/08/MF72_AUG_2018.pdf">datasheet dos MF72</a>.</p>
""")
    raise KeyError(page)
