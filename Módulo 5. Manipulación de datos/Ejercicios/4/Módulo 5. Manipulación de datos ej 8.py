'''
Calcula los datos de ventas totales del último
año para cada producto y muéstralos mediante
un gráfico circular. Nota: En el gráfico circular
muestra el número de unidades vendidas por año
para cada producto en porcentaje.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

x1 = df['facecream'].sum()
x2 = df['facewash'].sum()
x3 = df['toothpaste'].sum()
x4 = df['bathingsoap'].sum()
x5 = df['shampoo'].sum()
x6 = df['moisturizer'].sum()

x = np.array([x1, x2, x3, x4, x5, x6])
labels = ['facecream', 'facewash', 'toothpaste',
          'bathingsoap', 'shampoo', 'moisturizer']

plt.title('Sales data')
plt.pie(x, labels = labels, autopct= '%1.1f%%', startangle = 90)

plt.show()
