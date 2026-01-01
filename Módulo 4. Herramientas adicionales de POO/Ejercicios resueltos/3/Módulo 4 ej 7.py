'''
Escribe un programa en Python para obtener el
número de la semana.
'''
import datetime
fecha_actual = datetime.date.today()
numero_semana = fecha_actual.isocalendar()[1]
print('{}'.format(numero_semana))
