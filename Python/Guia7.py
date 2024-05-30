import math
import random
import numpy as np


def list_to_str(caracteres: list[chr]):
    convertida: str = ''
    for c in caracteres:
        convertida = convertida + c
    return convertida


def revertir(lista: list) -> list:
    rev: list = []
    for i in range(len(lista) - 1, -1, -1):
        rev.append(lista[i])
    return rev

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
def ordenados(sequencia: list) -> bool:
    return ordenar(sequencia) == sequencia


def ordenar(sequencia: list[int]) -> list[int]:
    sequencia_a_ordenar: list[int] = sequencia.copy()
    sequenciaOrdenada: list[int] = []
    while sequencia_a_ordenar != []:
        sequenciaOrdenada = sequenciaOrdenada + [max(sequencia_a_ordenar)]
        sequencia_a_ordenar.remove(max(sequencia_a_ordenar))
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
        if vocal in sequencia or vocal.upper() in sequencia:
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
        dada_vuelta += palabra_sin_mod[i]
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


# Ej 4.3                !!! Esta rara idea del problema, no me queda del todo claro como se gana. No se si esta bien hecho realmente. Pero bueno yo lo intenté.!!!
def siete_y_medio():
    lista_rans: list = [siete_y_medio_rand_2()]
    decision: str = ""
    while decision != "P":
        suma_rans: float = 0
        if decision == "S":
            lista_rans += [siete_y_medio_rand_2()]
        for n in range(len(lista_rans)):
            valor: int = lista_rans[n]
            if valor in [10, 11, 12]:
                suma_rans += 0.5
            else:
                suma_rans += valor
        if suma_rans > 7.5:
            print("La suma de sus cartas supera siete y medio. Ha perdido")
            decision = "P"
        else:
            print("¿Desea seguir o plantarse? S/P")
            decision = input()
    print(lista_rans)


def siete_y_medio_rand() -> int:
    numero_random: int = 8
    while numero_random == 8 or numero_random == 9:
        numero_random = random.randint(1, 12)
    return numero_random


# Otra forma de hacer el random, medio paja usarla si son muchos numeros. Pero si son poquitos como en este ej, esta bastante buena.
def siete_y_medio_rand_2() -> int:
    figuras: list[int] = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    numero_random: int = random.choice(figuras)
    return numero_random


# Ej 5.1
# la funcion in es lo mismo que pertenece, no me rompas los huevos persona que este leyendo esto por alguna razon. Si sos tom, comeme los huevos hostia chaval.
def pertenece_a_cada_uno_version_1(seq: list[list[int]], num: int, valores_de_verdad: bool):
    for lista in seq:
        valores_de_verdad += [(num in lista)]


# Ej 5.2
# Cambia el primer asegura, osea |res| = |s| y el primero era |res| >= |s|
# Ya que 0 <= i < |s| para ambos, el indice maximo de res es |s|-1. Osea |res| no va a ser mayor a |s|, siempre van a ser iguales con el segundo asegura.
# Se puede usar la implementacion del ejercicio 2 para la especificacion del 1 y viceversa.
# ¿ Relacion de fuerza ? -> Que pingo es.

# Ej 5.3
def es_matriz(seq: list[list[int]]) -> bool:
    cant_elem: int = -1
    misma_cantidad: bool = True
    mas_de_un_elemento: bool = False
    if len(seq) > 0:
        if len(seq[0]) > 0:
            mas_de_un_elemento = True
    for i in range(len(seq)):
        if cant_elem == -1:
            cant_elem = len(seq[i])
        elif cant_elem != len(seq[i]):
            misma_cantidad = False
    return mas_de_un_elemento and misma_cantidad


# Ej 5.4
def filas_ordenadas(seq: list[list[int]]) -> list[bool]:
    lista_bools: list[bool] = []
    for i in range(len(seq)):
        lista_bools += [ordenados(seq[i])]
    return lista_bools


# Ej 5.5
def potencia_matriz(d: int, p: int):
    mat = np.random.random((d, d))
    # mat = np.matrix([[1, 2, 6], [0, 3, -3], [3, 1, 0]])
    num = mat.copy()
    if p > 0:
        for a in range(p-1):
            num = mult_matriz(num, mat, d)
    else:
        num = np.identity(d, int)
    return num


def mult_matriz(n: np.matrix, m: np.matrix, d: int):
    mat_prim: np.matrix = n.copy()
    mat_sec: np.matrix = m.copy()
    res: np.matrix = n.copy()
    for i in range(d):
        for k in range(d):
            suma_col: int = 0
            for j in range(d):
                suma_col += mat_prim[i, j] * mat_sec[j, k]
            res[i, k] = suma_col
    return res


d = 2
p = 5
print(potencia_matriz(d, p))
