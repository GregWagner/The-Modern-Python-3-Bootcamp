
for num in range(1, 21):
    type = 'odd'
    if num == 4 or num == 13:
        type = 'UNLUCKY!'
    elif num % 2 == 0:
        type = 'even'
    print(f'{num} is {type}')

