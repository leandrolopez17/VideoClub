import sys
sys.path.append('./control_libreria')

from peliculas import add_dictionary, findByCodigo
##
# with open("./base_de_datos/peliculas_data.json") as json_leer:
##info = json.load(json_leer)


def agregar_al_diccionario():

    codigo = input(" Ingrese el codigo para agregar una pelicula ")

    funciona = False
    while funciona == False:
        pelicula = findByCodigo(codigo)
        if pelicula != None:
            codigo = input(" ingrese el codigo nuevamente porque ya existe")

        else:
            funciona = True

    datos = peliculas()

    return add_dictionary(datos, codigo)


def generar_data(campos):

    datos = {}
    for campo in campos:
        data = input("Ingrese " + campo["label"] + ": ")

        if (campo["type"] == "int"):
            data = int(data)
        if (campo["type"] == "float"):
            data = float(data)

        datos[campo["label"]] = data

    return datos


def peliculas():

    campos = [
        {
            "label": "titulo",
            "type": "string"
        },
        {
            "label": "genero",
            "type": "string"
        },
        {
            "label": "año_creacion",
            "type": "int"
        },
        {
            "label": "pais_origen",
            "type": "string"
        },
        {
            "label": "precio_alquiler",
            "type": "float"
        }
    ]

    return generar_data(campos)
