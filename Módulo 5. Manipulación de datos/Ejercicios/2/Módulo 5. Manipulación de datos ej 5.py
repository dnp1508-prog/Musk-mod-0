'''
Cuenta el total de coches por empresa
'''
import pandas as pd

def contar_coches_por_empresa(ubicacion_archivo):
    datos = pd.read_csv(ubicacion_archivo)
    empresas = datos['company']
    cuenta = {}

    for empresa in empresas:
        if empresa in cuenta:
            cuenta[empresa] += 1
        else:
            cuenta[empresa] = 1

    print(cuenta)

ubicacion = 'Automobile_data.csv'
contar_coches_por_empresa(ubicacion)

