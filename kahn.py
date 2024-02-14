# Implementação do Algoritmo de Kahn para encontrar uma ordenação linear
# O programa imprime a ordenaçao linear de um grafo usando o numero de arestas de entrada
# a ordenação linear só ocorre se o grafo for DAG
# Sobre o programa...
# o programa faz o uso de fila
# Primeiro é calculado o grau de cada um dos vértices ou seja o numero de arestas de entrada e depois é inicializada a
# contagem de vertices visitados como zero
# Depois são escolhidos vertices com grau de entrada 0 e eles são adicionados a uma fila
# Em seguida esse vertice é removido da fila e incrementado a contagem de vertices visitados em 1
# Após isso, o grau é diminuido em 1 para todos os vertices vizinho e se o grau de entrada de um vertice vizinho
# for resduzido a zero, ele é adicionado à fila
# Esse processo é repetido até que a fila fique vazia
# Obs: se a contagem de vertices visitados não for igual ao numero de vertices no grafo, entao a ordenação linear não é
# possível

from collections import defaultdict

# Classe para representar o grafo
class Grafo:
    def __init__(self, vertices):
        self.grafo = defaultdict(list)  # dicionário onde está contido a lista de adjacencias
        self.Vert = vertices # numero de vertices

# Funcao para adcionar uma aresta no grafo
    def adic_aresta(self, x, y):
        self.grafo[x].append(y)

# Função para fazer a Ordenação Linear
    def ord_lin(self):

# Cria um vetor para armazenar os graus de todos os vértices
# Todos os graus são inicializados como 0
        grau_vert = [0] * (self.Vert)

# Atravessa a listas de adjacência para preencher o grau dos vertices
        for i in self.grafo:
            for j in self.grafo[i]:
                grau_vert[j] += 1

# Cria uma fila e enfileira todos os vértices com grau 0
        fila = []
        for i in range(self.Vert):
            if grau_vert[i] == 0:
                fila.append(i)


# Inicializa a contagem dos vértices visitados
        cont_vert = 0

# Cria um vetor para armazenar a ordenação linear dos vértices
        ord_line = []

# Desenfileira os vertices da fila e enfileira os adjacentes se o grau de adjacentes se tornar 0

        while fila:

# Extrai a frente da fila ou começa o desenfileiramento e adiciona à ordenação linear
            x = fila.pop(0)
            ord_line.append(x)

# Itera todos os vértices vizinhos do vertice desenfileirado x e diminui seu grau em 1
            for i in self.grafo[x]:
                grau_vert[i] -= 1
# Se o grau de entrada se tornar zero, ele deve ser adcionado a fila
                if grau_vert[i] == 0:
                    fila.append(i)

            cont_vert += 1

# Verifica a existencia de ciclo
        if cont_vert != self.Vert:
            print("Tem um ciclo no grafo")
        else:
# Imprime a ordenação linear
            print(ord_line)

teste_1 = Grafo(10)
teste_1.adic_aresta(0, 1);
teste_1.adic_aresta(0, 2);
teste_1.adic_aresta(0, 3);
teste_1.adic_aresta(0, 5);
teste_1.adic_aresta(1, 2);
teste_1.adic_aresta(2, 3);
teste_1.adic_aresta(2, 4);
teste_1.adic_aresta(4, 6);
teste_1.adic_aresta(5, 4);
teste_1.adic_aresta(5, 6);
teste_1.adic_aresta(6, 7);
teste_1.adic_aresta(6, 8);
teste_1.adic_aresta(7, 8);
teste_1.adic_aresta(9, 6);

teste_2 = Grafo(8)
teste_2.adic_aresta(0, 3);
teste_2.adic_aresta(0, 4);
teste_2.adic_aresta(1, 3);
teste_2.adic_aresta(2, 4);
teste_2.adic_aresta(2, 7);
teste_2.adic_aresta(3, 5);
teste_2.adic_aresta(3, 6);
teste_2.adic_aresta(3, 7);
teste_2.adic_aresta(4, 6);

teste_3 = Grafo(6)
teste_3.adic_aresta(5, 2);
teste_3.adic_aresta(5, 0);
teste_3.adic_aresta(4, 0);
teste_3.adic_aresta(4, 1);
teste_3.adic_aresta(2, 3);
teste_3.adic_aresta(3, 1);


print("A ordenação linear do grafo  é")
teste_1.ord_lin() # chama a função
print("A ordenação linear do grafo 2 é")
teste_2.ord_lin()
print("A ordenação linear do grafo 3 é")
teste_3.ord_lin()
