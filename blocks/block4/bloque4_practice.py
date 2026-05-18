class SolarTelemetryInput:
    def __init__(self):
        self.operator_name: str = ""
        self.panel_generation_watts: float = 0.0
        self.battery_count: int = 0

    def capture_telemetry_data(self) -> None:
        print("REGISTRO DE TELEMETRÍA SOLAR ACTIVA")
        while True:
            self.operator_name = input("Ingrese el nombre del operador: ").strip()
            if self.operator_name:
                break
            print("Error: El nombre del operador no puede quedar vacío.\n")

        while True:
            try:
                user_input = input("Ingrese la generación actual de los paneles (Watts): ")
                self.panel_generation_watts = float(user_input)

                if self.panel_generation_watts < 0.0:
                    print("Error: La potencia de generación no puede ser un valor negativo.\n")
                    continue
                break  
            except ValueError:
                print("Error: Entrada inválida. Debe ingresar un número decimal o entero.\n")

        while True:
            try:
                user_input = input("Ingrese la cantidad de baterías LiFePO4 conectadas: ")
                self.battery_count = int(user_input)
                
                if self.battery_count <= 0:
                    print(" Error: Debe haber al menos 1 batería en el banco logístico.\n")
                    continue
                break 
            except ValueError:
                print("Error: Entrada inválida. Debe ingresar un número entero.\n")

    def display_formatted_report(self) -> None:
        print("\nREPORTE DE TELEMETRÍA PROCESADO CON ÉXITO ")
        print(f"Operador Responsable:  {self.operator_name.upper()}")
        print(f"Generación Fotovoltaica: {self.panel_generation_watts:.2f} W")
        print(f"Banco de Almacenamiento: {self.battery_count} unidades")

        average_watts_per_battery = self.panel_generation_watts / self.battery_count
        print(f"Carga Teórica Promedio:  {average_watts_per_battery:.2f} W por batería")


def run_bloque4_practice():
    telemetry_system = SolarTelemetryInput()
    
    telemetry_system.capture_telemetry_data()
    telemetry_system.display_formatted_report()