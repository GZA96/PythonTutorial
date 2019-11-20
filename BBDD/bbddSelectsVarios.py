import sqlite3

my_con = sqlite3.connect("bd_example")
cursor = my_con.cursor()
cursor.execute("SELECT * FROM categorias")
lineas = cursor.fetchall()
print(lineas[0])

my_con.close()