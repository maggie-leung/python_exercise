import random

list1 = sorted(random.sample(range(30), 15))
check = int(input('Enter the number you wanna check'))

print(check in list1)
