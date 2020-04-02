import random

possResult = ['r', 's', 'p']

con = 0
while(con == 0):
    answerCom = random.choice(possResult)
    print(answerCom)
    answerUser = input('What do you want to play R,S or P').lower()

    if ((answerUser == 'r' and answerCom == 's') or (answerUser == 's' and answerCom == 'p') or
            (answerUser == 'p' and answerCom == 'r')  ):
        print('You win!')
    elif (answerUser == answerCom):
        print('It\'s a draw')
    else:
        print('You loss - Game finished')
        con = 1

    cont = input('Do you want to continue?')
    if (cont == 'no'):
        print('See you!')
        con = 1
