import sqlite3

# Pasos para conectar a BBDD
# 1 - Abrir-Crear conexión
# 2 - Crear puntero
# 3 - Ejecutar query(consulta) SQL
# 4 - Manejar los resultados de la query (consulta).
# 5 - Cerrar puntero
# 6 - cerrar conexion


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
def create_mydb():
    my_conex = sqlite3.connect("bd_example")
    cursor = my_conex.cursor()
    cursor.execute('''
                    CREATE TABLE categorias (
                    id INTEGER  PRIMARY KEY, 
                    nombre VARCHAR(100) UNIQUE NOT NULL)
                    ''')
    cursor.execute('''
                    CREATE TABLE cursos (
                    id INTEGER  PRIMARY KEY, 
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL, 
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
                    ''')
    my_conex.close()


create_mydb()

