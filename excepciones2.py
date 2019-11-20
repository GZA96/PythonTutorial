def get_key(dic, dkey):
    try:
        if dkey in dic:
            return dic[dkey]
        else:
            raise ValueError
    except ValueError:
        print("Error la clave no existe en el diccionario")
        return "Ejecución fallida"


dic = {"A": 1, "B": 2, "C": 3, "D": 4}
dkey = "R"
print(get_key(dic, dkey))
