'''
Ecribe un programa en Python para crear 12
fechas fijas a partir de una fecha especificada en
un periodo determinado. La diferencia entre dos
fechas será de 20.
'''
from datetime import datetime, timedelta
fecha_inicial = input('Ingrese la fecha inicial formato (DD/MM/AAAA): ')
fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y')
for i in range(12):
    fecha_fija = fecha_inicial + timedelta(days=i*20)
    print('{}'.format(fecha_fija.strftime('%d/%m/%Y')))
