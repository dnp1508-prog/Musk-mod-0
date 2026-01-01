'''
Crea un array de enteros 4X2 e imprime sus 
atributos. Nota: El elemento debe ser de tipo 
unsignedint16. Imprime los siguientes atributos:
La shape del array.
Las dimensiones del array.
El tamaño de cada elemento del array en bytes.
'''

import numpy as np

array = np.zeros((4,2), dtype=np.uint16)

print('{}'.format(array.shape))
print('{}'.format(array.ndim))
print('{}'.format(array.itemsize))


