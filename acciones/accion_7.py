import sys
sys.path.append('./control_libreria')

from clientes import encontrar_codigo_clientes


def consultar_datos_socio():

    codigo = input(" ingrese el codigo para consultar los datos del socio ")

    funciona = False
    while funciona == False:
        cliente = encontrar_codigo_clientes(codigo)
        if cliente == None:
            codigo = input(" ingrese el codigo nuevamente porque no existe")

        else:
            funciona = True

    print("el nombre es: " + cliente["nombre"])
    print("la fecha de ingreso es: " + cliente["fecha_alta"])
