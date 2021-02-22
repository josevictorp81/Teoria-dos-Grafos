import sys
import networkx as nx

def largura(grafo, vertices):
    visitados = [0 for i in range(len(vertices))]

    componente = 0
    for i in range(len(grafo.keys())):
        if visitados[i] == 0:
            componente = componente + 1
            #print(componente)
            aux(grafo, i, vertices, visitados, componente)
    return visitados, componente
    
def aux(grafo, i, vertices, visitados, componente):
    visitados[i] = componente
    fila = [vertices[i]]
    while fila:
        w = fila[0]
        for i in grafo[w]:
            if visitados[vertices.index(i)] == 0:
                visitados[vertices.index(i)] = componente
                fila.append(i)
        fila.remove(w)


arquivo = open(sys.argv[1], "r")
G = nx.Graph()


''' vertices '''
n_vertices = int(arquivo.readline())
vertices = arquivo.readline().replace("\n","").split(" ")
G.add_nodes_from(vertices)

''' arestas '''
n_arestas = int(arquivo.readline())
for i in range(n_arestas):
    arestas = arquivo.readline().replace("\n","").split(" ")
    G.add_edge(arestas[0], arestas[1])

''' grafo '''
grafo = {}
grafo = dict.fromkeys(vertices)
for i in range(len(grafo.keys())):
    grafo[vertices[i]] = list(G.adj[vertices[i]])

print('--- BFS ---')
lar = []
lar = largura(grafo, vertices)
print(lar[0])
print('Componentes: {}'.format(lar[1]))