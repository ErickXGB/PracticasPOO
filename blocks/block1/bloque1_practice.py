class ChargeControllerPractice:
    def __init__(self, model_name: str, max_amperage: int, system_voltage: int):
        self.model_name: str = model_name              
        self.max_amperage: int = max_amperage          
        self.system_voltage: int = system_voltage     
        self.is_charging: bool = False                 
        self.panel_input_watts: float = 0.0           
        
        self.power_history: list[float] = []

    @classmethod
    def create_lithium_preset(cls, model_name: str, max_amperage: int):
        print("Valores optimizados para baterías de Litio (LiFePO4)...")
        return cls(model_name=model_name, max_amperage=max_amperage, system_voltage=12)

    def log_power_reading(self, watts: float) -> None:

        self.panel_input_watts = watts
        self.power_history.append(watts)

    def display_controller_data(self) -> None:
        print("MONITOR DE REGULADOR DE CARGA SOLAR")
        print(f"Modelo del Equipo:     {self.model_name}")
        print(f"Amperaje Máximo:       {self.max_amperage}A")
        print(f"Voltaje del Banco:     {self.system_voltage}V")
        print(f"Estado de Carga:       {'CARGANDO' if self.is_charging else 'ESPERANDO RADIACIÓN'}")
        print(f"Potencia Actual:       {self.panel_input_watts}W")
        print(f"Historial de Lecturas: {self.power_history} (Watts)")



def run_bloque1_practice():
    controller_unit = ChargeControllerPractice.create_lithium_preset(
        model_name="SmartSolar MPPT 100/30", 
        max_amperage=30
    )
    
    controller_unit.is_charging = True
    
    controller_unit.log_power_reading(120.5)
    controller_unit.log_power_reading(245.0)
    controller_unit.log_power_reading(345.5)

    print()
    controller_unit.display_controller_data()