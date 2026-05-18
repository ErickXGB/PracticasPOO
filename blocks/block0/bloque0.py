from blocks.block0.bloque0_practice import run_bloque0_practice

class Book:
    def __init__(self, isbn: str, title: str, author: str, target_year: int):
        self.isbn: str = isbn                    
        self.title: str = title                  
        self.author: str = author                
        self.publication_year: int = target_year 
        self.is_available: bool = True           

class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id: str = customer_id      
        self.name: str = name                   
        self.email: str = email                          

class Librarian:
    def __init__(self, employee_id: str, name: str, shift: str):
        self.employee_id: str = employee_id     
        self.name: str = name                    
        self.shift: str = shift                  

class Loan:
    def __init__(self, loan_id: str, book: Book, customer: Customer, issue_date: str):
        self.loan_id: str = loan_id              
        self.book: Book = book                   
        self.customer: Customer = customer       
        self.issue_date: str = issue_date        
        self.due_date: str = ""                  
        self.is_active: bool = True              

class Catalog:
    def __init__(self):
        self.books_collection: list = []  
        self.total_books_count: int = 0

class Person:
    def __init__(self, name, age):
        if not name: raise ValueError("El nombre no puede estar vacío")
        if age < 0: raise ValueError("La edad no puede ser negativa")
        self.name = name
        self.age = age


def run_exercise_1():
    print("Clase Book; Atributos: ['isbn', 'title', 'author', 'publication_year', 'is_available']")
    print("Clase Customer; Atributos: ['customer_id', 'name', 'email']")
    print("Clase Librarian; Atributos: ['employee_id', 'name', 'shift']")
    print("Clase Loan; Atributos: ['loan_id', 'book', 'customer', 'issue_date', 'due_date', 'is_active']")
    print("Clase Catalog; Atributos: ['books_collection', 'total_books_count']")

def run_exercise_2():
    p1 = Person("Anthony", 20)
    p2 = Person("Ashlee", 20)
    p3 = Person("Ileana", 21)
    print(f"Personas creadas: {p1.name} con {p1.age} años; {p2.name} con {p2.age} años y {p3.name} con {p3.age} años")

def run_exercise_3():
    print("Las clases son unas plantillas que tiene la información básica,\ncomo las propiedades, atributos y métodos, que comparten entre\nsí los objetos. Los objetos son creados a partir de la clase,\ncon datos específicos del objeto. Por ejemplo, la clase:\nJuguete, los objetos: carroJuguete (Mazda rx7, hootWhels),\nmuñecaJuguete (set muñeca, barbie).")


options_bloque_0 = {
    "1": ("Clases para un sistema de biblioteca", run_exercise_1),
    "2": ("Crear Personas (Instancia de 3 objetos)", run_exercise_2),
    "3": ("Diferencias entre clase y objeto", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque0_practice)
}