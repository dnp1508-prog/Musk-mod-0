from datetime import datetime

class Slot:
    def __init__(self, id=None, fecha_llegada=None, fecha_despegue=None, retraso=None, destino=None):
        self.id = id
        self.fecha_inicial = fecha_llegada
        self.fecha_final = fecha_despegue
        self.retraso = retraso
        self.destino = destino

    def asigna_vuelo(self, id, fecha_llegada, fecha_despegue, destino):
        vuelo = {}
        vuelo['id'] = id
        vuelo['fecha_llegada'] = fecha_llegada
        vuelo['fecha_despegue'] = fecha_despegue
        vuelo['destino'] = destino
        self.fecha_inicial = fecha_llegada
        self.fecha_final = fecha_despegue
        return vuelo

    def slot_esta_libre_fecha_determinada(self, fecha_inicio):
        if self.fecha_final is None:
            return True
        return fecha_inicio >= self.fecha_final