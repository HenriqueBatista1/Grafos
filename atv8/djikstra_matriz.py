import math
import heapq
    
def dijkstra(matriz, vOrigem, vDestino):

    dist = {}
    prev = {}

    for v in range(len(matriz)):
        dist[v] = math.inf
        prev[v] = None

    dist[vOrigem] = 0

    fila = [(0, vOrigem)]

    while fila:

        dist_atual, v = heapq.heappop(fila)

        if dist_atual > dist[v]:
            continue

        if v == vDestino:
            break

        for u in range(len(matriz)):
            peso = matriz[v][u]
            if peso > 0:
                if dist[u] > dist_atual + peso:
                    dist[u] = dist_atual + peso
                    prev[u] = v
                    heapq.heappush(fila, (dist[u], u))

    caminho = []
    u = vDestino

    if dist[u] != math.inf:
        while u != None:
            caminho.append(u)
            u = prev[u]
        caminho.reverse()

    if not caminho:
        return False

    return(caminho, dist[vDestino])    