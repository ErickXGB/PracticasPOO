from blocks.block2.bloque2_practice import run_bloque2_practice

class StationReport:
    def display_system_info(self):
        firmware_version: str = "v2.0.26-Solar"     
        charge_levels: list = [20, 50, 80, 100]
        metadata: dict = {
            "id": "ST-01",
            "manager": "Anthony",
            "uptime": "99.9%"
        }
        
        print(f"Primer carácter del firmware: {firmware_version[0]} (este es el string)")
        print(f"Último nivel de carga: {charge_levels[-1]} (esta es la lista)")
        print(f"Manager: {metadata['manager']} (este es el diccionario)")


def run_exercise_1():
    entero: int = 9
    flotante: float = 3.14
    cadena: str = "Hola, mundo" 
    booleano: bool = True
    
    lista: list = [1, 2, "Guía POO", 6.1, False]

    tupla: tuple = (42, "Python", 3.14)
    conjunto: set[int] = {1, 2, 3}
    diccionario: dict = {"nombre": "Alice", "edad": 30, "es_estudiante": False}

    print(f"Entero: {entero} (Tipo: {type(entero)})")
    print(f"Flotante: {flotante} (Tipo: {type(flotante)})")
    print(f"Cadena: '{cadena}' (Tipo: {type(cadena)})")
    print(f"Booleano: {booleano} (Tipo: {type(booleano)})")
    print(f"Lista: {lista} (Tipo: {type(lista)})")
    print(f"Tupla: {tupla} (Tipo: {type(tupla)})")
    print(f"Conjunto: {conjunto} (Tipo: {type(conjunto)})")
    print(f"Diccionario: {diccionario} (Tipo: {type(diccionario)})")
 

def run_exercise_2():
    lista: list = [1, 2, "Guía POO", 6.1, False]
    print(lista)

    print("\nAccediendo a elementos de la lista:")
    print(f"Primer elemento de la lista: {lista[0]}")
    print(f"Último elemento de la tupla: {lista[-1]}")
    print(f"Valores intermedios de la lista: {lista[1:4]}")


def run_exercise_3():
    report = StationReport()
    report.display_system_info()



options_bloque_2 = {
    "1": ("Ejercicio 1", run_exercise_1),
    "2": ("Ejercicio 2", run_exercise_2),
    "3": ("Ejercicio 3", run_exercise_3),
    "4": ("Ejercicio de práctica", run_bloque2_practice)
}