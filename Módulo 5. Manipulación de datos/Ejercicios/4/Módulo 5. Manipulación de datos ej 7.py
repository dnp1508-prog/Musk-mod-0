'''
Lee el beneficio total de cada mes y muéstralo
utilizando el histograma para ver los rangos de
beneficio más comunes.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

xlabel = np.array(df['total_profit'])

plt.title('Profit')
plt.xlabel('profit en dolares')
plt.ylabel('Actual profit en dolares')
plt.legend('Profit')

plt.hist(xlabel)

plt.show()
