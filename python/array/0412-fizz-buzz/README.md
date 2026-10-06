# fizz-buzz

- Tipo: Array
- Dificuldade Easy
- 0412: FizzBuzz (Explore)

# Link do problema
https://leetcode.com/problems/fizz-buzz/

# Minha explicação e entendimento:

Pelo que entendi, o "jogo" consiste em contar até o número informado pelo usuário. Nos testes, foi até o 15 no máximo.
como os índices começam em 0, setei o range para que começasse em um e fosse até n + 1 para que pudesse aumentar uma casa no índice e ficar parelho, ao invés de 0 (primeira posição), ficasse 1 (primeira posição ao invés de segunda.)

As estruturas condicionais verificam se ao iterar, o número é divisível por 3 e 5, 3 ou apenas o 5, assim armazenando fizz buzz ou fizzbuzz dentro de uma nova lista, além de transformar o número atual (i) em string.