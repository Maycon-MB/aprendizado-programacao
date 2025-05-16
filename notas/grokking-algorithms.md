# Notas sobre Grokking Algorithms

## Capítulo 1 - Busca Binária
- **Conceito**: Serve para encontrar um valor dentro de uma lista ordenada. Sempre começando pelo meio da lista:
    - Se o valor procurado for menor que o valor do meio, descarta a metade de cima. 
    - Se for maior, descarta a metade de baixo.
    - Isso irá se repetir até encontrar o valor procurado, ou não ter mais nada pra procurar.
- **Logaritmos**: São basicamente o oposto de exponenciais. Se tenho uma potência, o logaritmo serve para saber qual expoente foi usado
    - Exemplos:
        - 10² = 100 <-> log10(100) = 2
        - 10³ = 1000 <-> log10(1000) = 3
        - 2³ = 8 <-> log2(8) = 3
- **Complexidade**: O(log n), porque a lista é dividida pela metade a cada passo.
- **Obs**: Conceito bem aprendido. Implementação em 'projetos/busca-binária'

