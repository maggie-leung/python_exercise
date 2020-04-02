string = input('Enter the word that you want to check').lower()

check = ''

for x in range(len(string)):
    check += string[len(string) - 1 - x]

if (check  == string):
    print('it is a palindrome ')
else:
    print('it is not a palindrome')

reverse = string[::-1]

if (reverse == string):
    print('It is a palindorme, from reverse')
else:
    print('It is not')
   
