'''
Crea una función que compute la diferencia
entre dos enteros. En caso de que la diferencia
sea negativa genera una excepción inventada
por ti que informe sobre ello. Por ejemplo. la
excepción podría llamarse
NegativeDifferenceException.
'''

def diferencia(a, b):
    res = a - b
    if res < 0:
        raise NegativeDifferenceException('La diferencia es negativa.')
    return res
class NegativeDifferenceException(Exception):
    pass
diferencia(3, 5)