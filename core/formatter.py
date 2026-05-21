import shutil
import textwrap
import builtins

# Guardamos las referencias reales de Python para evitar bucles infinitos
builtins_print = builtins.print
builtins_input = builtins.input

def get_padding() -> str:

    terminal_width, _ = shutil.get_terminal_size(fallback=(120, 40))
    start_x = max(1, (terminal_width - 65) // 2)
    # Agregamos espacios adicionales para que nazca dentro de los límites visuales
    return " " * (start_x + 1)

def cprint(*args, sep: str = " ", end: str = "\n", flush: bool = False) -> None:
    """
    Reemplazo modular de print(). Envuelve el texto largo para que no 
    se salga de los límites visuales de la caja y le aplica el margen.
    """
    pad = get_padding()
    full_text = sep.join(str(arg) for arg in args)
    
    # Límite máximo de caracteres por línea antes de hacer un salto automático
    max_text_width = 62 
    
    # Respetamos los saltos de línea manuales que ya tengas en tus ejercicios
    original_lines = full_text.split("\n")
    
    final_lines = []
    for line in original_lines:
        if line.strip() == "":
            final_lines.append(pad) # Mantiene las líneas en blanco
        else:
            # Corta el texto si es muy largo, sin romper las palabras por la mitad
            wrapped = textwrap.wrap(line, width=max_text_width)
            for w in wrapped:
                final_lines.append(pad + w)
    
    # Imprime el bloque final formateado
    builtins_print("\n".join(final_lines), end=end, flush=flush)

def cinput(prompt: str = "") -> str:
    """
    Reemplazo modular de input(). Desplaza la pregunta al bloque central.
    """
    pad = get_padding()
    builtins_print(f"{pad}{prompt}", end="", flush=True)
    return builtins_input()