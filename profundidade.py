import sys
import networkx as nx

def profundidade(grafo, vertices):
    visitados = [0 for i in range(len(vertices))]
    
    componente = 0
    for i in range(len(visitados)):
        if visitados[i] == 0:
            componente = componente + 1
            prof(grafo, i, visitados, vertices, componente)
            
    return visitados, componente

def prof(grafo, no, visitados, vertices, marcar):
    visitados[no] = marcar
    for i in grafo[vertices[no]]:
        if visitados[vertices.index(i)] == 0:
            prof(grafo, vertices.index(i), visitados, vertices, marcar)
    

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

print('--- DFS ---')
prof = []
prof = profundidade(grafo, vertices)
print(prof[0])
print('Componentes: {}\n'.format(prof[1]))