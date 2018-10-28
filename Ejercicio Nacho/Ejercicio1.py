d = [ 'Nombre' ,'Fecha' , 'telefono' , 'mail' , 'direccion' ]

agenda = [ ]

c = 0
for k in range(1):
    c = c+1
    cliente = dict.fromkeys(d)

    for clave in d:
        a = input("ingresar "+clave+": ")
        cliente [clave] = a
    agenda.append(cliente)

print(c)
print(agenda)





#for cliente in agenda:
 #   if cliente [d[posicion ]] == " # nombre ":
  #      print ("existe")
   # else:
    #    print ("no existe")








    






