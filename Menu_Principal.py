import sys
sys.path.append('./acciones')

from accion_1 import agregar_al_diccionario
from accion_2 import borrar_del_diccionario
from accion_3 import modificar_peliculas

print()
print('~ ~ ~ B I E N V E N I D O ~ ~ ~')
print()


def tomar_decision(value, operation):
    operation[value]()
    return None


decision = {
    "1": agregar_al_diccionario,
    "2": borrar_del_diccionario,
    "3": modificar_peliculas

}

seguir = True

while seguir == True:
    print('///////////////////////////////////////////////////////////////////////////')
    print('// (1)  Añadir un cliente                                                                   //')
    print('// (2)  Eliminar un cliente                                                                 //')
    print('// (3)  Modificar un cliente                                                                //')
    print('// (4)  Añadir una pelicula                                                                 //')
    print('// (5)  Eliminar una pelicula                                                               //')
    print('// (6)  Modificar una pelicula                                                              //')
    print('// (7)  Consultar el codigo,nombre y fecha de ingreso en el videoclub de un socio           //')
    print('// (8)  Cuál es el precio de una película determinada en el videoclub                       //')
    print('// (9)  Consultar las películas en préstamo mostrando los datos del cliente que la alquilo  //')
    print('// (10) Mostrar la lista de socios y la cantidad de películas que han alquilado             //')
    print('// (11) Calcular lo que un socio determinado debe abonar por el alquiler de las películas   //')
    print('// (12) Mostrar la lista de películas que no han sido alquiladas                            //')
    print('///////////////////////////////////////////////////////////////////////////')

    print()

    accion = input("Ingrese numero de operacion que desea realizar: ")

    tomar_decision(accion, decision)

    decidir = input(" ingrese si, si desea seguir ")

    if decidir != "si":
        seguir = False
        print(" Hasta luego, Nos vemos pronto! ")
