from queue import Queue as Cola


# Ej 1
def reordenar_cola_priorizando_vips(fila_clientes: Cola[tuple[str, str]]) -> Cola[str]:
    in_clientes: list[tuple[str, str]] = []
    clientes_comunes: list[tuple[str, str]] = []
    clientes_vip: list[tuple[str, str]] = []
    res: Cola[str] = Cola()
    while not fila_clientes.empty():
        cliente: tuple[str, str] = fila_clientes.get()
        in_clientes += [cliente]
        if cliente[1] == "comun":
            clientes_comunes += [cliente]
        else:
            clientes_vip += [cliente]
    for i in range(len(in_clientes)):
        fila_clientes.put(in_clientes[i])
    for i in range(len(clientes_vip)):
        res.put(clientes_vip[i][0])
    for i in range(len(clientes_comunes)):
        res.put(clientes_comunes[i][0])
    return res


# Ej 2
def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    jugadores: list[tuple[str, str]] = list(estrategias.items())
    res: dict[str, str] = {}
    for i in range(len(jugadores)):
        jugador: tuple[str, str] = jugadores[i]
        estrategia_jugador: str = jugador[1]
        for n in range(len(jugadores)):
            if jugador[0] != jugadores[n][0]:
                estrategia_contrincante: str = jugadores[n][1]
                if estrategia_jugador == "me desvio siempre":
                    if estrategia_contrincante == "me desvio siempre":
                        sumar_valor(jugador[0], -10, res)
                    if estrategia_contrincante == "me la banco y no me desvio":
                        sumar_valor(jugador[0], -15, res)
                else:
                    if estrategia_contrincante == "me desvio siempre":
                        sumar_valor(jugador[0], 10, res)
                    if estrategia_contrincante == "me la banco y no me desvio":
                        sumar_valor(jugador[0], -5, res)
    return res


def sumar_valor(clave: str, n: int, dict: dict[str, int]):
    if clave in dict.keys():
        dict[clave] += n
    else:
        dict[clave] = n


# Ej 3
def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    res: int = 0
    gano_ana: bool = False
    gano_beto: bool = False

    for i in range(len(tablero)):
        fila: list[str] = tablero[i]
        for c in range(len(fila)):
            seq_ganadora: str = fila[c]
            if seq_ganadora == "X":
                for n in range(1, 3):
                    if len(tablero) > i + n:
                        seq_ganadora += tablero[i+n][c]
                if seq_ganadora == "XXX":
                    gano_ana = True
            elif seq_ganadora == "O":
                for n in range(1, 3):
                    if len(tablero) > i + n:
                        seq_ganadora += tablero[i+n][c]
                if seq_ganadora == "OOO":
                    gano_beto = True

    if gano_ana and not gano_beto:
        res = 1
    if not gano_ana and gano_beto:
        res = 2
    if gano_ana and gano_beto:
        res = 3
    return res


# Ej 4
def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res: int = 0
    for i in range(len(texto)):
        palabra: str = ""
        for n in range(i, len(texto)):
            palabra += texto[n]
        if palabra == reverse(palabra) and palabra != "":
            res += 1
    return res


def reverse(palabra: str) -> str:
    res: str = ""
    for i in range(len(palabra)-1, -1, -1):
        res += palabra[i]
    return res
