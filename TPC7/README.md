# Dicionário Médico

Aplicação web desenvolvida em **Flask** para consulta de termos médicos em português.
## Estrutura do Projeto

TPC7/
│
├── tpc7.py                   # Servidor Flask (rotas e lógica)
├── dicionario_medico.json    # Base de dados com os termos médicos
│
└── templates/
    ├── layout.html           # Template base (navbar + footer)
    ├── home.html             # Página inicial
    ├── conceitos.html        # Lista de todos os conceitos
    ├── conceito.html         # Página individual de um conceito
    └── error.html            # Página de erro


### Abrir no browser

http://localhost:4002 -  Não abrir os ficheiros HTML diretamente no browser — o Jinja2 só funciona através do Flask.


## Rotas Disponíveis

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial |
| `/conceitos` | Lista de todos os conceitos médicos |
| `/conceitos/<designacao>` | Página de um conceito específico |
| `/api/conceitos` | Dicionário completo em formato JSON |

## Funcionalidades

- **Pesquisa em tempo real** na lista de conceitos
- **Filtro por letra** (A-Z) com destaque do botão ativo
- **Design responsivo** com Bootstrap 5
- **Ficheiro** que devolve o dicionário em JSON