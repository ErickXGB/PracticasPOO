from blocks.block7.bloque7_practice import run_bloque7_practice

class exercise_1:
    def double(self, x):
        return x * 2
    
class MathOperations:
    def sum_numbers(self, *args) -> float:
        return sum(args)
    
class RecursionOperations:
    def calculate_factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo.")
            
        if n == 0:
            return 1

        return n * self.calculate_factorial(n - 1)


def run_exercise_2():
    print("Función que sume todos los elementos de una lista con *args.")
    operation = MathOperations()

    my_numbers = [5, 15, 25]
    total_list = operation.sum_numbers(*my_numbers)
    print(f"Suma de la lista desempaquetada [5, 15, 25] = {total_list}")

def run_exercise_3():
    print("Función recursiva para calcular el factorial de un número.")
    recursive_math = RecursionOperations()
    
    try:
        number = 5
        result = recursive_math.calculate_factorial(number)
        print(f"El factorial de {number} ({number}!) es = {result}")
    except ValueError as e:
        print(f"Error: {e}")

options_bloque_7 = {
    "1": ("Ejercicio 1: Duplicar un número", lambda: print(exercise_1().double(7))),
    "2": ("Ejercicio 2: Suma los elementos de una lista", lambda: run_exercise_2()),
    "3": ("Ejercicio 3: Calcular el factorial de un número", lambda: run_exercise_3()),
    "4": ("Ejercicio de práctica", run_bloque7_practice),
}