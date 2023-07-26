import sys

COLORS = {
    "yellow": "\033[93m",
    "orange": "\033[91m",
    "red": "\033[31m",
    "reset": "\033[0m"
}

def imprimir_con_color(texto, color):
    color_code = COLORS.get(color.lower())
    if color_code:
        return f"{color_code}{texto}{COLORS['reset']}"
    return texto

def detectar_errores(file_path):
    found_error = False
    found_fatal = False
    found_panic = False

    with open(file_path, 'r') as file:
        for line in file:
            line_lower = line.lower()
            if "error" in line_lower:
                line = line.replace("ERROR", imprimir_con_color("ERROR", "yellow"))
                print(line.strip())
                found_error = True
            if "fatal" in line_lower:
                line = line.replace("FATAL", imprimir_con_color("FATAL", "orange"))
                print(line.strip())
                found_fatal = True
            if "panic" in line_lower:
                line = line.replace("PANIC", imprimir_con_color("PANIC", "red"))
                print(line.strip())
                found_panic = True

    if not found_error:
        print("No se encontró ningun 'ERROR' en el archivo.")
    if not found_fatal:
        print("No se encontró ningun 'FATAL' en el archivo.")
    if not found_panic:
        print("No se encontró ningun 'PANIC' en el archivo.")

if __name__ == "__main__":
    archivo_log = "/var/log/postgresql.log"  
    detectar_errores(archivo_log)
