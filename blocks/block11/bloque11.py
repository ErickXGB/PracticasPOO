from blocks.block11.bloque11_practice import run_bloque11_practice

class SetOperationsManager:
    def __init__(self):
        self.set_a: set = {1, 2, 3, 4}
        self.set_b: set = {3, 4, 5, 6}

    def calculate_union(self) -> None:
        result = self.set_a | self.set_b
        print(f"Unión (A | B):          {result}")

    def calculate_intersection(self) -> None:
        result = self.set_a & self.set_b
        print(f"Intersección (A & B):   {result}")

    def calculate_difference(self) -> None:
        diff_a_b = self.set_a - self.set_b
        diff_b_a = self.set_b - self.set_a
        print(f"Diferencia (A - B):     {diff_a_b}")
        print(f"Diferencia (B - A):     {diff_b_a}")

class DuplicateRemover:
    def __init__(self):
        self.original_list: list = [1, 2, 2, 3, 3, 3, 4]

    def remove_duplicates(self) -> list:
        print(f"Lista original con duplicados: {self.original_list}")
        unique_set = set(self.original_list)
        print(f"Paso intermedio (Convertido a set): {unique_set}")
 
        clean_list = list(unique_set)
        return clean_list
    
class AdvancedSetOperations:
    def __init__(self):
        self.set_a: set = {1, 2, 3, 4}
        self.set_b: set = {3, 4, 5, 6}

    def calculate_composite_operation(self) -> None:
        union_res = self.set_a | self.set_b 
        intersection_res = self.set_a & self.set_b  
        
        final_result = union_res - intersection_res 
        
        print(f"Conjunto A: {self.set_a}")
        print(f"Conjunto B: {self.set_b}\n")
        print(f"Paso 1: Unión (A | B)        = {union_res}")
        print(f"Paso 2: Intersección (A & B) = {intersection_res}")
        print(f"Paso 3: (A | B) - (A & B)    = {final_result}\n")
        
        print("EXPLICACIÓN DEL RESULTADO:")
        print("El resultado contiene los elementos {1, 2, 5, 6}.")
        print("Esto ocurre porque se eliminaron el 3 y el 4, que eran los números")
        print("repetidos (la intersección). A esto se le conoce matemáticamente")
        print("como la 'Diferencia Simétrica'.")


def run_exercise_1():
    manager = SetOperationsManager()
    
    print(f"Conjunto A: {manager.set_a}")
    print(f"Conjunto B: {manager.set_b}\n")

    manager.calculate_union()
    manager.calculate_intersection()
    manager.calculate_difference()

def run_exercise_2():
    print("Removiendo duplicados de una lista usando set:")
    remover = DuplicateRemover()
    
    result = remover.remove_duplicates()
    print(f"Lista final sin duplicados:       {result}")

def run_exercise_3():
    print("Prueba de operación de conjunto compuesto")
    
    manager = AdvancedSetOperations()
    manager.calculate_composite_operation()

options_bloque_11 = {
    "1": ("Operaciones con conjuntos", run_exercise_1),
    "2": ("Eliminar duplicados usando set", run_exercise_2),
    "3": ("Operación compuesta: (A | B) - (A & B)", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque11_practice),
}