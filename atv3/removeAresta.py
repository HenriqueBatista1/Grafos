def removeArestaLista(listaAdj, vi, vj):
    vizinhos = listaAdj[vi]
    for v in vizinhos:
        if v == vj:
            vizinhos.remove(vj)
    listaAdj[vi] = vizinhos

    vizinhos = listaAdj[vj]
    for v in vizinhos:
        if v == vi:
            vizinhos.remove(vi)
    listaAdj[vj] = vizinhos

    print(listaAdj) 