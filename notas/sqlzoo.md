# Notas SQLZoo

## Semana 00 - SELECT basics (05/05/2025 - 11/05/2025)
- Aprendi: Usar 'IN' no select para consultar apenas o que está entre as opções do 'IN'. Aprendi também o uso do 'BETWEEN' (entre).

### SELECT basics

world
name	continent	area	population	gdp
Afghanistan	Asia	652230	25500100	20343000000
Albania	Europe	28748	2831741	12960000000
Algeria	Africa	2381741	37100000	188681000000
Andorra	Europe	468	78115	3712000000
Angola	Africa	1246700	20609294	100990000000
....

#### Introducing the world table of countries
- **Exercício 1**: Modify it to show the population of Germany
    - Consulta: 'SELECT population FROM world WHERE name = 'Germany''
- **Exercício 2**: Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
    - Consulta: 'SELECT name, population FROM world
                    WHERE name IN ('Sweden', 'Norway', 'Denmark')'
- **Exercício 3**: Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
    - Consulta: 'SELECT name, area FROM world
                    WHERE area BETWEEN 200000 and 250000'