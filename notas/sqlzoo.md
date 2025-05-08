# Notas SQLZoo

## Semana 00 - SELECT basics (05/05/2025 - 11/05/2025)
- Aprendi: Usar 'IN' no select para consultar apenas o que está entre as opções do 'IN'. Aprendi também o uso do 'BETWEEN' (entre).

- **Exercício 1**: Modify it to show the population of Germany
    - Consulta: 'SELECT population FROM world WHERE name = 'Germany''
- **Exercício 2**: Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
    - Consulta: 'SELECT name, population FROM world WHERE name IN ('Sweden', 'Norway', 'Denmark')'
- **Exercício 3**: Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
    - Consulta: 'SELECT name, area FROM world WHERE area BETWEEN 200000 and 250000'