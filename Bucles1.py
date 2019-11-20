def descompon_num(n):
    if n % 1 != 0:
        return "Introduce un entero"
    listaPrimos = []
    for i in range(2, n):
        listaPrimos.append(i)
        for x in range(1, i):
            division = i / x
            if division % 1 == 0 and x != 1 and x != i:
                listaPrimos.remove(i)
                break
    # print(listaPrimos)

    cociente = n
    counter = 0
    descomposicion = []
    while cociente != 1:
        cociente = cociente / listaPrimos[counter]
        if cociente % 1 != 0:
            cociente *= listaPrimos[counter]
            counter += 1
        else:
            descomposicion.append(listaPrimos[counter])
    return descomposicion


print(descompon_num(int(input("Introduzca el número a descomponer:  "))))