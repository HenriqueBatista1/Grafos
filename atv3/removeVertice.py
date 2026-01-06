

def removeVerticeLista(listaAdj, vi):

    del listaAdj[vi]

    for vizinhos in listaAdj.values():
        for v in vizinhos[:]:
            if v == vi:
                vizinhos.remove(v)

    print(listaAdj)


removeVerticeLista({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 2)