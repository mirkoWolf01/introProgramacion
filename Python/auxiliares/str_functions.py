# Devuelve la primera instancia que encuentra de elem en text, en terminos de index de text
# Requiere len (text) >= len (elem)
def find(elem: str, text: str) -> int:
    val: int = -1
    for i in range(len(text)):
        if elem[0] == text[i]:
            palabra: str = text[i]
            if len(text) >= i + len(elem):
                for c in range(1, len(elem)):
                    palabra += text[i+c]
            if elem == palabra and val == -1:
                val = i
    return val


def find_all(elem: str, text: str) -> list[int]:
    val: list[int] = []
    for i in range(len(text)):
        if elem[0] == text[i]:
            palabra: str = text[i]
            if len(text) >= i + len(elem):
                for c in range(1, len(elem)):
                    palabra += text[i+c]
            if elem == palabra:
                val += [i]
    return val


def pertenece_str(elem: str, text: str) -> bool:
    res: bool = True
    if find(elem, text) == -1:
        res = False
    return res


def terminaEn(elem: str, text: str) -> bool:
    sec_final: str = ""
    for i in range(len(elem)):
        index: int = len(text) - len(elem) + i
        sec_final += text[index]
    return elem == sec_final


# Requiere que exista hasta en texto
def cortar_hasta(hasta: str, text: str) -> str:
    destino: int = find(hasta, text)
    res: str = ""
    for i in range(destino):
        res += text[i]
    return res


def cortar_hasta_index(ini: int, dest: int, text: str) -> str:
    res: str = ""
    for i in range(ini, dest):
        res += text[i]
    return res
