import random
import time


def crear_matriz(n: int):
    """Crea una matriz nxn con enteros aleatorios desde el 0 hasta el 99."""
    return [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]

def multiplicar(A, B):
    m = len(A)
    n1 = len(A[0])
    n2 = len(B)
    p = len(B[0])

    if n1 != n2:
        raise Exception("Las matrices no se pueden multiplicar")

    B_T = [[0 for _ in range(n2)] for _ in range(p)]
    for i in range(n2):
        filaB = B[i]
        for j in range(p):
            B_T[j][i] = filaB[j]

    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        filaA = A[i]
        for j in range(p):
            columnaB = B_T[j]
            s = 0
            for k in range(n1):
                s += filaA[k] * columnaB[k]
            result[i][j] = s

    return result



def imprimir_parcial(M, max_filas: int = 4, max_cols: int = 4):
    n_filas = len(M)
    n_cols  = len(M[0])
    filas_mostrar = min(max_filas, n_filas)
    cols_mostrar  = min(max_cols,  n_cols)

    for i in range(filas_mostrar):
        fila_str = [str(M[i][j]).rjust(5) for j in range(cols_mostrar)]
        sufijo = "  ..." if n_cols > cols_mostrar else ""
        print("  [" + "  ".join(fila_str) + sufijo + " ]")

    if n_filas > filas_mostrar:
        print(f"  ... ({n_filas} filas x {n_cols} cols en total)")



def ejecutar_para_tamano(n: int, mostrar_matrices: bool = True):
    print(f"\n{'='*60}")
    print(f"  Tamaño: {n} x {n}")
    print(f"{'='*60}")

    t0 = time.perf_counter()
    A = crear_matriz(n)
    B = crear_matriz(n)
    t1 = time.perf_counter()
    print(f"  Tiempo creación matrices: {t1 - t0:.6f} s")

    if mostrar_matrices:
        print("\n  Matriz A:")
        imprimir_parcial(A, max_filas=n, max_cols=n)
        print("\n  Matriz B:")
        imprimir_parcial(B, max_filas=n, max_cols=n)
    else:
        print(f"\n  (Matrices demasiado grandes para mostrar completas)")
        print("  Primeros 4x4 de A:")
        imprimir_parcial(A)
        print("  Primeros 4x4 de B:")
        imprimir_parcial(B)

    print("\n  Multiplicando...")
    t2 = time.perf_counter()
    C = multiplicar(A, B)
    t3 = time.perf_counter()
    print(f"  Tiempo multiplicación: {t3 - t2:.6f} s")

    if mostrar_matrices:
        print("\n  Resultado C = A x B:")
        imprimir_parcial(C, max_filas=n, max_cols=n)
    else:
        print("\n  Primeros 4x4 del resultado C = A x B:")
        imprimir_parcial(C)

    return t3 - t2


def comparar_tamanos(tamanos: list):
    resultados = []

    for n in tamanos:
        mostrar_completo = (n <= 20)
        try:
            t = ejecutar_para_tamano(n, mostrar_matrices=mostrar_completo)
            resultados.append((n, t))
        except MemoryError:
            print(f"\n  [!] MemoryError para n={n}. Tu computadora no soporta este tamaño.")
            break
        except Exception as e:
            print(f"\n  [!] Error para n={n}: {e}")
            break


    print(f"\n{'='*60}")
    print("  RESUMEN DE TIEMPOS")
    print(f"{'='*60}")
    print(f"  {'n':>8}  {'Tiempo (s)':>12}")
    print(f"  {'-'*8}  {'-'*12}")
    for n, t in resultados:
        print(f"  {n:>8}  {t:>12.6f}")
    print(f"{'='*60}\n")



if __name__ == "__main__":
    print("Opciones:")
    print("  1. Ejecutar todos los tamaños de prueba (10, 100, 1000)")
    print("  2. Ingresar un tamaño personalizado")
    opcion = input("\nElige una opción (1/2): ").strip()

    if opcion == "1":
        tamanos = [10, 100, 1000]
        agregar = input("¿Agregar 10000x10000? Puede tardar mucho (s/n): ").strip().lower()
        if agregar == "s":
            tamanos.append(10000)
        comparar_tamanos(tamanos)

    elif opcion == "2":
        try:
            n = int(input("Ingresa el tamaño n (entero positivo): "))
            if n <= 0:
                raise ValueError("n debe ser positivo")
            ejecutar_para_tamano(n, mostrar_matrices=(n <= 20))
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Opción no válida.")