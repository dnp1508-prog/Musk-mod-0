'''
Lee los datos de ventas de los productos crema
facial y lavado de cara y muéstralos mediante el
gráfico barras. El gráfico de barras debe mostrar
el número de unidades vendidas por mes para
cada producto. Añade de una barra distinta para
cada producto en el mismo gráfico.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

xlabel = np.array(df['month_number'])
y1 = np.array(df['facecream'])
y2 = np.array(df['facewash'])

w = 0.3

x1 = xlabel - w/2
x2 = xlabel + w/2

plt.bar(x1, y1, width = w)
plt.bar(x2, y2, width = w)

plt.xlabel('Número de mes')
plt.ylabel('Unidades de venta por número')
plt.title('Facewash & facecream sales data')
plt.legend(['Ventas crema facial', 'Ventas lavado de cara'])

plt.show()
