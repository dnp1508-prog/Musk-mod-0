'''
Lee todos los datos de ventas de productos y
mostrarlos mediante un gráfico multilínea.
Muestra el número de unidades vendidas por
mes para cada producto utilizando gráficos
multilínea. (es decir, una línea de trazado
separada para cada producto).
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

plt.plot(x, y1, marker = 'o', color = 'red', label = 'Face cream Sales Data')
plt.plot(x, y2, marker = 'o', color = 'green', label = 'Face Wash Sales Data')
plt.plot(x, y3, marker = 'o', color = 'blue', label = 'ToothPaste Sales Data')
plt.plot(x, y4, marker = 'o', color = 'purple', label = 'Bathingsoap')
plt.plot(x, y5, marker = 'o', label = 'Shampoo')
plt.plot(x, y6, marker = 'o', color = 'brown', label = 'moisturizer')

plt.legend(loc = 'upper left')
plt.xlabel('Número mes')
plt.ylabel('Undad de ventas en número')
plt.title('Ventas')

plt.show()
