# Number Number of Steps to Reduce a Number to Zero

- Categoria: math
- Exercício: 1342
- Dificuldade: easy (verde)

# Link do Problema
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

# Minha explicação e entendimento:

O desafio consiste em descobrir quantos passos são necessários até que o número de teste chegue em zero, verificando par e ímpar.
Utilize um loop while até que o número seja zero, dentro do loop, duas verificações utilizando módulo para descobrir se o número é par ou ímpar.
Após a verificação, a operação é feita de acordo com par ou ímpar e atualizada na variável do número informado para que possa ser reduzido e guardado aos poucos até chegar à zero.
Fiz uma variável cont para somar 1 toda vez que uma condição for completada, somando assim as quantidades de passos para o objetivo.
par = divide por 2, conta 1
ímpar = subtrai por 1, conta 1

