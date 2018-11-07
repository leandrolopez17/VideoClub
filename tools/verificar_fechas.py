from datetime import datetime, date, time, timedelta
import calendar


def verificar_fecha():

    while True:
        try:
            fecha_str = input('\n Ingrese fecha "dd/mm/aaaa"...: ')

            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            if fecha < datetime.now():
                break
            else:
                print(" todavia no hemos llegado a esa fecha ")
        except:
            print("\n No ha ingresado una fecha correcta...")

    return(fecha_str)
