import pickle


class Persona:
    def __init__(self, nombre, edad, genero, altura, peso):
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


p1 = Persona("Juan", 35, "M", 180, 180)
p2 = Persona("Maria", 20, "F", 160, 60)
p3 = Persona("Alberto", 25, "M", 170, 90)
personas = [p1, p2, p3]
fil_s = open("Las_personas", "wb")
pickle.dump(personas, fil_s)
fil_s.close()
del fil_s
