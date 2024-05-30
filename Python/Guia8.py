import auxiliares.str_functions as str_f
import auxiliares.list_functions as lst_f


# Ej 1.1
def contar_lineas(nombre_archivo: str) -> int:
    cont: int = 0
    with open(f"{nombre_archivo}.txt", 'r') as file:
        lst_text: list = file.readlines()
        for i in range(len(lst_text)):
            if str_f.terminaEn("\n", lst_text[i]):
                cont += 1
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
# Me quedo medio raro, no se si esta bie hecho.
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
