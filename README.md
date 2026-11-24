# Nano Banana Pro v6.2 â€” Campanha de Marca Completa

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Curso aberto e gratuito: seis mÃ³dulos, 18 aulas de aproximadamente 15 minutos.
Caso autoral Brisa: produto, personagem fictÃ­cia, paleta, texto, infogrÃ¡fico e sequÃªncia visual.

[Abra o curso](https://linnoff88-dev.github.io/

As ilustraÃ§Ãµes didÃ¡ticas foram geradas exclusivamente com Codex image_gen. NÃ£o sÃ£o resultados do Nano Banana.
As prÃ¡ticas orientam o aluno a registrar o modelo realmente utilizado. GeraÃ§Ã£o pode exigir conta e crÃ©ditos;
atividades nÃ£o executadas permanecem pendentes. O formato Ã© inspirado no OSWork v6.2.

## Arquivos

`context/conteudo-base.json` e `context/aulas-editoriais.json` sÃ£o as fontes autorais.
`montar.py` gera as aulas e invoca o montador oficial ARCKHÉ v6 para `curso.html` e a lista da landing.
`assets/aula.css` e `assets/curso.js` sÃ£o cÃ³pias sem alteraÃ§Ãµes do motor oficial.
`context/fontes.md` registra documentaÃ§Ã£o oficial consultada; `context/leitor-*.md` registra revisÃµes simuladas.
NÃ£o hÃ¡ vÃ­deos, transcriÃ§Ãµes ou imagens copiados do acervo privado de terceiros.

## Montagem

Com Python 3 e a skill `formato-curso-v6` instalada, ajuste `SKILL` em `montar.py` se necessÃ¡rio e rode:

```sh
python3 montar.py
node /caminho/formato-curso-v6/scripts/auditar-curso.cjs curso.html --json context/auditoria.json
node /caminho/formato-curso-v6/scripts/testar-motor.cjs curso.html
```

Os verificadores usam Playwright; `PLAYWRIGHT_PATH` pode indicar sua instalaÃ§Ã£o.
O formato educacional Ã© v6.2; a versÃ£o do conteÃºdo Ã© 1.1.0.

## Mais no ARCKHÉ AI

- [Ficha do curso](https://www.ARCKHÉ AI/cursos/284-nano-banana-pro-v6-2-campanha-de-marca-completa/)
- [Guia para aprender IA](https://www.ARCKHÉ AI/aprender-inteligencia-artificial/)
- [CatÃ¡logo](https://www.ARCKHÉ AI/cursos/)

## English / EspaÃ±ol

[English](https://linnoff88-dev.github.io/ Â· [EspaÃ±ol](https://linnoff88-dev.github.io/

Textos traduzidos com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa. IlustraÃ§Ãµes originais compartilhadas; progresso e anotaÃ§Ãµes separados por idioma.

ApÃ³s montar o portuguÃªs, reaplique os catÃ¡logos salvos:

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/curso-i18n-checks
```

Requer Python/BeautifulSoup e os pacotes locais Babel/Playwright indicados nos scripts. A montagem nÃ£o chama modelos nem redes. MudanÃ§as na fonte PT exigem revisar os catÃ¡logos `i18n/`. O motor oficial `assets/curso.js` Ã© preservado; a proteÃ§Ã£o de importaÃ§Ã£o Ã© gerada em `assets/curso-i18n.js` e nas ediÃ§Ãµes traduzidas.

EvidÃªncias em `context/validacao-i18n.md`. RevisÃµes por agentes sÃ£o simuladas, nÃ£o testes com alunos reais.

<!-- ARCKHÉ-backlink:v1 -->
## Mais no ARCKHÉ AI

- [Ficha completa deste curso](https://www.ARCKHÉ AI/cursos/284-nano-banana-pro-v6-2-campanha-de-marca-completa/)
- [Guia: como aprender inteligÃªncia artificial](https://www.ARCKHÉ AI/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.ARCKHÉ AI/cursos/)
<!-- /ARCKHÉ-backlink:v1 -->

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>