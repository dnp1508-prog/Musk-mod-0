'''
Encuentra el coche con el precio más alto de
cada empresa.
'''

import pandas as pd

def coche_mas_caro(ubicacion):
    datos = pd.read_csv(ubicacion)
    resultado = datos.loc[datos.groupby("company")["price"].idxmax()]
    print(resultado)
    
ubicacion = 'Automobile_data.csv'
coche_mas_caro(ubicacion)
