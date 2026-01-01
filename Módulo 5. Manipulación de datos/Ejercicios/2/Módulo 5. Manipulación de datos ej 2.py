'''
Limpia el conjunto de datos y actualiza el archivo
CSV. Reemplaza todos los valores de las
columnas que contengan ?, n.a, o NaN.
'''

import pandas as pd

def limpiar_datos(ubicacion):
    datos = pd.read_csv(ubicacion)
    datos_limpios = datos.replace(['?', 'n.a', 'NaN'], pd.NA)
    datos_limpios.to_csv(ubicacion, index=False)
ubicacion = 'Automobile_data.csv'
limpiar_datos(ubicacion)
