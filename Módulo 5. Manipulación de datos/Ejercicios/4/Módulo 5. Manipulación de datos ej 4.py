'''
Lee los datos de las ventas de pasta de dientes
de cada mes y muéstralos mediantes un gráfico
de dispersión (scatter). Además, añade una
cuadrícula en el gráfico. El estilo de la cuadrícula
debe ser "-".
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

xlabel = np.array(df['month_number'])
ylabel = np.array(df['toothpaste'])

plt.scatter(xlabel, ylabel, label = 'Ventas pasta de dientes')

plt.grid(linestyle = '--')

plt.title('Ventas pasta de dientes')
plt.xlabel('Número del mes')
plt.ylabel('Número de unidades vendidas')
plt.legend(loc = 'upper left')

plt.show()
