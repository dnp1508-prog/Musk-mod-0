'''
1. Haz un programa que lea una secuencia de caracteres acabada en punto
y que escriba cuántas letras ‘a’ contiene.
'''
x = input('Introduce una frase: ')
count = 0
for a in x:
    if a == 'a':
        count += 1
print('La secuencia tiene {} as'.format(count))
'''
2. Haz un programa que encuentre todas las
apariciones de una subcadena en una cadena dada.
'''
x = input('Introduce una frase: ')
s = input('Introduce la subcadena: ')
count = x.count(s.lower())
print('La subcadena {} aparece {} en {}'.format(s, count, x))
'''
3. Haz un programa que invierta una cadena dada.
'''
x = input('Introduce una frase: ')
x_reverse = ''.join(reversed(x))
print('{}'.format(x_reverse))
'''
4. Haz un programa que divida una cadena en guiones.
'''
x = input('Introduce una frase: ')
s = x.replace(' ', '-')
print(s)
'''
5. Haz un programa que añada una nueva cadena en medio de una cadena dada.
'''
x = input('Introduce la cadena original: ')
y = input('Introduce la cadena a insertar: ')
n = len(x) // 2
z = x[:n] + y + x[n:]
print(z)
'''
6. Haz un programa que encuentre la última posición de una subcadena dada.
'''
x = input('Introduce una cadena: ')
y = input('Introduce una subcadena: ')

p = x.rfind(y)
print('"{}" empieza en la posicion {} dentro de "{}"'.format(y, p, x))
'''
7. Haz un programa que elimine cadenas vacías de una lista de cadenas.
'''
x = input('Introduce una cadena: ')
y = x.replace(' ', '')
print('{}'.format(y))
'''
8. Haz un programa que
elimine símbolos especiales / signos de puntuación de una cadena.
'''
import string
x = input('Introduce una cadena: ')
y = x.translate(str.maketrans('','', string.punctuation))
print(y)
'''
9. Haz un programa que encuentre palabras con letras y números.
'''
x = input('Introduce una Cadena: ')
y = x.split()
print(y)
n = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
z = ''
for i in y:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        z = z + ' ' + i
print(z)
'''
10. Haz un programa que sustituya
cada símbolo especial por # en la siguiente cadena.
'''
import string
x = input('Introduce una cadena: ')
for spc in string.punctuation:
    x = x.replace(spc, '#')
print(x)

#Listas

'''
1. Haz un programa que lea una
lista dado su tamaño e imprima el segundo elemento (si existe).
'''
y = []
n = int(input('Introduce el tamaño de la lista: '))
while n > 0:
    x = input('Introduce un elemento de la secuencia: ')
    y.append(x)
    n -= 1
print('El segundo elemento de la lista es {}'.format(y[1]))
print(y)
'''
2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1,
y que escriba cuántos son iguales al último.
'''
x = int(input('Introduce un número entero: '))
y = []

while x != -1:
    y.append(x)
    x = int(input('Introduce un número entero: '))
y.append(int('-1'))
n = len(y)
print('Existen {} elementos iguales al último elemento'.format((y.count(y[n-2])-1)))
'''
3. Haz un programa que lea secuencias de enteros acabada en -1,
y que escriba cada una invirtiendo la orden de sus elementos.
'''
x = int(input('Introduce un número entero de la secuencia: '))
y = []

while x != -1:
    y.append(x)
    x = int(input('Introduce un número entero de la secuencia: '))
print(y)
y.reverse()
print(y)
'''
4. Haz un programa que lea n palabras,
y que escriba cada una invirtiendo la orden de sus caracteres.
'''
n = int(input('Introduce la longitud de la secuencia: '))
z = ()
for i in range(0, n):
    x = input('Introduce una cadena: ')
    x = list(x)
    x.reverse()
    y = tuple(x)
    z += y
z = list(z)
print('{}'.format(z))
'''
5. Haz un programa que lea una secuencia de números mientras sean positivos
y que escriba la media.
'''
x = int(input('Introduce un número entero: '))
y = 0
count = 0
while x > 0:
    y += x
    count += 1
    print('{}'.format(count))
    print('{}'.format(y))
    x = int(input('Introduce un número entero: '))
n = y//count
print('La media de la secuencia es {}'.format(n))
'''
6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos
listas de tamaño n y m. Es decir, hay quedevolver un vector que tenga los
elementos de v1 seguidos de los elementos de v2.
'''
n = int(input('Introduce la longitud de v1: '))
m = int(input('Introduce la longitud de v2: '))

v1 = []
v2 = []

