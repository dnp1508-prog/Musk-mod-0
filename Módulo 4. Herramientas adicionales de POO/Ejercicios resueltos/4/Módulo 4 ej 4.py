'''
Implementa un generador, que dado un entero n,
imprima todos los números inferiores a n
multiplicados por dos.
'''

n = int(input('Ingresa un número entero: '))

def num_inf_por_dos(n):
    for i in range(n):
        yield i*2
for num in num_inf_por_dos(n):
        print(num)

num_inf_por_dos(n)
