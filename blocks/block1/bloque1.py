from blocks.block1.bloque1_practice import run_bloque1_practice

class Product:
    def __init__(self, code, name, price):
        if price < 0: raise ValueError("El precio no puede ser negativo")
        self.code = code
        self.name = name
        self.price = price

class Student:
    def __init__(self, name: str, grades: list=None):
        if not name: raise ValueError("El nombre es obligatorio")
        self.name = name
        self.grades = grades if grades is not None else []

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"), 
            grades=data.get("grades")
    )


    
def run_product_exercise_1_and_2():
    p1 = Product("P001", "Laptop", 900)
    p2 = Product("P002", "Smartphone", 500)
    print(f"Producto: {p1.name} - ${p1.price}")
    print(f"Producto: {p2.name} - ${p2.price}")


def run_exercise_3():
    print("Prueba de Lista vacía")
    s1 = Student("Anthony")
    print(f"Estudiante: {s1.name}, Notas: {s1.grades}")
    
    s2 = Student("Ashlee", [95, 88, 92])
    print(f"Estudiante: {s2.name}, Notas: {s2.grades}")

def run_exercise_4():
    student_data = {"name": "Anthony", "grades": [90, 85, 100]}
    new_student = Student.from_dict(student_data)
    print(f"Estudiante cargado como diccionario: {new_student.name} con notas {new_student.grades}")
    

options_bloque_1 = {
    "1": ("Ejercicio Producto (1 y 2)", run_product_exercise_1_and_2),
    "2": ("Ejercicio 3", run_exercise_3),
    "3": ("Ejercicio 4. Agregar un @classmethod", run_exercise_4),
    "4": ("Ejercicio de práctica", run_bloque1_practice)
}