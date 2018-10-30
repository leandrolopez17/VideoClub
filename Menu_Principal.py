import sys
sys.path.append('./acciones')

from accion_1 import agregar_a_peliculas
from accion_2 import borrar_de_peliculas
from accion_3 import modificar_peliculas
from accion_4 import agregar_a_clientes
from accion_5 import borrar_de_clientes
from accion_6 import modificar_clientes
from accion_7 import consultar_datos_socio
from accion_8 import precio_pelicula
from accion_9 import alquiler_pelicula

print()
print('¿?¿?¿?¿? LE DAMOS LA BIENVENIDA A NUESTRO PORTAL VIDEOCLUB ¿?¿?¿?¿?')
print()


def tomar_decision(value, operation):
    operation[value]()
    return None


decision = {
    "1": agregar_a_peliculas,
    "2": borrar_de_peliculas,
    "3": modificar_peliculas,
    "4": agregar_a_clientes,
    "5": borrar_de_clientes,
    "6": modificar_clientes,
    "7": consultar_datos_socio,
    "8": precio_pelicula,
    "9": alquiler_pelicula

}

seguir = True

while seguir == True:
    print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')
    print('// (1)  Añadir una pelicula                                                                 //')
    print('// (2)  Eliminar una pelicula                                                               //')
    print('// (3)  Modificar una pelicula                                                              //')
    print('// (4)  Añadir un cliente                                                                   //')
    print('// (5)  Eliminar un cliente                                                                 //')
    print('// (6)  Modificar un cliente                                                                //')
    print('// (7)  Consultar el codigo,nombre y fecha de ingreso en el videoclub de un socio           //')
    print('// (8)  Cuál es el precio de una película determinada en el videoclub                       //')
    print('// (9)  Añadir pelicula que se alquilo                                                      //')
    print('// (10) Consultar las películas en préstamo mostrando los datos del cliente que la alquilo  //')
    print('// (11) Mostrar la lista de socios y la cantidad de películas que han alquilado             //')
    print('// (12) Calcular lo que un socio determinado debe abonar por el alquiler de las películas   //')
    print('// (13) Mostrar la lista de películas que no han sido alquiladas                            //')
    print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')

    print()

    accion = input("Ingrese numero de operacion que desea realizar: ")

    tomar_decision(accion, decision)

    decidir = input(" ingrese si, si desea seguir ")

    if decidir != "si":
        seguir = False
        print(" Hasta luego, Nos vemos pronto! ")
