import pandas as pd
import json
from pathlib import Path

class Lector:
    def __init__(self, path: str):
        self.path = path

    def comprueba_extension(self):
        ext = Path(self.path).suffix.lower()
        if ext == '.txt':
            return LectorTXT(self.path)
        elif ext == '.json':
            return LectorJSON(self.path)
        elif ext == '.csv':
            return LectorCSV(self.path)
        else:
            raise ValueError('La extensión no es válida')

    def lee_archivo(self):
        pass

    @staticmethod
    def convierte_dict_a_csv(data):
        df = pd.DataFrame(data)
        df.to_csv(index = False)
        return df


class LectorCSV(Lector):
    def __init__(self, path):
        super().__init__(path)

    def lee_archivo(self, datetime_columns=[]):
        return pd.read_csv(self.path, parse_dates=datetime_columns)

class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        with open(self.path, 'r', encoding='utf-8') as archivo:
            archivosjson = json.load(archivo)
        return pd.DataFrame(archivosjson)

class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        return pd.read_csv(self.path)