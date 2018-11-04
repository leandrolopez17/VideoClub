import sys
sys.path.append('./peliculas')
sys.path.append('./clientes')

from peliculas import traer_todo_peliculas
from clientes import traer_todo_clientes


def socios():
    data_peli = traer_todo_peliculas()
    data_client = traer_todo_clientes()

    dicc = {}

    for n in data_client["clientes"]:
        dicc[n] = 0

    for t in (data_peli["peliculas"]):
        for r in (data_peli["peliculas"][t]["alquiler"]):
            for f in r:
                if f == "codigo_cliente":
                    variable = r[f]
                    dicc[variable] += 1

    print(dicc)
