"""Fontes independentes do curso; monta aulas e invoca o motor oficial v6."""
from pathlib import Path
from html import escape as esc
import json, re, subprocess, sys

ROOT = Path(__file__).resolve().parent
SKILL = Path('/home/nmaldaner/projetos/formato-curso-ARCKHê/formato-curso-v6')
base = json.loads((ROOT/'context/conteudo-base.json').read_text())
lessons = json.loads((ROOT/'context/aulas-editoriais.json').read_text())

def clean(text):
    substitutions = {
        'download':'salvamento', 'upload':'envio', 'JSON':'ficha estruturada', 'backup':'cêÂ³pia de seguranêÂ§a',
        'briefing':'resumo da encomenda', 'invariantes':'caracterêÂ­sticas fixas', 'pipeline':'sequêÂªncia de trabalho', 'workflow':'sequêÂªncia de trabalho',
        'êÂ  direita':'no lado da alêÂ§a', 'êÂ  esquerda':'pelo lado da janela',
        'nos materiais':'no aprofundamento desta aula',
        'no material':'no aprofundamento desta aula',
        'a ficha SVG do produto disponêÂ­vel nos materiais':'uma foto prêÂ³pria de objeto',
        'Consulte a documentaêÂ§êÂ£o de Seeds nos materiais.':'Confira a explicaêÂ§êÂ£o desse controle na ferramenta utilizada.',
    }
    for a,b in substitutions.items(): text=text.replace(a,b)
    return text

def p(text, cls=''):
    return f'<p{(" class="+chr(34)+cls+chr(34)) if cls else ""}>{esc(clean(text))}</p>'

def sentence_paragraphs(text):
    return ''.join(p(t) for t in re.split(r'(?<=[.!?])\s+',text))

def comparison(d, n):
    # Esses quadros mostram instruêÂ§êÂµes e critêÂ©rios autorais, sem simular saêÂ­das de um modelo.
    if n == 1 or n % 3 == 2:
        return f'''<figure class="largo"><div class="tela">
<div class="tela-top"><i></i><i></i><i></i><span>Pedidos para comparar êÂ· exemplo didêÂ¡tico</span></div>
<div class="tela-caso" data-rotulo="Pedido vago"><div class="tela-body"><p class="msg eu"><span class="quem">Pedido</span>{esc(d['antes'])}</p></div><p class="tela-nota ruim">Faltam limites observêÂ¡veis para conferir o trabalho.</p></div>
<div class="tela-caso" data-rotulo="Pedido verificêÂ¡vel"><div class="tela-body"><p class="msg eu"><span class="quem">Pedido</span>{esc(d['depois'])}</p></div><p class="tela-nota bom">HêÂ¡ uma mudanêÂ§a definida e algo que precisa permanecer.</p></div>
</div><figcaption>Compare as duas instruêÂ§êÂµes. SêÂ£o exemplos escritos para a aula, sem resposta simulada de ferramenta.</figcaption></figure>'''
    return f'''<figure class="largo"><div class="lado"><div class="antes"><span class="rot">DecisêÂ£o frêÂ¡gil</span>{p(d['antes'])}</div><div class="depois"><span class="rot">DecisêÂ£o verificêÂ¡vel</span>{p(d['depois'])}</div></div><figcaption>Observe quais caracterêÂ­sticas tornam a segunda decisêÂ£o conferêÂ­vel.</figcaption></figure>'''

def window(d):
    items=''.join(f'<div class="item doc"><span class="pin">{i}</span>{esc(x)}</div>' for i,x in enumerate(d['campos'],1))
    return f'<figure class="largo"><div class="janela"><div class="tela-top"><i></i><i></i><i></i><span>Ficha preenchida êÂ· exemplo da aula</span></div><div class="janela-body">{items}</div></div><figcaption>Use esta ficha como referêÂªncia. Troque o exemplo pelo seu prêÂ³prio produto.</figcaption></figure>'

