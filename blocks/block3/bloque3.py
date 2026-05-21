from core.formatter import cprint as print, cinput as input
from blocks.block3.bloque3_practice import run_bloque3_practice

class ArithmeticCalculator:
    def __init__(self):
        self.value_a: int = 20
        self.value_b: int = 4

    def execute_operations(self) -> None:
        print("Operadores Aritméticos")
        print(f"Suma:            {self.value_a} + {self.value_b} = {self.value_a + self.value_b}")
        print(f"Resta:           {self.value_a} - {self.value_b} = {self.value_a - self.value_b}")
        print(f"Multiplicación:  {self.value_a} * {self.value_b} = {self.value_a * self.value_b}")
        print(f"División:        {self.value_a} / {self.value_b} = {self.value_a / self.value_b}")
        print(f"División entera: {self.value_a} // {self.value_b} = {self.value_a // self.value_b}")
        print(f"Módulo (residuo):{self.value_a} % {self.value_b} = {self.value_a % self.value_b}")
        print(f"Potencia:        {self.value_a} ** {self.value_b} = {self.value_a ** self.value_b}")


class IdentityComparator:
    def __init__(self):
        self.list_a: list = [1, 2, 3]
        self.list_b: list = [1, 2, 3]

    def compare_lists(self) -> None:
        print("Ejercicio 2: Operadores de Comparación")
        print(f"¿Tienen el mismo contenido? (a == b): {self.list_a == self.list_b}")
        print(f"¿Son el mismo objeto en memoria? (a is b): {self.list_a <= self.list_b is self.list_b}")


class OperatorPrecedenceAnalyzer:

    def evaluate_expression(self) -> None:
        result = 2 + 1 * 2 % 2 + (2**1) // 2
        print("Ejercicio 3: Jerarquía de Operadores")
        print("Expresión: 2 + 1 * 2 % 2 + (2**1) // 2")
        print(f"Resultado:  {result}")
        print("Orden de Evaluación: Paréntesis/Potencia -> Multiplicación/Módulo -> División Entera -> Suma")



def run_exercise_1():
    calculator = ArithmeticCalculator()
    calculator.execute_operations()

def run_exercise_2():
    comparator = IdentityComparator()
    comparator.compare_lists()

def run_exercise_3():
    analyzer = OperatorPrecedenceAnalyzer()
    analyzer.evaluate_expression()


options_bloque_3 = {
    "1": ("Ejercicio 1: Operadores aritméticos", run_exercise_1),
    "2": ("Ejercicio 2: Comparación e Identidad", run_exercise_2),
    "3": ("Ejercicio 3: Jerarquía de Operadores", run_exercise_3),
    "4": ("Ejercicio práctica", run_bloque3_practice),
}