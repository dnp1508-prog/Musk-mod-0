'''
Ordena todos los coches por la columna Precio
'''

import pandas as pd

def ordenar_precio(ubicacion):
    datos = pd.read_csv(ubicacion)
    resultado = datos.sort_values(by=['price'])
    print(resultado)
ubicacion = 'Automobile_data.csv'
ordenar_precio(ubicacion)