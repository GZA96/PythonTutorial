def isVocal(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return "Es una vocal"
    return "no es una vocal"


resultado = isVocal("a")

print(resultado)
