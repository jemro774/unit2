#Jack Robey
#9/13/17
#movie.py - tells the user the most scandulous type of movie they can watch

ageUser = int(input('Enter your age: '))
if ageUser>=17:
    print('You can watch R-rated movies')
elif ageUser>=13:
    print('You can watch PG-13 movies')
elif ageUser>=5:
    print('You can watch PG-rated movies')
else:
    print('You can watch G-rated movies')

