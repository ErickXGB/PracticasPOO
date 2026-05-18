class BatteryGuardBMS:
    def __init__(self):
        self.cell_voltage: float = 0.0
        self.temperature_celsius: float = 0.0
        self.is_emergency_button_pressed: bool = False

    def capture_sensor_data(self) -> None:
        print("PANEL DE CONTROL - SISTEMA PROTECTOR BMS")

        while True:
            try:
                self.cell_voltage = float(input("Ingrese el voltaje de la celda LiFePO4 (2.0V - 4.0V): "))
                if self.cell_voltage < 0.0:
                    print("Error: El voltaje no puede ser un valor negativo.\n")
                    continue
                break
            except ValueError:
                print("Error: Tipo de dato inválido. Ingrese un número decimal.\n")

        while True:
            try:
                self.temperature_celsius = float(input("Ingrese la temperatura actual del sensor (°C): "))
                break
            except ValueError:
                print(" Error: Ingrese un valor numérico válido para la temperatura.\n")

        while True:
            choice = input("¿Está activado el botón de parada de emergencia manual? (s/n): ").strip().lower()
            if choice == 's':
                self.is_emergency_button_pressed = True
                break
            elif choice == 'n':
                self.is_emergency_button_pressed = False
                break
            print("Error: Responda únicamente con 's' para Sí o 'n' para No.\n")

    def evaluate_battery_state(self) -> None:
        print("\nDIAGNÓSTICO DEL ESTADO DE CARGA")
        print(f"Voltaje Evaluado: {self.cell_voltage} V")

        if self.cell_voltage >= 3.65:
            print("ESTADO: [!] SOBRECARGA DETECTADA (Peligro térmico)")
        elif self.cell_voltage >= 3.40:
            print("ESTADO: [+] CARGA COMPLETA (Modo Flotación)")
        elif self.cell_voltage >= 3.10:
            print("ESTADO: [*] OPERACIÓN ÓPTIMA (Rango Nominal)")
        elif self.cell_voltage >= 2.80:
            print("ESTADO: [-] BAJA TENSIÓN (Se requiere recarga)")
        else:
            print("ESTADO: [CRÍTICO] DESCARGA PROFUNDA (Corte inminente)")

    def audit_safety_disconnection(self) -> None:
        print("\nAUDITORÍA DE SEGURIDAD INTERNA (CORTACIRCUITO)")

        voltage_out_of_bounds = (self.cell_voltage >= 3.65 or self.cell_voltage <= 2.50)
        extreme_heat = (self.temperature_celsius > 55.0)
        
        should_disconnect = self.is_emergency_button_pressed or voltage_out_of_bounds or extreme_heat

        print(f"Parada de Emergencia Activa: {self.is_emergency_button_pressed}")
        print(f"Voltaje Fuera de Rango:      {voltage_out_of_bounds}")
        print(f"Alerta por Alta Temperatura: {extreme_heat}")
        
        if should_disconnect:
            print("[ALERTA CRÍTICA] RELEVADOR BMS: >>> DESCONECTADO <<<")
            print("Motivo: Protección perimetral de hardware activada por lógica booleana.")
        else:
            print("[NORMAL] RELEVADOR BMS: >>> CONECTADO <<<")
            print("Motivo: Todos los parámetros operan dentro de los márgenes seguros.")



def run_bloque5_practice():
    bms = BatteryGuardBMS()

    bms.capture_sensor_data()
    bms.evaluate_battery_state()
    bms.audit_safety_disconnection()