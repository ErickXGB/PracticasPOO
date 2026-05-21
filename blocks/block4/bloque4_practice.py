from core.formatter import cprint as print, cinput as input
from core.input_validation_mixin import InputValidationMixin


class SolarTelemetryInput(InputValidationMixin):
    def __init__(self):
        self.operator_name: str = ""
        self.panel_generation_watts: float = 0.0
        self.battery_count: int = 0

    def capture_telemetry_data(self) -> None:
        print("REGISTRO DE TELEMETRÍA SOLAR ACTIVA")

        self.operator_name = self.input_text_alpha(
            prompt="Ingrese el nombre del operador: ",
            field_name="nombre del operador"
        )

        self.panel_generation_watts = self.input_float_non_negative(
            prompt="Ingrese la generación actual de los paneles (Watts): "
        )

        self.battery_count = self.input_int_positive(
            prompt="Ingrese la cantidad de baterías LiFePO4 conectadas: "
        )

    def display_formatted_report(self) -> None:
        print("\nREPORTE DE TELEMETRÍA PROCESADO CON ÉXITO")
        print(f"Operador Responsable:    {self.operator_name.upper()}")
        print(f"Generación Fotovoltaica: {self.panel_generation_watts:.2f} W")
        print(f"Banco de Almacenamiento: {self.battery_count} unidades")
        average_watts_per_battery = self.panel_generation_watts / self.battery_count
        print(f"Carga Teórica Promedio:  {average_watts_per_battery:.2f} W por batería")


def run_bloque4_practice():
    telemetry_system = SolarTelemetryInput()
    telemetry_system.capture_telemetry_data()
    telemetry_system.display_formatted_report()