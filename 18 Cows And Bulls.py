import random

def cowBull(answer):
    c = 0
    cow = 0
    while cow != 4:
        cow = 0
        bull = 0

        guess = input('Put a guess')
        for x in range(len(answer)):
            if answer[x] == guess[x]:
                cow += 1
            elif answer[x] in guess:
                bull += 1
            else:
                pass
        c += 1
        print(cow, ' cows and ', bull, 'bulls')
    print('Total Trials', c)


if __name__ == "__main__":
    answer = str(random.randint(1000, 9999))
    print(answer)

    cowBull(answer)

