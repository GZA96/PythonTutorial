def sum_values(valuesList):
    sum = 0
    for item in valuesList:
        sum += item
    return sum


valueList = [4, 5, 7, 9, 35 , 67]
result = sum_values(valueList)
print(result)

