import math

def Bellman_ford(G, vInicio, vDestino):
    dist = {}
    pred = {}

    num_vertices = len(G)
    
    for v in G:
        dist[v] = math.inf
        pred[v] = None

    dist[vInicio] = 0


    arestas = []
    for v in G:
        for u, peso in G[v].items():
            arestas.append((v, u, peso))


    for _ in range(num_vertices - 1):
        trocou = False

        for v, u, peso in arestas:
            if dist[v] != math.inf and dist[u] > dist[v] + peso:
                dist[u] = dist[v] + peso
                pred[u] = v
                trocou = True

        if not trocou: break

    for v, u, peso in arestas:
        if dist[v] != math.inf and dist[u] > dist[v] + peso:
            print("Ciclo negativo encontrado")
            return None
        
    caminho = []
    u = vDestino
    if dist[vDestino] != math.inf:
        while u != None:
            caminho.append(u)
            u = pred[u]
        caminho.reverse()

    print(caminho)

    return dist[vDestino]

def Bellman_ford_matriz(G, vInicio, vDestino):
    dist = {}
    pred = {}

    num_vertices = len(G)
    
    for v in range(num_vertices):
        dist[v] = math.inf
        pred[v] = None

    dist[vInicio] = 0


    arestas = []
    for i in range(num_vertices):
        for j in range(num_vertices):
            if G[i][j] != math.inf and G[i][j] != 0:
                arestas.append((i, j, G[i][j]))


    for _ in range(num_vertices - 1):
        trocou = False

        for v, u, peso in arestas:
            if dist[v] != math.inf and dist[u] > dist[v] + peso:
                dist[u] = dist[v] + peso
                pred[u] = v
                trocou = True

        if not trocou: break

    for v, u, peso in arestas:
        if dist[v] != math.inf and dist[u] > dist[v] + peso:
            print("Ciclo negativo encontrado")
            return None
        
    caminho = []
    u = vDestino
    if dist[vDestino] != math.inf:
        while u != None:
            caminho.append(u)
            u = pred[u]
        caminho.reverse()

    print(caminho)

    return dist[vDestino]
