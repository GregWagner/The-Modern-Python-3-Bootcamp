from random import randint
x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)

if x > 0 and y > 0:
    print('both positive')
elif x < 0 and y < 0:
    print('both negative')
elif x < 0:
    print('x is negative and y is positive')
else:
    print('x is positive and y is negative')
