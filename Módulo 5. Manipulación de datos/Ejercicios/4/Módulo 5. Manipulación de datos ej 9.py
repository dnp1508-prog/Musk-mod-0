'''
Lee el jabón de baño de todos los meses y
visualízalo utilizando el Subplot.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

x = np.array(df['month_number'])
y1 = np.array(df['bathingsoap'])
y2 = np.array(df['facewash'])

plt.subplot(2, 1, 1)
plt.plot(x, y1, marker='o')
plt.title('Ventas gel de baño')
plt.ylabel('Unidades vendidas')

plt.subplot(2, 1, 2)
plt.plot(x, y2, marker='o', color='red')
plt.title('Ventas lavado de cara')
plt.xlabel('Número del mes')
plt.ylabel('Unidades vendidas')

plt.show()

