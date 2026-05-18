import json

class JSONExportMixin:
    def export_to_json_string(self) -> str:
        return json.dumps(vars(self), indent=4, ensure_ascii=False)


class SafetyAuditMixin:
    def audit_operational_thresholds(self, current_voltage: float, limit: float) -> bool:

        if current_voltage > limit:
            print(f"[AUDITORÍA] ¡PELIGRO! Voltaje actual ({current_voltage}V) excede el límite crítico ({limit}V).")
            return False
        print(f"[AUDITORÍA] Parámetros eléctricos validados. Operando dentro de márgenes seguros.")
        return True


class AdvancedSolarArray(JSONExportMixin, SafetyAuditMixin):
    def __init__(self, string_id: str, operating_voltage: float):
        self.string_id: str = string_id
        self.operating_voltage: float = operating_voltage
        self.critical_voltage_limit: float = 150.0  

    def run_hardware_diagnostics(self) -> None:
        print("ESTACIÓN SOLAR AVANZADA (HERENCIA MÚLTIPLE CON MIXINS)")
        print(f"Monitoreando Arreglo: {self.string_id}")
        print(f"Voltaje en Barra:     {self.operating_voltage} V\n")

        is_safe: bool = self.audit_operational_thresholds(
            current_voltage=self.operating_voltage, 
            limit=self.critical_voltage_limit
        )

        print("\nSerializando ficha de telemetría para transmisión remota:")
        serialized_payload: str = self.export_to_json_string()
        print(serialized_payload)
        print("-" * 72)


def run_bloque17_practice() -> None:
    solar_field = AdvancedSolarArray(string_id="SOLAR-STRING-OMEGA", operating_voltage=132.5)

    solar_field.run_hardware_diagnostics()