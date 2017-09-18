#Jack Robey
#9/15/17
#fortuneTeller.py - displays fortune based on the color and number combination picked

colr = input('Pick red or blue: ')
num = int(input('Pick a number from 1 to 4: '))
if colr == 'red' and num == 1:
    print('You will inherit five million dollars')
elif colr == 'red' and num == 2:
    print('You will lose in chess')
elif colr == 'red' and num == 3:
    print('You will fall off a bridge')
elif colr == 'red' and num == 4:
    print('You will win the lottery')
elif colr == 'blue' and num == 1:
    print('You will go blind')
elif colr == 'blue' and num == 2:
    print('You will win a trip to Costa Rica')
elif colr == 'blue' and num == 3:
    print('You will find a four-leaf clover')
elif colr == 'blue' and num == 4:
    print('You will fail school')
else:
    print('Error')