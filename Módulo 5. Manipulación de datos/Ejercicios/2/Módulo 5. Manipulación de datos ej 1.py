'''
A partir del conjunto de datos dado, imprime las
5 primeras y ultimas filas.
'''
import pandas as pd

def leer_datos(ubicacion):
    datos = pd.read_csv(ubicacion)
    return datos
def imprimir_datos(datos):
    print("5 primeras filas:")
    print(datos.head())
    print("5 últimas filas:")
    print(datos.tail())
ubicacion = "Automobile_data.csv"
datos = leer_datos(ubicacion)
imprimir_datos(datos)