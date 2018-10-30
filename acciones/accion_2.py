import sys
sys.path.append('./control_libreria')

from peliculas import encontrar_codigo, eliminar_del_diccionario


def borrar_del_diccionario(): # define una funcion borrar_del_diccionario

    codigo = input(" ingrese el codigo a borrar de pelicula ") # pide al usuario que ingrese el codigo de la pelicula para borrar

    funciona = False # le da valor a fucnion false
    while funciona == False: # hace un ciclo con while afirmandpo que funciona es = false para que empiece el ciclo directo
        pelicula = encontrar_codigo(codigo) 
        if pelicula == None:
            codigo = input(" ingrese el codigo devuelta porque no hay nada para borrar") # pide al usuario que ingrese el codigo de la pelicula porqe no hay nada que borrar

        else:
            funciona = True

    return (eliminar_del_diccionario(codigo))
