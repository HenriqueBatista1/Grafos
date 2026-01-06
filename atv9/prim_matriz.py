import math

def prim(G, start):

    s = [start]
    n = []
    for x in range(len(G)):
        if x != start:
            n.append(x)

    mst = []
    custo_total = 0

    while(len(mst) < len(G) - 1):

        menorCusto = math.inf
        for v in s:
            for u in n:
                if G[v][u] != 0 and G[v][u] < menorCusto:
                    menorCusto = G[v][u]
                    menorV = v
                    menorU = u

        if menorCusto == math.inf:
            print("Grafo desconexo!")
            break

        n.remove(menorU)
        s.append(menorU)    
        mst.append((menorV, menorU))
        custo_total += menorCusto

    return mst, custo_total
