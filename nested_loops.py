# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    result = []
    for lista in matrix:
        for elemento in lista:
            result.append(elemento)
    return result
print(flatten([[1, 2], [3, 4], [5, 6]]))


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    result = []
    for lista in matrix:
        suma = 0
        for elemento in lista:
            suma = suma + elemento
        result.append(suma)
    return result

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    rta = []

    for j in range(len(matrix[0])):
        total = 0

        for fila in matrix:
            total = total + fila[j]

        rta.append(total)

    return rta
    return rta
print(col_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))