'''
Lee el beneficio total de todos los meses y
muéstralo mediante un gráfico de líneas. Se
proporcionan los datos del beneficio total de
cada mes. El gráfico de líneas generado debe
incluir las siguientes propiedades:
Nombre de la etiqueta X = Número de mes
Nmobre de etiqueta Y = Beneficio total
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

Xlabel = np.array(df['month_number'])
Ylabel = np.array(df['total_profit'])

plt.plot(Xlabel, Ylabel)

plt.title('Beneficios por mes')
plt.xlabel('Número de mes')
plt.ylabel('Beneficio total')

plt.show()
