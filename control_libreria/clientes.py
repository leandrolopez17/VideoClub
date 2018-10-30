import sys
sys.path.insert(0, './tools')
import json
from readwrite import leer, escribir


def traer_todo():
    return leer("clientes_data")


def encontrar_codigo(cod):
    resultados = traer_todo()
    data = None
    if resultados["clientes"].__contains__(cod):
        data = resultados["clientes"][cod]
    return data


def subir_diccionario(datos, codigo):
    resultado = traer_todo()
    resultado["clientes"][codigo] = datos
    escribir("clientes_data", resultado)


def eliminar_del_diccionario(codigo):

    resultado = traer_todo()
    (resultado["clientes"]).pop(codigo)
    escribir("clientes_data", resultado)