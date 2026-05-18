class SolarUnpackingManager:
    def __init__(self) -> None:
        self.sensor_metadata: tuple[int, str, str] = (101, "MPPT_INTERNAL", "AZIMUTH_SOUTH")

        self.amperage_stream: list[float] = [4.2, 5.1, 5.5, 5.8, 6.2, 4.0]

    def execute_fixed_unpacking(self) -> None:
        print("DESEMPAQUETADO 1: ESTRUCTURAS DE ASIGNACIÓN FIJA")
        print(f"Metadatos crudos del sensor central: {self.sensor_metadata}")

        sensor_id, sensor_type, alignment = self.sensor_metadata

        print("\nVariables mapeadas de forma independiente:")
        print(f"- ID del Hardware:   {sensor_id}")
        print(f"- Tipo de Sensor:    {sensor_type}")
        print(f"- Orientación Panel: {alignment}")

    def execute_advanced_asterisk_unpacking(self) -> None:
        print("\nDESEMPAQUETADO 2: SEGMENTACIÓN DINÁMICA (* RESTO)")
        print(f"Flujo total de lecturas de amperaje: {self.amperage_stream}")

        first_reading, *midday_readings, last_reading = self.amperage_stream

        print("\nExtracción quirúrgica con operador asterisco (*):")
        print(f"- Lectura Inicial (Amanecer):  {first_reading} A")
        print(f"- Lecturas Intermedias (Bloque Central): {midday_readings} A (Lista recolectada)")
        print(f"- Lectura Final (Atardecer):   {last_reading} A")


def run_bloque14_practice() -> None:
    manager = SolarUnpackingManager()

    manager.execute_fixed_unpacking()
    manager.execute_advanced_asterisk_unpacking()