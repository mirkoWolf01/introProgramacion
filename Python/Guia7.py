import math


def list_to_str(caracteres: list[chr]):
    convertida: str = ''
    for c in caracteres:
        convertida = convertida + c
    return convertida

# PRIMERA PARTE


# Ej 1.1
def pertenece(num: int, sequencia: list) -> bool:   # Forma 1
    está: bool = False
    for n in sequencia:
        if num == n:
            está = True
            break
    return está


def pertenece2(elemento, sequencia: list) -> bool:  # a in [a,b,c,d]
    return 0 < sequencia.count(elemento)


def pertenece3(num: int, sequencia: list) -> bool:
    while sequencia != []:
        if num == sequencia.pop(0):
            return True
    return False

# print(pertenece(int(input()), [int(x) for x in list(input())])) --> [int(x) for x in list(input())] Sirve para convertir chars del input a una lista de ints
# print(pertenece(2, [123, 3, 2]))


# Ej 1.2
def divide_a_todos(num: int, sequencia: list) -> bool:
    for elem in sequencia:
        if elem % num != 0:
            return False
    return True


# Ej 1.3
def suma_total(sequecia: list) -> int:  # Es basicamente sum ()
    valorActual: int = 0
    while sequecia != []:
        valorActual = valorActual + sequecia.pop(0)
    return valorActual


# Ej 1.4
def ordenados(sequencia: list) -> list:
    sequenciaOrdenada: list = []
    while sequencia != []:
        sequenciaOrdenada = sequenciaOrdenada + [max(sequencia)]
        sequencia.remove(max(sequencia))
    return sequenciaOrdenada


# Ej 1.5
def alguna_palabra_larga(palabras: list[str]) -> bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False


# Ej 1.6
def es_palidromo(texto: str) -> list:
    reverso: list[str] = list(texto)
    reverso.reverse()
    return list(texto) == reverso


# Ej 1.7
def fortaleza_contraseña(contraseña: str) -> str:
    largo: int = len(contraseña)
    if largo < 5:
        return "ROJA"
    elif largo <= 8 or contraseña.isalpha() or contraseña.islower() or contraseña.isupper() or contraseña.isnumeric():
        return "AMARILLO"
    else:
        return "VERDE"


# Ej 1.8
def mov_bancario(historial: list[tuple]) -> int:
    monto_total: int = 0
    for (tipo_de_movimiento, cantidad) in historial:
        if tipo_de_movimiento == 'R':
            monto_total = monto_total - cantidad
        if tipo_de_movimiento == 'I':
            monto_total = monto_total + cantidad
    return monto_total


# Ej 1.9
def vocales_distintas(sequencia: str) -> bool:
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador: int = 0
    for vocal in vocales:
        if vocal in sequencia:
            contador = contador + 1
    return contador >= 3

# SEGUNDA PARTE


# Ej 2.1
def par_a_0_inout(sequencia: list):   # ¿Es inout?
    for i in range(len(sequencia)):
        if (i % 2 == 0):
            sequencia[i] = 0


# Ej 2.2
def par_a_0_in(sequencia: list) -> list:    # ¿Es in?
    entrada: list = sequencia.copy()
    for i in range(len(entrada)):
        if (i % 2 == 0):
            entrada[i] = 0
    return entrada


# Ej 2.3
def borrar_vocales(seq: list) -> list:
    caracteres: list = seq.copy()
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        while vocal in caracteres:
            caracteres.remove(vocal)
    return caracteres


# Ej 2.4
def reemplaza_vocales(seq: list) -> list:
    caracteres: list = seq.copy()
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        while vocal in caracteres:
            caracteres[caracteres.index(vocal)] = '-'
    return caracteres


# Ej 2.5
# Podria haber usado .reverse y pasalrlo a str pero me parecio muy secillo.
def da_vuelta_str(palabra: str) -> str:
    dada_vuelta: str = ''
    palabra_sin_mod: str = list(palabra).copy()
    for i in range(len(palabra_sin_mod)-1, -1, -1):
        dada_vuelta = dada_vuelta + palabra_sin_mod[i]
    return dada_vuelta


def da_vuelta_str_facil(palabra: str) -> str:
    palabra_a_revertir: list = list(palabra).copy()
    palabra_a_revertir.reverse()
    return list_to_str(palabra_a_revertir)


# Ej 2.6
def elimiar_repetidos(sequencia: list[chr]) -> str:  # Es in
    mod_sequencia: list = sequencia.copy()
    mod_sequencia.reverse()
    for i in sequencia:
        while mod_sequencia.count(i) > 1:
            mod_sequencia.remove(i)
    mod_sequencia.reverse()
    return list_to_str(mod_sequencia)


# Ej 3
def aprobado(notas: list[int]) -> int:
    promedio: float = 0
    todas_aprobadas: bool = True
    res: int = 0
    for nota in notas:
        promedio = promedio + nota
        if nota < 4:
            todas_aprobadas = False
    promedio = promedio / len(notas)
    if not todas_aprobadas:
        res = 3
    elif promedio >= 7:
        res = 1
    else:
        res = 2
    return res


# Ej 4.1
def generar_lista_alumnos():
    termino: bool = False
    lista_alumos: list[str] = []
    while not termino:
        estudiante: str = input()
        if estudiante == "listo":
            termino = True
        else:
            lista_alumos = lista_alumos + [estudiante]
    print(lista_alumos)

# Ej 4.2


def historial_monedero():
    finalizo: bool = False
    dinero_total: int = 0
    while not finalizo:
        print("Ingrese tipo de movimiento: ")
        movimiento: str = input()
        if movimiento == "C":
            print("Ingrese monto a cargar: ")
            dinero_total += int(input())
        if movimiento == "D":
            print("Ingrese monto a descontar: ")
            dinero_total -= int(input())
        if movimiento == "X":
            finalizo = True
    print(dinero_total)
