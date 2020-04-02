import random

answer = random.randint(1, 10)
guess = 0
c = 0

while guess != answer and guess != 'exit':
    guess = input('Enter a guess')

    if guess == 'exit':
        break

    guess = int(guess)
    c += 1

    if guess == answer:
        print('you got it')
        print('it takes you', c, 'try')
    elif (guess > answer):
        print('too high')
    else:
        print('too low')
