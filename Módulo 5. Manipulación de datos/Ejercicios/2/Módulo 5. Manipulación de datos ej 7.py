'''
Encuentra el kilometraje medio de cada empresa
fabricante de automóviles. average_mileage
'''

import pandas as pd

def encontrar_media_kilometraje(ubicacion):
    datos = pd.read_csv(ubicacion)
    media = datos.groupby('company')['average-mileage'].mean()
    print(media)

ubicacion = 'Automobile_data.csv'
encontrar_media_kilometraje(ubicacion)
