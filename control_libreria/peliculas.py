import sys
sys.path.insert(0, './tools')
import json
from readwrite import leer, escribir


def traer_todo():
    return leer("peliculas_data")


def encontrar_codigo(cod):
    resultados = traer_todo()
    data = None
    if resultados["peliculas"].__contains__(cod):
        data = resultados["peliculas"][cod]
    return data


def subir_diccionario(datos, codigo):
    resultado = traer_todo()
    print(resultado["peliculas"])

    resultado["peliculas"][codigo] = datos
    escribir("peliculas_data", resultado)


def eliminar_del_diccionario(codigo):

    resultado = traer_todo()
    (resultado["peliculas"]).pop(codigo)
    escribir("peliculas_data", resultado)
