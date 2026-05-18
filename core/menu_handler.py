from core.console_ui import ConsoleScreen

class InterfaceFrame:
    def __init__(self, width: int = 60):
        self.width = width
        self.frame_color: int = 33

    def print_header(self, title: str, start_y: int) -> int:
        ConsoleScreen.move_cursor(x=1, y=start_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╔" + "═" * (self.width - 2) + "╗", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=start_y + 1)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.set_text_color(93) 
        print(f"{title.upper().center(self.width - 2)}", end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=start_y + 2)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╠" + "═" * (self.width - 2) + "╣", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=start_y + 3)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(' ' * (self.width - 2), end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()
        
        return start_y + 4

    def print_line(self, text: str, current_y: int) -> None:
        ConsoleScreen.move_cursor(x=1, y=current_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        
        print(f"  {text.ljust(self.width - 4)}", end="")
        
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()

    def print_footer(self, action_text: str, current_y: int) -> int:
        ConsoleScreen.move_cursor(x=1, y=current_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(' ' * (self.width - 2), end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=current_y + 1)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╠" + "═" * (self.width - 2) + "╣", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=current_y + 2)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(f"{action_text.center(self.width - 2)}", end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()
        
        ConsoleScreen.move_cursor(x=1, y=current_y + 3)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╚" + "═" * (self.width - 2) + "╝", end="")
        ConsoleScreen.reset_styles()
        print()
        
        return current_y + 4


class MenuHandler:
    def __init__(self, title: str, options: dict):
        self.title = title
        self.options = options
        self.ui = InterfaceFrame(width=65)
        ConsoleScreen.initialize()

    def display(self) -> None:
        while True:
            ConsoleScreen.clear_screen()
            current_y = 2
            
            current_y = self.ui.print_header(self.title, start_y=current_y)
            
            for key, (description, _) in self.options.items():
                self.ui.print_line(f"[{key}] {description}", current_y=current_y)
                current_y += 1
            
            current_y = self.ui.print_footer(action_text="[x] Salir", current_y=current_y)
            
            ConsoleScreen.move_cursor(x=1, y=current_y + 1)
            padding = (self.ui.width - 22) // 2
            print(" " * padding + "Selecciona una opción: ", end="", flush=True)
            choice = input().strip()
            
            if choice == "x":
                break
            
            if choice in self.options:
                description, function = self.options[choice]
                ConsoleScreen.clear_screen()
                

                ConsoleScreen.move_cursor(x=1, y=2)
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("╔" + "═" * (self.ui.width - 2) + "╗", end="")
                
                ConsoleScreen.move_cursor(x=1, y=3)
                print("║", end="")
                ConsoleScreen.set_text_color(93)
                print(f"{f'Ejecutando: {description}'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║", end="")
                
                ConsoleScreen.move_cursor(x=1, y=4)
                print("╚" + "═" * (self.ui.width - 2) + "╝", end="")
                ConsoleScreen.reset_styles()
                print()

                ConsoleScreen.move_cursor(x=1, y=6)
                try:
                    function()  
                except Exception as e:
                    print(f"\n[!] Error de ejecución: {e}")

                print()
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("╔" + "═" * (self.ui.width - 2) + "╗", end="")
                print(f"\n║", end="")
                ConsoleScreen.reset_styles()
                print(f"{'Presiona Enter para regresar al menú...'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║", end="")
                print(f"\n╚" + "═" * (self.ui.width - 2) + "╝", end="")
                ConsoleScreen.reset_styles()
                print()
                input()
            else:
                ConsoleScreen.clear_screen()
                ConsoleScreen.move_cursor(x=1, y=2)
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("╔" + "═" * (self.ui.width - 2) + "╗\n║", end="")
                ConsoleScreen.reset_styles()
                print(f"{'[!] Opción inválida. Inténtalo de nuevo.'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║\n╚" + "═" * (self.ui.width - 2) + "╝", end="")
                ConsoleScreen.reset_styles()
                print()
                input()