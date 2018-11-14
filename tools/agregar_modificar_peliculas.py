# AGREGAR O MODFICAR PELICULA
import sys
sys.path.append('./control_libreria')

from peliculas import encontrar_codigo_peliculas


def agregar_peli(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo_peliculas(codigo)
        if buscar != None:
            codigo = input(" ingrese el codigo nuevamente porque ya existe")

        else:
            funciona = True

    return codigo


def modificar_peli(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo_peliculas(codigo)
        if buscar == None:
            codigo = input(
                " ingrese el codigo nuevamente porque no se encuentra ")

        else:
            funciona = True

    return codigo
