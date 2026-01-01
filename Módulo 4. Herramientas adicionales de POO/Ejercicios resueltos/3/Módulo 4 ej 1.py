'''
Escribe un script en Python para mostrar los
distintos formatos de fecha y hora.
'''
from datetime import datetime
now = datetime.now()
print('Fecha y hora actual: {}'.format(now))
print('Estamos en el año: {}'.format(now.year))
print('Estamos en el mes: {}'.format(now.month))
print('Número de la semana del año: {}'.format(now.isocalendar()[1]))
print('Día de la semana: {}'.format(now.isocalendar()[2]))
print('Día del año: {}'.format(now.timetuple().tm_yday))
print('Día del mes: {}'.format(now.day))
print('Día de la semana: {}'.format(now.weekday() + 1))
'''
a) Fecha y hora actuales
b) Año actual
c) Mes del año
d) Número de la semana del año
e) Día de la semana
f) Día del año
g) Día del mes
h) Día de la semana
'''