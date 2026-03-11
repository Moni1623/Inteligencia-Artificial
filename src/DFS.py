def dfs(grafo, nodo_inicio):
    visitados = []        # Nodos ya visitados (en orden)
    pila = [nodo_inicio]  # Pila: el último en entrar es el primero en salir

    while pila:
        nodo = pila.pop()  # Saca el último nodo de la pila

        if nodo not in visitados:
            visitados.append(nodo)  # Lo marcamos como visitado

            # Agrega los vecinos a la pila (en reversa para mantener orden)
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)

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

print("\nRecorrido DFS desde A:")
resultado = dfs(grafo, 'A')
print(" ->".join(resultado))