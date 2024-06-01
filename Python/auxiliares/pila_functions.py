from queue import LifoQueue as Pila


def getAll(queue: Pila) -> list:
    lst: list = []
    while not queue.empty():
        lst += [queue.get()]
    for i in range(len(lst)-1, -1, -1):
        queue.put(lst[i])
    return lst


def cantidad_elementos(p: Pila) -> int:
    lst_elementos: list = []
    cant_elementos: int = 0
    while not p.empty():
        lst_elementos += [p.get()]
    cant_elementos = len(lst_elementos)
    for i in range(cant_elementos - 1, -1, -1):
        p.put(lst_elementos[i])
    return cant_elementos


def buscar_max(pint: Pila[int]) -> int:
    lst_enteros: list[int] = [pint.get()]
    max_num: int = lst_enteros[0]
    for i in range(cantidad_elementos(pint)):
        num_actual: int = pint.get()
        lst_enteros.append(num_actual)
        if num_actual > max_num:
            max_num = num_actual
    for i in range(len(lst_enteros) - 1, -1, -1):
        pint.put(lst_enteros[i])
    return max_num
