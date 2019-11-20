def five_times(n):
    return 5 * n


list_n = [1, 2, 3, 5, 6, 7, 8, 9, 6, 5456, 5, 654, 5, 6, 43, 54, 44, 3, 2]
newList_n = map(five_times, list_n)
# aplica una función a todos los elementos que se encuentren dentro de un elemento iterable 
for item in newList_n:
    print(item)

