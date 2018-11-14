# ACCION 9


import sys
sys.path.append('./tools')
sys.path.append('./control_libreria')

from agregar_modificar_clientes import modificar_client
from agregar_modificar_peliculas import modificar_peli
from peliculas import subir_alquiler
from verificar_fechas import verificar_fecha


def alquiler_pelicula():

    codigo_cliente = input(
        " ingrese el codigo del cliente que alquilo la pelicula ")

    codigo_cliente = modificar_client(codigo_cliente)

    codigo_pelicula = input(
        " ingrese el codigo de la pelicula que se ha alquilado ")

    codigo_pelicula = modificar_peli(codigo_pelicula)

    fecha = verificar_fecha(None)

    data = {"codigo_cliente": codigo_cliente, "fecha": fecha}

    subir_alquiler(data, codigo_pelicula)
