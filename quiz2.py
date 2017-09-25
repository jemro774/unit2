#Jack Robey
#9/25/17
#quiz2.py - prompts user to enter in 2 numbers and tells him/her properties of the 2 numbers

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))

if num1>num2:
    print('The first number is bigger')
elif num2>num1:
    print('The second number is bigger')
else:
    print('The numbers are the same')

if num1%3 == 0 and num2%3 == 0:
    print('Both numbers are divisible by 3')
elif num1%3 == 0:
    print('Only the first number is divisible by 3')
elif num2%3 == 0:
    print('Only the second number is divisible by 3')
else:
    print('Neither number is divisble by 3')


