import auxiliares.str_functions as str_f
import auxiliares.list_functions as lst_f
import auxiliares.pila_functions as pif
from queue import LifoQueue as Pila
from queue import Queue as Cola
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


# Ej 12
# No funciona para numeros de mas de dos digitos, me da paja hacer para que filtre numeros de mas de dos digitos :)
def evaluar_expresion(s: str) -> float:
    operadores = Pila()
    operandos = Pila()
    res: float = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] in ["+", "-", "*", "/"]:
            operandos.put(s[i])
        elif s[i] != " ":
            operadores.put(s[i])
    while cantidad_elementos(operadores) > 1:
        for i in range(cantidad_elementos(operandos)):
            primer_num: float = float(operadores.get())
            seg_num: float = float(operadores.get())
            operando = operandos.get()
            if operando == "+":
                res = primer_num + seg_num
            elif operando == "-":
                res = primer_num - seg_num
            elif operando == "*":
                res = primer_num * seg_num
            elif operando == "/":
                res = primer_num / seg_num
            operadores.put(res)
    return operadores.get()


# Ej 13
def formar_cola_azar():
    p: Pila[int] = generar_nros_al_azar(cantidad=5, desde=2, hasta=10)
    c = Cola()
    for i in range(cantidad_elementos(p)):
        c.put(p.get())
    return c


# Ej 14
def cant_elem_in_cola(c: Cola) -> int:
    lst_elem: list = []
    res: int = 0
    while not c.empty():
        lst_elem += [c.get()]
    res = len(lst_elem)
    for i in range(res):
        c.put(lst_elem[i])
    return res


# Ej 15
def bmax_col(c: Cola[int]) -> int:
    max_num: int = c.get()
    c.put(max_num)
    for i in range(cant_elem_in_cola(c) - 1):
        act_num: int = c.get()
        if act_num > max_num:
            max_num = act_num
        c.put(act_num)
    return max_num

# Ej 16


def armar_sec_bingo() -> Cola[int]:
    res = Cola()
    unused: list[int] = list(range(100))
    for i in range(100):
        elem: int = rand.randint(0, len(unused)-1)
        num: int = unused[elem]
        res.put(num)
        unused.remove(num)
    return res


def jugar_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    faltan_para_bingo: int = carton.copy()
    jugadas: int = -1
    for i in range(cant_elem_in_cola(bolillero)):
        actual_num: int = bolillero.get()
        if actual_num in faltan_para_bingo:
            faltan_para_bingo.remove(actual_num)
        if faltan_para_bingo == [] and jugadas == -1:
            jugadas = i
        bolillero.put(actual_num)
    return jugadas


# Ej 17
def n_pacietes_urgentes(c: Cola[tuple[int, str, str]]) -> int:
    alta_prioridad: list[int] = [1, 2, 3]
    res: int = 0
    for i in range(cant_elem_in_cola(c)):
        datos_paciente: tuple[int, str, str] = c.get()
        c.put(datos_paciente)
        if datos_paciente[0] in alta_prioridad:
            res += 1
    return res


# Ej 18
def atencion_a_clietes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_extrema_prioridad = Cola()
    cola_prioridad = Cola()
    cola_preferencial = Cola()
    cola_normal = Cola()
    orden: list[Cola] = [cola_extrema_prioridad,
                         cola_prioridad, cola_preferencial, cola_normal]

    for i in range(cant_elem_in_cola(c)):
        cliente: tuple[str, int, bool, bool] = c.get()
        c.put(cliente)
        if cliente[3] and cliente[2]:
            cola_extrema_prioridad.put(cliente)
        elif cliente[3]:
            cola_prioridad.put(cliente)
        elif cliente[2]:
            cola_preferencial.put(cliente)
        else:
            cola_normal.put(cliente)

    res: Cola[tuple[str, int, bool, bool]] = Cola()
    for i in range(len(orden)):
        cola_actual = orden[i]
        for n in range(cant_elem_in_cola(cola_actual)):
            res.put(cola_actual.get())
    return res


