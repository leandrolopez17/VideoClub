import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from peliculas import encontrar_codigo_peliculas
from clientes import traer_todo_clientes
from agregar_modificar_peliculas import modificar_peli


def consultar_pelicula():

    peli = input("ingrese el codigo de la pelicula que quiere ver clientes ")

    peli = modificar_peli(peli)

    data = encontrar_codigo_peliculas(peli)

    consulta = []

    for n in (data["alquiler"]):

        for s in n:

            if s == "codigo_cliente" and n[s] not in consulta:
                consulta.append(n[s])

    todo = traer_todo_clientes()

    cant = 0

    for r in consulta:
        for s in (todo["clientes"]):
            if s == r:
                cant += 1
                print(" el cliente numero " + str(cant) +
                      " que ha alquilado " + peli)
                for l in (todo["clientes"][s]):
                    print(l + ": " + (todo["clientes"][s][l]))
