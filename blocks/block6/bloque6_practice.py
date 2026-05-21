from core.formatter import cprint as print, cinput as input

class SolarCycleSimulator:
    def __init__(self):
        self.max_simulation_hours: int = 12
        self.connected_appliances: list[str] = ["Inversor", "Bomba de Agua", "Iluminación LED"]
        self.raw_efficiency_samples: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def execute_hourly_timer(self) -> None:
        print("SIMULACIÓN 1: CICLO CRONOLÓGICO DE GENERACIÓN")
        current_hour: int = 1

        while current_hour <= self.max_simulation_hours:
            simulated_watts = current_hour * 65.5
            print(f"Hora {current_hour:02d}: Eficiencia en ascenso -> Generando {simulated_watts:.1f} W")
            current_hour += 1

    def display_appliance_indexes(self) -> None:
        print("\nSIMULACIÓN 2: INVENTARIO DE CARGAS (FOR + ENUMERATE)")
        print("Dispositivos activos extrayendo energía del banco:")

        for position, appliance in enumerate(self.connected_appliances):
            print(f"  [Canal Relevador {position}] Equipo Conectado: {appliance}")

    def compute_optimized_squares(self) -> None:
        print("\nSIMULACIÓN 3: OPTIMIZACIÓN MATEMÁTICA (LIST COMPREHENSION)")
        print(f"Muestras de eficiencia crudas: {self.raw_efficiency_samples}")

        processed_squares: list[int] = [
            sample ** 2 for sample in self.raw_efficiency_samples if sample % 2 == 0
        ]

        print(f"Factores de potencia optimizados (Cuadrados de Pares): {processed_squares}")
 


def run_bloque6_practice():
    simulator = SolarCycleSimulator()
    
    simulator.execute_hourly_timer()
    simulator.display_appliance_indexes()
    simulator.compute_optimized_squares()