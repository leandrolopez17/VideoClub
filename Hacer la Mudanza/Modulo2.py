
print ( " ingrese subir, si desea subir un cliente " )
print ( " ingrese bajar, si desea sacar un cliente " )
print ( " ingrese modificar si desea cambiar un cliente " )

desea = input( " que quiere hacer " )

def agregar_a_clientes(diccionario):

    codigo = input( " ingrese el codigo para agregar la pelicula " )
        
    datos = clientes()

    (diccionario["clientes"])[codigo] = datos   

    return diccionario


def borrar_de_clientes(diccionario):
    
    codigo = input( " ingrese el codigo a borrar de pelicula " )

    (diccionario["clientes"]).pop(codigo)

    return diccionario


def modificar_clientes(diccionario):

    codigo = input( " ingrese el codigo para modificar la pelicula " )

    if codigo in (diccionario["clientes"]):
        
        datos = clientes()

        (diccionario["clientes"])[codigo] = datos

    else:

        print ( " el codigo no existe " )

    return diccionario


def generar_data_clientes(campos):

    datos = {}
    for campo in campos:
        data = input("Ingrese " + campo["label"] + ": ")

        if (campo["type"] == "int"):
            data = int(data)
        if (campo["type"] == "float"):
            data = float(data)   
            
        datos[campo["label"]] = data

        
    return (datos)

def clientes():

    campos = [
            {
                "label": "nombre",
                "type": "string"
            },
            {
                "label": "fecha de alta",
                "type": "int"
            },
            {
                "label": "telefono",
                "type": "string"
            },
            {
                "label": "mail",
                "type": "string"
            },
            {
                "label": "direccion",
                "type": "string"
            }
        ]

    return (generar_data_clientes(campos))

