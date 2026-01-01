'''
Escribe un programa en Python para restar cinco
días a la fecha actual.
'''

import datetime
fecha_actual = datetime.datetime.now()
nueva_fecha = fecha_actual - datetime.timedelta(days=5)
print('{}'.format(fecha_actual))
print('{}'.format(nueva_fecha))