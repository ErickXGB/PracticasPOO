class SolarDataManager:
    def __init__(self):
        self.panel_count: int = 4                     
        self.efficiency_rate: float = 0.85             
        self.is_system_active: bool = True             
        self.station_name: str = "Estación Solar Sur"  


        self.voltage_readings: list[float] = [13.1, 13.2, 13.4, 13.3, 13.5]

    def display_basic_variables(self) -> None:
  
        print("TELEMETRÍA BASE DE LA ESTACIÓN SOLAR")
        print(f"Nombre de la Estación:   {self.station_name} (str)")
        print(f"Cantidad de Paneles:     {self.panel_count} unidades (int)")
        print(f"Eficiencia del Inversor: {self.efficiency_rate * 100}% (float)")
        print(f"Sistema Operativo:       {'SÍ' if self.is_system_active else 'NO'} (bool)")
        print(f"Lista de Voltajes:       {self.voltage_readings} (list)")
        print("-" * 55)

    def demonstrate_list_slicing(self) -> None:
        print("\nDEMONSTRACIÓN DE SEGMENTACIÓN DE LISTAS")

        print(f"Primera lectura (Índice 0):      {self.voltage_readings[0]} V")

        print(f"Última lectura (Índice -1):      {self.voltage_readings[-1]} V")

        sliced_range = self.voltage_readings[1:4]
        print(f"Segmentación solicitada [1:4]:   {sliced_range} V")
        print("-" * 55)

    def declare_internal_structures(self) -> None:
        print("\nESTRUCTURAS LOCALES DECLARADAS EN MÉTODO")
        
        alert_msg: str = "CRÍTICO: Sobrecarga térmica detectada"
        affected_zones: list[str] = ["Zona A", "Zona C"]
        hardware_log: dict[str, any] = {
            "componente": "Regulador MPPT",
            "temperatura_c": 42.5,
            "codigo_error": 104
        }
        
        print(f"Mensaje Local (str):   {alert_msg}")
        print(f"Zonas Afectadas (list): {affected_zones}")
        print(f"Log de Hardware (dict): {hardware_log}")


def run_bloque2_practice():
    manager = SolarDataManager()

    manager.display_basic_variables()
    manager.demonstrate_list_slicing()
    manager.declare_internal_structures()