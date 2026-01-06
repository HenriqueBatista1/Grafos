from collections import deque

def verificar_bipartido(G):
    """
    Verifica se um grafo é bipartido usando a abordagem de coloração com duas cores (BFS).

    Args:
        G (dict): O grafo representado como uma lista de adjacência.
                  Ex: G = {'A': ['B', 'C'], 'B': ['A', 'D'], ...}

    Returns:
        bool: True se o grafo for bipartido, False caso contrário.
    """
    # Dicionário para armazenar as cores dos vértices.
    # Nenhum vértice foi visitado/colorido ainda.
    cores = {}
    
    # Este laço garante que o algoritmo funcione para grafos desconexos.
    # Ele inicia uma nova busca para cada componente não visitado do grafo.
    for vertice_inicial in G:
        if vertice_inicial not in cores:
            # Passo 1: Iniciar pelo vértice e colori-lo com a Cor 1 (usaremos 0)
            cores[vertice_inicial] = 0
            fila = deque([vertice_inicial])

            while fila:
                vertice_atual = fila.popleft()

                # Passo 2 e 3: Colorir os adjacentes e verificar conflitos
                for vizinho in G[vertice_atual]:
                    # Caso 1: O vizinho ainda não foi colorido
                    if vizinho not in cores:
                        # Atribui a cor oposta à do vértice atual
                        cores[vizinho] = 1 - cores[vertice_atual]
                        fila.append(vizinho)
                    
                    # Caso 2: O vizinho já foi colorido
                    # Verifica se o vizinho tem a mesma cor do vértice atual
                    elif cores[vizinho] == cores[vertice_atual]:
                        # Conflito encontrado! O grafo não é bipartido.
                        print(f"Conflito: Vértice '{vertice_atual}' (cor {cores[vertice_atual]}) e seu vizinho '{vizinho}' (cor {cores[vizinho]}) têm a mesma cor.")
                        return False

    # Se o laço terminar sem encontrar conflitos, o grafo é bipartido.
    print("Nenhum conflito encontrado. O grafo é bipartido.")
    return True

# --- Exemplos de Uso ---

# Exemplo 1: Grafo Bipartido
# Partições: {A, C} e {B, D}
grafo_bipartido = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}
print("Verificando Grafo 1 (Bipartido):")
print(f"Resultado: {verificar_bipartido(grafo_bipartido)}\n")


# Exemplo 2: Grafo NÃO Bipartido (possui um ciclo ímpar A-B-C-A)
grafo_nao_bipartido = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
print("Verificando Grafo 2 (NÃO Bipartido):")
print(f"Resultado: {verificar_bipartido(grafo_nao_bipartido)}\n")


# Exemplo 3: Grafo Desconexo e Bipartido
grafo_desconexo = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C']
}
print("Verificando Grafo 3 (Desconexo e Bipartido):")
print(f"Resultado: {verificar_bipartido(grafo_desconexo)}")