import os

# Estrutura do cronograma em módulos
modulos = [
    {
        "nome": "Módulo 1: Fundamentos de Programação",
        "objetivos": "Aprender fundamentos de programação em Scratch, C, e Python, além de algoritmos básicos e SQL.",
        "tarefas": [
            "CS50x: Scratch (fundamentos, lógica de programação)",
            "Grokking Algorithms: Capítulo 1 (busca binária) + implementar manualmente",
            "SQLZoo: SELECT basics, WHERE (exercícios 1-10)",
            "CS50x: C (arrays, strings, memória)",
            "Grokking Algorithms: Capítulo 2 (recursão) + implementar recursão simples",
            "SQLZoo: JOIN (exercícios 1-10)",
            "LeetCode: 3 problemas fáceis (arrays, strings)",
            "CS50x: Python básico (variáveis, funções, OOP)",
            "SQLZoo: GROUP BY (exercícios 1-10)"
        ],
        "tempo": "12-15 horas",
        "notas": "Documentar conceitos em `notas/scratch.md`, `notas/c-basico.md`, `notas/python-basico.md`. Revisar notas semanalmente para retenção."
    },
    {
        "nome": "Módulo 2: Programação Intermediária e SQL Avançado",
        "objetivos": "Aprofundar Python, estruturas de dados, algoritmos, e consultas SQL complexas.",
        "tarefas": [
            "CS50x: Python intermediário (listas, arquivos)",
            "Grokking Algorithms: Capítulo 3 (ordenação)",
            "SQLZoo: Subqueries (exercícios 1-10)",
            "CS50x: Estruturas de dados (listas ligadas, árvores)",
            "Grokking Algorithms: Capítulo 4 (grafos)",
            "LeetCode: 4 problemas intermediários (listas, grafos)",
            "CS50x: SQL (consultas avançadas)",
            "SQLZoo: Revisar SELECT, JOIN, GROUP BY (2-3 exercícios cada)",
            "Projeto: Script Python para automação (ex.: tarefa do trabalho), documentar em `projetos/script-automatizacao`"
        ],
        "tempo": "12-15 horas",
        "notas": "Anotar em `notas/sql-avancado.md` e `notas/estruturas-dados.md`. Revisar notas após o módulo."
    },
    {
        "nome": "Módulo 3: Introdução ao Desenvolvimento Web",
        "objetivos": "Dominar HTML, CSS, JavaScript básico, e Flask para APIs simples.",
        "tarefas": [
            "100 Days of Code: Python OOP (dias 1-10)",
            "Web Bootcamp: HTML básico (tags, estrutura)",
            "LeetCode: 2 problemas fáceis (strings)",
            "100 Days of Code: Listas, arquivos (dias 11-20)",
            "Web Bootcamp: CSS básico (flexbox, grid)",
            "Grokking Algorithms: Capítulo 5 (busca em largura)",
            "Web Bootcamp: Projeto HTML/CSS (página simples), documentar em `projetos/pagina-simples`",
            "100 Days of Code: Automação (dias 21-25)",
            "LeetCode: 2 problemas médios (arrays)"
        ],
        "tempo": "10-12 horas",
        "notas": "Criar `notas/html-css.md` para conceitos web. Hospedar página simples no GitHub Pages."
    },
    {
        "nome": "Módulo 4: APIs e JavaScript Intermediário",
        "objetivos": "Construir APIs com Flask, aprender JavaScript intermediário, e praticar algoritmos.",
        "tarefas": [
            "100 Days of Code: APIs com Flask (dias 31-35)",
            "Web Bootcamp: JavaScript básico (variáveis, funções)",
            "Projeto: Iniciar API Flask (ex.: CRUD), documentar em `projetos/api-flask`",
            "100 Days of Code: Flask + PostgreSQL (dias 41-45)",
            "Web Bootcamp: JavaScript (DOM, eventos)",
            "LeetCode: 3 problemas médios (listas, árvores)",
            "Projeto: Concluir API Flask, hospedar no Heroku",
            "Web Bootcamp: Projeto JavaScript (ex.: calculadora), documentar em `projetos/calculadora-js`",
            "Explorar Upwork e bidar em um projeto simples (ex.: Flask API, $50-100)"
        ],
        "tempo": "12-15 horas",
        "notas": "Anotar em `notas/flask-api.md` e `notas/javascript-dom.md`. Documentar experiência de freelancing em `notas/freelancing.md`."
    },
    {
        "nome": "Módulo 5: JavaScript Avançado e Autenticação",
        "objetivos": "Aprofundar JavaScript, adicionar autenticação a APIs, e refatorar projetos.",
        "tarefas": [
            "100 Days of Code: Autenticação (dias 51-55)",
            "Web Bootcamp: JavaScript intermediário (async/await)",
            "Projeto: Adicionar autenticação à API Flask (ex.: JWT)",
            "100 Days of Code: Projeto avançado (dias 56-60)",
            "Web Bootcamp: Projeto JavaScript (ex.: jogo), documentar em `projetos/jogo-js`",
            "LeetCode: 3 problemas médios (grafos, recursão)",
            "Projeto: Refatorar API Flask com boas práticas",
            "Grokking Algorithms: Capítulo 6 (Dijkstra)"
        ],
        "tempo": "12-15 horas",
        "notas": "Documentar em `notas/autenticacao.md`. Hospedar projetos no Heroku ou Vercel."
    },
    {
        "nome": "Módulo 6: Back-end com Node.js e Express",
        "objetivos": "Aprender Node.js, Express, e bancos NoSQL (MongoDB), com projetos práticos.",
        "tarefas": [
            "Web Bootcamp: Node.js básico",
            "Projeto: Iniciar app com Express (ex.: blog), documentar em `projetos/blog-express`",
            "Web Bootcamp: Express básico",
            "LeetCode: 2 problemas médios (árvores)",
            "Web Bootcamp: Node.js + PostgreSQL",
            "Projeto: Concluir app Express, hospedar no Heroku",
            "Web Bootcamp: MongoDB básico",
            "LeetCode: 1 problema difícil (grafos)"
        ],
        "tempo": "10-12 horas",
        "notas": "Criar `notas/node-express.md` e `notas/mongodb.md`. Revisar conceitos de REST."
    },
    {
        "nome": "Módulo 7: Front-end com React",
        "objetivos": "Dominar React (componentes, hooks, roteamento) e integrar com APIs.",
        "tarefas": [
            "Web Bootcamp: MongoDB intermediário",
            "React (freeCodeCamp): Componentes, estado",
            "LeetCode: 1 problema médio (arrays)",
            "React: Props, projeto simples (ex.: lista de tarefas), documentar em `projetos/lista-tarefas`",
            "Web Bootcamp: Projeto com MongoDB",
            "React: Hooks (useState, useEffect)",
            "Projeto: App React simples, hospedar no Vercel",
            "React: Roteamento (React Router)",
            "LeetCode: 2 problemas difíceis (árvores, dinâmica)"
        ],
        "tempo": "12-15 horas",
        "notas": "Anotar em `notas/react-basico.md`. Revisar notas de JavaScript."
    },
    {
        "nome": "Módulo 8: Fullstack e Contribuições Open Source",
        "objetivos": "Construir apps fullstack, contribuir para open source, e praticar algoritmos avançados.",
        "tarefas": [
            "React: Integração com APIs",
            "Projeto: Iniciar app fullstack (React + Flask), documentar em `projetos/app-fullstack`",
            "Open Source: Encontrar projeto no GitHub ('good first issue')",
            "LeetCode: 2 problemas difíceis (grafos, dinâmica)",
            "React: Revisar roteamento, APIs",
            "Open Source: Concluir 1 pull request",
            "Projeto: Concluir app fullstack, hospedar no Vercel",
            "Escrever um blog post explicando o app fullstack e publicar no Medium/Dev.to"
        ],
        "tempo": "12-15 horas",
        "notas": "Documentar contribuições em `projetos/open-source`. Atualizar README do repositório."
    },
    {
        "nome": "Módulo 9: TypeScript e Projetos Complexos",
        "objetivos": "Aprender TypeScript, desenvolver projetos complexos, e continuar contribuições.",
        "tarefas": [
            "TypeScript: Básico (tipagem, interfaces)",
            "Projeto: Iniciar app complexa (ex.: rede social), documentar em `projetos/app-complexa`",
            "Open Source: Iniciar 2º pull request",
            "LeetCode: 2 problemas difíceis (árvores, dinâmica)",
            "TypeScript: Projeto simples (ex.: API)",
            "Projeto: Concluir app complexa, hospedar no Vercel",
            "Open Source: Concluir 2º pull request",
            "Escolher uma especialização (ex.: React, cloud) e completar 1 curso introdutório gratuito (ex.: freeCodeCamp AWS)"
        ],
        "tempo": "12-15 horas",
        "notas": "Criar `notas/typescript.md`. Revisar projetos no Vercel."
    },
    {
        "nome": "Módulo 10: System Design e Portfólio",
        "objetivos": "Entender design de sistemas com recursos gratuitos, finalizar projetos avançados, e preparar portfólio.",
        "tarefas": [
            "System Design Primer: Estudar 'Scalability Concepts' e 'Design a URL Shortener' (GitHub)",
            "Assistir 2 vídeos do System Design Interview (ex.: 'Design Twitter', 'Design Uber') e resumir em `notas/system-design.md`",
            "Projeto: Iniciar app avançada (ex.: clone de app conhecido), documentar em `projetos/app-avancada`",
            "LeetCode: 3 problemas difíceis (grafos, dinâmica)",
            "System Design Primer: Estudar 'Design a Messaging System' e 'Consistency Patterns'",
            "Praticar 1 mock interview de System Design no Pramp e documentar em `notas/system-design.md`",
            "Projeto: Concluir app avançada, hospedar no Vercel",
            "Portfólio: Finalizar README do repositório, documentar todos os projetos",
            "Compartilhar um projeto no LinkedIn ou comunidade (ex.: Reddit r/learnprogramming)"
        ],
        "tempo": "12-15 horas",
        "notas": "Anotar em `notas/system-design.md`. Atualizar LinkedIn com portfólio."
    }
]

