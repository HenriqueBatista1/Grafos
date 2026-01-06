def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        aux = lista[j]
        while j > 0 and aux < lista[j - 1]:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = aux
    return lista

def verificaDirigido(listaAdj):
    for (vertice, vizinhos) in listaAdj.items():
        for v in vizinhos:
            if vertice not in listaAdj[v]:
                return True
    return False

def insereArestaLista(listaAdj, vi, vj):

    ehDirigido = verificaDirigido(listaAdj)

    if ehDirigido:
        vertices = listaAdj[vi]
        vertices.append(vj)
        insertion_sort(vertices)
        listaAdj[vi] = vertices

        print(listaAdj)
    else:
        vertices = listaAdj[vi]
        vertices.append(vj)
        insertion_sort(vertices)
        listaAdj[vi] = vertices

        vertices = listaAdj[vj]
        vertices.append(vi)
        insertion_sort(vertices)
        listaAdj[vj] = vertices

        print(listaAdj)



insereArestaLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)