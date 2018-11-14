# VERIFICAR FECHAS
from datetime import datetime, date, time, timedelta
import calendar


def verificar_fecha(variable):

    while True:
        try:
            if variable == None:
                fecha_str = input('\n Ingrese fecha "dd/mm/aaaa"...: ')

                fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
                if fecha < datetime.now():
                    break
                else:
                    print(" todavia no hemos llegado a esa fecha ")
            else:
                fecha_str = variable
                fecha = datetime.strptime(variable, '%d/%m/%Y')
                if fecha < datetime.now():
                    break
                else:
                    print(" todavia no hemos llegado a esa fecha ")

        except:
            print("\n No ha ingresado una fecha correcta...")
            variable = None

    return(fecha_str)
