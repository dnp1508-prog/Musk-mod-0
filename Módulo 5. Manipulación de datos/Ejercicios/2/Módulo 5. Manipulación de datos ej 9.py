'''
Concatena dos dataframes utilizando las
siguientes condiciones.
'''
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'],
              'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubischi'],
                'Price': [29995, 23600, 61500, 900]}

germanCars = pd.DataFrame(GermanCars)
JapaneseCars = pd.DataFrame(japaneseCars)
resultado = pd.concat([germanCars, JapaneseCars], ignore_index=True)
print(resultado)