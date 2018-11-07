import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from clientes import encontrar_codigo_clientes, eliminar_del_diccionario
from agregar_modificar_clientes import modificar_client
from buscar_cliente_debe import buscar


def borrar_de_clientes():

    codigo = input(" ingrese el codigo a borrar de cliente ")

    if buscar(codigo) != True:

        codigo = modificar_client(codigo)

        return (eliminar_del_diccionario(codigo))

    else:

        return (print(" primero debe saldar cuentas para eliminar al cliente "))
