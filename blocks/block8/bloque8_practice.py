class SolarLoadAnalyzer:
    def __init__(self):
        self.load_readings_watts: list[float] = []

    def capture_consumption_data(self) -> None:
        print("INYECCIÓN DE LECTURAS DE CONSUMO (APPEND)")
        readings_to_add = [150.5, 45.0, 1200.0, 85.3, 320.0]
        
        for reading in readings_to_add:
            self.load_readings_watts.append(reading)
            print(f"Lectura registrada: {reading:.1f} W")
            
        print(f"\nEstado actual de la lista (Desordenada): {self.load_readings_watts}")

    def execute_sorting(self) -> None:
        print("\nORDENAMIENTO SECUENCIAL (SORT)")

        self.load_readings_watts.sort()
        
        print(f"Lista organizada de menor a mayor consumo:")
        print(f"    {self.load_readings_watts}")

    def compute_statistical_aggregations(self) -> None:
        print("\nAGREGACIONES ESTADÍSTICAS (SUM, MAX, MIN)")
        
        total_demand: float = sum(self.load_readings_watts)
        
        peak_consumption: float = max(self.load_readings_watts)
        
        standby_consumption: float = min(self.load_readings_watts)

        print(f"Demanda Total Acumulada:  {total_demand:.2f} W")
        print(f"Pico de Consumo Máximo:  {peak_consumption:.2f} W")
        print(f"Consumo Mínimo Registrado: {standby_consumption:.2f} W")



def run_bloque8_practice():
    analyzer = SolarLoadAnalyzer()
    
    analyzer.capture_consumption_data()
    analyzer.execute_sorting()
    analyzer.compute_statistical_aggregations()