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
        print("Nombre: ", self.nombre, "\nAltura: ", self.altura, "\nPeso: ", self.peso, "\nEn movimiento: ",
              self.movimiento)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.nombre, self.edad, self.genero, self.altura, self.peso, self.movimiento)


class ListaPersonas:

    ppl = []

    def __init__(self):
        lista_personas = open("fichExt", "ab+")
        lista_personas.seek(0)

        try:
            self.ppl = pickle.load(lista_personas)
            print(f"Se cargaron {len(self.ppl)} personas del fichero externo")
            # Remember: Tambien se puede usar:
            # print("Se cargaron {} personas del fichero externo".format(len(self.ppl)))

        except:
            print("El fichero esta vacio")
        finally:
            lista_personas.close()
            del lista_personas

    def add_personas(self, p):
        self.ppl.append(p)
        self.save_personas_en_fich_ext()

    def show_personas(self):
        for p in self.ppl:
            print(p)

    def save_personas_en_fich_ext(self):
        lista_personas = open("fichExt", "wb")
        pickle.dump(self.ppl, lista_personas)
        lista_personas.close()
        del lista_personas

    def show_info_fichext(self):
        print("Informacion de fich Ext: ")
        for p in self.ppl:
            print(p)


mi_lista = ListaPersonas()
p1 = Persona("Juan", 35, "M", 180, 180)
p2 = Persona("Maria", 20, "F", 160, 60)
p3 = Persona("Alberto", 25, "M", 170, 90)
mi_lista.add_personas(p1)
mi_lista.add_personas(p2)
mi_lista.add_personas(p3)
mi_lista.show_info_fichext()
