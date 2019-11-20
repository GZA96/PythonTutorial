import math


def f_decoradora(f_param):
    def f_interior(*args):
        for i in range(0, *args):
            yield f_param(i)
    return f_interior


@f_decoradora
def cubo(n):
    return n**3


# print(cubo(10))
n = 10
lista = cubo(n)
for a in range(0, n):
    print(next(lista))