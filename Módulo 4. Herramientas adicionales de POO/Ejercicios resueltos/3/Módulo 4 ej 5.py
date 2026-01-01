'''
Escribe un programa en Python para convertir
una cadena de marcas de tiempo unix en una
fecha legible.
'''
import datetime
tiempo_unix = 1284105682
fecha_legible = datetime.datetime.fromtimestamp(tiempo_unix)
print('{}'.format(tiempo_unix))
print('{}'.format(fecha_legible))