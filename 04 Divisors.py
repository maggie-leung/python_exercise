num = int(input('Enter a number you wanna check it\'s divisor!'))

divisor = []

for x in range(1, num+1):
    if(num % x == 0):
        divisor.append(x)
    else:
        pass

print (str(num) + '\'s divisors includes:')
print(divisor)
