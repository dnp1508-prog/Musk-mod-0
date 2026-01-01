'''
Lee todos los datos de las ventas de productos y
muéstrelos mediante el diagrama de pila.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

x = np.array(df['month_number'])
y1 = np.array(df['facecream'])
y2 = np.array(df['facewash'])
y3 = np.array(df['toothpaste'])
y4 = np.array(df['bathingsoap'])
y5 = np.array(df['shampoo'])
y6 = np.array(df['moisturizer'])

label = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
plt.stackplot(x, y1, y2, y3, y4, y5, y6, labels = label)
plt.title('Todas las ventas de productos en un stack plot')
plt.xlabel('Número del mes')
plt.ylabel('Unidades de ventas en número')
plt.legend(label, loc = 'upper left')

plt.show()
