﻿# Algoritmo-de-Kahn-
Este repositório contém uma implementação em Python do Algoritmo de Kahn para encontrar uma ordenação linear em um grafo direcionado acíclico (DAG - Directed Acyclic Graph).

Funcionamento:

O programa utiliza o algoritmo de Kahn para encontrar uma ordenação linear dos vértices do grafo. A ordenação linear é uma ordem na qual para cada aresta direcionada xy, o vértice x aparece antes do vértice y. Esse tipo de ordenação é válido apenas para DAGs.

Implementação:

O código é composto por uma classe Grafo, que representa o grafo e contém os métodos necessários para realizar a ordenação linear:

    __init__(self, vertices): Inicializa o grafo com um número especificado de vértices.
    adic_aresta(self, x, y): Adiciona uma aresta direcionada de x para y no grafo.
    ord_lin(self): Executa o Algoritmo de Kahn para encontrar a ordenação linear do grafo.

Detalhes do Algoritmo:

    Calcula o grau de entrada de cada vértice, ou seja, o número de arestas de entrada.
    Inicializa a contagem de vértices visitados como zero.
    Escolhe os vértices com grau de entrada zero e os adiciona a uma fila.
    Remove o vértice da frente da fila e incrementa a contagem de vértices visitados em 1.
    Diminui o grau de entrada de todos os vértices vizinhos e, se o grau de entrada de um vértice vizinho se tornar zero, ele é adicionado à fila.
    Repete esse processo até que a fila fique vazia.
    Se a contagem de vértices visitados não for igual ao número de vértices no grafo, então a ordenação linear não é possível, pois há um ciclo no grafo.

Exemplo de Uso:

O código inclui exemplos de três grafos diferentes, para os quais a ordenação linear é calculada e impressa:

    Grafo com 10 vértices e múltiplas arestas.
    Grafo com 8 vértices e múltiplas arestas.
    Grafo com 6 vértices e múltiplas arestas.

Execução:

Para executar o código, basta rodar o arquivo Python. Os resultados das ordenações lineares dos grafos serão impressos no terminal.