# Ej 19
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    res: dict = {}

    def add_to_res(palabra: str):
        largo_palabra: int = len(palabra)
        if largo_palabra > 0:
            if largo_palabra in res.keys():
                res[largo_palabra] += 1
            else:
                res.update({largo_palabra: 1})

    with open(f"{nombre_archivo}.txt", "r") as file:
        palabras: str = file.read()
        palabra: str = ""
        for i in range(len(palabras)):
            if palabras[i] != " " and palabras[i] != "\n":
                palabra += palabras[i]
            else:
                add_to_res(palabra)
                palabra = ""
        add_to_res(palabra)
    return res


# Ej 20
def calcular_promedio_por_estudiante_dict(nombre_archivo: str) -> dict[str, float]:
    libretas: str = []
    lst_estudiantes: list[Estudiante] = []
    res: dict[str, float] = {}
    with open(f"{nombre_archivo}.csv", 'r') as file:
        lst_lines: list[str] = file.readlines()
        for i in range(len(lst_lines)):
            lst_estudiantes += [Estudiante(lst_lines[i])]
            libreta = lst_estudiantes[i].getLU()
            if not libreta in libretas:
                libretas += [lst_estudiantes[i].getLU()]

    promedio: float = 0
    cant_notas_alumno: int = 0
    for n in range(len(libretas)):
        for i in range(len(lst_estudiantes)):
            lib: str = lst_estudiantes[i].getLU()
            if lib == libretas[n]:
                nota = lst_estudiantes[i].getNote()
                cant_notas_alumno += 1
                promedio += nota
                promedio = promedio / cant_notas_alumno
                res.update({lib: promedio})
        promedio = 0
        cant_notas_alumno = 0
    return res


# Ej 21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    res: dict[int] = {}

    # Añade palabra a res si no existe en res, sino le suma 1 al valor de res[palabra]
    def add_to_dict(palabra: str):
        if len(palabra) > 0:
            if palabra in res.keys():
                res[palabra] += 1
            else:
                res.update({palabra: 1})

    # Lee el archivo y separa palabras de no palabras y las guarda en res.
    with open(f"{nombre_archivo}.txt", "r") as file:
        text: str = file.read()
        palabra: str = ""
        for i in range(len(text)):
            if ord(text[i]) in range(97, 123) or ord(text[i]) in range(65, 91):
                palabra += text[i]
            else:
                add_to_dict(palabra)
                palabra = ""
        add_to_dict(palabra)

    # De todas las palabras identifico cual es la mas usada
    list_keys: list[str] = list(res.keys())
    mas_usada: str = " "
    for i in range(len(res.keys())):
        if mas_usada == " ":
            mas_usada = list_keys[i]
        elif res[list_keys[i]] > res[mas_usada]:
            mas_usada = list_keys[i]
    return mas_usada


# Ej 22
def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        p = Pila()
        p.put(sitio)
        historiales.update({usuario: p})


def navegar_atras(historiales: dict[str, Pila[str]], usuario: str):
    elem_actual: str = historiales[usuario].get()
    elem_anterior: str = historiales[usuario].get()
    p = Pila()
    historiales[usuario].put(elem_anterior)
    historiales[usuario].put(elem_actual)
    historiales[usuario].put(elem_anterior)


# Ej 23
def agregar_producto(inventario: dict[str, dict[str, int]], nombre: str, precio: int, cantidad: int):
    cualidades: dict[str, int] = {}
    cualidades.update({"precio": precio})
    cualidades.update({"cantidad": cantidad})
    inventario.update({nombre: cualidades})


def actualizar_stock(inventario: dict[str, dict[str, int]], nombre: str, cantidad: int):
    cualidades: dict[str, int] = inventario[nombre]
    cualidades["cantidad"] = cantidad


def actualizar_precio(inventario: dict[str, dict[str, int]], nombre: str, precio: int):
    cualidades: dict[str, int] = inventario[nombre]
    cualidades["precio"] = precio


def calcular_valor_inventario(inventario: dict[str, dict[str, int]]) -> float:
    keys: list[str] = list(inventario.keys())
    valor_total: float = 0
    for i in range(len(keys)):
        d: dict[str, int] = inventario[keys[i]]
        valor_total += d["cantidad"] * d["precio"]
    return valor_total


inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)

# Hicieron mal la guia JASJSAJSA da 1100



