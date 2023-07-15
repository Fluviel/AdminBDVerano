import psycopg2

def obtener_tamano_tablas():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="fluviel10"
        )
        cursor = conn.cursor()

        # Consultar información sobre el tamaño de las tablas
        query = """
        SELECT table_catalog, table_schema, table_name, pg_size_pretty(pg_total_relation_size('"' || table_schema || '"."' || table_name || '"')) AS size
        FROM information_schema.tables
        WHERE table_type='BASE TABLE'
        ORDER BY table_catalog, table_schema, table_name;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()

        # Imprimir los resultados
        print("Nombre de base de datos | Usuario propietario | Nombre de tabla | Tamaño de tabla")
        print("-----------------------+---------------------+----------------+---------------")
        for fila in resultados:
            print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]}")

        # Cerrar la conexión
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

# Llamar a la función para obtener el tamaño de las tablas
obtener_tamano_tablas()

    
