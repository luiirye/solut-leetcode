# Repositório para minhas soluções Leetcode

Repositório pessoal de estudos com soluções de desafios do [LeetCode](https://leetcode.com/) desenvolvidas grande parte (se não todas) em **Python**.

O objetivo é praticar lógica de programação, estruturas de dados e algoritmos, além de registrar o raciocínio utilizado em cada problema. (achei interessante essa abordagem para meu aprendizado)

## Estrutura do repositório

As soluções são organizadas por categoria e identificadas pelo número e pelo nome do exercício:

```text
python/
├── array/
│   └── <número>-<nome-do-problema>/main.py
│   └── <número>-<nome-do-problema>/README.md
├── linked-list/
│   └── <número>-<nome-do-problema>/main.py
│   └── <número>-<nome-do-problema>/README.md
└── math/
│   └── <número>-<nome-do-problema>/main.py
│   └── <número>-<nome-do-problema>/READMe.md
```

Cada pasta de exercício pode conter:

- `main.py`: implementação da solução na classe `Solution`.
- `README.md`: link para o enunciado, dificuldade e anotações sobre a resolução.

## Exercícios adicionados

| Nº | Problema | Categoria | Dificuldade |
| --: | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Array | Easy |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Array | Hard |
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Array | Easy |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Linked List | Easy |
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Math | Easy |
| 1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Array | Easy |
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Array | Easy |

## Como executar uma solução

Entre na pasta do exercício e execute o arquivo Python:

```bash
python main.py
```

Alguns arquivos incluem exemplos de entrada e saída para testes locais. No LeetCode, apenas a classe `Solution` e o método solicitado devem ser enviados.
