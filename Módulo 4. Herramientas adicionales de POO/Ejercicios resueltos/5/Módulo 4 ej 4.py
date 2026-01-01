'''
Añade a la función anterior, un mensaje que se
imprima al final de la ejecución de la función
independientemente de si se ha generado
excepción o no.
'''

def dividir_numeros(a, b):
    try:
        resultado = a / b
        return print(resultado)
    except TypeError:
        print('Los parámetros deben ser números enteros')
    except ZeroDivisionError:
        print('El divisor no puede ser 0')
    finally:
        print('Ejecución finalizada')
dividir_numeros(10, 0)
dividir_numeros(10, 5)