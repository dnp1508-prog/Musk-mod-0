#Haz un programa que lea un número decimal por pantalla,
#lo convierta a entero y lo imprima.
a = float(input('Introduce un número decimal: '))
print('{}' .format(int(a)))
#Haz un programa que lea un número decimal por pantalla
#e imprima su tipo y su valor redondeado en la misma línea.
b = float(input('Introduce un numero decimal: '))
print('{}, {}' .format(type(b), round(b)))
#Haz un programa que lea dos números por pantalla e imprima
#su diferencia en valor absoluto.
a = float(input('Introduce un número decimal: '))
b = float(input('Introduce un número decimal: '))
print('{}' .format(abs(a-b)))

