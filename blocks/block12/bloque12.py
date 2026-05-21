from core.formatter import cprint as print, cinput as input
from blocks.block12.bloque12_practice import run_bloque12_practice

class InputValidator:
    def convert_input_to_int(self) -> None:
        print("Prueba de manejo de excepciones con ValueError")
        user_input = input("Ingrese un número entero: ")
        
        try:
            number = int(user_input)
            print(f"Éxito! Su número es: {number}")
            
        except ValueError as error:
            print(f"\n[!] ValueError Capturado: {error}")
            print("Explicación: No haz ingresaddo un número (entero) valido.")

class ListBoundsValidator:
    def __init__(self):
        self.my_list: list = ["Alpha", "Bravo", "Charlie"]

    def trigger_index_error(self) -> None:
        print("Prueba de manejo de excepciones con IndexError")
        print(f"Contenido de la lista: {self.my_list} (Tamaño: {len(self.my_list)})")
        print("Intentando acceder de forma directa al índice 5...")
        
        try:
            broken_access = self.my_list[5]
            print(f"Elemento obtenido: {broken_access}")
        except IndexError as error:
            print(f"\n[!] IndexError Capturado: {error}")
            print("Explicación: Intentaste acceder a una posición fuera de los límites de la lista.")

class DivisionProcessor:
    def execute_safe_division(self) -> None:
        print("Prueba de manejo de excepciones con ZeroDivisionError")
        
        try:
            numerator_input = input("Ingrese el numerador: ")
            denominator_input = input("Ingrese el denominador: ")
            
            numerator = int(numerator_input)
            denominator = int(denominator_input)
            
            result = numerator / denominator
            print(f"¡Éxito! El resultado de la división es: {result}")  
        except ValueError as error:
            print(f"\n[!] ValueError capturado: {error}")
            print("Explicación: Uno o ambos valores ingresados no son números enteros válidos.")
        except ZeroDivisionError as error:
            print(f"\n[!] ZeroDivisionError capturado: {error}")
            print("Explicación: La división por cero no está permitida en matemáticas.")


def run_exercise_1():
    validator = InputValidator()
    validator.convert_input_to_int()

def run_exercise_2():
    validator = ListBoundsValidator()
    validator.trigger_index_error()    

def run_exercise_3():
    processor = DivisionProcessor()
    processor.execute_safe_division()

options_bloque_12 = {
    "1": ("Manejo de excepciones: ValueError", run_exercise_1),
    "2": ("Manejo de excepciones: IndexError", run_exercise_2),
    "3": ("Manejo de excepciones: ZeroDivisionError", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque12_practice),
}