import pandas as pd
from datetime import timedelta
from entities.slot import Slot


class Aeropuerto:
    def __init__(
        self,
        vuelos: pd.DataFrame,
        slots: int,
        t_embarque_nat: int,
        t_embarque_internat: int
    ):
        self.df = vuelos.copy()

        self.n_slots = slots
        self.t_embarque_nat = t_embarque_nat
        self.t_embarque_internat = t_embarque_internat

        self.slots = [Slot(i) for i in range(self.n_slots)]

        self.df['slot_asignado'] = pd.NA
        self.df['fecha_despegue_calculada'] = pd.NaT

    def calcula_fecha_despegue(self, vuelo) -> pd.Timestamp:
        if vuelo['tipo_vuelo'] == 'NACIONAL':
            minutos = self.t_embarque_nat
        else:
            minutos = self.t_embarque_internat

        return vuelo['fecha_llegada'] + timedelta(minutes=minutos)

    def encuentra_slot(self, fecha_llegada):
        for slot in self.slots:
            if slot.slot_esta_libre_fecha_determinada(fecha_llegada):
                return slot
        return None

    def asigna_slots(self) -> pd.DataFrame:
        for idx, vuelo in self.df.iterrows():
            fecha_despegue = self.calcula_fecha_despegue(vuelo)
            slot = self.encuentra_slot(vuelo['fecha_llegada'])

            if slot is None:
                continue

            slot.asigna_vuelo(
                vuelo['id'],
                vuelo['fecha_llegada'],
                fecha_despegue,
                vuelo['destino']
            )

            self.df.at[idx, 'slot_asignado'] = slot.id
            self.df.at[idx, 'fecha_despegue_calculada'] = fecha_despegue

            print(self.mostrar_resultados(vuelo, slot, fecha_despegue))

        return self.df

    def mostrar_resultados(self, vuelo, slot, fecha_despegue) -> str:
        return (
            f"El vuelo {vuelo['id']} con fecha de llegada {vuelo['fecha_llegada']} "
            f"y de despegue {fecha_despegue} ha sido asignado al slot {slot.id}"
        )
