# ACCION 1

import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')


from peliculas import subir_diccionario, encontrar_codigo_peliculas
from generar_datos import generar_data
from agregar_modificar_peliculas import agregar_peli


def agregar_a_peliculas():

    codigo = input(" Ingrese el codigo para agregar una pelicula ")

    codigo = agregar_peli(codigo)

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
