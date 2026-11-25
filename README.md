# Nano Banana Pro v6.2 ê¢â¬â Campanha de Marca Completa

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Curso aberto e gratuito: seis mêÂ³dulos, 18 aulas de aproximadamente 15 minutos.
Caso autoral Brisa: produto, personagem fictêÂ­cia, paleta, texto, infogrêÂ¡fico e sequêÂªncia visual.

[Abra o curso](https://linnoff88-dev.github.io/

As ilustraêÂ§êÂµes didêÂ¡ticas foram geradas exclusivamente com Codex image_gen. NêÂ£o sêÂ£o resultados do Nano Banana.
As prêÂ¡ticas orientam o aluno a registrar o modelo realmente utilizado. GeraêÂ§êÂ£o pode exigir conta e crêÂ©ditos;
atividades nêÂ£o executadas permanecem pendentes. O formato êÂ© inspirado no OSWork v6.2.

## Arquivos

`context/conteudo-base.json` e `context/aulas-editoriais.json` sêÂ£o as fontes autorais.
`montar.py` gera as aulas e invoca o montador oficial ARCKHê v6 para `curso.html` e a lista da landing.
`assets/aula.css` e `assets/curso.js` sêÂ£o cêÂ³pias sem alteraêÂ§êÂµes do motor oficial.
`context/fontes.md` registra documentaêÂ§êÂ£o oficial consultada; `context/leitor-*.md` registra revisêÂµes simuladas.
NêÂ£o hêÂ¡ vêÂ­deos, transcriêÂ§êÂµes ou imagens copiados do acervo privado de terceiros.

## Montagem

Com Python 3 e a skill `formato-curso-v6` instalada, ajuste `SKILL` em `montar.py` se necessêÂ¡rio e rode:

```sh
python3 montar.py
node /caminho/formato-curso-v6/scripts/auditar-curso.cjs curso.html --json context/auditoria.json
node /caminho/formato-curso-v6/scripts/testar-motor.cjs curso.html
```

Os verificadores usam Playwright; `PLAYWRIGHT_PATH` pode indicar sua instalaêÂ§êÂ£o.
O formato educacional êÂ© v6.2; a versêÂ£o do conteêÂºdo êÂ© 1.1.0.

## Mais no ARCKHê AI

- [Ficha do curso](https://www.ARCKHê AI/cursos/284-nano-banana-pro-v6-2-campanha-de-marca-completa/)
- [Guia para aprender IA](https://www.ARCKHê AI/aprender-inteligencia-artificial/)
- [CatêÂ¡logo](https://www.ARCKHê AI/cursos/)

## English / EspaêÂ±ol

[English](https://linnoff88-dev.github.io/ êÂ· [EspaêÂ±ol](https://linnoff88-dev.github.io/

Textos traduzidos com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa. IlustraêÂ§êÂµes originais compartilhadas; progresso e anotaêÂ§êÂµes separados por idioma.

ApêÂ³s montar o portuguêÂªs, reaplique os catêÂ¡logos salvos:

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/curso-i18n-checks
```

Requer Python/BeautifulSoup e os pacotes locais Babel/Playwright indicados nos scripts. A montagem nêÂ£o chama modelos nem redes. MudanêÂ§as na fonte PT exigem revisar os catêÂ¡logos `i18n/`. O motor oficial `assets/curso.js` êÂ© preservado; a proteêÂ§êÂ£o de importaêÂ§êÂ£o êÂ© gerada em `assets/curso-i18n.js` e nas ediêÂ§êÂµes traduzidas.

EvidêÂªncias em `context/validacao-i18n.md`. RevisêÂµes por agentes sêÂ£o simuladas, nêÂ£o testes com alunos reais.

<!-- ARCKHê-backlink:v1 -->
## Mais no ARCKHê AI

- [Ficha completa deste curso](https://www.ARCKHê AI/cursos/284-nano-banana-pro-v6-2-campanha-de-marca-completa/)
- [Guia: como aprender inteligêÂªncia artificial](https://www.ARCKHê AI/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.ARCKHê AI/cursos/)
<!-- /ARCKHê-backlink:v1 -->

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>