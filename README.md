# Algoritmo de Kahn 🔗

Este repositório contém uma implementação em Python do Algoritmo de Kahn para encontrar uma ordenação linear em um grafo direcionado acíclico (DAG - Directed Acyclic Graph).

## 📁 Estrutura do Projeto

O código é composto pelo arquivo principal:

- **kahn.py**: Implementação do algoritmo de Kahn, incluindo a lógica de ordenação linear e manipulação de grafos.

## Funcionamento

O programa utiliza o algoritmo de Kahn para encontrar uma ordenação linear dos vértices do grafo. A ordenação linear é uma ordem na qual, para cada aresta direcionada \(xy\), o vértice \(x\) aparece antes do vértice \(y\). Esse tipo de ordenação é válido apenas para DAGs.

### Detalhes do Algoritmo

1. Calcula o grau de entrada de cada vértice, ou seja, o número de arestas de entrada.
2. Inicializa a contagem de vértices visitados como zero.
3. Escolhe os vértices com grau de entrada zero e os adiciona a uma fila.
4. Remove o vértice da frente da fila e incrementa a contagem de vértices visitados em 1.
5. Diminui o grau de entrada de todos os vértices vizinhos e, se o grau de entrada de um vértice vizinho se tornar zero, ele é adicionado à fila.
6. Repete esse processo até que a fila fique vazia.
7. Se a contagem de vértices visitados não for igual ao número de vértices no grafo, então a ordenação linear não é possível, pois há um ciclo no grafo.

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabigam/Algoritmo-de-Kahn.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd Algoritmo-de-Kahn
   ```
3. Execute o arquivo Python:
   ```bash
   python kahn.py
   ```

Os resultados das ordenações lineares dos grafos serão impressos no terminal.
```

