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
