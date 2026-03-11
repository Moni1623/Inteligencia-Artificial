import heapq

def a_star(grafo, heuristicas, inicio, destino):
    # priority_queue guardará tuplas: (f_score, nodo, camino_actual, g_score)
    frontera = [(heuristicas[inicio], inicio, [inicio], 0)]
    visitados = set()

    while frontera:
        # Extraemos el nodo con el menor f(n) = g(n) + h(n)
        (f, nodo_actual, camino, g) = heapq.heappop(frontera)

        if nodo_actual == destino:
            return camino, g

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explorar vecinos
            for vecino, costo in grafo[nodo_actual].items():
                if vecino not in visitados:
                    nuevo_g = g + costo
                    nuevo_f = nuevo_g + heuristicas[vecino]
                    nuevo_camino = camino + [vecino]
                    heapq.heappush(frontera, (nuevo_f, vecino, nuevo_camino, nuevo_g))

    return None, float('inf')

# 1. Definición del Grafo (según las conexiones de tu imagen)
grafo = {
    'S': {'A': 5, 'B': 9, 'D': 6},
    'A': {'S': 5, 'B': 3, 'G': 9},
    'B': {'S': 9, 'A': 3, 'C': 1},
    'C': {'B': 1, 'D': 2, 'F': 7, 'I': 5},
    'D': {'S': 6, 'C': 2, 'E': 2},
    'E': {'D': 2, 'X': 3},
    'F': {'C': 7, 'I': 8, 'X': 2},
    'I': {'C': 5, 'F': 8, 'X': 3},
    'G': {'A': 9},
    'X': {'E': 3, 'F': 2, 'I': 3}
}

# 2. Valores de la Heurística h(n) (los números pequeños arriba de cada letra)
heuristicas = {
    'S': 5, 'A': 8, 'B': 4, 'C': 3, 'D': 2,
    'E': 1, 'F': 5, 'I': 2, 'G': 9, 'X': 0
}

# Ejecución
camino_optimo, costo_total = a_star(grafo, heuristicas, 'S', 'X')

print(f"Camino encontrado: {' -> '.join(camino_optimo)}")
print(f"Costo total (f): {costo_total}")