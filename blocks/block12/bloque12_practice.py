from core.formatter import cprint as print, cinput as input
from core.input_validation_mixin import InputValidationMixin


class SolarExceptionAnalyzer(InputValidationMixin):
    def __init__(self):
        self.total_voltage: float = 240.0
        self.load_divisor: float = 0.0

    def execute_fault_calculation(self) -> None:
        print("PROCESADOR DE FLUJO ELÉCTRICO (MONITOREO DE EXCEPCIONES)")
        print(f"Voltaje Nominal Fijo del Barra: {self.total_voltage} V\n")

        # El try/except es intencional: demuestra manejo de excepciones.
        # input_text() solo garantiza que no se envíe una cadena vacía,
        # pero permite "0" y texto para que ValueError/ZeroDivisionError actúen.
        try:
            user_input = self.input_text(
                prompt="Ingrese el divisor de carga para el cálculo de amperaje: ",
                field_name="divisor"
            )
            self.load_divisor = float(user_input)
            calculated_amperage: float = self.total_voltage / self.load_divisor
            print(f"\nCálculo Exitoso: El amperaje resultante es {calculated_amperage:.2f} A")

        except ValueError:
            print("\nERROR DE EXCEPCIÓN: >>> ValueError <<<")
            print("Motivo: Se ingresaron letras o caracteres inválidos. Se requería un número decimal.")

        except ZeroDivisionError:
            print("\nERROR DE EXCEPCIÓN: >>> ZeroDivisionError <<<")
            print("Motivo: El divisor no puede ser 0. Físicamente representa un cortocircuito infinito.")

        finally:
            print("\n[BMS HARDWARE] Ejecutando bloque obligado (FINALLY)")
            print("Estado: Relevadores de seguridad auditados y estables.")


def run_bloque12_practice():
    analyzer = SolarExceptionAnalyzer()
    analyzer.execute_fault_calculation()