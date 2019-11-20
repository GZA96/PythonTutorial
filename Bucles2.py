def mcd(n1, n2):
    if n1 <= n2:
        return "Error"
    fst = n1
    snd = n2
    resto = fst % snd
    if resto != 0:
        return mcd(snd, resto)
    else:
        return snd


print(mcd(2366, 273))
