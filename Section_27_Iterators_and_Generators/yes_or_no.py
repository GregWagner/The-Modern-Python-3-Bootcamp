def yes_or_no():
    say_yes = True
    while True:
        if say_yes:
            yield 'yes'
        else:
            yield 'no'
        say_yes = not say_yes

gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))

