import numpy as np

def valorCelula(matriz, linha, coluna):
    linhas, colunas = np.shape(matriz)
    if linha > linhas or coluna > colunas:
        print('Erro')
    else:
        print(f'Celula[{linha}][{coluna}] = {matriz[linha][coluna]}')

valorCelula([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2, 3)