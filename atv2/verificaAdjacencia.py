def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0 and matriz[vj][vi] > 0:
        print('True')
    else:
        print('False')
    
verificaAdjacencia([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 0, 3)

    