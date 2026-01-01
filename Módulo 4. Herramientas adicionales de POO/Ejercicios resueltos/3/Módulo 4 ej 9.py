'''
Escribe un programa en Python para contar el
número de lunes del primer día del mes desde
2015 hasta 2016.
'''
import datetime
contador_lunes = 0
for i in range(2015, 2017):
    for j in range(1, 13):
        if datetime.date(i, j, 1).weekday() == 0:
            contador_lunes += 1
print('En el período de 2015 a 2016, el primer día del mes fue lunes {} veces'.format(contador_lunes))
