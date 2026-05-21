from core.formatter import cprint as print, cinput as input

class SolarArrayPractice:
    def __init__(self, array_id: str, panel_count: int, total_watts: int):
        self.array_id: str = array_id            
        self.panel_count: int = panel_count      
        self.max_power_watts: int = total_watts  
        self.is_active: bool = True              


class SolarStationMonitor:
    def __init__(self):
        self.main_array = SolarArrayPractice(
            array_id="ARRAY-ZONE-A",
            panel_count=4,
            total_watts=800
        )

    def display_blueprint_details(self) -> None:
        print("Sistema de Monitoreo de Estación Solar")
        print(f"Nombre de la clase:   {self.main_array.__class__.__name__}")
        print(f"ID de la estructura: {self.main_array.array_id}")
        print(f"Conteo de paneles:  {self.main_array.panel_count} unidades")
        print(f"Potencia pico:   {self.main_array.max_power_watts}W")
        print(f"Estado del enlace:  {'ACTIVO' if self.main_array.is_active else 'DESCONECTADO'}")



def run_bloque0_practice():

    monitor = SolarStationMonitor()
    monitor.display_blueprint_details()