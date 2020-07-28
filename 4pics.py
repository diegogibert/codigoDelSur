#!/usr/bin/env python3
''' un programa que recibe una cadena de letras, un largo de palabra esperado y opcinalmente un inicio de palabra
y busca en un archivo (generalmente un diccionario) palabras que contengan las letras pasadas, sean del largo deseado
y opcinalmente comiencen con los caracteres indicados

el archivo donde se buscan las palabras se indica desde el codigo, podria configurarse rapidamente para
que se pase como argumento al programa'''

import argparse
from collections import Counter

def parsear():  # todo lo de parser nos lo da gerardo en clase
    DICT = open("p.txt", 'r')
    parser = argparse.ArgumentParser(description= '4pics - elige palabras para el juego "4pics 1word"')
    parser.add_argument('-s', '--string', help ='lista de letras',required=True, type=str.upper)
    parser.add_argument('-l', '--length', help ='largo palabra',required=True, type=int)
    parser.add_argument('-i', '--initial', help ='letra inicial de la palabra',default=None, type=str.upper)
    parser.add_argument('-d', '--dicctionary', help =f'archivo diccionario ({DICT})',default=DICT, type=argparse.FileType('r'))
    args = parser.parse_args()  #guardo los argumentos en args.length args.string etc
    return args

def filtrar(palabra, letrasInputDict):
    palabraDict = Counter(palabra)
    for j in palabraDict:
        if letrasInputDict[j] < palabraDict[j]:  #los valores (osea la ocurrencia de las letras) en el input tienen q ser mayores o iguales a las del diccionario siemp$
            return False
    return True

def sinTilde(palabra):
    vocales = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for i, j in vocales:
        palabra = palabra.replace(i.upper(), j.upper())
    return palabra

def encontraPalabras(args):
    letrasInput = args.string.upper()
    letrasInputDict = Counter(letrasInput)      # hace un diccionario con key letra, valor ocurrencia
    coincidencias = []
    for palabra in args.dicctionary:
        palabra = palabra.strip().upper()      #Saco el del final y hago todo mayuscula
        palabra = sinTilde(palabra)             #Saca los tildes de la palabra
        if len(palabra) == args.length:
            if args.initial is None or palabra.startswith(args.initial):
                if filtrar(palabra, letrasInputDict):
                    coincidencias.append(palabra)
    return coincidencias

def main():
    args = parsear()
    coincidencias = encontraPalabras(args)
    print (coincidencias)

if __name__=='__main__':
        main()
