# PROGRAMACIÓN
# Una biblioteca realiza una encuesta en la que preguntan
# 1) tipo de libro que te gusta: 1 = ficcion 2 = no ficcion
# 2) ciudad a la que perteneces con un número pre asignado entre las 20 posibles ciudades (no hace falta aclarar a que ciudad va cada numero)
# 3) edad
# 4) sexo: f:femenino m:masculini
# 5) nivel de educacion: p=primaria s=secundaria u=universidad
##
# Los datos se presentan en el formato: '1,3,30,f,s'
# Donde 1 corresponde a ficcion 3 a la ciudad y 30 a la edad y vienen en una lista de caracteres en la que cada item de la lista es una encuesta
##
# El programa tiene que ejecutar las siguientes opciones
# a) promedio de lectores de cada tipo
# b) promedio de edad de los encuestados
# c) cantidad de encuestados por ciudad
# d) cantidad de encuestados universitarios

base_datos = [
    [2, 5, 10, "f", "s"],
    [1, 5, 70, "m", "u"],
    [1, 7, 50, "m", "p"],
    [1, 8, 20, "f", "u"]
]



def promedio_tipo_lectores(datos):

    lectores_ficcion = 0
    lectores_no_ficcion = 0
    for n in datos:
        if n[0] == 1:
            lectores_ficcion += 1
        else:
            lectores_no_ficcion += 1

    print(lectores_ficcion)
    print(lectores_no_ficcion)

    t = (lectores_ficcion) / (lectores_ficcion + lectores_no_ficcion)
    s = (lectores_no_ficcion) / (lectores_no_ficcion + lectores_ficcion)

    print(t, s)

def promedio_edad(datos):

    promedio = 0

    for n in datos:
        promedio += n[2]
    
    promedio = promedio / len(datos)

    print(promedio)

def cantidad_encuestados(datos):

    lista_datos = []
    otra_lista = []
    
    for n in datos:
        seguir = True
        for s in lista_datos:
            if n[1] == s:
                seguir = False
                
        if seguir == True:
            lista_datos.append(n[1])
            otra_lista.append([n[1],1])

        else:
            for l in otra_lista:
                l[1] += 1

    print(otra_lista)
        
                    
promedio_tipo_lectores(base_datos)

promedio_edad(base_datos)

cantidad_encuestados(base_datos)