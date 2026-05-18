from functools import reduce
from blocks.block15.bloque15_practice import run_bloque15_practice

class MapNamedTransformer:
    def __init__(self):
        self.numbers_list: list = [2, 4, 6]

    def _add_one(self, value: int) -> int:
        return value + 1

    def increment_elements_with_def(self) -> list:
        print(f"Lista original: {self.numbers_list}")

        result_iterator = map(self._add_one, self.numbers_list)
        transformed_list = list(result_iterator)
        
        return transformed_list

class ListFilter:
    def __init__(self):
        self.numbers_list: list = [1, 2, 3, 4, 5]

    def _is_greater_than_three(self, value: int) -> bool:
        return value > 3

    def get_filtered_elements(self) -> list:
        print(f"Lista original antes del filtro: {self.numbers_list}")
        
        result_iterator = filter(self._is_greater_than_three, self.numbers_list)
        filtered_list = list(result_iterator)
        return filtered_list
    
class ListReducer:
    def __init__(self):
        self.numbers_list: list = [1, 2, 3, 4]

    def _multiply_accumulators(self, accumulator: int, current_value: int) -> int:
        return accumulator * current_value

    def get_reduced_product(self) -> int:
        print(f"Lista original a multiplicar: {self.numbers_list}")
        total_product = reduce(self._multiply_accumulators, self.numbers_list)
        
        return total_product


def run_exercise_1():
    print("Prueba de función de orden superior con map()")
    transformer = MapNamedTransformer()

    result = transformer.increment_elements_with_def()
    print(f"Lista transformada ([3, 5, 7]): {result}")

def run_exercise_2():
    print("Prueba de función de orden superior con filter()")
    cleaner = ListFilter()
    
    result = cleaner.get_filtered_elements()
    print(f"Lista filtrada resultante:   {result}")
    
def run_exercise_3():
    print("Prueba de función de orden superior con reduce()")
    reducer = ListReducer()

    result = reducer.get_reduced_product()
    print(f"Resultado acumulado final: {result}")

options_bloque_15 = {
    "1": ("Ejercicio 1: Función de Orden Superior con map()", run_exercise_1),
    "2": ("Ejercicio 2: Función de Orden Superior con filter()", run_exercise_2),
    "3": ("Ejercicio 3: Función de Orden Superior con reduce()", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque15_practice),
}