# Replace the "ANSWER HERE" for your answer

def countdown(n):
    """
    Retorna una lista con la cuenta regresiva desde n hasta 0.
    Si n < 0, retorna una lista vacia.

    Ejemplo: countdown(5) -> [5, 4, 3, 2, 1, 0]
    Ejemplo: countdown(0) -> [0]
    Ejemplo: countdown(-1) -> []
    """
    if n < 0:
        return []
    rta = []
    while n >= 0:
        if n == 0:
            rta.append(n)
            return rta
        else:
            rta.append(n)
            n = n - 1

print(countdown(5))

print(countdown(-1))

def double_until(limit):
    """
    Comenzando desde 1, va duplicando el valor y agrega cada uno
    a una lista mientras sea menor o igual a limit.
    Si limit < 1, retorna una lista vacia.

    Ejemplo: double_until(10) -> [1, 2, 4, 8]
    Ejemplo: double_until(1) -> [1]
    Ejemplo: double_until(0) -> []
    """
    if limit == 1:
        return [1]

    if limit == 0:
        return []

    else:
        rta = []
        n = 1
        while n <= limit:
            rta.append(n)
            n = n * 2
            if n *2 > limit:
                rta.append(n)
                return rta

print(double_until(10))
