# Pesquisa — Dicionário Médico

A pesquisa em tempo real permite ao utilizador escrever um termo e ver resultados a aparecer automaticamente, sem recarregar a página. Inclui opções para pesquisa por palavra exata e distinção de maiúsculas/minúsculas, com destaque visual das palavras encontradas.

# Frontend — `pesquisar.html`

- O <input> captura o que o utilizador escreve.
- O <div id="resultados"> é o contentor onde os resultados aparecem dinamicamente.
- Os dois checkboxes controlam o modo de pesquisa e disparam uma nova pesquisa ao serem alterados.
- Não há <form> nem botão de submissão — tudo acontece enquanto se escreve.
- O uso de "pills" faz com que as pesquisas fiquem azuis quando ativas, cards individuais por resultado e animações suaves ao passar o rato.

# JavaScript — `script.js`

Lógica para aparecer conceitos que coincidam com o que está a ser pesquisado.

- addEventListener("input", ...) — dispara a cada tecla pressionada
- query.length < 2 — evita pesquisas com apenas 1 letra (demasiados resultados)
- encodeURIComponent(query) — garante que caracteres especiais (ç, ã, etc.) são enviados corretamente
- X-Requested-With: XMLHttpRequest — sinaliza ao Flask que o pedido vem do JavaScript e não do browser diretamente
- exact e case — parâmetros enviados na URL com o estado dos checkboxes
- destacar(texto, query, caseSensitive) — função que usa 'String.replace' com regex para colocar a negrito todas as ocorrências da palavra pesquisada, tanto no conceito como na descrição
- descricao.substring(0, 120) — mostra apenas os primeiros 120 caracteres da descrição na lista
- Os checkboxes têm o seu próprio 'addEventListener("change", ...)' que também dispara 'fazerPesquisa()'

# Backend — `tpc8.py`

- request.args.get("q", "") — lê o parâmetro 'q' da URL 
- request.args.get("exact", "false") — lê se a pesquisa deve ser por palavra exata
- request.args.get("case", "false") — lê se deve distinguir maiúsculas/minúsculas
- .lower() — torna a pesquisa insensível a maiúsculas/minúsculas (quando case=false)
- query in designacao.lower() or query in descricao.lower() — pesquisa por substring no conceito e na descrição
- re.search(r'\b' + re.escape(q) + r'\b', ...) — quando exact=true, usa expressão regular com \b para garantir que só encontra a palavra isolada (ex: "teste" não apanha "testemunho")
- X-Requested-With — distingue pedidos AJAX de pedidos normais do browser
- return resultados — Flask converte automaticamente o dicionário Python em JSON

# Opções de pesquisa

- Normal - substring em qualquer sítio, sem distinção de maiúsculas ("hiper" encontra "Hipertensão", "hipertermia", etc.)
- Palavra exata - só encontra a palavra isolada ("teste" não encontra "testemunho")
- Maiúsculas/minúsculas - "Teste" não encontra "teste" nem "TESTE" 
- Ambas ativas - Palavra exata e case-sensitive em simultâneo 

# Fluxo completo — exemplo

1. Utilizador escreve "hiper" no campo de pesquisa (com "Palavra exata" desmarcado)
2. JavaScript envia 'GET /pesquisar?q=hiper&exact=false&case=false' com header AJAX
3. Flask percorre o dicionário e encontra todos os conceitos/descrições com "hiper" em qualquer posição
4. Flask devolve {"Hipertensão": "Pressão arterial acima...", "Hiperglicemia": "..."}
5. JavaScript aplica destacar() e injeta os resultados com a palavra a negrito no <div id="resultados">
6. Utilizador vê os resultados sem a página recarregar
7. Ao clicar num resultado, vai para '/conceitos/Hipertensão'