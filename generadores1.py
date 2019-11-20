def num_pares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


iterItem = num_pares(20)
for i in iterItem:
    print(i)
