import sqlite3


def lista_cursos(nom_cat):
    try:
        con = sqlite3.connect("bd_example")
        c = con.cursor()
        c.execute("SELECT id FROM categorias WHERE nombre=?", (nom_cat,))
        cat_id = c.fetchone()
        print(*cat_id)
        c.execute("SELECT * FROM cursos WHERE categoria_id=?", cat_id)
        resultado = c.fetchall()
        for itm in resultado:
            print(itm)

    except sqlite3.Error as e:
        print("Error! :", e)
    finally:
        con.close()


lista_cursos("Dificil")
