### Inteligencia Artificial

## Multiplicación de Matrices
La **multiplicación de matrices** es una operación del álgebra lineal que permite combinar dos matrices para obtener una nueva matriz como resultado. Para que esta operación sea posible, el número de **columnas de la primera matriz debe ser igual al número de filas de la segunda matriz**. El cálculo se realiza multiplicando cada elemento de una **fila de la primera matriz** por el elemento correspondiente de una **columna de la segunda matriz**, y luego sumando todos esos productos para obtener un solo valor en la matriz resultante. Este proceso se repite para cada fila y cada columna hasta completar toda la nueva matriz. En programación, este procedimiento normalmente se implementa con **tres ciclos anidados**, lo que hace que el algoritmo tenga una **complejidad de tiempo O(n³)**, ya que se realizan múltiples multiplicaciones y sumas para cada posición de la matriz resultado.



*Pseudocódigo*


Algoritmo CrearMatriz(n)
```text
    Crear matriz M de tamaño n x n
    Para i ← 0 hasta n-1
        Para j ← 0 hasta n-1
            M[i][j] ← número aleatorio entre 0 y 99
        FinPara
    FinPara
    Retornar M
```

Algoritmo Multiplicar(A, B)

```text
    m ← número de filas de A
    n1 ← número de columnas de A
    n2 ← número de filas de B
    p ← número de columnas de B

    Si n1 ≠ n2
        Mostrar "Las matrices no se pueden multiplicar"
        Terminar
    FinSi

    Crear matriz B_T de tamaño p x n2

    Para i ← 0 hasta n2-1
        Para j ← 0 hasta p-1
            B_T[j][i] ← B[i][j]
        FinPara
    FinPara

    Crear matriz RESULTADO de tamaño m x p

    Para i ← 0 hasta m-1
        Para j ← 0 hasta p-1
            suma ← 0
            Para k ← 0 hasta n1-1
                suma ← suma + A[i][k] * B_T[j][k]
            FinPara
            RESULTADO[i][j] ← suma
        FinPara
    FinPara

    Retornar RESULTADO
```