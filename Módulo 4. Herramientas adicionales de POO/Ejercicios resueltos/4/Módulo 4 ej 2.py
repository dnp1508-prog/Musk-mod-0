'''
Implementa un generador, que dado un entero n,
genere n números aleatorios. Puedes usar el
método random de la librería random para
generar números aleatorios.
'''
import random
n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
def numeros_aleatorios(n):
    for i in range(n):
        yield random.random()
for numero in numeros_aleatorios(n):
    print(numero)