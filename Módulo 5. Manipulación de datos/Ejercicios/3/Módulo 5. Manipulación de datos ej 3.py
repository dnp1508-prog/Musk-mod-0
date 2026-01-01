'''
A continuación se muestra el array Numpy
proporcionado. Devuelve un array de elementos
tomando la tercera columna de todas las filas.
'''

import numpy as np

sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

elemento1 = sampleArray[0][2]
elemento2 = sampleArray[1][2]
elemento3 = sampleArray[2][2]
print('{}, {}, {}'.format(elemento1, elemento2, elemento3))