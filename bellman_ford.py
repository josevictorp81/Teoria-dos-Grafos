import sys
import networkx as nx
import matplotlib.pyplot as plt


def bellmanFord(G, verticeInicial):
    distancia = {}
    for i in G.nodes:
        distancia[i] = float('inf')
        #print(i)

    distancia[verticeInicial] = 0

    for j in G.nodes:
        for k in G.adj[j]:
            if (G.get_edge_data(j, k)['weight'] + distancia[j]) < distancia[k]:
                distancia[k] = G.get_edge_data(j, k)['weight'] + distancia[j]
    return distancia



arquivo = open(sys.argv[1], "r")
G = nx.DiGraph()

n_vertices = int(arquivo.readline())
#print (n_vertices)
vertices = arquivo.readline().replace("\n","").split(" ")
#print (vertices)

G.add_nodes_from(vertices)
n_arestas = int(arquivo.readline())
for x in range(n_arestas):
    edge = arquivo.readline().replace("\n","").split(" ")
    G.add_edge(edge[0],edge[1],weight=float(edge[2]))
vi = arquivo.readline().replace("\n","").split(" ")[0]

arquivo.close()

res = bellmanFord(G, vi)
for i in res:
    print('a distância entre {} e {} = {}'.format(vi, i, res[i]))