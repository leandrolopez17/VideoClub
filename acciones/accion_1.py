import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')


from peliculas import subir_diccionario, encontrar_codigo
from generar_datos import generar_data


def agregar_a_peliculas():# agrego la funcion de agregar_a_peliculas
    codigo = input(" Ingrese el codigo para agregar una pelicula ") # pido al usuario que ingrese el codigo de la pelicula

    funciona = False # le doy un valor a funciona
    while funciona == False: # uso el while osea voy a hacer un ciclo, y ya tomo en cuenta que funciona es = a false para seguir con el ciclo
        pelicula = encontrar_codigo(codigo) 
        if pelicula != None: # da la otra condicion que si es distinto a none 
            codigo = input(" ingrese el codigo nuevamente porque ya existe") # le pedimos al usuario que ingrese denuevo el codigo ya que no existe el que introdujo

        else: # es conndicio pero con la reciproca, osea que si no pasa esto pasa lo otro significa el else
            funciona = True # hacemos que funciona es = a true entonces sigue el ciclo

    datos = peliculas() # le damos valor a datos como peliculas()

    return subir_diccionario(datos, codigo)


def peliculas(): # agrego una funcion

    campos = [ # campo es una losta donde adentro hay diccionarios con sus indices y sus valores
        {
            "label": "titulo",
            "type": "string"
        },
        {
            "label": "genero",
            "type": "string"
        },
        {
            "label": "año_creacion",
            "type": "int"
        },
        {
            "label": "pais_origen",
            "type": "string"
        },
        {
            "label": "precio_alquiler",
            "type": "float"
        }
    ]

    return generar_data(campos)

# () -> funcion (def)
# {} -> diccionario (dict)
# [] -> lista (list)
# 2 -> entero (int)
# 2.4 -> decimal (float)
# "" -> cadena (str)
# if -> condicion
# while -> ciclo
# for -> ciclo
# print -> imprimir 
# input -> ingreso de dato por teclado
