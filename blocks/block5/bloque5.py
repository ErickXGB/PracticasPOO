from core.formatter import cprint as print, cinput as input
from blocks.block5.bloque5_practice import run_bloque5_practice

class ParityEvaluator:
    def __init__(self):
        self.target_number: int = 0

    def evaluate_parity(self) -> None:
        print("Ejercicio 1: Número Par o Impar")
        
        while True:
            try:
                self.target_number = int(input("Ingrese un número entero: "))
                break 
            except ValueError:
                print("Error: Debe ingresar un número entero.\n")

        if self.target_number % 2 == 0:
            print(f"El número {self.target_number} es par.")
        else:
            print(f"El número {self.target_number} es impar.")


class GradeClassifier:
    def __init__(self):
        self.numerical_grade: float = 0.0

    def classify_grade(self) -> None:
        print("Ejercicio 2: Sistema de Calificaciones")

        while True:
            try:
                self.numerical_grade = float(input("Ingrese su calificación (0 - 100): "))
                if self.numerical_grade < 0.0 or self.numerical_grade > 100.0:
                    print("Error: La calificación debe estar en el rango de 0.0 a 100.0.\n")
                    continue
                break
            except ValueError:
                print("Error. Debe ingresar un número.\n")

        if self.numerical_grade >= 90:
            print("-> Su nota es: A")
        elif self.numerical_grade >= 80:
            print("-> Su nota es: B")
        elif self.numerical_grade >= 70:
            print("-> Su nota es: C")
        elif self.numerical_grade >= 60:
            print("-> Su nota es: D")
        else:
            print("-> Su nota es: F")


class SystemAuthenticator:
    def __init__(self):
        self.username: str = ""
        self.password: str = ""

    def authenticate(self) -> None:

        print("Ejercicio 3: Autenticación de Usuario")
        
        while True:
            self.username = input("Ingrese su nombre de usuario: ").strip()
            if self.username:
                break
            print("Error: El usuario no puede quedar vacío.\n")
            
        while True:
            self.password = input("Ingrese su contraseña: ").strip()
            if self.password:
                break
            print("Error: La contraseña no puede quedar vacía.\n")

        if self.username == "admin" and self.password == "1234":
            print("\nBienvenido")
        else:
            print("\nAcceso denegado")



def run_exercise_1():
    evaluator = ParityEvaluator()
    evaluator.evaluate_parity()

def run_exercise_2():
    classifier = GradeClassifier()
    classifier.classify_grade()

def run_exercise_3():
    auth = SystemAuthenticator()
    auth.authenticate()


options_bloque_5 = {
    "1": ("Ejercicio 1", run_exercise_1),
    "2": ("Ejercicio 2", run_exercise_2),
    "3": ("Ejercicio 3", run_exercise_3),
    "4": ("Ejercicio Práctica", run_bloque5_practice),
}