import random

list = []

for x in range (10):
    list.append(random.randint(1, 10))

print(list)
listSmallthan5 = []
for x in list:
    if (x <= 5):
        print(x)
        listSmallthan5.append(x)
    else:
        pass

print([obj for obj in list if obj <=5])

print(listSmallthan5)
listSmallthanCheck = []

check = int(input('Enter a number you wanna check for the list, within 10'))
for x in list:
    if(x <= check):
        listSmallthanCheck.append(x)
    else:
        pass

print(listSmallthanCheck)
