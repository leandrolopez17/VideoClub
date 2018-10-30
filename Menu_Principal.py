import sys
sys.path.append('./acciones') #importa todos los python a esa carpeta

from accion_1 import agregar_al_diccionario #importa la funcion agregar_al_diccionario desde el archivo accion 1
from accion_2 import borrar_del_diccionario #importa la funcion borrar_del_diccionario desde el archivo accion 2
from accion_3 import modificar_peliculas #importa la funcion modificar_peliculas desde el archivo accion 3
from accion_4 import agregar_a_clientes
from accion_5 import borrar_de_clientes
from accion_6 import modificar_clientes

print() # imprimo salto de linea
print('~ ~ ~ B I E N V E N I D O ~ ~ ~') # imprimo texto
print() # imprimo salto de linea

def tomar_decision(valor, operacion): # defino una funcion llamada tomar_decision que recibe dos parametros,valores,argumentos 
    operacion[valor]() # obtengo el valor del diccionario operacion que en relaidad es el diccionario decision y como es una funcion, la ejecuto poniendole los dos parentesis
    return None

# defino un diccionario llamado decision cuyas claves son strings y sus valores son funciones
decision = {
    "1": agregar_al_diccionario, # elemento del diccionario cuya clave o indice es = "1" y su valor es una funcion llamada agregar_al_diccionario
    "2": borrar_del_diccionario, # elemento del diccionario cuyo valor es = "2" y su valor es una funcion llamada borrar_del_diccionario
    "3": modificar_peliculas # elemento del diccionario cuyo valor es = "3" y su valor es una funcion llamada modificar_peliculas
    "4": agregar_a_clientes,
    "5": borrar_de_clientes,
    "6": modificar_clientes
}

seguir = True # define una variable le asigno el valor True (Boolean)

# defino un ciclo While
while seguir == True: # Asigno una condicion al While, si esta se cumple arranca el ciclo hasta que no se cumpla mas
    print('///////////////////////////////////////////////////////////////////////////') # imprime /////
    print('// (1)  Añadir un cliente                                                                   //') # imprime
    print('// (2)  Eliminar un cliente                                                                 //') # imprime
    print('// (3)  Modificar un cliente                                                                //') # imprime
    print('// (4)  Añadir una pelicula                                                                 //') # imprime
    print('// (5)  Eliminar una pelicula                                                               //') # imprime
    print('// (6)  Modificar una pelicula                                                              //') # imprime
    print('// (7)  Consultar el codigo,nombre y fecha de ingreso en el videoclub de un socio           //') # imprime
    print('// (8)  Cuál es el precio de una película determinada en el videoclub                       //') # imprime
    print('// (9)  Consultar las películas en préstamo mostrando los datos del cliente que la alquilo  //') # imprime
    print('// (10) Mostrar la lista de socios y la cantidad de películas que han alquilado             //') # imprime
    print('// (11) Calcular lo que un socio determinado debe abonar por el alquiler de las películas   //') # imprime
    print('// (12) Mostrar la lista de películas que no han sido alquiladas                            //') # imprime
    print('///////////////////////////////////////////////////////////////////////////') # imprime



    print() # imprime salto de linea

    accion = input("Ingrese numero de operacion que desea realizar: ") # pedirle al usuario que ingrese un valor que luego se almacenara en accion
    # if decision == "1":
    #     agregar_al_diccionario()
    # if decision == "2":
    #     borrar_del_diccionario()
    # if decision == "3":
    #     modificar_peliculas()
     #lo mejor es lo de abajo pero se podria poner lo de arriba hasta la opcion 12
    tomar_decision(accion, decision) # llamamos o invocamos a la funcion tomar_decision con sus dos parametros
    # los dos parametros son, accion que es lo que ingreso el usuario y decicion que es un diccionario 
    decidir = input(" ingrese si, si desea seguir ") #pedir al usuario que ingrese un valoir que luego va a ser alamcenada en decidir

    if decidir != "si": # condicional que determina de que si decidir es distinto de "si" (str) entonces entra al bloque
        seguir = False # a la variable seguir le seteo false para romper el ciclo while

print ("Vuelva pronto") # una ve terminado el ciclo while imprimimos

# () -> funcion (def)
# {} -> diccionario (dict)
# [] -> lista (list)
# 2 -> entero (int)
# 2.4 -> decimal (float)
# "" -> cadena (str)
# if -> condicion
# while -> ciclo
# for -> ciclo
# print -> imprimir 
# input -> ingreso de dato por teclado
