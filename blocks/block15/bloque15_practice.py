from core.formatter import cprint as print, cinput as input

class SolarFunctionalProcessor:
    def __init__(self) -> None:
        self.raw_generation_pool: list[float] = [450.0, 120.5, 520.0, 95.0, 310.8, 15.0]

    def execute_performance_filtering(self) -> None:
        print("PROCESAMIENTO FUNCIONAL 1: FILTRADO (FILTER + LAMBDA)")
        print(f"Pool completo de generación: {self.raw_generation_pool} W")

        critical_panels_iterator = filter(
            lambda watts: watts < 150.0, 
            self.raw_generation_pool
        )

        critical_panels: list[float] = list(critical_panels_iterator)

        print("\nDiagnóstico perimetral ejecutado:")
        print(f"- Paneles con anomalía o baja radiación (< 150W): {critical_panels} W")

    def execute_unit_mapping(self) -> None:
        print("\nPROCESAMIENTO FUNCIONAL 2: TRANSFORMACIÓN (MAP + LAMBDA)")
        print(f"Muestras originales en escala de Watts: {self.raw_generation_pool}")

        kilowatts_iterator = map(
            lambda watts: watts / 1000.0, 
            self.raw_generation_pool
        )
        
        converted_kilowatts: list[float] = list(kilowatts_iterator)

        print("\nConversión métrica de escala completada:")
        print("- Listado transformado a Kilowatios (kW):")
        formatted_kw = [f"{kw:.3f} kW" for kw in converted_kilowatts]
        print(f"    {formatted_kw}")



def run_bloque15_practice() -> None:
    processor = SolarFunctionalProcessor()
    
    processor.execute_performance_filtering()
    processor.execute_unit_mapping()