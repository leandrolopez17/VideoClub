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
    [1, 3, 70, "m", "u"],
    [1, 7, 50, "m", "p"],
    [1, 8, 20, "f", "u"]
]

tipodelibro = int(input("ingrese tipo de pelicula 1.ficcion 2.no ficcion")) # va 1 o 2
while tipodelibro > 2 or tipodelibro < 1:
    tipodelibro = int(input("ingrese otro valor"))

ciudadpertenencia = int(input("ingrese numero de ciudad que perteneces entre el 1 y el 20: "))
while ciudadpertenencia > 20 or ciudadpertenencia < 0:
    ciudadpertenencia = int(input("ingrese otra ciudad"))

edad = int(input("ingrese edad: "))
while edad < 0:
    edad = int(input("ingrese otra edad"))

sexo = input("ingrese f=femenino o m=masculino segun su correspondiente sexo: ")
while sexo == f or sexo == m:
    sexo = input("ingrese otra letra")

niveleducativo = input("ingrese p=primaria s=secundaria u=universidad")

lista = [
    [tipodelibro,ciudadpertenencia,edad,sexo,niveleducativo]
]