from queue import LifoQueue as Pila


def getAll(queue: Pila) -> list:
    lst: list = []
    while not queue.empty():
        lst += [queue.get()]
    for i in range(len(lst)-1, -1, -1):
        queue.put(lst[i])
    return lst
