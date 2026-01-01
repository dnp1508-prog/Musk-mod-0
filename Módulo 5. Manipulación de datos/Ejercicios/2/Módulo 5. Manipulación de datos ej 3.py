'''
Encuentra el nombre de la empresa del coche
mñas caro. Imprime el nombre de la empresa del
coche más caro y su precio.
'''
import pandas as pd

def buscar_coche_mas_caro(ubicacion_csv):
    datos = pd.read_csv(ubicacion_csv)
    coche_mas_caro = datos.loc[datos['price'].idxmax()]
    nombre_empresa = coche_mas_caro['company']
    precio_coche = coche_mas_caro['price']
    print('El coche más caro es de la empresa {} con un precio de {}€.'.format(nombre_empresa, precio_coche))
ubicacion_csv = 'Automobile_data.csv'
buscar_coche_mas_caro(ubicacion_csv)