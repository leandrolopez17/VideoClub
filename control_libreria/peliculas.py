import sys
sys.path.insert(0, './tools')
import json
from readwrite import read, write

def getAll ():
    return read("peliculas_data")

def findByCodigo(cod):
    resultados = getAll()
    data = None
    if resultados["peliculas"].__contains__(cod):
        data = resultados["peliculas"][cod]
    return data
        
def add_dictionary(datos,codigo):
    resultado = getAll()
    print(resultado["peliculas"])
        
    resultado["peliculas"][codigo] = datos
    write("peliculas_data", resultado)  



