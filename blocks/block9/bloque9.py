from core.formatter import cprint as print, cinput as input
from blocks.block9.bloque9_practice import run_bloque9_practice

class TupleContainer:
    def __init__(self):
        self.data_tuple: tuple = ("Alpha", "Bravo", "Charlie", "Delta")

    def read_element(self, index: int) -> str:
        if not (0 <= index < len(self.data_tuple)):
            raise IndexError("Índice fuera de rango.")
        return self.data_tuple[index]

    def try_modification(self, index: int, new_value: str) -> None:
        print(f"Intentando cambiar el elemento en el índice {index} a '{new_value}'...")
        try:
            self.data_tuple[index] = new_value
        except TypeError as e:
            print(f"Error esperado: {e}")
            print("Explicación: Las tuplas son inmutables y no se pueden modificar después de su creación.")

class UnpackingManager:
    def __init__(self):
        self.values_tuple: tuple = (100, 200, 300, 400)

    def unpack_values(self) -> None:
        a, b, *rest = self.values_tuple
        
        print(self.values_tuple)
        print("Resultado del desempaquetado:")
        print(f"Valor de a: {a}")
        print(f"Valor de b: {b}")
        print(f"Los demás valores: {rest}")

class CoordinateManager:
    def __init__(self):
        self.coordinates_list: list = [
            (10, 20),
            (30, 40),
            (50, 60)
        ]

    def display_coordinates(self) -> None:
        print("Recorrer las coordenadas (tuplas) en la lista:")
        for x, y in self.coordinates_list:
            print(f"Coordenada -> X: {x} | Y: {y}")

def run_exercise_1():
    print("Probando las propiedades de las tuplas (indexación e inmutabilidad)")

    container = TupleContainer()
    print(f"Contenido actual de la tupla: {container.data_tuple}")
    
    val = container.read_element(1)
    print(f"Elemento leído en el índice 1: {val}")

    print()
    container.try_modification(1, "Omega")

def run_exercise_2():
    manager = UnpackingManager()
    manager.unpack_values()

def run_exercise_3():
    manager = CoordinateManager()
    manager.display_coordinates()

options_bloque_9 = {
    "1": ("Crea una tupla con 4 elementos.", run_exercise_1),
    "2": ("Desempaqueta una tupla en variables individuales.", run_exercise_2),
    "3": ("Recorre una lista de coordenadas (tuplas).", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque9_practice),
}