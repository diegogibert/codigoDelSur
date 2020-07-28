#! /usr/bin/env python3
''' un programa para repartir 5 manos de poker y evaluar sus juegos '''

import random
from collections import namedtuple, Counter

palos = 'DIAMANTE', 'CORAZON', 'PICAS', 'TREBOL'
valores = '8','9','10', 'J', 'Q', 'K', 'A'
valorNumericoAsociadoAValores = { v: valores.index(v) for v in valores } #se usa en las escaleras


Carta = namedtuple('Carta', 'valor palo')
mazo = [Carta(valor, palo) for valor in valores for palo in palos]

random.shuffle(mazo)      # Entreverar mazo

manosJugadores = [[mazo.pop() for _ in range(5)] for _ in range(5)]

def es_color(mano):
    if len({palo for _, palo in mano}) == 1:
        return True

def es_poker(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    if cantidad == 4:
        return True
    return False

def es_par(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    otrosValores = {m.valor for m in mano if m.valor != valor}
    if cantidad == 2 and len(otrosValores) == 3:
        return True
    return False

def doble_par(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    otrosValores = {m.valor for m in mano if m.valor != valor}
    if cantidad == 2 and len(otrosValores) == 2:
        return True
    return False

def es_pierna(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    otrosValores = {m.valor for m in mano if m.valor != valor}
    if cantidad == 3 and len(otrosValores) == 2:
        return True
    return False

def es_full(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    otrosValores = {m.valor for m in mano if m.valor != valor}
    if cantidad == 3 and len(otrosValores) == 1:
        return True
    return False

def es_escalera_simple(mano):
    valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
    if cantidad != 1:
        return False
    valoresNumricosCartasEnMano = [valorNumericoAsociadoAValores[c.valor] for c in mano]
    valNum_carta_baja, *_, valNum_carta_alta = sorted(valoresNumricosCartasEnMano)
    return valNum_carta_alta - valNum_carta_baja == 4

def es_escalera_real(mano):
    valoresNumricosCartasEnMano = [valorNumericoAsociadoAValores[c.valor] for c in mano]
    return es_escalera_simple(mano) and es_color(mano) and max(valoresNumricosCartasEnMano) == valorNumericoAsociadoAValores['A']

def es_escalera_color(mano):
    return es_escalera_simple(mano) and es_color(mano)


def main():
    for mano in manosJugadores:
        cart = [(cartas.valor, cartas.palo) for cartas in mano]
        
        if es_escalera_real(mano):
            print(f"{cart} es escalera real")
            continue
        elif es_escalera_color(mano):
            palo = mano[0][1]
            print(f"{cart} es escalera color en palo {palo}")
            continue
        if es_poker(mano):
            valor, cantidad = Counter([c.valor for c in mano]).most_common(1)[0]
            print(f"{cart} poker con numero {valor}")
            continue
        if es_full(mano):
            print(f"{cart} es full")
            continue
        if es_color(mano):
            palo = mano[0][1]
            print(f"{cart} es color en {palo}")
            continue
        if es_escalera_simple(mano):
            print(f"{cart} escalera simple")
            continue
        if es_pierna(mano):
            print(f"{cart} es pierna")
            continue
        if doble_par(mano):
            print(f"{cart} es doble par")
            continue
        if es_par(mano):
            print(f"{cart} es par")
        else:
            print(f"{cart} no se tiene ningun juego en especial")
        
            
        
        

if __name__=='__main__':
        main()