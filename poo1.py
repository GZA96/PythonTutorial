from Bucles2 import mcd


class Fraccion():
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def sumar(self, otra_fraccion):
        # (x*y) = mcm * mcd --> mcm = (x*y) // mcd
        if self.divisor > otra_fraccion.divisor:
            mas_grande = self.divisor
            mas_peq = otra_fraccion.divisor
        else:
            mas_grande = otra_fraccion.divisor
            mas_peq = self.divisor
        mcm = (self.divisor * otra_fraccion.divisor) // mcd(mas_grande, mas_peq)
        print("MCM de ", mas_grande, " y ",mas_peq, " es ", mcm)
        suma = self.dividendo * (mcm // self.divisor) + (mcm // otra_fraccion.dividendo)
        return Fraccion(suma, mcm)

    def mult(self, otra_fraccion):
        ndivid = self.dividendo * otra_fraccion.dividendo
        ndivis = self.divisor * otra_fraccion.divisor
        return Fraccion(ndivid, ndivis)

    def simplifica(self):
        if self.dividendo > self.divisor:
            max_div = self.divisor
            for i in range(max_div, 1, -1):
                if self.dividendo % i == 0 and self.divisor % i == 0:
                    return Fraccion(self.dividendo // i, self.divisor // i)
            return self
        else:
            max_div = self.dividendo
            for i in range(max_div, 1, -1):
                if self.dividendo % i == 0 and self.divisor % i == 0:
                    return Fraccion(self.dividendo // i, self.divisor // i)
            return self

    def __str__(self):
        return str(self.dividendo) + "/" + str(self.divisor)


f1 = Fraccion(4, 8)
result = f1.simplifica()
print(result)

f2 = Fraccion(5, 9)
result1 = f1.sumar(f2)
print(result1)
