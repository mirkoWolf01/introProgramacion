import math


# Ej 1

def imprimir_hola_mundo():
    print("Hola mundo")


def imprimir_un_verso():
    print("Árbol, hoja, salto, luz \nAproximación \nMueble, lana, gusto, pie \nTé, mar, gas, mirada")


def raizDe2():
    print(round(math.sqrt(2), 4))


def factorial_de_dos():
    print(math.factorial(2))


def perimetro():
    round(2 * math.pi, 4)

# Ej 2


def imprimir_saludo(nombre: str):
    print("Hola " + nombre)


def raiz_cuadrada_de(num: int) -> float:
    return math.sqrt(num)


def fahrenheit_a_celsius(temp: float) -> float:
    return ((temp-32)*5)/9


def imprimir_dos_veces(escribillo: str):
    print(escribillo * 2)


def es_multiplo_de(multiplo: int, num: int) -> bool:
    return ((multiplo % num) == 0)


def es_par(num: int) -> bool:
    return ((num % 2) == 0)


def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return math.ceil((comensales * min_cant_de_porciones)/8)

# EJ 3


def alguno_es_0(n: int, m: int) -> bool:
    return ((n == 0) or (m == 0))


def ambos_son_0(n: int, m: int) -> bool:
    return ((n == 0) and (m == 0))


def es_nombre_largo(nombre: str) -> bool:
    return ((nombre >= 3) and (nombre <= 8))


def es_bisiesto(año: int) -> bool:
    return ((año % 400) == 0) or (((año % 4) == 0) and ((año % 100) != 0))

# EJ 4


def peso_pino(altura: int) -> int:
    if (altura <= 3):
        return (altura * 100 * 3)
    else:
        return (900 + (altura-3) * 100 * 2)


def es_peso_util(peso: int) -> bool:
    return (max(min(1000, peso), 400) == peso)


def sirve_pino(altura: int) -> bool:
    return (es_peso_util(peso_pino(altura)))

# EJ 5


def devolver_el_doble_si_es_par(n: int) -> int:
    if ((n % 2) == 0):
        return (2*n)
    else:
        return n


def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if ((n % 2) == 0):
        return n
    else:
        return (n+1)


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if ((n % 9) == 0):
        return (n*3)
    if ((n % 3) == 0):
        return (n*2)


def lindo_nombre(nombre: str):
    if (len(nombre) >= 5):
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 caracteres"


def elRango(n: int):
    if (n < 5):
        return "Menor a 5"
    if (max(min(20, n), 10) == n):
        return "Entre 10 y 20"
    if (n > 20):
        return "Mayor a 20"


def jubilacion(edad: int, sexo: chr):
    if (sexo == 'F'):
        if (edad >= 60 or edad < 18):
            print("Anda de vacaciones")
        else:
            print("Te toca laburar")
    if (sexo == 'M'):
        if (edad >= 65 or edad < 18):
            print("Anda de vacaciones")
        else:
            print("Te toca laburar")

# Ej 6


def del_1_al_10():
    i: int = 1
    while (i <= 10):
        print(i)
        i = i+1


def del_10_al_40():
    i: int = 10
    while (i <= 40):
        print(i)
        i = i+1


def imprimir_eco_10_veces():
    i: int = 1
    while (i <= 10):
        print("eco")
        i = i+1


def despegue_cohete():
    i: int = 10
    while (i != 0):
        print(i)
        i = i-1
    print("Despegue")


def viaje_al_pasado(fecha_de_origen: int, destino: int):
    año_actual: int = fecha_de_origen
    while (año_actual > destino):
        print("Viajó un año al pasado, estamos en el año:" + str(año_actual))
        año_actual = año_actual - 1
    print("Llegamos al destino, el año " + str(año_actual))


def viaje_al_pasado_cada_20_años(fecha_de_origen: int, destino: int):
    año_actual: int = fecha_de_origen
    while (año_actual > destino):
        print("Viajó un año al pasado, estamos en el año:" + str(año_actual))
        año_actual = año_actual - 20
    print("Llegamos al destino, el año " + str(destino))

# Ej 7


def imprimir_eco_10_vece_con_for():
    for num in range(0, 10):
        print("eco")


def viaje_al_pasado_con_for(fecha_de_origen: int, destino: int):
    for año_actual in range((fecha_de_origen - 1), destino, -1):
        print("Viajó un año al pasado, estamos en el año:" + str(año_actual))
    print("Llegamos al destino, el año " + str(destino))


""" print("Escriba el año elegido:")
viaje_al_pasado_con_for(int(input()), 2020) """

# EJ 9

"""
1. Evaluar 3 veces seguidas resultaria en agragar a la variable global un +1 3 veces. El resultado seria 2 la primera vez.
    3 la segunda vez. Y 4 la tercera vez que se ejecute. 
2. Evaluar 3 veces seguidas rt no es diferente a ejecutarla una sola vez. Da siempre igual para rt(1,0) ya que solo usa variables locales.
"""
g: int = 0


def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g


""" 
print(ro(1))
print(ro(1))
print(ro(1))
 """
