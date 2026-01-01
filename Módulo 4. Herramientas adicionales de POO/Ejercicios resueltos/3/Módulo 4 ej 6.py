'''
Escribe un programa en Python para sumar 5
segundos con la hora actual
'''
import datetime
hora_actual = datetime.datetime.now()
nueva_hora = hora_actual + datetime.timedelta(seconds=5)
print('{}'.format(hora_actual))
print('Hora actual más 5 segundos: {}'.format(nueva_hora))