def extra_visual_unused(n):
    if n==1:
        return '<figure class="largo"><div class="janela"><div class="janela-body"><div class="item doc">Modelo ê¢â â gera a imagem</div><div class="item doc">Plataforma ê¢â â mostra o campo de pedido e os botêÂµes</div><div class="item doc">Editor ê¢â â permite recortar e acrescentar texto</div></div></div><figcaption>Um aplicativo pode reunir mais de uma funêÂ§êÂ£o. Identifique o que ele permite fazer.</figcaption></figure>'
    if n==4:
        return '<figure class="largo"><img src="assets/img/aula-21.webp" width="1280" height="720" style="width:100%;height:auto" alt="TrêÂªs fotos ilustradas mostram produto inteiro, detalhe da alêÂ§a e caneca na mêÂ£o."><figcaption>Compare as trêÂªs fotos: produto inteiro, detalhe da alêÂ§a e uso. Cada recorte responde a uma pergunta.</figcaption></figure>'
    if n==5:
        return '''<figure class="diag"><svg viewBox="0 0 600 220" role="img" aria-label="ComparaêÂ§êÂ£o esquemêÂ¡tica de sombra com borda marcada e sombra suave">
<defs><radialGradient id="sombra-suave"><stop offset="0" stop-color="var(--ink)" stop-opacity=".35"/><stop offset="1" stop-color="var(--ink)" stop-opacity="0"/></radialGradient></defs>
<rect x="8" y="8" width="282" height="204" rx="12" fill="var(--panel)"/><rect x="308" y="8" width="282" height="204" rx="12" fill="var(--panel)"/>
<ellipse cx="170" cy="148" rx="80" ry="22" fill="var(--ink)" opacity=".32"/><ellipse cx="470" cy="148" rx="95" ry="35" fill="url(#sombra-suave)"/>
<rect x="62" y="70" width="65" height="78" rx="8" fill="var(--warm)"/><rect x="362" y="70" width="65" height="78" rx="8" fill="var(--warm)"/>
<text x="45" y="40" fill="var(--ink)" font-size="28">Borda marcada</text><text x="350" y="40" fill="var(--ink)" font-size="28">Borda suave</text>
<text x="45" y="195" fill="var(--ink)" font-size="26">TransiêÂ§êÂ£o abrupta</text><text x="350" y="195" fill="var(--ink)" font-size="26">TransiêÂ§êÂ£o gradual</text></svg><figcaption>Esquema da borda da sombra. Compare como ela termina, sem confundir sombra com material do objeto.</figcaption></figure>'''
    if n==7:
        return '<figure class="largo"><div class="lado"><div class="neutro"><span class="rot">512 êâ 512 pixels</span><div style="width:100px;height:100px;border:2px solid var(--accent);margin:12px auto"></div><p>Quadrado êÂ· 1:1</p></div><div class="bom"><span class="rot">1024 êâ 1024 pixels</span><div style="width:100px;height:100px;border:2px solid var(--accent);margin:12px auto"></div><p>Quadrado êÂ· 1:1</p></div></div><figcaption>RepresentaêÂ§êÂµes no mesmo tamanho de tela. A proporêÂ§êÂ£o permanece; as dimensêÂµes do arquivo mudam.</figcaption></figure>'
    return ''

def extra_visual(n):
    return ""

def third_visual(d,n):
    return f'<figure class="largo"><img src="assets/img/aula-{n}.webp" width="1280" height="720" loading="lazy" style="width:100%;height:auto;border-radius:12px" alt="{esc(d["observacao"])}"><figcaption><b>IlustraêÂ§êÂ£o Codex, nêÂ£o resultado do Nano Banana:</b> {esc(d["observacao"])}</figcaption></figure>'

