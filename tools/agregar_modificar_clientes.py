import sys
sys.path.append('./control_libreria')

from clientes import encontrar_codigo_clientes


def agregar_client(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo_clientes(codigo)
        if buscar != None:
            codigo = input(" ingrese el codigo nuevamente porque ya existe")

        else:
            funciona = True

    return codigo


def modificar_client(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo_clientes(codigo)
        if buscar == None:
            codigo = input(
                " ingrese el codigo nuevamente porque no se encuentra ")

        else:
            funciona = True

    return codigo
