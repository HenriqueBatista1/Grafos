from collections import deque

def DFS(G, v):
    marked = set([v])
    sequence = []
    stack = deque([v])
    ids = deque([v])
    for vertice in G.keys():
        if vertice != v:
            ids.append(vertice)

    while stack or ids:
        if not stack:
            visited = ids.popleft()
            if visited in marked:
                continue
            marked.add(visited)
            stack.append(visited)
        visited = stack.pop()
        sequence.append(visited)
        neighbors = G[visited]
        i = len(neighbors) - 1
        while (i >= 0):
            neighbor = neighbors[i]
            if neighbor not in marked:
                marked.add(neighbor)
                stack.append(neighbor)
            i -= 1
            
    print(sequence)

DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)


def DFS_mais_seguro(G, v):
    visitados = set()
    sequencia = []
    
    ids = [v] + [vertice for vertice in G.keys() if vertice != v]

    for id in ids:
        if id not in visitados:
            pilha = deque([id])
            visitados.add(id)
            while pilha:
                visitado = pilha.pop()
                sequencia.append(visitado)

                for vizinho in reversed(G[visitado]):
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        pilha.append(vizinho)
                            
    print(sequencia)

# Teste
DFS_mais_seguro({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
# Saída: [0, 1, 2, 3, 4, 5]


def dfs_professor_otimizado(listaAdj, v):
    """
    Implementação otimizada da lógica de DFS do pseudocódigo,
    usando um set para controle de visitados e uma estrutura clara
    para componentes desconexos.
    """
    # Estruturas de dados otimizadas
    visitados = set()
    sequencia = []
    # Usar deque é ligeiramente mais eficiente que list para append/pop
    P = deque() 
    
    # Lista priorizada de todos os vértices para o laço externo
    pontos_de_partida = [v] + [vertice for vertice in listaAdj.keys() if vertice != v]
    
    # Laço externo para garantir que todos os componentes sejam visitados
    for ponto_inicial in pontos_de_partida:
        if ponto_inicial not in visitados:
            # "Semeia" a pilha com o ponto de partida do novo componente
            P.append(ponto_inicial)

            # Laço interno da travessia DFS para um componente
            while P:
                # 1. "Espia" o topo da pilha, mas não remove (Lógica do Professor)
                t = P[-1]

                # Se o nó ainda não foi visitado/sequenciado...
                if t not in visitados:
                    # ...marca como visitado e adiciona à sequência
                    visitados.add(t)
                    sequencia.append(t)

                # Encontra vizinhos que ainda não foram visitados (eficiente com o set)
                adjViaveis = [vizinho for vizinho in listaAdj[t] if vizinho not in visitados]
                
                # 2. Se existem vizinhos viáveis, avança para o primeiro
                if adjViaveis:
                    P.append(adjViaveis[0])
                # 3. Se não, faz o backtrack (remove o topo da pilha)
                else:
                    P.pop()
            
    print(sequencia)

def DFS_marcar_no_processamento(G, v):
    visitados = set()
    sequencia = []
    
    ids = [v] + [vertice for vertice in G.keys() if vertice != v]

    for id in ids:
        if id not in visitados:
            pilha = deque([id])
            while pilha:
                visitado = pilha.pop()
                if visitado not in visitados:
                    visitados.add(visitado)
                    sequencia.append(visitado)
                    
                    for vizinho in reversed(G[visitado]):
                        pilha.append(vizinho)
                            
    print(sequencia)