import auxiliares.str_functions as str_f
import auxiliares.list_functions as lst_f
import auxiliares.pila_functions as pif
from queue import LifoQueue as Pila
import random as rand

# Ej 1.1


def contar_lineas(nombre_archivo: str) -> int:
    cont: int = 0
    with open(f"{nombre_archivo}.txt", 'r') as file:
        lst_text: list = file.readlines()
        cont = len(lst_text)
    return cont


# Ej 1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    with open(f"{nombre_archivo}.txt", 'r') as file:
        text: str = file.read()
    return str_f.pertenece_str(palabra, text)


# Ej 1.3
def cant_apariciones(palabra: str, nombre_archivo: str) -> int:
    cant: int = 0
    with open(f"{nombre_archivo}.txt", 'r') as file:
        text: str = file.read()
        cant = len(str_f.find_all(palabra, text))
    return cant


# Ej 2
def clonar_sin_comentarios(nombre_archivo: str):
    def primer_caracter_no_vacio(line: str) -> str:
        c: str = ""
        for i in range(len(line)):
            if line[i] != " " and c == "":
                c = line[i]
        return c

    clean_file: list[str] = []
    with open(f"{nombre_archivo}.txt", 'r') as file:
        lst_lines: list[str] = file.readlines()
        for i in range(len(lst_lines)):
            if primer_caracter_no_vacio(lst_lines[i]) != "#":
                clean_file += lst_lines[i]
    with open(f"{nombre_archivo}_clean.txt", "w") as file:
        file.writelines(clean_file)


# Ej 3
def revertir_archivo(nombre_archivo: str):
    lst_text: list[str] = []
    with open(f"{nombre_archivo}.txt", "r") as file:
        lst_text = file.readlines()
    reverse: list[str] = lst_f.revertir(lst_text)
    if len(reverse) > 0:
        reverse[0] += "\n"
        reverse[len(reverse)-1] = str_f.cortar_hasta(
            hasta="\n",
            text=reverse[len(reverse)-1]
        )
    with open(f"{nombre_archivo}_reverse.txt", "w") as file:
        file.writelines(reverse)


# Ej 4
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    with open(f"{nombre_archivo}.txt", 'a') as file:
        file.write(f"\n{frase}")


# Ej 5
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    lst_text: list[str] = []
    with open(f"{nombre_archivo}.txt", 'r') as file:
        lst_text = file.readlines()
    with open(f"{nombre_archivo}.txt", 'w') as file:
        file.writelines([f"{frase}\n"]+lst_text)


# Ej 6
# Me quedo medio raro, no se si esta bien hecho.
def listar_palabras_de_archivo(nombre_archivo: str) -> list:
    lst_palabras: list[str] = []

    def es_caracter_palabra(byte: int):
        es_caracter_valido: bool = False
        if byte in range(65, 91) or byte in range(97, 123) or byte in range(48, 58) or byte == 95 or byte == 32:
            es_caracter_valido = True
        return es_caracter_valido

    def filtrar(lista: list[str]) -> list[str]:
        filtrado: list[str] = []
        for i in range(len(lista)):
            if len(lista[i]) >= 5:
                filtrado += [lista[i]]
        return filtrado

    with open(f"{nombre_archivo}.zip", 'rb') as file:
        bin_text = file.read()
        palabra: str = ""
        for i in range(len(bin_text)):
            if es_caracter_palabra(bin_text[i]):
                palabra += str(chr(bin_text[i]))
            else:
                lst_palabras += [palabra]
                palabra = ""
    return filtrar(lst_palabras)


# Ej 7
class Estudiante:
    def __init__(self, carac: str):
        self.text = carac

    def getLU(self) -> str:
        pos_comas: list[int] = str_f.find_all(",", self.text)
        return str_f.cortar_hasta_index(0, pos_comas[0], self.text)

    def getSub(self) -> str:
        pos_comas: list[int] = str_f.find_all(",", self.text)
        return str_f.cortar_hasta_index(pos_comas[0] + 1, pos_comas[1], self.text)

    def getDate(self) -> str:
        pos_comas: list[int] = str_f.find_all(",", self.text)
        return str_f.cortar_hasta_index(pos_comas[1] + 1, pos_comas[2], self.text)

    def getNote(self) -> float:
        pos_comas: list[int] = str_f.find_all(",", self.text)
        return float(str_f.cortar_hasta_index(pos_comas[2] + 1, len(self.text), self.text))


def calcular_promedio_por_estudiante(nombre_archivo: str, nombre_archivos_promedio: str):
    libretas: str = []
    promedio: float = 0
    cant_notas_alumno: int = 0
    lst_estudiantes: list[Estudiante] = []
    with open(f"{nombre_archivo}.csv", 'r') as file:
        lst_lines: list[str] = file.readlines()
        for i in range(len(lst_lines)):
            lst_estudiantes += [Estudiante(lst_lines[i])]
            libreta = lst_estudiantes[i].getLU()
            if not libreta in libretas:
                libretas += [lst_estudiantes[i].getLU()]

    for n in range(len(libretas)):
        for i in range(len(lst_estudiantes)):
            if lst_estudiantes[i].getLU() == libretas[n]:
                nota = lst_estudiantes[i].getNote()
                cant_notas_alumno += 1
                promedio += nota
        with open(f"{nombre_archivos_promedio}.csv", "a") as file:
            file.write(f"{libretas[n]}, {promedio/cant_notas_alumno}")
            file.write("\n")
        promedio = 0
        cant_notas_alumno = 0


# Ej 8
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    queue = Pila()
    print(queue.empty())
    for i in range(cantidad):
        num = rand.randint(desde, hasta)
        queue.put(num)
    return queue


# Ej 9
def cantidad_elementos(p: Pila) -> int:
    lst_elementos: list = []
    cant_elementos: int = 0
    while not p.empty():
        lst_elementos += [p.get()]
    cant_elementos = len(lst_elementos)
    for i in range(cant_elementos - 1, -1, -1):
        p.put(lst_elementos[i])
    return cant_elementos


# Ej 10
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


# Ej 11
def esta_bien_balanceada(s: str) -> bool:
    p = Pila()
    p_abierto: int = 0
    p_cerrado: int = 0
    c_anterior: str = ""
    bien_hecho: bool = True
    for i in range(len(s)):
        p.put(s[i])
    print(pif.getAll(p))
    while not p.empty() and bien_hecho:
        c_actual: str = p.get()
        if c_anterior in [")", "+", "*", "/"] and c_actual in ["(", "+", "-", "*", "/"]:
            bien_hecho = False
        if c_actual == ")":
            p_cerrado += 1
        if c_actual == "(":
            p_abierto += 1
        if c_actual != " ":
            c_anterior = c_actual
    if bien_hecho:
        bien_hecho = (p_abierto == p_cerrado)
    return bien_hecho


print(esta_bien_balanceada("(1+2) * 2("))
