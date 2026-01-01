#Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!

print('¡Buenos días a todo el mundo!')

#Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.

cadena1 = 'a todo el mundo'
cadena2 = 'días '
cadena3 = 'Buenos '
print(cadena3 + cadena2 + cadena1)

#Haz un programa que declare dos números y que escriba la suma.

n1 = 3
n2 = 5
print( n1 + n2)

#Haz un programa que declare dos números y que escriba el máximo.

x = 5
y = 10
print(max(x, y))

#Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.

x = 5
y = 10
z = 15
print(max(x, y, z))

#Hacer un programa que dado un valor calcule su cuadrado y el cubo.

X = 2
cuadrado = x**2
cubo = x**3
print(a, b, cuadrado, cubo)

#Haz un programa que devuelva el valor absoluto de un número.

x = -3
print(abs(x))

'''
Haz un programa que lea dos naturales a y b, con b > 0,
y que escriba la división entera d y el residuo r de a entre b.
Recordad que, por definición, d y r tienen que ser los únicos enteros
tales que 0 ≤ r < b y d · b + r = a.
Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2
'''

x = 26
y = 4
division = a/b
residuo = a%b
print(x, y, division, residuo)

#Haz un programa que, dada una cantidad de segundos,
#diga cuántas horas, minutos y segundos representa."

segundos = 3600
minutos = segundos/60
horas = segundos / 3600
print(segundos, ' segundos',' son ', minutos, ' minutos',' y ',  horas, ' horas')

# Haz un programa que dada una temperatura en grados Celsius
#la muestre en grados Fahrenheit y en grados Kelvin.
#(F= 1.8C + 32 y  ºK =°C + 273ºK)."

Celsius = 18
Fahrenheit = 1.8*Celsius + 32
Kelvin = Celsius + 273.15
print(Celsius, ' ºcelsius ', 'son ', Fahrenheit, ' ºFarenheit ', 'y ', Kelvin, ' Kelvin')
