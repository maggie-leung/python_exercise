import datetime

age = input("What is your age?")
now = datetime.datetime.now()

yearOf100 = 100 - int(age) + now.year

print('You will turn 100 in ' + str(yearOf100))
