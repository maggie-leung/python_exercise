num = int(input('Input the number you want to check'))

if (num % 4 == 0):
    print('This is a multiple of 4')
elif (num % 2 == 0):
    print('This is an even number')
else:
    print('This is an odd number')

check = int(input('Check for the multiple'))
if (num % check == 0):
    print(str(num) + ' is a multiple of ' + str(check))
else:
    print(str(num) + ' is NOT a multiple of ' + str(check))
