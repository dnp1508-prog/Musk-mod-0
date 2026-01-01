'''
Lee los datos de vendas de jabón de baño de
todos los meses y muéstralos mediante un
gráfico de barras. Guarda este gráfico en tu disco
duro.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

xlabel = np.array(df['month_number'])
ylabel = np.array(df['bathingsoap'])

plt.title('Ventas jabón de baño')
plt.xlabel('Número del mes')
plt.ylabel('Unidades vendidas en número')
plt.grid(linestyle = '--', linewidth = 0.5)

plt.bar(xlabel, ylabel, width = 0.5)

plt.savefig('Ventas jabón de baño.png')

plt.show()
