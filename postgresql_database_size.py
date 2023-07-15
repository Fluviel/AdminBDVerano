import psycopg2
import sys

def get_database_size():
    try:
        url = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format('localhost', 'postgres', 'postgres', 'fluviel10')

        conn = psycopg2.connect(url)


        cursor = conn.cursor()

        sql = """SELECT pg_database.datname, pg_database_size(pg_database.datname)/1024/1024 AS size_mb, pg_user.usename FROM pg_database JOIN pg_user ON pg_database.datdba = pg_user.usesysid"""

        cursor.execute(sql)
        results = cursor.fetchall() 
 
        # imprimir la información solicitada
        print("{0:20} {1:10} {2:10}".format("Nombre de DB", "Usuario", "Tamaño (MB)"))
        for row in results:
            print("{0:20} {1:10} {2:10}".format(row[0], row[2], round(row[1], 2)))
            
        cursor.close()
        conn.close()
 
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)
 

if __name__ == "__main__":
    get_database_size()
    
    
    
    
    
   

