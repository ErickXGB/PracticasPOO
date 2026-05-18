import json
from blocks.block16.bloque16_practice import run_bloque16_practice

class FileHandler:
    def __init__(self):
        self.filename: str = "files/helloworld.txt"

    def write_to_file(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("Python")
        print(f"Archivo guardado correctamente '{self.filename}'")

    def read_from_file(self) -> str:
        print(f" Leyendo contenido desde '{self.filename}'...")
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content

class JsonConfigHandler:
    def __init__(self):
        self.filename: str = "files/data.json"
        self.source_data: dict = {"x": 10, "y": 20}

    def save_to_json(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.source_data, file, indent=4)
        print(f"Datos guardados correctamente en '{self.filename}'")

    def load_from_json(self) -> dict:
        print(f"Leyendo datos desde '{self.filename}'...")
        with open(self.filename, "r", encoding="utf-8") as file:
            parsed_dict = json.load(file)
        return parsed_dict
    
class UserStorageManager:
    def __init__(self):
        self.filename: str = "files/users.json"

        self.users_list: list = [
            {"username": "user_alpha", "role": "admin"},
            {"username": "user_beta", "role": "user"}
        ]

    def save_users(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.users_list, file, indent=4)
        print(f"Lista de usuarios guardada correctamente en: '{self.filename}'")

    def load_and_iterate_users(self) -> None:
        print(f"Cargando usuarios desde '{self.filename}'...")
        with open(self.filename, "r", encoding="utf-8") as file:
            loaded_users = json.load(file)
        
        print("\nIterando sobre usuarios sobrecargados")
        for user in loaded_users:
            name = user.get("username")
            role = user.get("role")
            print(f"Usuario: {name} | Rol: {role}")


def run_exercise_1():
    print("Prueba de manejo de archivos")
    handler = FileHandler()

    handler.write_to_file()
    file_content = handler.read_from_file()
    print(f"Resultado del contenido del archivo: '{file_content}'")

def run_exercise_2():
    print("Prueba de manejo de archivos JSON")
    handler = JsonConfigHandler()
    
    handler.save_to_json()
    loaded_data = handler.load_from_json()

    print(f"Resultado de los datos cargados: {loaded_data}")
    print(f"Tipo de dato verificado: {type(loaded_data)}")

def run_exercise_3():
    print("Prueba de manejo de archivos JSON con listas de diccionarios")

    manager = UserStorageManager()
    manager.save_users()
    manager.load_and_iterate_users()

options_bloque_16 = {
    "1": ("Ejercicio 1: Manejo básico de archivos", run_exercise_1),
    "2": ("Ejercicio 2: Datos en JSON", run_exercise_2),
    "3": ("Ejercicio 3: Listas en JSON", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque16_practice)
}