from blocks.block6.bloque6_practice import run_bloque6_practice

class SequentialCounter:
    def __init__(self):
        self.max_limit: int = 10

    def execute_counter(self) -> None:
        print(f"Ejercicio 1: Contador Secuencial (1 - {self.max_limit})")
        current_counter: int = 1

        while current_counter <= self.max_limit:
            print(current_counter)
            current_counter += 1


class FruitInventory:
    def __init__(self):
        self.fruits: list = ["pera", "manzana", "banana", "uva"]

    def display_indexed_fruits(self) -> None:
        print("Ejercicio 2: Lista de Frutas Indexada")
        
        for index, fruit in enumerate(self.fruits):
            print(f"Índice {index}: {fruit}")


class EvenSquaresGenerator:
    def __init__(self):
        self.start_range: int = 1
        self.end_range: int = 11 

    def generate_and_print_squares(self) -> None:
        print("Ejercicio 3: Cuadrados de Números Pares")
        
        even_squares: list = [
            x**2 for x in range(self.start_range, self.end_range) if x % 2 == 0
        ]
        
        print(f"Resultado (1-10): {even_squares}")


def run_exercise_1():
    counter_service = SequentialCounter()
    counter_service.execute_counter()

def run_exercise_2():
    inventory = FruitInventory()
    inventory.display_indexed_fruits()

def run_exercise_3():
    generator = EvenSquaresGenerator()
    generator.generate_and_print_squares()


options_bloque_6 = {
    "1": ("Ejercicio 1: Contador", run_exercise_1),
    "2": ("Ejercicio 2: Lista de frutas", run_exercise_2),
    "3": ("Ejercicio 3: Cuadrados de números pares", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque6_practice),
}