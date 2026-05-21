from core.console_ui import ConsoleScreen

class InterfaceFrame:
    def __init__(self, width: int = 60):
        self.width = width
        self.frame_color: int = 33
        self.start_x: int = 1

    def _recalculate_offset(self) -> None:
        terminal_width, _ = ConsoleScreen.get_terminal_size()
        self.start_x = max(1, (terminal_width - self.width) // 2)

    def print_header(self, title: str, start_y: int) -> int:
        x = self.start_x
        ConsoleScreen.move_cursor(x=x, y=start_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╔" + "═" * (self.width - 2) + "╗", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=start_y + 1)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.set_text_color(93)
        print(f"{title.upper().center(self.width - 2)}", end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=start_y + 2)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╠" + "═" * (self.width - 2) + "╣", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=start_y + 3)
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
        ConsoleScreen.move_cursor(x=self.start_x, y=current_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(f"  {text.ljust(self.width - 4)}", end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()

    def print_footer(self, action_text: str, current_y: int) -> int:
        x = self.start_x
        ConsoleScreen.move_cursor(x=x, y=current_y)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(' ' * (self.width - 2), end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=current_y + 1)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╠" + "═" * (self.width - 2) + "╣", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=current_y + 2)
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print(f"{action_text.center(self.width - 2)}", end="")
        ConsoleScreen.set_text_color(self.frame_color)
        print("║", end="")
        ConsoleScreen.reset_styles()
        print()

        ConsoleScreen.move_cursor(x=x, y=current_y + 3)
        ConsoleScreen.set_text_color(self.frame_color)
        print("╚" + "═" * (self.width - 2) + "╝", end="")
        ConsoleScreen.reset_styles()
        print()

        return current_y + 4


class MenuHandler:
    _is_menu_active = False

    def __init__(self, title: str, options: dict):
        self.title = title
        self.options = options
        self.ui = InterfaceFrame(width=65)
        ConsoleScreen.initialize()

    def display(self) -> None:
        while True:
            MenuHandler._is_menu_active = True
            ConsoleScreen.clear_screen()
            self.ui._recalculate_offset()

            current_y = 2
            current_y = self.ui.print_header(self.title, start_y=current_y)

            for key, (description, _) in self.options.items():
                self.ui.print_line(f"[{key}] {description}", current_y=current_y)
                current_y += 1

            current_y = self.ui.print_footer(action_text="[x] Salir", current_y=current_y)

            # Input del menú principal centrado
            ConsoleScreen.move_cursor(x=self.ui.start_x, y=current_y + 1)
            print(" " * ((self.ui.width - 22) // 2) + "Selecciona una opción: ", end="", flush=True)
            choice = input().strip().lower()

            if choice == "x":
                break

            if choice in self.options:
                description, function = self.options[choice]
                ConsoleScreen.clear_screen()
                self.ui._recalculate_offset()
                x = self.ui.start_x

                # Tarjeta Centrada: "Ejecutando..."
                ConsoleScreen.move_cursor(x=x, y=2)
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("╔" + "═" * (self.ui.width - 2) + "╗", end="")

                ConsoleScreen.move_cursor(x=x, y=3)
                print("║", end="")
                ConsoleScreen.set_text_color(93)
                print(f"{f'{description}'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║", end="")

                ConsoleScreen.move_cursor(x=x, y=4)
                print("╚" + "═" * (self.ui.width - 2) + "╝", end="")
                ConsoleScreen.reset_styles()
                print()

                # El cursor se va a la línea 6 de forma limpia
                ConsoleScreen.move_cursor(x=1, y=6)
                MenuHandler._is_menu_active = False 
                try:
                    function()
                except Exception as e:
                    print(f"\n[!] Error de ejecución: {e}")

                if MenuHandler._is_menu_active:
                    continue

                # Tarjeta Centrada: "Presiona Enter..."
                print("\033[0m\r\n") 
                pad = " " * (x - 1)
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print(pad + "╔" + "═" * (self.ui.width - 2) + "╗")
                print(pad + "║", end="")
                ConsoleScreen.reset_styles()
                print(f"{'Presiona Enter para regresar al menú...'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║")
                print(pad + "╚" + "═" * (self.ui.width - 2) + "╝")
                ConsoleScreen.reset_styles()
                
                input(pad + " " * ((self.ui.width // 2) - 1))

            else:
                ConsoleScreen.clear_screen()
                self.ui._recalculate_offset()
                x = self.ui.start_x
                
                ConsoleScreen.move_cursor(x=x, y=2)
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("╔" + "═" * (self.ui.width - 2) + "╗", end="")
                
                ConsoleScreen.move_cursor(x=x, y=3)
                print("║", end="")
                ConsoleScreen.reset_styles()
                print(f"{'[!] Opción inválida. Inténtalo de nuevo.'.center(self.ui.width - 2)}", end="")
                ConsoleScreen.set_text_color(self.ui.frame_color)
                print("║", end="")
                
                ConsoleScreen.move_cursor(x=x, y=4)
                print("╚" + "═" * (self.ui.width - 2) + "╝", end="")
                ConsoleScreen.reset_styles()
                
                ConsoleScreen.move_cursor(x=x, y=6)
                pad_interno = " " * ((self.ui.width - 32) // 2)
                input(f"{pad_interno}Presiona Enter para continuar...")