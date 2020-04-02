
def checkDivisor(num):
    divisor = []
    for x in range(2, num):
        if(num % x == 0):
            divisor.append(x)
        else:
            pass
    if len(divisor) == 0:
        print('It is a prime number')
        print(divisor)
    else:
        print('It is not a prime number')
        print(divisor)

check = int(input('Enter a number you wanna check it\'s prime!'))

checkDivisor(check)
