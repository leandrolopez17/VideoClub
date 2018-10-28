def generar_data(campos, key):

    datos = {}
    for campo in campos:
        data = input("Ingrese " + campo["label"] + ": ")

        if (campo["type"] == "int"):
            data = int(data)
        if (campo["type"] == "float"):
            data = float(data)
            
        if campo["label"] == "codigo":

            codigo = data
        
            
        datos[campo["label"]] = data
