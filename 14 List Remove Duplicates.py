import random

def removeDuplicate(check):
    result = list(set(check))
    return result

list1 = []
for x in range(20):
    list1.append(random.randint(1, 15))

print(list1)

print(removeDuplicate(list1))
