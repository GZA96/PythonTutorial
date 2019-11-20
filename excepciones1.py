def try_append(lista, elemento):
    try:
        if elemento not in lista:
            lista.append(elemento)
            return "Success!"
        else:
            raise ValueError
    except ValueError:
        print("Error, el elemento ya existe en la lista")
        return "Ejecución fallida"


lista = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 34, 1243, 22, 33]
elemento = 32

print(try_append(lista, elemento))