# Criar pasta cronograma se não existir
os.makedirs("cronograma", exist_ok=True)

# Nome do arquivo
filename = "cronograma/cronograma.md"

# Conteúdo do arquivo
content = """# Cronograma de Estudos: Jornada Fullstack

Este cronograma organiza o aprendizado em módulos sequenciais, sem datas fixas, para flexibilidade. Siga a ordem dos módulos, avançando no seu ritmo (10-15 horas por módulo). Documente o progresso em `notas` e `projetos`, e use LeetCode para prática de entrevistas.

"""

# Adicionar cada módulo
for modulo in modulos:
    content += f"## {modulo['nome']}\n\n"
    content += f"**Objetivos**: {modulo['objetivos']}\n\n"
    content += f"**Tarefas**:\n"
    for tarefa in modulo['tarefas']:
        content += f"- [ ] {tarefa}\n"
    content += f"\n**Estimativa de Tempo**: {modulo['tempo']}\n"
    content += f"\n**Notas**: {modulo['notas']}\n\n"

# Adicionar seção de recomendações
content += """## Recomendações Gerais

- **Ritmo**: Dedique 10-15 horas por módulo, ajustando conforme sua rotina (ex.: 2h/dia, 4h sábado).
- **Retenção**: Escreva resumos em `notas` após cada módulo (ex.: `notas/react-basico.md`) e revise a cada 2 módulos.
- **Portfólio**: Hospede projetos no Vercel/Heroku e atualize o `README.md` do repositório.
- **Bem-estar**: Faça pausas regulares e pratique meditação (5-10min/dia) para evitar burnout.
- **Freelancing**: A partir do Módulo 4, busque projetos simples (ex.: Upwork) para aplicar habilidades.
- **Comunidade**: Participe de fóruns (ex.: Reddit r/learnprogramming) para networking e feedback.

"""

# Escrever arquivo
with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Arquivo Markdown gerado em 'cronograma/cronograma.md' com cronograma modular, usando recursos gratuitos para System Design.")