# Semana 01 - CS50: linguagem C (12/05/2025 - 17/05/2025)

## Particularidades do C

- Para conseguir inserir um input do usuário dentro de um print, é necessário utilizar porcentagem + o tipo de dado.
    - Exemplo:
        ```c 
        #include <cs50.h> // Biblioteca que o curso criou para facilitar algumas interações.
        #include <stdio.h>

        int main(void)
        {
            string answer = get_string("What's your name? ");
            prinf("Hello, %s\n", answer);
        }
        ```