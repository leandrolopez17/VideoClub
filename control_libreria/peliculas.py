# PELICULAS
import sys
sys.path.append('./tools')
import json
from readwrite import leer, escribir


def traer_todo_peliculas():
    return leer("peliculas_data")


def encontrar_codigo_peliculas(cod):
    resultados = traer_todo_peliculas()
    data = None
    if resultados["peliculas"].__contains__(cod):
        data = resultados["peliculas"][cod]
    return data


def subir_diccionario(datos, codigo):
    resultado = traer_todo_peliculas()
    resultado["peliculas"][codigo] = datos
    escribir("peliculas_data", resultado)


def eliminar_del_diccionario(codigo):

    resultado = traer_todo_peliculas()
    (resultado["peliculas"]).pop(codigo)
    escribir("peliculas_data", resultado)


def subir_alquiler(data, codigo):
    resultado = traer_todo_peliculas()
    resultado["peliculas"][codigo]["alquiler"].append(data)
    escribir("peliculas_data", resultado)
