from io import open


def primeras_nlineas(file, num):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    print("".join(lines[0:num]))


primeras_nlineas("TextoEjemplo.txt", 4)
