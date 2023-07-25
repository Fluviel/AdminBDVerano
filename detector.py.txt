def detectar_errores(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line or "FATAL" in line or "PANIC" in line:
                print(line.strip())

if __name__ == "__main__":
    archivo_log = "/var
/log/postgresql.log" 
    detectar_errores(archivo_log)
