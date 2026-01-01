'''
Crea una función que calcule la división entre
dos números. Debe imprimir el mensaje 'Los
parámetros deben ser número enteros' cuando
se genera una excepción de tipo y 'El divisor no
puede ser 0' cuando se genera un
zerodivisionerror.
'''

def dividir_numeros(a, b):
    try:
        resultado = a / b
        return print(resultado)
    except TypeError:
        print('Los parámetros deben ser números enteros')
    except ZeroDivisionError:
        print('El divisor no puede ser 0')
dividir_numeros(10, 0)
dividir_numeros(10, 5)