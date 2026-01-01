import os
import pandas as pd
from entities.aeropuerto import Aeropuerto
from entities.lector import Lector

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower()
    df = df.replace('-', pd.NA)
    if 'tipo_vuelo' in df.columns:
        df['tipo_vuelo'] = df['tipo_vuelo'].str.strip().str.upper()
        df['tipo_vuelo'] = df['tipo_vuelo'].replace({
            'NAT': 'NACIONAL',
            'INTERNAT': 'INTERNACIONAL'
        })

    if 'fecha_llegada' in df.columns:
        df['fecha_llegada'] = pd.to_datetime(
            df['fecha_llegada'],
            errors='coerce',
            dayfirst=True
        )
    df = df.dropna(subset=['fecha_llegada'])
    df = df.sort_values('fecha_llegada').reset_index(drop=True)

    return df

if __name__ == '__main__':
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')

    lector_base1 = Lector(path_1)
    lector1 = lector_base1.comprueba_extension()
    lector_base2 = Lector(path_2)
    lector2 = lector_base2.comprueba_extension()
    lector_base3 = Lector(path_3)
    lector3 = lector_base3.comprueba_extension()

    df1 = preprocess_data(lector1.lee_archivo())
    df2 = preprocess_data(lector2.lee_archivo())
    df3 = preprocess_data(lector3.lee_archivo())

    df_total = pd.concat([df1, df2, df3], ignore_index=True)

    aeropuerto = Aeropuerto(df_total, slots=10, t_embarque_nat=30, t_embarque_internat=60)
    resultado = aeropuerto.asigna_slots()