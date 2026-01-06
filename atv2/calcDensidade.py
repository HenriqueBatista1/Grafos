import numpy as np

def calcDensidade(matriz):
    qtdVertices = np.shape(matriz)[0]
    qtdArestas = np.sum(matriz)
    densidade = (qtdArestas) / (qtdVertices * (qtdVertices - 1))
    print(f'{densidade:.3f}')