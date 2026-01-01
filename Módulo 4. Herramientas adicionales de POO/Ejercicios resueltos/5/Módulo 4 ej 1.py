'''
Crea una función que genere una excepción excepción e
imprima su tipo, los argumentos de la excepción
y su mensaje de error.
'''

def generar_excepcion():
    try:
        res = 10/0
    except Exception as e:
        print('Tipo de excepción: {}'. format(type(e)))
        print('Argumentos de la excepción: {}'. format(e.args))
        print('Mensaje de error: {}'. format(e))
generar_excepcion()