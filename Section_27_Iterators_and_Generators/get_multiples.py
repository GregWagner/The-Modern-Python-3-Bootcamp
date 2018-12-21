def get_multiples(number=1, count=10):
    for i in range(1, count + 1):
        yield number * i


default = get_multiples()
print(list(default))
