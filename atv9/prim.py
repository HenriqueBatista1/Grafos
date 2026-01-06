import heapq

def prim(grafo, start):
    num_vertices = len(grafo)
    pq = []
    visitados = [False] * num_vertices
    custo_total = 0

    # Inicialização do nó de partida
    visitados[start] = True
    
    # Adiciona arestas do nó inicial na fila: (peso, origem, destino)
    for destino, peso in grafo[start]:
        if not visitados[destino]:
            heapq.heappush(pq, (peso, start, destino))

    mst = []

    while pq and len(mst) < num_vertices - 1:
        # Extrai a aresta de menor peso
        peso, origem, destino = heapq.heappop(pq)

        # Se o destino já foi visitado, ignoramos (Lazy Deletion)
        if visitados[destino]:
            continue

        # 1. Confirma a aresta na MST (Correção da tupla)
        mst.append((origem, destino))
        custo_total += peso
        
        # 2. Marca o NOVO vértice como visitado (Correção de lógica)
        visitados[destino] = True
        
        # 3. Adiciona os vizinhos do NOVO vértice na fila (Correção de expansão)
        for vizinho, peso_aresta in grafo[destino]:
            if not visitados[vizinho]:
                heapq.heappush(pq, (peso_aresta, destino, vizinho))

    # Validação final
    # Nota: Em grafos desconexos, len(mst) pode ser menor e isso é normal, 
    # mas para MST válida deve conectar tudo.
    if len(mst) != num_vertices - 1:
        print("Atenção: O grafo é desconexo, não há MST global.")

    return (custo_total, mst)