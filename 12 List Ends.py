import random

size = int(input('What\'s the size you want for the list'))

list1 = random.sample(range(1, 30), size)
print(list1)

def listEnd(list1):
    result = [list1[0], list1[-1]]
    print(result)

listEnd(list1)
