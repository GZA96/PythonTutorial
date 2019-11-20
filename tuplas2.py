
baraja = ("Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
          "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh",
          "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks",
          "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd")


def is_poker(mano):
    i = 0
    cartas_iguales = 0
    num = mano[0][0]

    while i < 5:
        if mano[i] not in baraja:
            return "Error, tienes cartas no válidas"

        if num == mano[i][0]:
            cartas_iguales += 1
        else:
            num = mano[i][0]

        if cartas_iguales == 4:
            return "Poker!"

        i += 1
    return "No tienes poker"

print(is_poker(("4c", "4h", "4s", "4d", "6s")))
