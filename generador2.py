def mult_tres(num):
    x = 1
    while x < num:
        yield x * 3
        x += 1


lista_multiplos = mult_tres(100)
for item in lista_multiplos:
    print(item)