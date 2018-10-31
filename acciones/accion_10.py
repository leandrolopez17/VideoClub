import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')

from peliculas import encontrar_codigo_peliculas
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

    print(consulta)
