'''
Implementa un generador de Fibonacci que
genere n números de la secuencia de Fibonaccі,
que tiene la forma:
0, 1, 1, 2, 3, 5, 8, 13, ...
Cuyos dos primeros valores son 0 y 1 por
definición y el resto se calculan sumando los dos
últimos valores de la sucesión.
'''

n = int(input("Ingrese la cantidad de números de Fibonacci a generar: "))
def generador_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
sucesion = list(generador_fibonacci(n))
print(sucesion)