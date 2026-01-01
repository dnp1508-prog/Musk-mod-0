'''
1. Haz un programa que lea dos palabras y que indique el orden lexicográfico.
Escribe en una línea indicando si a < b, a > b o a = b.
Ejemplo: a = Anna, b = Javier, Anna < Javier.
'''
a = input('Introduce una palabra: ')
b = input('Introduce otra palabra: ')
if a > b:
    print('{} > {}'.format(a, b))
elif b > a:
    print('{} > {}'.format(b, a))
else:
    print('{} = {}'.format(a, b))
'''
2. Haz un programa que lea una letra y que indique por pantalla
si es una mayúscula,si es una minúscula, si es una vocal,
y si es una consonante.
'''
a = input('Introduce una letra: ')
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('{} es una vocal'.format(a))
else:
    print('{} no es una vocal'.format(a))
if a.islower():
    print('{} es minúscula'.format(a))
else:
    print('{} es mayúscula'.format(a))
'''
3. Haz un programa que lea un entero que representa una temperatura en grados
Celsius, y que diga si hace calor, si hace frío, o si se está bien.
Suponed que hace calor si la temperatura es más alta que 30 grados,
que hace frío si es más baja que 10 grados, y que se está bien en otro caso.
'''
Temperatura = float(input('Introduce la temperatura actual: '))
if Temperatura > 30:
    print('Hace calor')
elif Temperatura < 10:
    print('hace frío')
else:
    print('Se está bien')
'''
4. Haz un programa que, dados dos intervalos,
calcule el intervalo correspondiente
a la intersección o indique que esta es vacía.
'''
x1 = float(input('Introduce el extermo izquierdo del primer intervalo: '))
y1 = float(input('Introduce el derecho izquierdo del primer intervalo: '))
x2 = float(input('Introduce el extermo izquierdo del segundo intervalo: '))
y2 = float(input('Introduce el extermo derecho del segundo intervalo: '))
minimo = x1
if x2 > x1:
    minimo = x2,
    
maximo = y1
if y2 < y1:
    maximo = y2
if minimo <= maximo:
    print('[{}, {}]'.format(minimo, maximo))
else:
    print('Esta vacia')
'''
5. Haz un programa que indique si un año es bisiesto o no.
Un año bisiesto tiene 366 días. Después de la reforma gregoriana,
los años bisiestos son los múltiplos de cuatro que no acaban en dos ceros,
y también los acabados en dos ceros tales que el número que queda después
de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900,
a pesar de ser múltiples de cuatro,
no fueran bisiestos; en cambio, 2000 lo fue.
'''
año = int(input('¿Que año es? '))
if año%4 == 0 and (año%100 != 0 or año%400 == 0):
    print('El año {} es bisiesto'.format(año))
else:
    print('El año {} no es bisiesto'.format(año))
'''
6. Haz un programa que añada un segundo en una hora del día,
dadas sus horas, minutos y segundos.
'''
hora = int(input('Introduce las horas: '))
minuto = int(input('Introduce los minutos: '))
segundo = int(input('Introduce los segundos: '))
if segundo + 1 > 59:
    segundo = 0
    minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
        if hora == 24 and minutos == 60 and segundo == 60:
            hora = 0
            minuto = 0
            segundo = 0
else:
    segundo += 1
print('Hora {}, minuto {}, segundo {}'.format(hora, minuto, segundo))
'''
7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋
(la parte entera inferior de x), ⌈x⌉ (la parte entera superior de x),
y el redondeo de x.
'''
x = float(input('Introduce un número: '))
print('[X]: {}, [X]: {}, redondeo: {}'.format(int(x), round(x), round(x)))

'''
8. Haz un programa que lea dos números a y b, y que escriba todos los números
enteros a y b. Debe cumplirse que a < b.
En caso que a > b, escribe los número de manera descendente.
'''
while True:
    a = int(input('Introduce un número entero: '))
    b = int(input('Introduce un número entero: '))

    if a < b:
        for i in range (b, a - 1, -1):
           print(i)
    elif a > b:
        for i in range (a, b - 1, -1):
            print(i)
    else:
        print('a y b son iguales')
'''
9. Haz un programa que lea una secuencia de 10 números y que escriba la media.
'''
a = int(input('Introduce un número: '))
b = int(input('Introduce un número: '))
c = int(input('Introduce un número: '))
d = int(input('Introduce un número: '))
e = int(input('Introduce un número: '))
f = int(input('Introduce un número: '))
g = int(input('Introduce un número: '))
h = int(input('Introduce un número: '))
i = int(input('Introduce un número: '))
j = int(input('Introduce un número: '))
media = (a + b + c + d + e + f + g + h + i + j)//10
print('{}'.format(media))

'''
10. Haz un programa que dada una lista de naturales de tamaño n,
indique la posición del primer número par.
'''
n = int(input('Introduce cuantos elementos tendrá la lista: '))
for i in range (0, n):
    x = int(input('Introduce un número: '))
    if x%2 == 0:
        print('El primer número par es {} en la posicion {}'.format(x, i + 1))
        break
'''
11. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
'''
n = int(input('Introduce un numero: '))
for i in range(0, 11):
    x = n*i
    print('{}'.format(x))
'''
12. Haz un programa que lea un número y que lo escriba del revés.
'''
x = int(input('Introduce un número: '))
x_revés = ' '
while x > 0:
    x_revés += str(x%10)
    x = x//10
