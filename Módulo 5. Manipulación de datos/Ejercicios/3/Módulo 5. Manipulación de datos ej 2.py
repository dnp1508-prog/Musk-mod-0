'''
Crea una matriz de enteros 5X2 de un rango
entre 100 y 200 tal que la diferencia entre cada
elemento sea 10.
'''

import numpy as np

count = 100
count2 = 0
l1 = []
l2 = []
while count != 200:
    if count2 <= 4:
        l1.append(count)
    else:
        l2.append(count)
    count += 10
    count2 += 1
array = np.array([l1, l2])
print(array)