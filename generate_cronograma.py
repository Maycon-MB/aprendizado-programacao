import os
from datetime import datetime, timedelta

# Lista de tarefas para as 52 semanas (corrigida, com CS50x Semana 0 = Scratch)
tarefas_por_semana = [
    ["CS50x: Semana 0 (Scratch, fundamentos)", "Grokking Algorithms: Capítulo 1 (busca binária)", "SQL: Praticar SELECT, WHERE no SQLZoo"],
    ["CS50x: Semana 1 (C, arrays)", "Grokking Algorithms: Revisar busca binária, implementar manualmente", "SQL: JOIN no SQLZoo"],
    ["CS50x: Semana 2 (C, strings)", "HackerRank: 2 problemas fáceis (strings)", "SQL: Filtros avançados no SQLZoo"],
    ["CS50x: Semana 3 (C, memória)", "HackerRank: 2 problemas fáceis (loops)", "SQL: Revisar SELECT, JOIN"],
    ["CS50x: Semana 4 (Python básico)", "Grokking Algorithms: Capítulo 2 (recursão)", "HackerRank: 3 problemas fáceis"],
    ["CS50x: Semana 5 (estruturas de dados)", "Grokking Algorithms: Implementar recursão simples", "SQL: GROUP BY no SQLZoo"],
    ["CS50x: Semana 6 (Python intermediário)", "HackerRank: 3 problemas intermediários (listas)", "SQL: Subqueries no SQLZoo"],
    ["CS50x: Semana 7 (algoritmos, ordenação)", "Grokking Algorithms: Capítulo 3 (ordenação)", "HackerRank: 3 problemas intermediários"],
    ["CS50x: Semana 8 (SQL)", "Grokking Algorithms: Capítulo 4 (grafos)", "Exercism: 1 exercício Python"],
    ["CS50x: Semana 9 (Flask básico)", "SQL: Query complexa com PostgreSQL (trabalho)", "Exercism: 1 exercício Python"],
    ["CS50x: Semana 10 (final)", "Grokking Algorithms: Capítulo 5 (busca em largura)", "Projeto: Iniciar script Python (ex.: automatizar tarefa do trabalho)"],
    ["CS50x: Projeto final (Flask + PostgreSQL)", "HackerRank: 2 problemas intermediários", "Projeto: Concluir script Python, documentar em `projetos`"],
    ["100 Days of Code: Dias 1-10 (Python básico, OOP)", "Web Bootcamp: HTML básico", "HackerRank: 2 problemas fáceis"],
    ["100 Days of Code: Dias 11-20 (listas, arquivos)", "Web Bootcamp: CSS básico", "Grokking Algorithms: Capítulo 6 (Dijkstra)"],
    ["100 Days of Code: Dias 21-25 (automação)", "Web Bootcamp: HTML/CSS projeto (página simples)", "LeetCode: 2 problemas médios"],
    ["100 Days of Code: Dias 26-30 (projeto simples)", "Web Bootcamp: Revisar HTML/CSS", "LeetCode: 2 problemas médios"],
    ["100 Days of Code: Dias 31-35 (APIs)", "Web Bootcamp: JavaScript básico (variáveis, funções)", "Projeto: Iniciar API Flask"],
    ["100 Days of Code: Dias 36-40 (Flask básico)", "Web Bootcamp: JavaScript (DOM)", "Projeto: Continuar API Flask (ex.: CRUD)"],
    ["100 Days of Code: Dias 41-45 (Flask + PostgreSQL)", "Web Bootcamp: JavaScript exercícios", "Projeto: Concluir API Flask, hospedar no Heroku"],
    ["100 Days of Code: Dias 46-50 (revisão APIs)", "Web Bootcamp: JavaScript projeto (ex.: calculadora)", "LeetCode: 2 problemas médios"],
    ["100 Days of Code: Dias 51-55 (autenticação)", "Web Bootcamp: JavaScript intermediário (eventos)", "Clean Code: Capítulos 1-2 (formatação)"],
    ["100 Days of Code: Dias 56-60 (projeto avançado)", "Web Bootcamp: JavaScript (async/await)", "Clean Code: Capítulo 3 (funções)"],
    ["100 Days of Code: Dias 61-65 (revisão)", "Web Bootcamp: JavaScript projeto (ex.: jogo)", "LeetCode: 2 problemas médios"],
    ["100 Days of Code: Dias 66-70 (projeto final)", "Web Bootcamp: Revisar JavaScript", "Clean Code: Refatore projeto Flask"],
    ["Web Bootcamp: Node.js básico", "Clean Code: Capítulo 4 (erros)", "Projeto: Iniciar app com Express (ex.: blog)"],
    ["Web Bootcamp: Express básico", "Clean Code: Capítulo 5 (formatação avançada)", "Projeto: Continuar app Express"],
    ["Web Bootcamp: Node.js + PostgreSQL", "LeetCode: 2 problemas médios", "Projeto: Concluir app Express, documentar em `projetos`"],
    ["Web Bootcamp: Revisar Node.js/Express", "Clean Code: Capítulo 6 (objetos)", "LeetCode: 2 problemas médios"],
    ["Web Bootcamp: MongoDB básico", "React (freeCodeCamp): Componentes, estado", "LeetCode: 1 problema médio"],
    ["Web Bootcamp: MongoDB intermediário", "React: Props, projeto simples (ex.: lista de tarefas)", "LeetCode: 1 problema médio"],
    ["Web Bootcamp: Projeto com MongoDB", "React: Revisar componentes", "LeetCode: 1 problema difícil"],
    ["Web Bootcamp: Concluir MongoDB", "React: Estado avançado", "Projeto: App React simples, hospedar no Vercel"],
    ["React: Hooks (useState, useEffect)", "LeetCode: 1 problema difícil", "Open Source: Encontrar projeto no GitHub ('good first issue')"],
    ["React: Projeto com hooks", "Open Source: Iniciar contribuição (ex.: corrigir bug)", "Clean Code: Capítulo 7 (sistemas)"],
    ["React: Roteamento (React Router)", "Open Source: Concluir 1 pull request", "Clean Code: Capítulo 8 (concorrência)"],
    ["React: Integração com APIs", "LeetCode: 1 problema difícil", "Projeto: Iniciar app fullstack (React + Flask)"],
    ["React: Revisar roteamento, APIs", "Open Source: Iniciar nova contribuição", "Projeto: Continuar app fullstack (ex.: dashboard)"],
    ["Clean Code: Capítulo 9 (formatação)", "LeetCode: 1 problema difícil", "Projeto: Avançar app fullstack"],
    ["Clean Code: Capítulo 10 (classes)", "Open Source: Concluir 2º pull request", "Projeto: Concluir app fullstack, hospedar no Vercel"],
    ["React: Refatore app fullstack com Clean Code", "LeetCode: 1 problema difícil", "Open Source: Revisar contribuições"],
    ["Nova linguagem: TypeScript básico (ou Go)", "Projeto: Iniciar app complexa (ex.: rede social)", "LeetCode: 1 problema difícil"],
    ["TypeScript: Tipagem, interfaces", "Projeto: Continuar app complexa", "Open Source: Iniciar 3º pull request"],
    ["TypeScript: Projeto simples (ex.: API)", "Projeto: Avançar app complexa", "LeetCode: 1 problema difícil"],
    ["TypeScript: Revisar tipagem", "Projeto: Continuar app complexa", "Open Source: Concluir 3º pull request"],
    ["System Design: Grokking the System Design Interview (Capítulo 1)", "Projeto: Concluir app complexa, documentar em `projetos`", "LeetCode: 1 problema difícil"],
    ["System Design: Capítulo 2", "Projeto: Hospedar app complexa no Vercel", "Portfólio: Atualizar README com projetos"],
    ["System Design: Capítulo 3", "LeetCode: 2 problemas difíceis", "Portfólio: Revisar repositório"],
    ["Projeto: Iniciar app avançada (ex.: clone de app conhecido)", "LeetCode: 2 problemas difíceis", "Portfólio: Adicionar app ao README"],
    ["Projeto: Continuar app avançada", "System Design: Revisar capítulos 1-3", "LeetCode: 1 problema difícil"],
    ["Projeto: Avançar app avançada", "Open Source: Iniciar 4º pull request", "Portfólio: Atualizar LinkedIn"],
    ["Projeto: Concluir app avançada, hospedar no Vercel", "Open Source: Concluir 4º pull request", "LeetCode: 1 problema difícil"],
    ["Portfólio: Finalizar README, documentar todos os projetos", "System Design: Projeto simples de design", "LeetCode: Revisar problemas difíceis"]
]

# Data inicial: 01/05/2025 (quinta-feira)
start_date = datetime(2025, 5, 1)

# Criar pasta cronograma se não existir
os.makedirs("cronograma", exist_ok=True)

# Gerar 52 arquivos Markdown (semana00.md a semana51.md)
for week in range(0, 52):
    # Calcular datas da semana (quinta a quarta)
    week_start = start_date + timedelta(days=week*7)
    week_end = week_start + timedelta(days=6)
    
    # Formatar nome do arquivo (ex.: semana00.md)
    filename = f"cronograma/semana{week:02d}.md"
    
    # Conteúdo do arquivo
    content = f"""# Semana {week:02d} ({week_start.strftime('%d/%m/%Y')} - {week_end.strftime('%d/%m/%Y')})

## Tarefas
"""
    # Adicionar tarefas da semana
    for tarefa in tarefas_por_semana[week]:
        content += f"- [ ] {tarefa}\n"
    
    # Adicionar seção de notas
    content += "\n## Notas\n(Anotar após a semana, ex.: 'Scratch foi intuitivo, mas busca binária precisa de prática.')"

    # Escrever arquivo
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("52 arquivos Markdown gerados na pasta 'cronograma' (semana00.md a semana51.md).")