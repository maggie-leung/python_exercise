import random

list1 = random.sample(range(1, 30), 10)
list2 = random.sample(range(15, 60), 15)

list1_uni = list(set(list1))

result = [obj for obj in list1_uni if obj in list2]
