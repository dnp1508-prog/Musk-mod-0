'''
Ordena el siguiente array de NumPy:
Caso 1: Ordenar el array por la segunda fila.
Caso 2: Ordenar el array por la segunda columna.
'''

import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

array_ordenado_1 = sampleArray[:, [sampleArray[1].argsort()]]
print(array_ordenado_1)

array_ordenado_2 = sampleArray[[sampleArray[:, 1].argsort()]]
print(array_ordenado_2)
