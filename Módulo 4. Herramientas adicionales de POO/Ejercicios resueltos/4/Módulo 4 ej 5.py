'''
Implementa un generador, que dado un entero n, 
genere n números senares
'''

n = int(input('Ingrese un número entero: '))

def generador_senares(n):
    for i in range(n):
        yield i * 2 + 1

num_senares = list(generador_senares(n))
print(num_senares)