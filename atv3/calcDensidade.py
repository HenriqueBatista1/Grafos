
def verificaDirigido(listaAdj):
    for (vertice, vizinhos) in listaAdj.items():
        for v in vizinhos:
            if vertice not in listaAdj[v]:
                return True
    return False


def calcDensidadeLista(listaAdj):
    ehDirigido = verificaDirigido(listaAdj)
    arestas = 0
    vertices = 0

    for vizinhos in listaAdj.values():
        vertices += 1
        for _ in vizinhos:
            arestas += 1

    if (ehDirigido):
        resultado = (2 * arestas) / (vertices * (vertices - 1))
        print(f'{resultado:.3f}')
    else:
        resultado = arestas / (vertices * (vertices - 1))
        print(f'{resultado:.3f}')
        

