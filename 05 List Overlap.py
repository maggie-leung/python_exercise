import random

list1 = random.sample(range(1, 30), 10)
list2 = random.sample(range(15, 40), 15)


print(list1)
print(list(set(list1)))
print(list2)

result = []

for obj in list(set(list1)):
    if obj in list2:
        result.append(obj)

print(result)

print([obj for obj in list(set(list1)) if obj in list2])
