import Data
diccionario = Data.diccionario

import json

que_queres = input(
    " si desea clientes ponga clientes, si desea peliculas, ponga peliculas ")

if que_queres == "peliculas":

    import Modulo1

    desea = Modulo1.desea

    if desea == "subir":

        Modulo1.agregar_al_diccionario(diccionario)

        with open('Data.py', 'w') as file:

            file.escribir(json.dumps(diccionario))

    elif desea == "bajar":

        Modulo1.borrar_del_diccionario(diccionario)

    elif desea == "modificar":

        Modulo1.modificar_peliculas(diccionario)

    for n in diccionario["peliculas"]:

        print(n)

        for r in (diccionario["peliculas"])[n]:

            print(r + " :", ((diccionario["peliculas"])[n])[r])
            print("")


if que_queres == "clientes":

    import Modulo2

    desea = Modulo2.desea

    if desea == "subir":

        Modulo2.agregar_a_clientes(diccionario)

    elif desea == "bajar":

        Modulo2.borrar_de_clientes(diccionario)

    elif desea == "modificar":

        Modulo2.modificar_clientes(diccionario)

    for n in diccionario["clientes"]:

        print(n)

        for r in (diccionario["clientes"])[n]:
            print(r + " :", ((diccionario["clientes"])[n])[r])
            print("")
