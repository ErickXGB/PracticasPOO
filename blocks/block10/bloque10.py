from core.formatter import cprint as print, cinput as input
from blocks.block10.bloque10_practice import run_bloque10_practice

class DictionaryManager:
    def __init__(self):
        self.person_dict: dict = {
            "name": "Anthony",
            "age": 20,
            "city": "Guayaquil"
        }

    def access_with_brackets(self) -> None:
        print("Accediendo con corchetes []")
        name_val = self.person_dict["name"]
        age_val = self.person_dict["age"]
        print(f"Nombre: {name_val} | Edad: {age_val}")

    def access_with_get(self) -> None:
        print("\nAccediendo con .get()")
        city_val = self.person_dict.get("city")
        
        country_val = self.person_dict.get("country", "Not Found")
        print(f"Ciudad: {city_val}")
        print(f"País (Inexistente): {country_val}")


    def print_all_items(self) -> None:
        print("Iterando sobre el diccionario con .items()")
        
        for key, value in self.person_dict.items():
            print(f"Clave: {key} -> Valor: {value}")

class DictionaryCopyManager:
    def __init__(self):
        self.original_data: dict = {"a": 1, "b": 10}

    def demonstrate_reference_error(self) -> None:
        print("Caso 1: Asignación directa (copia = datos)")
        self.original_data = {"a": 1, "b": 10}
        print(f"Diccionario original: {self.original_data}")

        wrong_copy = self.original_data
        wrong_copy["b"] = 2
        
        print(f"Copia incorrecta (b=2):  {wrong_copy}")
        print(f"Diccionario original después:  {self.original_data} -> [¡También cambió!]")

    def demonstrate_correct_copy(self) -> None:
        print("\nCaso 2: Copia segura con .copy()")
        self.original_data = {"a": 1, "b": 10}
        print(f"Diccionario original antes: {self.original_data}")
        
        safe_copy = self.original_data.copy()
        safe_copy["b"] = 2
        
        print(f"Copia segura (b=2):   {safe_copy}")
        print(f"Diccionario original después:  {self.original_data} -> [Se mantuvo intacto]")


def run_exercise_1():
    manager = DictionaryManager()
    manager.access_with_brackets()
    manager.access_with_get()

def run_exercise_2():
    iterator = DictionaryManager()
    iterator.print_all_items()

def run_exercise_3():
    manager = DictionaryCopyManager()
    manager.demonstrate_reference_error()
    manager.demonstrate_correct_copy()

options_bloque_10 = {
    "1": ("Crea un dict. Accede con [] y con get().", run_exercise_1),
    "2": ("Itera sobre un diccionario.", run_exercise_2), 
    "3": ("Diferencia entre asignación directa y copia con .copy()", run_exercise_3), 
    "4": ("Ejercicio de práctica", run_bloque10_practice)
}
