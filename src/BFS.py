def bfs(grafo, nodo_inicio):
    visitados = []          # Nodos ya visitados (en orden)
    cola = [nodo_inicio]    # Cola: el primero en entrar es el primero en salir

    while cola:
        nodo = cola.pop(0)  # Saca el primer nodo de la cola

        if nodo not in visitados:
            visitados.append(nodo)  # Lo marcamos como visitado

            # Agrega los vecinos al final de la cola
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

    return visitados


# ---- PRUEBA ----
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Grafo:")
for nodo, vecinos in grafo.items():
    print(f"  {nodo} -> {vecinos}")

print("\nRecorrido BFS desde A:")
resultado = bfs(grafo, 'A')
print(" -> ".join(resultado))