from core.formatter import cprint as print, cinput as input

class SolarTupleManager:
    def __init__(self):
        self.gps_coordinates: tuple[float, float] = (-2.1475, -79.9642)
        self.alert_history_codes: tuple[str, ...] = ("OK", "WARN_LOW_VOLT", "OK", "ERR_OVERHEAT", "WARN_LOW_VOLT", "OK")

    def display_immutable_coordinates(self) -> None:
        print("COMPONENTE DE GEOLOCALIZACIÓN (TUPLAS PROTEGIDAS)")
        print(f"Ubicación del Arreglo Solar Completo: {self.gps_coordinates}")

        print(f"Coordenada Latitud (Índice 0):  {self.gps_coordinates[0]}")
        print(f"Coordenada Longitud (Índice 1): {self.gps_coordinates[1]}")
        print("\n[Nota de Seguridad]: Esta estructura es inmutable; las coordenadas")
        print("no pueden alterarse dinámicamente en tiempo de ejecución, evitando hackeos de ruta.")

    def audit_system_logs(self) -> None:
        print("\nAUDITORÍA SÍNCROMA DE LOGS (.COUNT Y .INDEX)")
        print(f"Historial completo de alertas capturadas: {self.alert_history_codes}")

        target_warning = "WARN_LOW_VOLT"
        warning_count: int = self.alert_history_codes.count(target_warning)
        print(f"Análisis de Frecuencia: La alerta '{target_warning}' ocurrió {warning_count} veces hoy.")

        target_error = "ERR_OVERHEAT"
        try:
            error_index: int = self.alert_history_codes.index(target_error)
            print(f"Localización de Fallas: El primer '{target_error}' crítico se detectó en el Índice: {error_index}")
        except ValueError:
            print(f"El código '{target_error}' no se encuentra en los registros actuales.")



def run_bloque9_practice():
    manager = SolarTupleManager()

    manager.display_immutable_coordinates()
    manager.audit_system_logs()