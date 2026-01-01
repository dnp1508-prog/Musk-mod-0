'''
Combina dos dataframe utilizando la siguiente
condición. Crea dos dataframe utilizando
los siguientes dos Dicts, fusionalos y añade el
segundo dataframe como una nueva columna al
primer dataframe.
'''

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
             'Price': [23845, 17995, 135925, 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
                  'Horsepower': [141, 80, 182, 160]}

df = pd.DataFrame(Car_Price)
df2 = pd.DataFrame(Car_Horsepower)
resultado = pd.merge(df, df2, on='Company')
print(resultado)