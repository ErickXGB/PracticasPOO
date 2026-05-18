from blocks.block8.bloque8_practice import run_bloque8_practice

class ListManager:
    def __init__(self):
        self.elements_list: list = []

    def populate_and_sort_list(self) -> None:
        print("Ejercicio 1: Manipulación de Listas (append y sort)")

        self.elements_list.append(42)
        self.elements_list.append(15)
        self.elements_list.append(8)
        print(f"Lista después de usar append(): {self.elements_list}")

        self.elements_list.sort()

        print(f"Lista ordenada final:            {self.elements_list}")

class ListStatistics:
    def __init__(self):
        self.numbers_list: list = [5, 3, 8, 1, 9, 3]

    def compute_metrics(self) -> None:
        print("Ejercicio 2: Métricas de Listas (sum, max, min)")
        print(f"Lista de análisis: {self.numbers_list}\n")

        total_sum: int = sum(self.numbers_list)
        maximum_value: int = max(self.numbers_list)
        minimum_value: int = min(self.numbers_list)

        print(f"-Suma total:     {total_sum}")
        print(f"-Valor máximo:   {maximum_value}")
        print(f"-Valor mínimo:   {minimum_value}")

class ReferenceAssignmentDemo:
    def __init__(self):
        self.original_list: list = [1, 2, 3]

    def demonstrate_reference_behavior(self) -> None:
        print("Ejercicio 3: Asignación por Referencia vs Copia")
        print(f"Lista original al inicio:           {self.original_list}")
        print(f"Dirección de memoria original (id):  {id(self.original_list)}\n")

        assigned_reference = self.original_list
        print(f"Referencia asignada (copia = lista): {assigned_reference}")
        print(f"Dirección de memoria de la 'copia':  {id(assigned_reference)}\n")

        print("Ejecutando: copia.append(4)...")
        assigned_reference.append(4)

        print(f"\nResultado final de 'copia':          {assigned_reference}")
        print(f"Resultado final de 'lista original': {self.original_list}")
        
        print("\n¿Por qué pasa esto?")
        print("Porque el operador '=' solo copia el puntero o dirección de memoria.")
        print("Ambas variables son nombres distintos para el mismo objeto físico en la RAM.")


def run_exercise_1():

    manager = ListManager()
    manager.populate_and_sort_list()

def run_exercise_2():
    statistics = ListStatistics()
    statistics.compute_metrics()

def run_exercise_3():
    demo = ReferenceAssignmentDemo()
    demo.demonstrate_reference_behavior()

options_bloque_8 = {
    "1": ("Ejercicio 1: Manipulación de Listas (append y sort)", run_exercise_1),
    "2": ("Ejercicio 2: Suma, máximo, mínimo de una lista", run_exercise_2),
    "3": ("Ejercicio 3: Asignación por referencia vs copia", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque8_practice),
}