for i in range(0, n):
    x = (input('Introduce un elemento de v1: '))
    v1.append(x)
for l in range(0, m):
    y = (input('Introduce un elemento de v2: '))
    v2.append(y)
v1 = tuple(v1)
v2 = tuple(v2)
vT = list(v1 + v2)
print(vT)
'''
7. Haz un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor
y el mayor de los precios.
'''
x = [50, 75, 46, 22, 80, 65, 8]
count = 0
x.sort()

for i in x:
    count += 1
    
print(x[0], x[count - 1])
'''
8. Haz un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
'''
x = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for i in x:
    print(i)
'''
9. Haz un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
'''
x = list(range(1, 11))
x.reverse()
z = ''
for i,y in enumerate(x):
    if i == 0:
        z += str(y)
    else:
        z += ', {}'.format(y)
print(z)
'''
10. Haz un programa que concatene dos listas del mismo tamaño n
alternando elementos de una lista y otra.
'''
n = int(input('Introduce la longitud de las secuencias: '))
z = []
for i in range(0, n):
    x = input('Introduce un elemento de la primera secuencia: ')
    y = input('Introduce un elemento de la segunda secuencia: ')
    z.extend(x)
    z.extend(y)
print(z)
'''
11. Haz un programa que itere ambas listas de tamaños n y m
(siendo n y m números distintos )simultáneamente e imprima sus elementos.
'''
n = int(input('Introduce la longitud de la primera secuencia: '))
m = int(input('Introduce la longitud de la segunda secuencia: '))
s1 = []
s2 = []

for i in range(0, n):
    x = input('Introduce un elemento de la primera secuencia: ')
    s1.append(x)
for e in range(0, m):
    y = input('Introduce un elemento de la segunda secuencia: ')
    s2.append(y)

count1 = 0
count2 = 0
sT = []
while n > count1 or m > count2:
    if n > count1:
        print(s1[count1])
    if m > count2:
        print(s2[count2])
    count1 += 1
    count2 += 1
'''
12. Haz un programa que añada un nuevo elemento 60 a la lista
[10, 50, 40, 20, 30] después de un elemento especificado por el usuario.
Si el elemento introducido no está presente en la lista debe mostrar el
mensaje: 'Elemento no presente en la lista'.
'''
l = ['10', '50', '40', '20', '30']
x = input('Introduce el elemento tras el cual irá 60: ')
if x in l:
    l.insert((l.index(x) + 1), '60')
    print(l)
else:
    print('Elemento no presente en la lista')
'''
13. Haz un programa que elimine todas las apariciones de un elemento
específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].
'''
l = ['10', '50', '40', '20', '60', '30']
x = input('Introduce el elemento de la lista que quieres eliminar: ')
position = l.index(x)
l.pop(position)
print(l)

#Tuplas

'''
1. Haz una programa que invierta una tupla.
'''
x = (10, 20, 30, 40, 50)
y = x[::-1]
print(x)
print(y)
'''
2. Haz un programa que acceda al valor 15 de la tupla.
'''

t = ('Naranja', [10, 20, 30], (5, 15, 25))
print(t[2][1])
'''
3. Haz un programa que declare una tupla con un solo elemento 10.
'''
t = (10, )
print(t)
'''
4. Haz un programa que descomponga la tupla en 4 variables.
'''
t = (10, 20, 30, 40)
n = len(t)
a = (t[int(n/4)-1])
b = (t[int(2*(n/4)-1)])
c = (t[int(3*(n/4))-1])
d = (t[n-1])
print(a)
print(b)
print(c)
print(d)
'''
5. Haz un programa que intercambie dos tuplas en Python.
'''
t1 = (10, 20)
t2 = (30, 40)
t3 = t1
t1 = t2
t2 = t3
print(t1)
print(t2)
'''
6. Haz un programa que copie elementos específicos
de una tupla a una nueva tupla.
'''
t1 = (11, 22, 33, 44, 55, 66)
t2 = t1[-3:-1]
print(t2)
'''
7. Haz un programa que modifique una tupla.
'''
t1 = (11, [22, 33], 44, 55)
t1[1][0] = 222
print(t1)
'''
8. Ordena una tupla de tuplas por el 2º elemento.
'''
t1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
t1 = tuple(sorted(list(t1), key=lambda x: x[1]))
print(t1)
'''
9. Haz un programa que cuente el número de
apariciones del elemento 50 de una tupla.
'''
t1 = (50, 10, 60, 70, 50)
count = 0
for i in t1:
    if i == 50:
        count += 1
