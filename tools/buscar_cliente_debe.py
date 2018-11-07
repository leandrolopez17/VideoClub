import sys
sys.path.append('./control_libreria')

from peliculas import traer_todo_peliculas


def buscar(cliente):

    todo = traer_todo_peliculas()

    for n in (todo["peliculas"]):
        for r in (todo["peliculas"][n]["alquiler"]):
            for s in r:
                if s == "codigo_cliente" and cliente == r[s]:
                    return True
