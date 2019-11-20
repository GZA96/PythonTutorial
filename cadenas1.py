def first_two(una_cadena):
    return una_cadena.strip().replace(" ", "")[:2]


def three_last(otra_cadena):
    f_cadena = otra_cadena.strip().replace(" ", "")
    return f_cadena[len(f_cadena)-3:]


def cada_dos(cadena_tres):
    f_cadena = cadena_tres.strip().replace(" ", "")
    return f_cadena[0:len(f_cadena):2]


def reversed_string(cadena_cuatro):
    return cadena_cuatro[::-1]


print(first_two("   H  oLA Pyth on So y Una Cadena    a   "))
print(three_last("   H  oLA Pyth on So y Una Cadena    a   "))
print(cada_dos("Hola python soy una cadena"))
print(reversed_string("Hola python soy una cadena"))

