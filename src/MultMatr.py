def transponer(B):
    # Crea una matriz vacía con dimensiones invertidas
    filas = len(B)
    cols  = len(B[0])
    B_T = [[0] * filas for _ in range(cols)]
    
    # Intercambia filas por columnas
    for i in range(filas):
        for j in range(cols):
            B_T[j][i] = B[i][j]
    
    return B_T


def multiplicar(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    B_T = transponer(B)  # Transponemos B para acceder por filas en vez de columnas
    
    C = [[0] * p for _ in range(m)]
    
    for i in range(m):        # Recorre filas de A
        for j in range(p):    # Recorre columnas de B (filas de B_T)
            for k in range(n):  # Producto punto fila x columna
                C[i][j] += A[i][k] * B_T[j][k]  # Ahora B_T[j][k] en vez de B[k][j]
    
    return C


# ---- PRUEBA 3x3 ----
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matriz A:")
for fila in A:
    print(" ", fila)

print("\nMatriz B:")
for fila in B:
    print(" ", fila)

print("\nMatriz B transpuesta:")
for fila in transponer(B):
    print(" ", fila)

print("\nResultado A x B:")
C = multiplicar(A, B)
for fila in C:
    print(" ", fila)