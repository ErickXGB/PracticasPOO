from blocks.block14.bloque14_practice import run_bloque14_practice

class AdvancedUnpacking:
    def __init__(self):
        self.numbers_tuple: tuple = (10, 20, 30, 40)
        print(f"Tupla original: {self.numbers_tuple}")

    def unpack_middle_elements(self) -> None:
        first, *middle, last = self.numbers_tuple
        
        print("Resultado del desempaquetado")
        print(f"Primer valor:  {first}")
        print(f"Valores del medio: {middle}")
        print(f"Último valor:   {last}")

class MathUnpacker:
    def multiply(self, a: int, b: int, c: int) -> int:
        result = a * b * c
        print(f"Multiplicando: {a} x {b} x {c}")
        return result

    def execute_unpacking(self) -> None:
        print("Prueba de desempaquetado con argumentos")
        
        arguments_list: list = [2, 3, 4]
        print(f"Lista de origen: {arguments_list}")
        final_result = self.multiply(*arguments_list)
        
        print(f"Resultado final:  {final_result}")

class DictionaryMerger:
    def __init__(self):
        self.dict_first: dict = {"alpha": 1, "bravo": 2}
        self.dict_second: dict = {"charlie": 3, "delta": 4}

    def merge_dictionaries(self) -> dict:
        print("Prueba de combinación de diccionarios con **")
        print(f"Diccionario 1: {self.dict_first}")
        print(f"Diccionario 2: {self.dict_second}\n")

        combined_dict = {**self.dict_first, **self.dict_second}
        return combined_dict
    

def run_exercise_1():
    manager = AdvancedUnpacking()
    manager.unpack_middle_elements()

def run_exercise_2():
    unpacker = MathUnpacker()
    unpacker.execute_unpacking()

def run_exercise_3():
    merger = DictionaryMerger()
    result = merger.merge_dictionaries()

    print(f"Diccionario combinado:   {result}")
    print(f"Diccionario 1:    {merger.dict_first} -> [Intacto]")
    print(f"Diccionario 2:    {merger.dict_second} -> [Intacto]")

options_bloque_14 = {
    "1": ("Ejercicio 1: Desempaquetado", run_exercise_1),
    "2": ("Ejercicio 2: Desempaquetado de Argumentos", run_exercise_2),
    "3": ("Ejercicio 3: Combinación de Diccionarios con **", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque14_practice),
}