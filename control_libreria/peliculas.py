import sys
sys.path.append('./tools')
import json
from readwrite import leer, escribir


def traer_todo():
    return leer("peliculas_data")


def encontrar_codigo_peliculas(cod):
    resultados = traer_todo()
    data = None
    if resultados["peliculas"].__contains__(cod):
        data = resultados["peliculas"][cod]
    return data


def subir_diccionario(datos, codigo):
    resultado = traer_todo()
    resultado["peliculas"][codigo] = datos
    escribir("peliculas_data", resultado)


def eliminar_del_diccionario(codigo):

    resultado = traer_todo()
    (resultado["peliculas"]).pop(codigo)
    escribir("peliculas_data", resultado)


def subir_alquiler(data, codigo):
    resultado = traer_todo()
    resultado["peliculas"][codigo]["alquiler"].append(data)
    escribir("peliculas_data", resultado)
