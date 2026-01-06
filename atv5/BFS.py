from collections import deque

def BFS(listaAdj, v):

    Q = deque([v])
    ids = deque([v])
    visitados = set([v])
    sequencia = []
    for vertice in listaAdj.keys():
        if (vertice != v):
            ids.append(vertice)
    
    while Q or ids:
        if not Q:
            visitado = ids.popleft()
            if visitado in visitados:
                continue
            visitados.add(visitado)
            Q.append(visitado)
        visitado = Q.popleft()
        for vizinho in listaAdj[visitado]:
            if (vizinho not in visitados):
                visitados.add(vizinho)
                Q.append(vizinho)
        sequencia.append(visitado)

    print(sequencia)


def verificaConexo(listaAdj, v):

    Q = deque([v])
    ids = deque([v])
    visitados = set([v])
    sequencia = []
    for vertice in listaAdj.keys():
        if (vertice != v):
            ids.append(vertice)
    
    while Q:
        visitado = Q.popleft()
        for vizinho in listaAdj[visitado]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                Q.append(vizinho)
        sequencia.append(visitado)

    if len(sequencia) != len(ids):
        return False
    else:
        return True
    

def BFS(G, v):
    visitados = set()
    sequencia = []

    ids = [v] + [vertice for vertice in G.keys() if vertice != v]

    for id in ids:
        if id not in visitados:
            fila = deque([id])
            visitados.add(id)
        while fila:
            visitado = fila.popleft()
            sequencia.append(visitado)

            for vizinho in G[visitado]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
    print(sequencia)