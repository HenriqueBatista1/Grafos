def criaDicionario(matriz):
    matrizDict = {}
    for i, linha in enumerate(matriz):
        qtdElementos = []
        for j, elemento in enumerate(linha):
            if elemento > 0:
                qtdElementos.append(j)
        matrizDict[i] = qtdElementos
    print(matrizDict)

criaDicionario([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
                
