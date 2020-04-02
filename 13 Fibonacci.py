def getList(size):
    result = []
    for x in range(size):
        if x is 0:
            result.append(1)
        elif x is 1:
            result.append(result[x-1] + 0)
        else:
            result.append(result[x-1] + result[x-2])
    return result

number = int(input('How many numbers you want?'))

list = getList(number)
print(list)
