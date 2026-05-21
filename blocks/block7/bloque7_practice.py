from core.formatter import cprint as print, cinput as input

class SolarFunctionManager:
    def __init__(self):
        self.raw_generation_watts: float = 450.0
        self.cable_loss_watts: float = 18.5

    def print_diagnostic_welcome(self) -> None:
        print("MÓDULO ANÁLISIS DE EFICIENCIA Y CABLEADO")
        print("[SISTEMA] Iniciando cálculo de transporte de electrones...")

    def calculate_net_power(self, gross_power: float, loss: float) -> float:
        net_result: float = gross_power - loss
        return net_result

    def execute_analysis_workflow(self) -> None:
        self.print_diagnostic_welcome()

        final_power: float = self.calculate_net_power(
            self.raw_generation_watts, 
            self.cable_loss_watts
        )

        print(f"Potencia Bruta en Paneles: {self.raw_generation_watts:.2f} W")
        print(f"Pérdida por Caída en Cable: {self.cable_loss_watts:.2f} W")
        print(f"Potencia Neta en Inversor:  {final_power:.2f} W")

        efficiency_percentage: float = (final_power / self.raw_generation_watts) * 100
        print(f"Eficiencia del Transporte:  {efficiency_percentage:.1f}%")



def run_bloque7_practice():
    manager = SolarFunctionManager()

    manager.execute_analysis_workflow()