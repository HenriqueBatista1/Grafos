from collections import deque

def coloracaoSequencialCorreta(G, start):
    """
    Implementa o algoritmo de Coloração Sequencial Gulosa para um grafo.

    Args:
        G (dict): O grafo representado como uma lista de adjacência (dicionário).
                  Ex: G = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
        start (any): O vértice inicial para a ordem de coloração.

    Returns:
        tuple: Um dicionário com as cores de cada vértice e o número total de cores usadas.
    """
    # 1. Estrutura para armazenar as cores. Usamos um dicionário.
    #    Nenhum vértice está colorido no início.
    cores = {}

    # 2. Define a ordem de visita dos vértices. A sua ideia de usar deque é boa.
    ordem_vertices = deque([start] + [vertice for vertice in G.keys() if vertice != start])

    # 3. Itera sobre cada vértice na ordem definida para colori-lo.
    for vertice_atual in ordem_vertices:
        cores_dos_vizinhos = set()
        
        # 4. Encontra as cores de todos os vizinhos já coloridos.
        for vizinho in G[vertice_atual]:
            if vizinho in cores:
                cores_dos_vizinhos.add(cores[vizinho])
        
        # 5. Encontra a menor cor disponível.
        idCor = 0
        while idCor in cores_dos_vizinhos:
            idCor += 1
            
        # 6. Atribui a menor cor encontrada ao vértice atual.
        cores[vertice_atual] = idCor
        
    # O número total de cores é o valor da maior cor + 1.
    num_cores = max(cores.values()) + 1 if cores else 0
    
    return cores, num_cores

# Exemplo de uso:
grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

cores_finais, total_cores = coloracaoSequencialCorreta(grafo_exemplo, 'A')

print(f"Cores atribuídas: {cores_finais}")
# Saída esperada (pode variar com a ordem, mas a lógica é a mesma): 
# Cores atribuídas: {'A': 0, 'B': 1, 'C': 2, 'D': 0}

print(f"Número total de cores usadas: {total_cores}")
# Saída esperada: 3