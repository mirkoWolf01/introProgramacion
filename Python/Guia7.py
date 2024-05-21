import math

# PRIMERA PARTE


# Ej 1
def pertenece(num: int, sequencia: list) -> bool:   # Forma 1
    está: bool = False
    for n in sequencia:
        if num == n:
            está = True
            break
    return está


def pertenece2(num: int, sequencia: list) -> bool:
    if 0 < sequencia.count(num):
        return True
    else:
        return False


def pertenece3(num: int, sequencia: list) -> bool:
    while sequencia != []:
        if num == sequencia.pop(0):
            return True
    return False

# print(pertenece(int(input()), [int(x) for x in list(input())])) --> [int(x) for x in list(input())] Sirve para convertir chars del input a una lista de ints
# print(pertenece(2, [123, 3, 2]))


# Ej 2
def divide_a_todos(num: int, sequencia: list) -> bool:
    for elem in sequencia:
        if elem % num != 0:
            return False
    return True


# Ej 3
def suma_total(sequecia: list) -> int:  # Es basicamente sum ()
    valorActual: int = 0
    while sequecia != []:
        valorActual = valorActual + sequecia.pop(0)
    return valorActual


# Ej 4
def ordenados(sequencia: list) -> list:
    sequenciaOrdenada: list = []
    while sequencia != []:
        sequenciaOrdenada = sequenciaOrdenada + [max(sequencia)]
        sequencia.remove(max(sequencia))
    return sequenciaOrdenada


# Ej 5
def alguna_palabra_larga(palabras: list[str]) -> bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False


# Ej 6
def es_palidromo(texto: str) -> list:
    reverso: list[str] = list(texto)
    reverso.reverse()
    return list(texto) == reverso


# Ej 7
def fortaleza_contraseña(contraseña: str) -> str:
    largo: int = len(contraseña)
    if largo < 5:
        return "ROJA"
    elif largo <= 8 or contraseña.isalpha() or contraseña.islower() or contraseña.isupper() or contraseña.isnumeric():
        return "AMARILLO"
    else:
        return "VERDE"
