class SolarInverterRegistry:
    def __init__(self):
        self.inverter_metrics: dict[str, any] = {
            "device_model": "Must Solar PV1800",
            "input_voltage_v": 120.4,
            "output_frequency_hz": 60.0,
            "is_grid_connected": False
        }

    def modify_and_expand_registry(self) -> None:
        print("MODIFICACIÓN Y EXPANSIÓN DE DICCIONARIOS")
        print(f"Estado inicial del diccionario: {self.inverter_metrics}\n")

        self.inverter_metrics["input_voltage_v"] = 138.2
        print("Llave modificada: 'input_voltage_v' ha sido actualizada a 138.2 V")

        self.inverter_metrics["temperature_celsius"] = 38.5
        print("Nueva llave inyectada: 'temperature_celsius' agregada con valor 38.5 °C")

    def generate_telemetry_reports(self) -> None:
        print("\nREPORTES DETALLADOS DE TELEMETRÍA (MÉTODOS NATIVOS)")

        print("Listado Exhaustivo de Parámetros Auditados (.keys()):")
        for parameter_name in self.inverter_metrics.keys():
            print(f"Parámetro: {parameter_name}")

        print("\nListado de Lecturas Crudas Capturadas (.values()):")
        for telemetry_value in self.inverter_metrics.values():
            print(f"Valor Registrado: {telemetry_value}")

        print("\nDespliegue de Ficha Técnica Completa Formateada (.items()):")

        for key, value in self.inverter_metrics.items():
            print(f"||  {key.replace('_', ' ').title().ljust(22)} : {value}")



def run_bloque10_practice():
    registry = SolarInverterRegistry()
    
    registry.modify_and_expand_registry()
    registry.generate_telemetry_reports()