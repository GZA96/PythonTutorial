def is_subcadena(cad1, cad2):
    if cad2 in cad1:
        return "La segunda cadena sí es una subcadena de la primera"
    return "La segunda cadena no es una subcadena de la primera"


def alf_anterior(cad1, cad2):
    return min(cad1.lower(), cad2.lower())



c1 = "Soy una cadena"
c2 = "una"
c11 = "Hola python soy una cadena"
c12 = "Es un buen día para programar"
print(is_subcadena(c1, c2))
print(alf_anterior(c1, c2))