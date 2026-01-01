'''
Imprime todos los datos de los coches Toyota.
'''
import pandas as pd

def imprimir_datos_totyota(ubicacion_archivo):
    datos = pd.read_csv(ubicacion_archivo)
    datos_toyota = datos[datos['company'] == 'Toyota']
    print(datos_toyota)
ubicacion = 'Automobile_data.csv'
imprimir_datos_totyota(ubicacion)