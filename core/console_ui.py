import os
import shutil 

class ConsoleScreen:
    @staticmethod
    def initialize() -> None:
        if os.name == 'nt':
            os.system('')

    @staticmethod
    def get_terminal_size() -> tuple[int, int]:
        size = shutil.get_terminal_size(fallback=(120, 40))
        return size.columns, size.lines  # (ancho, alto)

    @staticmethod
    def move_cursor(x: int, y: int) -> None:
        print(f"\033[{y};{x}H", end="", flush=True)

    @staticmethod
    def clear_screen() -> None:
        print("\033[2J\033[3J\033[H", end="", flush=True)

    @staticmethod
    def set_text_color(color_code: int) -> None:
        print(f"\033[{color_code}m", end="", flush=True)

    @staticmethod
    def reset_styles() -> None:
        print("\033[0m", end="", flush=True)