print(x_revés)
'''
13. Haz un programa que lea un número y que escriba el número de dígitos.
'''
x = int(input('Introduce un numero: '))
x1 = x
count = 0
while x > 0:
    x //= 10
    count += 1
print('{} tiene {} digitos '.format(x1, count))
'''
14. Haz un programa que diga si un natural n es capicua o no.
'''
n = int(input('Introduce un numero: '))
x = n
count = 0
while x > 0:
    x //= 10
    count += 1
if (n%10) == (n//(10**(count - 1))):
    print('El numero {} es capicua'.format(n))
else:
    print('No es capicua')
'''
15. Haz un programa que dada una secuencia de años acabada en
0 nos diga cuántos hay del siglo 20.
'''
n = int(input('Introduce cuantos años tiene la secuéncia: '))
count = 0
for i in range(0, n):
    x = int(input('Introduce un año: '))
    if x//100 == 19:
        count += 1
print('Hay {} años del siglo XX'.format(count))
'''
16. Haz un programa que reciba una secuencia de naturales de tamaño n y
nos devuelva cuál es el primer natural que tiene un valor inferior
al primer natural leído.
'''
n = int(input('Introduce cuantos naturales tienes la secuéncia: '))
x1 = int(input('Introduce un número natural: '))
for i in range(0, n-1):
    x = int(input('Introduce un número natural: '))
    if x1 > x:
        print('El número {} es el primero más pequeño que {}'.format(x, x1))
        break
'''
17. Haz un programa que cuente cuántos valores hay en una
secuencia de enteros acabada en 0.
'''
count = int(input('Introduce un entero: '))
x = 1
while x != 0:
    count += 1
    x = int(input('Introduce un entero: '))
print('La secuéncia tiene {} elementos'.format(count))
'''
18. Haz un programa que devuelva
el máximo de una secuencia de temperaturas acabada en 1000.
'''
x = float(input('Introduce la temperatura: '))
valor_max = -273
while x != 1000:
    if x > valor_max:
        valor_max = x
    x = float(input('Introduce la temperatura: '))
print('La temperatura más alta es {}'.format(valor_max))
'''
19. Haz un programa que dada una secuencia de valores acabada
en 0 compruebe que ningún valor supera 50.
'''
x = int(input('introduce un número menor a 50: '))
count = 0
while x != 0:
    x = int(input('introduce un número menor a 50: '))
    if x > 50:
        count += 1
if count == 0:
    print('No existe ningun número mayor a 50 en la secuencia')
elif count == 1:
    print('Existe un elementto en la secuencia mayor a 50')
else:
    print('Existen {} elementos en la secuencia mayores a 50'.format(count))
'''
20. Haz un programa que dada una secuencia de valores acabada en 0 compruebe 
que ningún valor supera 50 y que no hay más de tres que superen 40.
'''
x = int(input('introduce un número: '))
count1 = 0
count2 = 0
while x != 0:
    x = int(input('introduce un número: '))
    if x > 50:
        count1 += 1
    if x > 40:
        count2 += 1
if count1 == 0 and 3 > count2:
    print('No existe ningun número mayor a 50 ni 3 valores mayores a 40 en la secuencia')
elif count1 == 1 and count2 >= 3:
    print('Existe un elemento en la secuencia mayor a 50 y 3 o más mayores a 40')
elif count1 == 0 and count2 >= 3:
    print('No existe ningun elemento en la secuencia mayor a 50 pero si 3 o más mayores a 40')
else:
    print('Existe un elemento o más en la secuencia mayor a 50 pero no 3 o más mayores a 40')
'''
21. Haz un programa que dada una secuencia de valores
acabada en 0 diga si hay más positivos o negativos.
'''
x = int(input('Introduce un número entero: '))
count1 = 0
count2 = 0
while x != 0:
    x = int(input('Introduce un número entero: '))
    if x > 0:
        count1 += 1
    elif 0 > x:
        count2 += 1
if count1 == count2:
    print('Hay la misma cantidad de positivos que de negativos')
elif count1 > count2:
    print('Hay más positivos que negativos')
else:
    print('Hay más negativos que positivos')
'''
22. Haz un programa que dada una secuencia de valores enteros acabada
en 0 diga cuál es el número que hay antes de primer negativo encontrado.
'''
x = int(input('Introduce un número: '))
while x != 0:
    x = int(input('Introduce un número: '))
    if 0 > x:
        print('El número previo al primer negativo es el {}'.format(n))
        break
    n = x
'''
23. Haz un programa que lea varias descripciones de rectángulos y de círculos,
y que para cada una escriba el área correspondiente. La entrada empieza con
un número n, seguido de n descripciones. Si es de un rectángulo, se tiene la
palabra “rectángulo” seguida de dos reales estrictamente positivos que indican
la longitud y la anchura. Si es de un círculo, se tiene la palabra
“círculo” seguida de un real estrictamente positivo que indica el radio.
'''
import math
n = int(input('Introduce la longitud de la secuencia: '))
for i in range(0, n):
    x = input('Introduce el tipo de poligono: ')
    if x == 'rectángulo':
        L = int(input('Introduce la longitud del rectángulo: '))
        A = int(input('Introduce la anchura del rectangulo: '))
        S = L * A
    elif x == 'círculo':
        R = int(input('Introduce el radio del círculo: '))
        S = pow(R, 2) * math.pi
    else:
        print('El tipo de poligono es incorrecto')
    print('El {} tiene un area de {}'.format(x, S))














