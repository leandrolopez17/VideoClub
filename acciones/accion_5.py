import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from clientes import encontrar_codigo, eliminar_del_diccionario
from agregar_modificar_clientes import modificar_client


def borrar_de_clientes():

    codigo = input(" ingrese el codigo a borrar de pelicula ")

    modificar_client(codigo)

    return (eliminar_del_diccionario(codigo))
