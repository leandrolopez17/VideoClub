import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from peliculas import encontrar_codigo_peliculas, eliminar_del_diccionario
from agregar_modificar_peliculas import modificar_peli


def borrar_de_peliculas():

    codigo = input(" ingrese el codigo a borrar de pelicula ")

    codigo = modificar_peli(codigo)

    return (eliminar_del_diccionario(codigo))
