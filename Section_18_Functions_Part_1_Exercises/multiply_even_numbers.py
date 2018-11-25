def multiple_even_numbers(l):
    total = 1
    for i in l:
        if i % 2 == 0:
            total *= i
    return total

print(multiple_even_numbers([2, 3, 4, 5, 6]))
