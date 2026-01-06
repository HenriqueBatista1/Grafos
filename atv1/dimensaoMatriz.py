import numpy as np

def dimensaoMatriz(matriz):
    diagonal = np.diagonal(matriz)
    print(np.shape(matriz), diagonal)

dimensaoMatriz([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
