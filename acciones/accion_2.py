import sys
sys.path.append('./control_libreria')

from peliculas import encontrar_codigo, eliminar_del_diccionario


def borrar_del_diccionario():

    codigo = input(" ingrese el codigo a borrar de pelicula ")

    funciona = False
    while funciona == False:
        pelicula = encontrar_codigo(codigo)
        if pelicula == None:
            codigo = input(
                " ingrese el codigo devuelta porque no hay nada para borrar")

        else:
            funciona = True

    return (eliminar_del_diccionario(codigo))
