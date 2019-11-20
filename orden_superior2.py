# OG:
# def mult_tres(lista_nums):
#     res = []
#     for n in lista_nums:
#         if n % 3 == 0:
#             res.append(n)
#     return res
#
#
# print(mult_tres([1,2,3,4,5,6,7,8,9,33,30,13,17,18,46,99]))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 30, 13, 17, 18, 46, 99]
print(list(filter(lambda mult_tres: mult_tres % 3 == 0, nums)))

'''
puede utilizarse para objetos tambien, recordar ejemplo del video con objetos Empleado
y filtras el salario con --> salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)
'''

