'''
1. Haz un programa que cree una función en Python que
dada una secuencia devuelva únicamente los números pares.
'''
def num_pares(l):
    s = []
    for i in l:
        if i%2 == 0:
            s.append(i)
    return(s)
l = [5, 7, 3, 4, 2, 1]
x = num_pares(l)
print(x)
'''
2. Haz un programa que cree una función con longitud variable de argumentos.
'''
def fun(*t):
    for i in t:
        print(i)

fun(20, 40, 60)
'''
3. Haz un programa que devuelva múltiples valores desde una función.

Crea la función calculaion() de modo que pueda aceptar dos variables
y calcular sumas y restas.
Además, debe devolver tanto la suma como la resta en una sola llamada.
'''

def calculation(x, y):
    r1 = x + y
    r2 = x - y
    return(r1, r2)

print(calculation(40, 10))
'''
4. Haz un programa que cree una función con un argumento por defecto.

Crea una función show_employee() usando las siguientes condiciones.
Debe aceptar el nombre y el salario del empleado y mostrar ambos.
Si falta el salario en la llamada de función, asigne el valor
predeterminado 9000 al salario.
'''
def show_employee(x, y = 9000):
    s = {
        'Nombre': x,
        'Salario': y }
    print(s)
show_employee('Ben', 12000)
show_employee('Jessa')
'''
5. Haz un programa que cree una función interna para calcular la
suma de la siguiente manera:
Crea una función externa que acepte dos parámetros, a y b.
Crea una función interna dentro de una función externa que calculará la suma de
a y b. Por último, una función externa que sumará 5 en la suma y la devolverá.
'''
def ext(a, b):
    def inte(a, b):
        res = a + b
        return(res)
    res2 = inte(a, b) + 5
    return(res2)

x = ext(5, 10)
print(x)
'''
6. Haz un que cree una función que escriba el cuadrado
y la raíz cuadrada de una secuencia de naturales.
'''
import math
def fun1(l):
    r1 = []
    for i in l:
        x = i**2
        r1.append(x)
    return(r1)
def fun2(l):
    r2 = []
    for e in l:
        y = math.sqrt(e)
        r2.append(y)
    return(r2)
l = [10, 4, 1, 15]
print(fun1(l), fun2(l))
'''
7. Haz un programa que cree una función que deje a, b y c
ordenados de pequeño a grande. Por ejemplo, si a =7, b = −3 y c = 1,
los valores después de la llamada deben ser a =−3, b = 1 y c = 7.
'''
def ord1(a, b, c):
    x = [a, b, c]
    x.sort()
    return(x)
print(ord1(7, -3, 1))
