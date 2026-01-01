'''
Implementa una función generadora que dadas
dos listas del mismo tamaño, devuelva la
multiplicación entre los elementos de cada una,
el primer elemento de la lista 1 por el primero de
la lista 2, el segundo con el segundo y así
sucesivamente. Sigue la siguiente estructura:
'''
n = int(input("Ingrese el tamaño de las listas: "))
lista1 = []
lista2 = []
for i in range(n):
    lista1.append(int(input('Ingresa un número para la lista 1: ')))
    lista2.append(int(input('Ingresa un número para la lista 2: ')))
def prod(lista1, lista2):
    for i in range(len(lista1)):
        yield lista1[i] * lista2[i]

resultado = prod(lista1, lista2)

while True:
    try:
        value = next(resultado)
        print(value)
    except StopIteration:
        break
