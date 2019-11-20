import pickle

lista = ["manzana", "pera", "naranja", "platano", "mango"]

fichero_binario = open("lista_frutas", "wb")

pickle.dump(lista, fichero_binario)

fichero_binario.close()

del fichero_binario


