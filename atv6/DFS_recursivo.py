from collections import deque

def DFS(G, v):
    visitados = set()
    sequencia = []
    def DFS_recursivo(vertice_atual):
        visitados.add(vertice_atual)
        sequencia.append(vertice_atual)
        for vizinho in G[vertice_atual]:
            if vizinho not in visitados:
                DFS_recursivo(vizinho)

    ids = deque([v])
    for vertice in G.keys():
        if vertice != v:
            ids.append(vertice)

    for id in ids:
        if id not in visitados:
            DFS_recursivo(id)
            
    print(sequencia)

DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
