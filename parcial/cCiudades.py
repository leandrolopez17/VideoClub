# data = [
#     [2, 5, 10, "f", "s"],
#     [1, 3, 70, "m", "u"],
#     [1, 7, 50, "m", "p"],
#     [1, 8, 20, "f", "u"]
# ]

# 2) ciudad a la que perteneces con un número pre asignado entre las 20 posibles ciudades (no hace falta aclarar a que ciudad va cada numero)
def cCiudades(data):
    ciudades = {}
    for d in data:
        if d[1] in ciudades:
            ciudades[d[1]] = 0
        else:
            ciudades[d[1]] += 1

    return ciudades
