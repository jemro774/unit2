#Jack Robey
#9/18/17
#insulter.py - asks the user to enter their name and then generates a random insult

from random import randint
nameUser = input('Enter your name: ')
num = randint(1,5)
if num == 1:
    print('You are bad at computer programming')
elif num == 2:
    print('Is that your face? Or did your neck just throw up?')
elif num == 3:
    print('Stop whining')
elif num == 4:
    print('We all sprang from apes, but you did not spring far enough')
elif num == 5:
    print('I would ask how old you are, but I know you cannot count that high')
else:
    print('Error')

