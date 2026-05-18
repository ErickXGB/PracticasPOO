from typing import Callable, Any

def log_inverter_action(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[DECORADOR] >>> Iniciando auditoría segura sobre: '{func.__name__}'")
        print("Estabilizando canales de datos fotovoltaicos...")

        result = func(*args, **kwargs)

        print(f"[DECORADOR] <<< Proceso '{func.__name__}' finalizado con éxito.")
        print("Cerrando túnel de telemetría segura.\n")
        return result
        
    return wrapper


class SolarOperationManager:
    def __init__(self) -> None:
        self.grid_frequency_hz: float = 60.0
        self.is_synchronized: bool = False

    @log_inverter_action
    def connect_to_external_grid(self) -> None:
        print("COMPONENTE DE HARDWARE: SINCRONIZACIÓN DE RED")
        print(f"Analizando frecuencia de acoplamiento: {self.grid_frequency_hz} Hz")
        self.is_synchronized = True
        print(f"Resultado Interno: Estación sincronizada con la red externa.")

    @log_inverter_action
    def purge_thermal_overload(self) -> None:

        print("COMPONENTE DE HARDWARE: PURGA TÉRMICA INVERTER")
        print("Activando extractores auxiliares a máxima revolución...")
        print("Disipando calor acumulado en los MOSFETs de potencia.")


def run_bloque13_practice() -> None:
    manager = SolarOperationManager()
    
    manager.connect_to_external_grid()
    manager.purge_thermal_overload()