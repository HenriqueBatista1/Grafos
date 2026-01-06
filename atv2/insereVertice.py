import numpy as np

def insereVertice(matriz):
    ordem = np.shape(matriz)[0]
    matriz2 = np.array([[0 for i in range(ordem + 1)] for j in range(ordem + 1)])

    for i in range(ordem):
        for j in range(ordem):
            matriz2[i][j] = matriz[i][j]

    print(matriz2)
    
insereVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])