for i,d in enumerate(lessons,1):
    m=base['modules'][(i-1)//3]
    start=((i-1)%3)*2
    topics=m['topics'][start:start+2]
    steps=[]
    for j,t in enumerate(topics,1):
        prose=sentence_paragraphs(t['concept'])+sentence_paragraphs(t['why'])
        if i==1 and j==1:
            prose=prose.replace('Modelo êÂ© o sistema', '<span class="gterm" data-def="Sistema que produz a imagem; seu nome pode ser diferente do nome da conversa.">Modelo</span> êÂ© o sistema')
        example=f'<p data-ex="{"designer" if j==1 else "comerciante"}">{esc(d["ex"+str(j)])}</p>'
        visual=(comparison(d,i) if j==1 else window(d)) + (extra_visual(i) if j==1 else '')
        steps.append(f'<section class="step" data-kind="fundamento"><h2><span class="n">{j}</span>{esc(t["title"])}</h2>{prose}{example}{visual}</section>')
    feedback=['Essa escolha nêÂ£o resolve o critêÂ©rio principal do caso.']*3
    feedback[d['correta']]='Essa escolha atende ao problema observado e preserva o objetivo da peêÂ§a.'
    options=''.join(f'<button class="opt" data-k="{chr(97+j)}" data-fb="{esc(feedback[j])}">{esc(o)}</button>' for j,o in enumerate(d['opcoes']))
    quiz=f'<div class="quiz" data-answer="{chr(97+d["correta"])}"><p class="qk">Teste-se</p><p class="q">{esc(d["q"])}</p>{options}<p class="qfb" aria-live="polite"></p></div>'
    steps.append(f'<section class="step" data-kind="pratica"><h2><span class="n">3</span>Confira a decisêÂ£o pelo uso</h2>{p(d["confira"])}<p data-ex="comerciante">Renato usa a observaêÂ§êÂ£o abaixo para decidir: {esc(d["campos"][-1].lower())}.</p>{third_visual(d,i)}{quiz}<div class="calma"><p><span class="k">Se travou aqui, êÂ© normal</span>{esc(d["calma"])}</p></div></section>')
    checklist=''.join(f'<li><label><input type="checkbox" data-ptask="{j}"><span>{esc(x)}</span></label></li>' for j,x in enumerate(d['passos'],1))
    summary=''.join(f'<li>{esc(x)}</li>' for x in d['resumo'])
    cola=''.join(f'<li><span>{esc(x)}</span></li>' for x in d['resumo'])
    complement=''.join(f'<section class="comp-sec"><h3>{esc(t["title"])}</h3><h4>Experimente com calma</h4>{p(t["practice"])}<h4>O que observar</h4>{p(t["caution"])}</section>' for t in topics)
    # Aprofundamento usa apenas material autoral deste projeto; nêÂ£o publica acervo de terceiros.
    complement += '<section class="comp-sec"><h3>Fontes oficiais</h3><p>Consultadas em 25/09/2026. Disponibilidade e interface podem mudar.</p><p><a href="https://support.google.com/gemini/answer/14286560">Criar e editar imagens no Gemini</a> êÂ· <a href="https://ai.google.dev/gemini-api/docs/image-generation">Modelos e geraêÂ§êÂ£o de imagens</a></p></section>'
    next_title=lessons[i]['titulo'] if i<len(lessons) else 'Leve o mêÂ©todo para outro produto e compare suas decisêÂµes.'
    next_link=f'#aula-{i+1}' if i<len(lessons) else '#trilha'
    html=f'''<section class="view" id="v-aula-{i}" data-aula="{i}" data-tempo="15min">
<div class="aula"><header class="a-hero"><p class="kicker">MêÂ³dulo {(i-1)//3+1} êÂ· Aula {i} de {len(lessons)}</p><h1>{esc(d['titulo'])}</h1>
<figure class="cena"><img src="assets/img/aula-{i}.webp" width="1280" height="720" alt="IlustraêÂ§êÂ£o didêÂ¡tica de planejamento visual: {esc(d['titulo'].lower())}."></figure>
<p class="promise">VocêÂª consegue {esc(d['entrega'])}.</p>{p(d['dor'],'why')}<div class="em1min"><p class="k">Em 1 minuto</p><ol>{summary}</ol></div></header>
{''.join(steps)}
<section class="practice" data-mode="tarefa"><p class="pk">Pratique agora <span class="pcount">0/3</span></p><h3 class="ph">{esc(d['tarefa'])}</h3><p class="pgoal">Cerca de 10 minutos. Pronto quando {esc(d['pronto'])}.</p>
<p class="psafe">Use fotos prêÂ³prias ou autorizadas. A ficha pode ser preenchida no papel ou nas Notas. Se a prêÂ¡tica pedir ediêÂ§êÂ£o, preserve o original e trabalhe numa cêÂ³pia.</p>
<div class="pcodewrap"><button class="pcopy" type="button">copiar ficha</button><pre class="pcode">{esc(d['molde'])}</pre></div><ol class="psteps">{checklist}</ol><p class="pdone">Ao cumprir os passos, vocêÂª consegue {esc(d['entrega'])}.</p></section>
<div class="fecho"><div class="cola"><p class="k">Cola da aula</p><h3>{esc(d['titulo'])}</h3><ol>{cola}</ol></div><div class="next-action"><p class="nak">Seu prêÂ³ximo passo</p><p class="na-win">VocêÂª jêÂ¡ tem critêÂ©rios para {esc(d['entrega'])}.</p><p class="na-action">Use a ficha desta aula numa imagem do seu trabalho. Reserve dez minutos e anote a decisêÂ£o tomada.</p><p class="na-hook">PrêÂ³ximo passo: {esc(next_title)}</p></div></div>
<details class="complementar"><summary>Material complementar êÂ· mêÂ³dulo {(i-1)//3+1}<small>PrêÂ¡ticas e cuidados dos dois têÂ³picos. NêÂ£o entram no tempo da aula.</small></summary>{complement}</details>
<nav class="lnav"><a href="#trilha">trilha</a><a class="next" href="{next_link}">{'prêÂ³xima aula' if i<len(lessons) else 'rever a trilha'}</a></nav><p class="aula-pe">Aula {i} êÂ· Nano Banana Pro v6.2 êÂ· ARCKHê AI PRO</p></div>
<script type="application/json" id="cards-{i}">{json.dumps([{'front':a,'back':b} for a,b in d['cartoes']],ensure_ascii=False)}</script></section>'''
    (ROOT/f'aulas/aula-{i}.html').write_text(html)

cfg={'id':'nano-banana-pro-v62','titulo':'Nano Banana Pro v6.2 ê¢â¬â Campanha de Marca Completa','titulo_html':'Uma campanha com <em>identidade</em>','curso_curto':'Nano Banana v6.2','kicker':'Nano Banana Pro v6.2 êÂ· 6 mêÂ³dulos êÂ· 18 aulas','lead':'Organize referêÂªncias, preserve o produto e construa uma campanha com linguagem visual coerente. Planeje, produza e revise cada peêÂ§a com critêÂ©rios claros.','imagem_trilha':'assets/img/trilha.webp','alt_trilha':'ArtesêÂ£ e comerciante organizam uma caneca de cerêÂ¢mica, fundo e luz para uma imagem de produto.','rodape':'Nano Banana Pro v6.2 êÂ· ARCKHê AI PRO êÂ· <a href="landing.html">sobre o curso</a>','landing':'landing.html','glossario':True,'modulos':[{'titulo':f'MêÂ³dulo {i} êÂ· '+m['title'],'resumo':m['promise'],'aulas':list(range((i-1)*3+1,i*3+1))} for i,m in enumerate(base['modules'],1)]}
(ROOT/'curso.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(SKILL/'scripts/montar-curso.py'),str(ROOT)],check=True)
