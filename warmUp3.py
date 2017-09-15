#Jack Robey
#9/15/17
#warmUp3.py - tells if a number is divisible by 2, 3, neither, or both

num = int(input('Enter a number: '))
if num%2 == 0 and num%3 == 0:
    print(num, 'is divisible by 2 and 3')
elif num%2 == 0:
    print(num, 'is divisible by 2')
elif num%3 == 0:
    print(num, 'is divisible by 3')
else:
    print(num, 'is neither divisible by 2 or 3')
    
