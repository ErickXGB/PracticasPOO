from blocks.block13.bloque13_practice import run_bloque13_practice

# DEFINICIÓN DEL DECORADOR
def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Iniciando...") 
        return func(*args, **kwargs)
    return wrapper 

class TaskProcessor:
    @my_simple_decorator
    def execute_core_task(self) -> None:
        print("Ejecutando la tarea principal.")

# DECORADOR DE VALIDACIÓN
def validate_positive(func):
    def wrapper(*args, **kwargs):
        number = args[1]
        
        if number < 0:
            print(f"[!] El número {number} es negativo.")
            return None  
        return func(*args, **kwargs)
    return wrapper

class MathProcessor:
    @validate_positive
    def calculate_square(self, value: float) -> float:
        result = value ** 2
        print(f"Operación exitosa. El cuadrado de {value} es: {result}")
        return result

# DECORADOR LOG
def log(func):
    def wrapper(*args, **kwargs):
        print("Llamando función...")
        return func(*args, **kwargs)
    return wrapper

class CalculatorService:
    @log
    def add_numbers(self, a: int, b: int) -> int:
        return a + b
    

def run_exercise_1():
    print("Prueba del decorador")
    
    processor = TaskProcessor()
    processor.execute_core_task()

def run_exercise_2():
    print("Prueba del decorador de validación")
    processor = MathProcessor()
    
    print("Caso 1: Pasando el número 6...")
    processor.calculate_square(6)

    print("\nCaso 2: Pasando el número -4...")
    processor.calculate_square(-4)

def run_exercise_3():
    print("Analizando Decorador @log")
    service = CalculatorService()
    
    result = service.add_numbers(2, 3)
    print(f"Resultado devuelto por la función: {result}")

options_bloque_13 = { 
    "1": ("Ejercicio 1: Prueba del decorador", run_exercise_1),
    "2": ("Ejercicio 2: Prueba del decorador de validación", run_exercise_2),
    "3": ("Ejercicio 3: Analizando el decorador @log", run_exercise_3),
    "4": ("Ejercicio de prática", run_bloque13_practice),
}