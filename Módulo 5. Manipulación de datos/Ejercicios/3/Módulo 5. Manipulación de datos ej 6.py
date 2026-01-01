'''
Divide la matriz en cuatro submatrices de igual tamaño.
Nota: Crea un matriz de enteros 8X3 de un rango entre 10 y 34
de tal manera que la diferencia entre cada elemento sea 1 y luego
divide la matriz en cuatro submatrices de igual tamaño.
'''

import numpy as np

array = np.arange(10, 34).reshape(8, 3)
print(array)

subarray = np.split(array, 4)

for i, sub in enumerate(subarray, 1):
    print("Subarray nº{}:".format(i))
    print(sub)
