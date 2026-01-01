'''
Obtenga el beneficio total de todos los meses y
muestre un gráfico de líneas con las siguientes
propiedades de estilo:
Estilo de línea punteada y el color de la línea debe ser rojo.
Mostrar la leyenda en la parte inferior derecha.
Nombre de la etiqueta X = Número de mes
Nombre de la etiqueta Y = Número de unidades vendidas
Añadir un marcador de círculo.
El ancho de la línea debe ser 3
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

Xlabel = np.array(df['month_number'])
Ylabel = np.array(df['total_profit'])

plt.plot(
    Xlabel,
    Ylabel,
    marker = 'o',
    linewidth = 3,
    color = 'red',
    linestyle = '--',
    label = 'Profit data of last year'
    )

plt.legend(loc = 'lower right')
plt.title('Beneficios por mes')
plt.xlabel('Número de mes')
plt.ylabel('Beneficio total')

plt.show()
