class InputValidationMixin:

    # ── Texto ──────────────────────────────────────────────────────────────────

    def input_text(self, prompt: str, field_name: str = "campo") -> str:
        """Solicita un texto no vacío. Rechaza entradas en blanco."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print(f"  [!] Error: El {field_name} no puede quedar vacío.\n")

    def input_text_alpha(self, prompt: str, field_name: str = "campo") -> str:
        """Solicita un texto que solo contenga letras y espacios."""
        while True:
            value = input(prompt).strip()
            if not value:
                print(f"  [!] Error: El {field_name} no puede quedar vacío.\n")
                continue
            if not all(c.isalpha() or c.isspace() for c in value):
                print(f"  [!] Error: El {field_name} solo puede contener letras y espacios.\n")
                continue
            return value

    # ── Números enteros ────────────────────────────────────────────────────────

    def input_int(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        """Solicita un entero con rango opcional [min_val, max_val]."""
        while True:
            try:
                value = int(input(prompt).strip())
                if min_val is not None and value < min_val:
                    print(f"  [!] Error: El valor mínimo permitido es {min_val}.\n")
                    continue
                if max_val is not None and value > max_val:
                    print(f"  [!] Error: El valor máximo permitido es {max_val}.\n")
                    continue
                return value
            except ValueError:
                print("  [!] Error: Debes ingresar un número entero válido.\n")

    def input_int_positive(self, prompt: str) -> int:
        """Solicita un entero estrictamente positivo (>= 1)."""
        return self.input_int(prompt, min_val=1)

    # ── Números decimales ──────────────────────────────────────────────────────

    def input_float(self, prompt: str, min_val: float = None, max_val: float = None) -> float:
        """Solicita un decimal con rango opcional [min_val, max_val]."""
        while True:
            try:
                value = float(input(prompt).strip())
                if min_val is not None and value < min_val:
                    print(f"  [!] Error: El valor mínimo permitido es {min_val}.\n")
                    continue
                if max_val is not None and value > max_val:
                    print(f"  [!] Error: El valor máximo permitido es {max_val}.\n")
                    continue
                return value
            except ValueError:
                print("  [!] Error: Debes ingresar un número decimal válido (ej: 3.5).\n")

    def input_float_non_negative(self, prompt: str) -> float:
        """Solicita un decimal >= 0."""
        return self.input_float(prompt, min_val=0.0)

    def input_float_non_zero(self, prompt: str) -> float:
        """Solicita un decimal que no sea cero (para evitar ZeroDivisionError)."""
        while True:
            value = self.input_float(prompt)
            if value == 0.0:
                print("  [!] Error: El valor no puede ser 0.\n")
                continue
            return value

    # ── Opciones ───────────────────────────────────────────────────────────────

    def input_yes_no(self, prompt: str) -> bool:
        """Solicita confirmación s/n. Retorna True para 's', False para 'n'."""
        while True:
            value = input(prompt).strip().lower()
            if value == 's':
                return True
            elif value == 'n':
                return False
            print("  [!] Error: Responde únicamente con 's' para Sí o 'n' para No.\n")

    def input_choice(self, prompt: str, valid_options: list[str]) -> str:
        """Solicita una opción de una lista de valores válidos."""
        options_str = "/".join(valid_options)
        full_prompt = f"{prompt} ({options_str}): "
        while True:
            value = input(full_prompt).strip().lower()
            if value in valid_options:
                return value
            print(f"  [!] Error: Opción inválida. Elige entre: {options_str}\n")