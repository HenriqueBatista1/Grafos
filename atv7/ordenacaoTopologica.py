def classificaArestasDFS(G, start):
    num_vertices = len(G)
    L = []
    cor = ["branco"] * num_vertices
    tipoArestas = []
    for _ in range(num_vertices):
        nova_linha = []
        for _ in range(num_vertices):
            nova_linha.append("")
        tipoArestas.append(nova_linha)
    tempoD = [0] * num_vertices
    tempoT = [0] * num_vertices
    tempo = 0

    def visitaDFS(v):
        cor[v] = "cinza"
        nonlocal tempo
        tempo += 1
        tempoD[v] = tempo
        for vizinho in G[v]:
            if cor[vizinho] == "branco":
                tipoArestas[v][vizinho] = "tree"
                visitaDFS(vizinho)
            elif cor[vizinho] == "cinza":
                tipoArestas[v][vizinho] = "back"
            else:
                if tempoD[v] < tempoD[vizinho]:
                    tipoArestas[v][vizinho] = "forward"
                else:
                    tipoArestas[v][vizinho] = "cross"
        cor[v] = "preto"
        tempo += 1
        tempoT[v] = tempo
        L.append(v)

    vertices = [start] + [vertice for vertice in range(num_vertices) if vertice != start]

    for vertice in vertices:
        if cor[vertice] == "branco":
            visitaDFS(vertice)

    return reversed(L)

def OrdenacaoTopologica(G, v):
    L = []
    num_vertices = len(G)
    cor = ["branco"] * num_vertices
    tipoArestas = []
    for _ in range(num_vertices):
        nova_linha = []
        for _ in range(num_vertices):
            nova_linha.append("")
        tipoArestas.append(nova_linha)
    TempoD = [0] * num_vertices
    TempoT = [0] * num_vertices
    tempo = 0

    ciclo_encontrado = False

    def classificaArestaDFS(v):
        nonlocal ciclo_encontrado
        cor[v] = "cinza"
        nonlocal tempo
        tempo += 1
        TempoD[v] = tempo
        for vizinho in G[v]:

            if ciclo_encontrado:
                return

            if cor[vizinho] == "branco":
                tipoArestas[v][vizinho] = "tree"
                classificaArestaDFS(vizinho)
            elif cor[vizinho] == "cinza":
                tipoArestas[v][vizinho] = "back"
                ciclo_encontrado = True
                return
            else:
                if TempoD[v] < TempoD[vizinho]:
                    tipoArestas[v][vizinho] = "forward"
                else:
                    tipoArestas[v][vizinho] = "cross"
        
        cor[v] = "preto"
        tempo += 1
        TempoT[v] = tempo
        L.append(v)

    vertices = [v] + [vertice for vertice in range(num_vertices) if vertice != v]

    for vertice in vertices:
        if cor[vertice] == "branco":
            classificaArestaDFS(vertice)
            if ciclo_encontrado:
                break

    if ciclo_encontrado:
        return False
    else:
        return reversed(L)