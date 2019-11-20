import pickle


class Persona:
    def __init__(self, nombre, edad, genero,  altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.movimiento = False

    def andar(self):
        self.movimiento = True

    def parar_andar(self):
        self.movimiento = False

    def estado(self):
        print("Nombre: ", self.nombre, "\nAltura: ", self.altura, "\nGenero: ", self.genero, "\nEdad: ", self.edad,
              "\nPeso: ", self.peso, "\nEn movimiento: ", self.movimiento)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.nombre, self.edad, self.genero, self.altura, self.peso, self.movimiento)


f = open("Las_personas", "rb")
lista = pickle.load(f)
f.close()
for it in lista:
    print(it)

