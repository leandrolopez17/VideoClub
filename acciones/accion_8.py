import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from peliculas import encontrar_codigo_peliculas
from agregar_modificar_peliculas import modificar_peli


def precio_pelicula():

    codigo = input(" ingrese el codigo para buscar el precio de una pelicula ")

    modificar_peli(codigo)

    datos = encontrar_codigo_peliculas(codigo)

    print(" El precio es de: " + str(datos["precio_alquiler"]))
