from core.menu_handler import MenuHandler
from blocks.block0.bloque0 import options_bloque_0
from blocks.block1.bloque1 import options_bloque_1
from blocks.block2.bloque2 import options_bloque_2
from blocks.block3.bloque3 import options_bloque_3
from blocks.block4.bloque4 import options_bloque_4
from blocks.block5.bloque5 import options_bloque_5
from blocks.block6.bloque6 import options_bloque_6
from blocks.block7.bloque7 import options_bloque_7
from blocks.block8.bloque8 import options_bloque_8
from blocks.block9.bloque9 import options_bloque_9
from blocks.block10.bloque10 import options_bloque_10
from blocks.block11.bloque11 import options_bloque_11
from blocks.block12.bloque12 import options_bloque_12
from blocks.block13.bloque13 import options_bloque_13
from blocks.block14.bloque14 import options_bloque_14
from blocks.block15.bloque15 import options_bloque_15
from blocks.block16.bloque16 import options_bloque_16
from blocks.block17.bloque17 import options_bloque_17

def main() -> None:
    main_options = {
        "0": ("Bloque 0: Introducción a POO", lambda: MenuHandler("Bloque 0 Menú", options_bloque_0).display()),
        "1": ("Bloque 1: Constructor __init__", lambda: MenuHandler("Bloque 1 Menú", options_bloque_1).display()),
        "2": ("Bloque 2: Variables y tipos de datos", lambda: MenuHandler("Bloque 2 Menú", options_bloque_2).display()),
        "3": ("Bloque 3: Operadores", lambda: MenuHandler("Bloque 3 Menú", options_bloque_3).display()),
        "4": ("Bloque 4: Entrada y salidade datos", lambda: MenuHandler("Bloque 4 Menú", options_bloque_4).display()),
        "5": ("Bloque 5: Condicionales", lambda: MenuHandler("Bloque 5 Menú", options_bloque_5).display()),
        "6": ("Bloque 6: Bucles", lambda: MenuHandler("Bloque 6 Menú", options_bloque_6).display()),
        "7": ("Bloque 7: Funciones", lambda: MenuHandler("Bloque 7 Menú", options_bloque_7).display()),
        "8": ("Bloque 8: Listas", lambda: MenuHandler("Bloque 8 Menú", options_bloque_8).display()),
        "9": ("Bloque 9: Tuplas", lambda: MenuHandler("Bloque 9 Menú", options_bloque_9).display()),
        "10": ("Bloque 10: Diccionarios", lambda: MenuHandler("Bloque 10 Menú", options_bloque_10).display()),
        "11": ("Bloque 11: Conjuntos", lambda: MenuHandler("Bloque 11 Menú", options_bloque_11).display()),
        "12": ("Bloque 12: Manejo de excepciones (Try / Except)", lambda: MenuHandler("Bloque 12 Menú", options_bloque_12).display()),
        "13": ("Bloque 13: Decoradores", lambda: MenuHandler("Bloque 13 Menú", options_bloque_13).display()),
        "14": ("Bloque 14: UNPACKING (Desempaquetado)", lambda: MenuHandler("Bloque 14 Menú", options_bloque_14).display()),
        "15": ("Bloque 15: Funciones de Orden Superior", lambda: MenuHandler("Bloque 15 Menú", options_bloque_15).display()),
        "16": ("Bloque 16: Archivos y JSON", lambda: MenuHandler("Bloque 16 Menú", options_bloque_16).display()),
        "17": ("Bloque 17: Mixins", lambda: MenuHandler("Bloque 17 Menú", options_bloque_17).display()),
    }

    main_menu = MenuHandler("Menú General - Práctica experimental", main_options)
    main_menu.display()

if __name__ == "__main__":
    main()