import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')


from clientes import subir_diccionario, encontrar_codigo
from generar_datos import generar_data
from agregar_modificar_clientes import agregar_client


def agregar_a_clientes():

    codigo = input(" Ingrese el codigo para agregar un cliente ")

    agregar_client(codigo)

    datos = clientes()

    return subir_diccionario(datos, codigo)


def clientes():

    campos = [
        {
            "label": "nombre",
            "type": "string"
        },
        {
            "label": "fecha de alta (aa/mm/dd)",
            "type": "string",
            "key": "fecha"
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

    return (generar_data(campos))
