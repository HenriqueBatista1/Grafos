
def criaListaAdjacencias(matriz):
    listaAdjacencia = {}
    for i, linha in enumerate(matriz):
        qtdElementos = []
        for j, elemento in enumerate(linha):
            if elemento > 0:
                for _ in range(elemento):
                    qtdElementos.append(j)
        listaAdjacencia[i] = qtdElementos
    print(listaAdjacencia)



criaListaAdjacencias([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])