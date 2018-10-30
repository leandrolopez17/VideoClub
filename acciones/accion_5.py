import sys
sys.path.append('./control_libreria')

from clientes import encontrar_codigo, eliminar_del_diccionario


def borrar_de_clientes():

    codigo = input(" ingrese el codigo a borrar de pelicula ")

    funciona = False
    while funciona == False:
        cliente = encontrar_codigo(codigo)
        if cliente == None:
            codigo = input(
                " ingrese el codigo devuelta porque no hay nada para borrar")

        else:
            funciona = True

    return (eliminar_del_diccionario(codigo))
