import sys
sys.path.append('./control_libreria')

from peliculas import traer_todo_peliculas
from datetime import datetime


def precio_pagar():

    cliente = input(" ingrese el cliente para ver cuanto debe pagar ")

    todo = traer_todo_peliculas()

    dicc = []

    hoy = datetime.now()

    total = 0

    for n in (todo["peliculas"]):
        for r in (todo["peliculas"][n]["alquiler"]):
            for s in r:
                if s == "codigo_cliente" and cliente == r[s]:
                    fecha = datetime.strptime(r["fecha"], '%d/%m/%Y')
                    tiempo = hoy - fecha
                    tiempo = tiempo.days
                    precio_parcial = (
                        todo["peliculas"][n]["precio_alquiler"]) * tiempo
                    total += precio_parcial
    print(" debe un total de " + str(total) + " pesos ")
