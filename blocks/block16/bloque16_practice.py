from core.formatter import cprint as print, cinput as input
import os
import json

class SolarJsonManager:
    def __init__(self) -> None:
        self.target_directory: str = "files"
        self.file_path: str = os.path.join(self.target_directory, "telemetria.json")

        self.system_payload: dict[str, any] = {
            "estacion_id": "SOLAR-CENTRAL-01",
            "paneles_watts": 800,
            "bateria_quimica": "LiFePO4",
            "lecturas_voltaje": [13.2, 13.4, 13.3],
            "bms_seguro": True
        }

    def save_telemetry_to_json(self) -> None:
        print("COMPONENTE DE PERSISTENCIA: ESCRITURA JSON")

        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
            print(f"Carpeta '{self.target_directory}/' creada físicamente en el disco duro.")
        
        try:
            with open(self.file_path, "w", encoding="utf-8") as file_object:
                json.dump(self.system_payload, file_object, indent=4, ensure_ascii=False)
            
            print(f"ÉXITO: Datos serializados correctamente en: '{self.file_path}'")
        except Exception as error:
            print(f"Error crítico al guardar el archivo: {error}")
            

    def load_telemetry_from_json(self) -> None:
        print("\nCOMPONENTE DE PERSISTENCIA: LECTURA JSON")

        if not os.path.exists(self.file_path):
            print(f"Error: El archivo '{self.file_path}' no existe en el almacenamiento.")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file_object:
                loaded_data: dict[str, any] = json.load(file_object)
            
            print(f"Archivo físico leído y reconstruído en memoria RAM con éxito:")
            print(f"- ID de Planta:   {loaded_data['estacion_id']}")
            print(f"- Celdas Conectadas: {loaded_data['bateria_quimica']}")
            print(f"- Historial Recuperado: {loaded_data['lecturas_voltaje']} V")
            print(f"\n[Estructura Cruda Recuperada]:\n{json.dumps(loaded_data, indent=2)}")
            
        except Exception as error:
            print(f"Error crítico al parsear el archivo JSON: {error}")


def run_bloque16_practice() -> None:
    manager = SolarJsonManager()

    manager.save_telemetry_to_json()
    manager.load_telemetry_from_json()