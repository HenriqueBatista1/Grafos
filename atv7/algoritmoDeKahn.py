from collections import deque

def ordenacaoTopologicaKahn(G):
    L = []
    S = deque()

    num_vertices = len(G)
    grau_de_entrada = [0] * num_vertices

    for w in range(num_vertices):
        for v in G[w]:
            grau_de_entrada[v] += 1
            
    for i in range(num_vertices):
        if grau_de_entrada[i] == 0:
            S.append(i)

    while S:
        v = S.popleft()
        L.append(v)
        for w in G[v]:
            grau_de_entrada[w] -= 1
            if grau_de_entrada[w] == 0:
                S.append(w)
    
    if len(L) < num_vertices:
        return False
    else:
        return True
