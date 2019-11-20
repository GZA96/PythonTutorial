def rep_letters(cadena):
    cadena = cadena.lower().replace(" ", "")
    i = 1
    letter = cadena[0]
    dicc = {letter: 1}
    while i < len(cadena):
        if cadena[i] == letter:
            dicc[letter] += 1
        else:
            letter = cadena[i]
            if letter in dicc:
                dicc[letter] += 1
            else:
                dicc[letter] = 1
        i += 1
    return dicc


print(rep_letters("Hola HoLa hOLA hoLA"))