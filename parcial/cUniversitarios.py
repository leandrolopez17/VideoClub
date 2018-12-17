# data = [
#     [2, 5, 10, "f", "s"],
#     [1, 3, 70, "m", "u"],
#     [1, 7, 50, "m", "p"],
#     [1, 8, 20, "f", "u"]
# ]

# nivel de educacion: p=primaria s=secundaria u=universidad
def cUniversitarios(data):
    cPrimaria = 0
    cSecundaria = 0
    cUniversidad = 0
    for d in data:
        if (d[4] == "p"):
            cPrimaria += 1
        else if (d[4] == "s"):
            cSecundaria += 1
        else if (d[4] == "u"):
            cUniversidad += 1

    return [cUniversidad, cSecundaria, cPrimaria]
