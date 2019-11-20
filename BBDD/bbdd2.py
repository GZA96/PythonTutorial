import sqlite3


def ins_cat(nombre_cat):
    my_conex = sqlite3.connect("bd_example")
    cursor = my_conex.cursor()
    try:
        cursor.execute("INSERT INTO categorias values(NULL, ?)", (nombre_cat,))
        my_conex.commit()
        print("Success!")

    except sqlite3.Error as e:
        print(f"Error ! : {e}")
    finally:
        my_conex.close()


ins_cat("Intermedio")
