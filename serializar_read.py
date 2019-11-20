import pickle


def read_serialized(file1):
    f = open(file1, "rb")
    lista = pickle.load(f)
    print(lista)