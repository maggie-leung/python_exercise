import random

list = []

for x in range (10):
    list.append(random.randint(1, 10))

print(list)
listSmallthan5 = []
for x in range(10):
    if(list[x] <= 5):
        print(list[x])
        listSmallthan5.append(list[x])
    else:
        pass

print(listSmallthan5)
listSmallthanCheck = []

check = int(input('Enter a number you wanna check for the list, within 10'))
for x in range(10):
    if(list[x] <= check):
        listSmallthanCheck.append(list[x])
    else:
        pass

print(listSmallthanCheck)
