import json
from blocks.block17.bloque17_practice import run_bloque17_practice

class AverageMixin:
    def calculate_average(self, grades: list) -> float:
        if not grades:
            return 0.0
        total_sum = sum(grades)
        total_elements = len(grades)
        
        return float(total_sum / total_elements)

class Student(AverageMixin):
    def __init__(self, name: str, grades: list):
        self.name: str = name
        self.grades: list = grades

    def display_final_report(self) -> None:
        final_average = self.calculate_average(self.grades)
        
        print(f"Estudiante:        {self.name}")
        print(f"Calificaciones:         {self.grades}")
        print(f"Promedio Final:  {final_average}")



class ValidationMixin:
    def validate_email(self, email: str) -> bool:
        if "@" in email and email.endswith(".com"):
            return True
        print(f"Formato de correo electrónico no válido: '{email}'")
        return False

    def validate_age(self, age: int) -> bool:
        if age >= 18:
            return True
        print(f"Edad no válida: {age} no cumple con el requisito mínimo de 18 años.")
        return False

class User(ValidationMixin):
    def __init__(self, username: str, email: str, age: int):
        self.username: str = username
        self.email: str = email
        self.age: int = age

    def register_user(self) -> None:

        print(f"\nIntentando registrar al usuario: '{self.username}'")
        
        is_email_valid = self.validate_email(self.email)
        is_age_valid = self.validate_age(self.age)
        
        if is_email_valid and is_age_valid:
            print(f"Guardado: Uasuario '{self.username}' registrado exitosamente con correo '{self.email}' y edad {self.age}.")



class ExportMixin:
    def export_json(self, data: list) -> str:
        print("[*] ExportMixin: Serializando datos a formato JSON")
        return json.dumps(data, indent=4)

    def export_csv(self, data: list) -> str:
        print("[*] ExportMixin: Serializando datos a formato CSV...")
        if not data:
            return ""

        headers = list(data[0].keys())
        csv_lines = []

        csv_lines.append(",".join(headers))

        for item in data:
            row_values = [str(item[header]) for header in headers]
            csv_lines.append(",".join(row_values))

        return "\n".join(csv_lines)


class Report(ExportMixin):
    def __init__(self, title: str):
        self.title: str = title
        self.sales_data: list = [
            {"product": "Laptop Asus", "quantity": 2, "total": 2400},
            {"product": "Panel Solar", "quantity": 4, "total": 800},
            {"product": "Batería LiFePO4", "quantity": 1, "total": 350}
        ]

    def generate_and_export_reports(self) -> None:
        print(f"Reporte: {self.title}")
        json_output = self.export_json(self.sales_data)
        print("\nJSON")
        print(json_output)
        
        csv_output = self.export_csv(self.sales_data)
        print("\nCSV")
        print(csv_output)

def run_exercise_1():
    print("Prueba del Mixin de Promedio con un estudiante de ejemplo")
    student_sample = Student(name="Domenica", grades=[8, 7, 8, 9, 10])
    student_sample.display_final_report()

def run_exercise_2():
    print("Prueba del Mixin de Validación con un usuario de ejemplo")
    #Caso con datos válidos
    user_sample = User(username="Domenica", email="domenica@example.com", age=20)
    user_sample.register_user()
    #Caso con correo no válido
    user_invalid_email = User(username="Anthony", email="invalidemail.com", age=20)
    user_invalid_email.register_user()
    #Caso con edad no válida
    user_invalid_age = User(username="Adrian", email="invalidage@example.com", age=17)
    user_invalid_age.register_user()

def run_exercise_3():
    print("Prueba del Mixin de Exportación con un reporte de ejemplo")
    sales_report = Report(title="Reporte Mayo")
    sales_report.generate_and_export_reports()

options_bloque_17 = {
    "1": ("Ejercicio 1: Mixin de Promedio", run_exercise_1),
    "2": ("Ejercicio 2: Mixin de Validación", run_exercise_2),
    "3": ("Ejercicio 3: Mixin de Exportación", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque17_practice)
}