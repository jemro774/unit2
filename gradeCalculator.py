#Jack Robey
#9/13/17
#gradeCalculator.py - calculates one's grade

percentage = int(input('Enter your grade: '))
if percentage>=90:
    print('You earned an A')
elif percentage>=80:
    print('You eaned a B')
elif percentage>=70:
    print('You eaned a C')
elif percentage>=60:
    print('You eaned a D')
else:
    print('Your are failing')