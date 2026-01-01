'''
Imprime el máximo del eje 0 y el mínimo del eje 1
de siguiente matriz bidimensional:
'''
import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

máx_0 = np.max(sampleArray[0])
print(máx_0)

min_1 = np.min(sampleArray[1])
print(min_1)
