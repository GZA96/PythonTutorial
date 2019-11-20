import sqlite3


def new_curso(curso, cat):
    try:
        my_conn = sqlite3.connect("bd_example")
        c = my_conn.cursor()
        nombre_cat = (cat,)
        c.execute("SELECT id FROM categorias WHERE nombre=?", nombre_cat)
        cat_id = c.fetchone()
        datos = (curso, *cat_id)
        c.execute("INSERT INTO cursos VALUES(NULL, ?, ?)", datos)
        my_conn.commit()
        print("Success! ")
    except sqlite3.Error as e:
        print("Error! : ", e)
    finally:
        my_conn.close()


new_curso("Ecuaciones diferenciales", "Dificil")
