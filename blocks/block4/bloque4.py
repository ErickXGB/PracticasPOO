from blocks.block4.bloque4_practice import run_bloque4_practice

class ProfileRegister:
    def __init__(self):
        self.username: str = ""
        self.user_age: int = 0

    def collect_profile_data(self) -> None:

        print("Ejercicio 1: Entrada de Datos")
        while True:
            raw_input = input("Ingrese su nombre: ").strip()
            
            clean_check = raw_input.replace(" ", "")
            if clean_check and clean_check.isalpha():
                self.username = raw_input
                break     
            print("Error: El nombre solo puede contener letras y espacios, y no puede quedar vacío.\n")
        
        while True:
            try:
                self.user_age = int(input("Ingrese su edad: "))
                if self.user_age < 0 or self.user_age > 120:
                    print("Error: Ingrese una edad realista (0 - 120).\n")
                    continue
                break
            except ValueError:
                print("Error: La edad debe ser un número entero válido.\n")
     
        print(f"\nRegistro Exitoso: Hola {self.username}, tienes {self.user_age} años.")


class AverageCalculatorIO:
    def __init__(self):
        self.first_number: float = 0.0
        self.second_number: float = 0.0

    def compute_average_from_input(self) -> None:
        print("Ejercicio 2: Suma y Promedio")

        while True:
            try:
                self.first_number = float(input("Ingrese el primer número: "))
                break
            except ValueError:
                print("Error: Entrada inválida. Debe ingresar un número decimal.\n")

        while True:
            try:
                self.second_number = float(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Entrada inválida. Debe ingresar un número decimal.\n")
                
        total_sum: float = self.first_number + self.second_number
        calculated_average: float = total_sum / 2
        
        print(f"\nLa suma de {self.first_number} y {self.second_number} es: {total_sum}")
        print(f"Su promedio real es: {calculated_average}")


class StringConcatenator:
    def __init__(self):
        self.input_string: str = ""

    def demonstrate_concatenation(self) -> None:
        print("Ejercicio 3: Concatenación de Cadenas")
        
        while True:
            self.input_string = input("Ingrese un número (se leerá como texto): ").strip()
            if self.input_string:
                break
            print("Error: Debe ingresar al menos un carácter para concatenar.\n")

        print("\nEjemplo de concatenación:")
        concatenation_result = self.input_string + "5"
        print(f"El número ingresado es: {concatenation_result}")



def run_exercise_1():
    register = ProfileRegister()
    register.collect_profile_data()

def run_exercise_2():
    calculator = AverageCalculatorIO()
    calculator.compute_average_from_input()

def run_exercise_3():
    concatenator = StringConcatenator()
    concatenator.demonstrate_concatenation()


options_bloque_4 = {
    "1": ("Ejercicio 1", run_exercise_1),
    "2": ("Ejercicio 2", run_exercise_2),
    "3": ("Ejercicio 3", run_exercise_3),
    "4": ("Ejercicio Práctica", run_bloque4_practice),
}