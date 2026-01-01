'''
Escribe un programa en Python para obtener la hora actual
'''

import datetime
hora_actual = datetime.datetime.now().time()
print('{}'.format(hora_actual))