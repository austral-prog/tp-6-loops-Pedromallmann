# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    if target not in lst:
        return -1
    else:
        suma = -1
        for elemento in lst:
            suma += 1
            if target == elemento:
                return suma


print(index_of("Black", ["Red", "Green", "Black"]))
print(index_of("Black", ["Red", "Green"]))



def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """

    nueva = lst[start:]
    if target not in nueva:
        return -1
    else:
        suma = -1
        for elemento in lst:
            suma += 1
            if suma >= start:
                if target == elemento:
                    return suma


print(index_of_by_index("Black", ["Red", "Green", "Black"], 2))
print(index_of_by_index("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"], 4))


def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    if "" not in lst:
        return -1
    else:
        suma = -1
        for elemento in lst:
            suma += 1
            if elemento == "":
                return suma

print(index_of_empty(["Red", "", "Green"]))
print(index_of_empty(["Red", "Green"]))
