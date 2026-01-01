'''
Escribe un programa en Python para seleccionar
todos los domingos de un año determinado.
'''
import datetime
def obtener_domingos(año):
    domingos = []
    for mes in range(1, 13):
        for dia in range(1, 32):
            try:
                fecha = datetime.date(año, mes, dia)
                if fecha.weekday() == 6:
                    domingos.append(fecha)
            except ValueError:
                continue
    return domingos
año = int(input('Ingrese un año: '))
domingos = obtener_domingos(año)
print('{}'.format(domingos))