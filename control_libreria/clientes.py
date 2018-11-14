# CLIENTES
import sys
sys.path.append('./tools')
import json
from readwrite import leer, escribir


def traer_todo_clientes():
    return leer("clientes_data")


def encontrar_codigo_clientes(cod):
    resultados = traer_todo_clientes()
    data = None
    if resultados["clientes"].__contains__(cod):
        data = resultados["clientes"][cod]
    return data


def subir_diccionario(datos, codigo):
    resultado = traer_todo_clientes()
    resultado["clientes"][codigo] = datos
    escribir("clientes_data", resultado)


def eliminar_del_diccionario(codigo):

    resultado = traer_todo_clientes()
    (resultado["clientes"]).pop(codigo)
    escribir("clientes_data", resultado)
