import sys
sys.path.append('./control_libreria')

from peliculas import traer_todo_peliculas


def no_alquiladas():

    todo = traer_todo_peliculas()

    pelis_no = []

    for n in (todo["peliculas"]):
        if len(todo["peliculas"][n]["alquiler"]) == 0:
            pelis_no.append(n)

    print(" la peliculas no alquiladas son ", pelis_no)
