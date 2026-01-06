import heapq
import math

def dijkstra(G, vInicio, vDestino):

    dist = {v: math.inf for v in G}
    prev = {v: None for v in G}

    dist[vInicio] = 0

    fila = [(0, vInicio)]

    while fila:
        dist_atual, v = heapq.heappop(fila)

        if dist_atual > dist[v]:
            continue

        if v == vDestino:
            break

        for u, peso in G[v].items():
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

# --- Exemplo de Uso ---

# Saída Esperada:
# O caminho mais curto de A para D é: A -> B -> C -> D
# Distância total: 4
if __name__ == '__main__':
    grafo_exemplo = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    inicio = 'A'
    fim = 'D'
    
    caminho, distancia = dijkstra(grafo_exemplo, inicio, fim)

    if caminho:
        print(f"O caminho mais curto de {inicio} para {fim} é: {' -> '.join(caminho)}")
        print(f"Distância total: {distancia}")
    else:
        print(f"Não existe caminho de {inicio} para {fim}.")