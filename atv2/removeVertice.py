import numpy as np

def removeVertice(matriz, vi):
    ordem = np.shape(matriz)[0]
    for i in range(ordem):
        matriz[i][vi] = -1
        matriz[vi][i] = -1

    print(np.array(matriz))


removeVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2)