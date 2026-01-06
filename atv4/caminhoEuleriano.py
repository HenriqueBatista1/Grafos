import numpy as np

def caminhoEuleriano(matriz):
    
    n = np.shape(matriz)[0]

    conexo = True
    for i in range(0, n):
        conexo_check = 0
        for j in range(0, n):
            conexo_check += matriz[i][j]
            conexo_check += matriz[j][i]
        if conexo_check == 0:
            conexo = False
            break

    total = 0
    i = 0
    while (total <= 2 and i < n):
        grau = 0
        for j in range(0, n):
            grau += matriz[i][j]
        if grau % 2 != 0:
            total += 1
        i += 1

    if conexo:
        if total > 2 or total == 1:
            return False
        else:
            return True
    else:
        return False        