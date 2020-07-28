#! /usr/bin/env python3
''' un programa para conseguir la informacion relacionada al covid 19 de uno o varios paises a la vez 
(hay q descargar el paquete Covid, se hace con el comando "pip install Covid")  '''

from covid import Covid
covid = Covid()

paisP = input('Que pais?: ')


def empiezaCon(listita, letra):
    listita = list(listita.values())
    pp = listita[1].lower()
    if pp.startswith(letra):
        getInfo(listita[1])


def getInfo(pais):
    paisInfo = covid.get_status_by_country_name(pais)
    data = {key : paisInfo[key] for key in paisInfo.keys() and { 'confirmed','active','deaths','recovered'}}  #and { 'confirmed','active','deaths','recovered'}
    print(pais)
    print(data)
    

def main():
    for p in covid.list_countries():
        empiezaCon(p,paisP)

if __name__== "__main__":
    main() 