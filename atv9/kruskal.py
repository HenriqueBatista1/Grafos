import heapq

# Variáveis globais (ou poderiam estar numa classe)
link = {}
size = {}

def make_set(vertice):
    link[vertice] = vertice
    size[vertice] = 1

def find(x):
    # Path Compression
    if x != link[x]:
        link[x] = find(link[x]) # Correção: Chamada recursiva com ()
    return link[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False # Já estão no mesmo conjunto

    # Union by Size
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a # Swap para garantir que A é maior
        
    link[root_b] = root_a
    size[root_a] += size[root_b]
    return True

def kruskal(G):
    # 1. Inicializa o Union-Find para cada vértice existente no grafo
    for v in G:
        make_set(v)

    # 2. Monta a MinHeap
    arestas = []
    # Não precisa de heapify inicial se appendarmos com heappush
    
    visitados = set() # Para evitar duplicar arestas em grafos não direcionados (opcional)

    for v in G:
        for u, peso in G[v].items():
            # Opcional: só adiciona se v < u para não por (A,B) e (B,A)
            # Mas o Kruskal funciona mesmo sem isso, só é menos eficiente
            heapq.heappush(arestas, (peso, v, u))

    mst = []

    # O BLOCO DE UNION QUE VOCÊ TINHA AQUI FOI REMOVIDO

    # 3. Processa as arestas
    while arestas and len(mst) < len(G) - 1:
        peso, u, v = heapq.heappop(arestas)

        # Se u e v não estão conectados, une e adiciona na MST
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, peso))

    return mst