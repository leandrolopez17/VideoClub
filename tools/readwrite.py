import json

def read(file):
    with open("./base_de_datos/"+ file +".json") as json_leer:
        resultado = json.load(json_leer)

    return resultado

def write (file, datos):
    with open("./base_de_datos/"+ file + ".json", "w") as escribir:
        json.dump(datos, escribir)

    return None