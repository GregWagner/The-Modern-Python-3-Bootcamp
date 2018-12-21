def get_unlimited_multiples(number=1):
    i = 1
    while True:
        yield number * i
        i += 1

sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])
