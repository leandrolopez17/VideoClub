def generar_data(campos):

    datos = {}
    for campo in campos:
        data = input("Ingrese " + campo["label"] + ": ")

        if (campo["type"] == "int"):
            data = int(data)
        if (campo["type"] == "float"):
            data = float(data)

        if (campo.__contains__("key")):
            key = campo["key"]
        else:
            key = campo["label"]

        datos[key] = data

    datos["alquiler"] = []

    return datos
