import numpy as np

def tipoGrafo(matriz):
    qtdVertices = np.shape(matriz)[0]
    flag = '0'
    for i in range(0, qtdVertices):
        for j in range(i + 1, qtdVertices):
            if matriz[i][j] != matriz[j][i]:
                flag = '1'
    
    if np.sum(np.diagonal(matriz)) > 0: 
        flag = '3' + flag
        return flag
    else:
        for i in range(0, qtdVertices):
            for j in range(i + 1, qtdVertices):
                if matriz[i][j] > 1 or matriz[j][i] > 1:
                    flag = '2' + flag
                    return flag
    return flag


tipoGrafo([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])