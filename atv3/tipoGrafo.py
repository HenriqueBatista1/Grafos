

def tipoGrafoLista(listaAdj):
    flag = '0'
    for (vertice, vizinhos) in listaAdj.items():
        for v in vizinhos:
            if vertice not in listaAdj[v]:
                flag = '1'

        
    for vertice, vizinhos in listaAdj.items():
        if (vertice in vizinhos):
            flag = '3' + flag
            print(flag)
            return
        
    for vizinhos in listaAdj.values():
        if len(vizinhos) != len(set(vizinhos)):
            flag = '2' + flag
            print(flag)
            return
        
    print(flag)  
        

tipoGrafoLista({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]})