import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from peliculas import subir_diccionario, encontrar_codigo
from generar_datos import generar_data


def modificar_peliculas():

    codigo = input(" Ingrese el codigo para modificar una pelicula ")

    funciona = False
    while funciona == False:
        pelicula = encontrar_codigo(codigo)
        if pelicula == None:
            codigo = input(" ingrese el codigo nuevamente porque no existe")

        else:
            funciona = True

    datos = peliculas()

    return subir_diccionario(datos, codigo)


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
            "label": "anio_creacion",
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