print('{}'.format(count))
'''
10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.
'''
t1  =(45, 45, 45, 45)
count = 1
while count < len(t1) and t1[count - 1] == t1[count]:
    count += 1
if count == len(t1):
    print('Todos los elementos son iguales')
else:
    print('No todos los elementos son iguales')

#Diccionarios

'''
1. Haz un programa que convierta dos listas en un diccionario.
'''
x = ['a', 'b', 'c']
y = [1, 2, 3]
d = {}
for i in range(0, len(x)):
    d[x[i]] = y[i]
print(d)
'''
2. Haz un programa que fusione dos diccionarios de Python en uno solo.
'''
dict1 = {
    'diez': 10,
    'veinte': 20,
    'treinta': 30,
    }
dict2 = {
    'treinta': 30,
    'cuarenta': 40,
    'cincuenta': 50
    }
dict3 = {**dict1, **dict2}
print(dict3)
'''
3. Haz un programa que imprima el valor de la clave 'history'
del siguiente diccionario.
'''
X ={
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'fisica': 70,
                'historia': 80
            }
        }
    }
}
print(X['class']['student']['marks']['historia'])
'''
4. Haz un programa que inicialice el diccionario con valores por defecto.
'''
employees = ['Kelly', 'Emma']
defaults = {
        'designation': 'Developer',
        'salary': 8000,
        }
defecto = dict.fromkeys(employees, defaults)
print(defecto)
'''
5. Haz un programa que cree un
diccionario extrayendo las claves de un diccionario dado.
'''
dict1 = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York' }
keys = ['name', 'salary']
dict2 = dict()
for i in keys:
    dict2.update({i: dict1[i]})
print(dict2)
'''
6. Haz un programa que elimine una lista de claves de un diccionario.
'''
dict1 = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York',
    }
keys = ['name', 'salary']
for i in keys:
    dict1.pop(i)
print(dict1)
'''
7. Haz un programa que compruebe si un valor existe en un diccionario.
'''
dict1 = {
    'a': 100,
    'b': 200,
    'c': 300 }
x = int(input('Introduce un elemento del diccionario: '))

if x in dict1.values():
    print('{} está dentro de {}'.format(x, dict1))
else:
    print('{} no está dentro de {}'.format(x, dict1))
'''
8. Haz un programa que cambie el nombre de la clave de un diccionario.
'''
dict1 = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York',
    }
dict1['location'] = dict1.pop('city')
print(dict1)
'''
9. Haz un programa que obtenga la clave de
un valor mínimo del siguiente diccionario.
'''
dict1 = {
    'Fisica': 82,
    'Mates': 65,
    'Historia': 75 }
print(min(dict1, key=dict1.get))
'''
10. Haz un programa que cambie el valor de una clave en un diccionario anidado.
'''
dict1 = {
    'emp1': {
        'name': 'John',
        'salary': 7500 },
    'emp2': {
        'name': 'Emma',
        'salary': 8000 },
    'emp3': {
        'name': 'Brad',
        'salary': 500 }
    }
dict1['emp3']['salary'] = 8500
print(dict1)

#Sets

'''
1. Haz un programa que añada una lista de elementos a un conjunto.
'''
s = {'Yellow', 'Orange', 'Black'}
l = ['Blue', 'Green', 'Red']
s.update(l)
print(s)
'''
2. Haz un programa que devuelva un nuevo
conjunto de elementos idénticos de dos conjuntos.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

s3 = s1.intersection(s2)
print(s3)
'''
3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print(s1.union(s2))
'''
4. Haz un programa que actualice el primer conjunto con elementos
que no existen en el segundo conjunto.
'''
s1 = {10, 20, 30}
s2 = {20, 40, 50}

s1.difference_update(s2)
print(s1)
'''
5. Haz un programa que elimine elementos del conjunto a la vez.
'''
s = {10, 20, 30, 40, 50}
x = {10, 20, 30}
s.difference_update(x)
print(s)
'''
6. Haz un programa que devuelva un conjunto de elementos
presentes en el conjunto A o B, pero no en ambos.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

print(s1.symmetric_difference(s2))
'''
7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común.
En caso afirmativo, mostrar los elementos comunes.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {60, 70, 80, 90, 10}

if s1.isdisjoint(s2):
    print('No tienen elementos en común')
else:
    print('Tienen en común {}'.format(s1.intersection(s2)))
'''
8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2,
excepto los elementos comunes.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

s1.symmetric_difference_update(s2)
print(s1)
'''
9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2,
excepto los elementos comunes.
'''
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

s1.intersection_update(s2)
print(s1)
