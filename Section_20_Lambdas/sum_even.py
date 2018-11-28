def sum_even_values(*args):
    return(sum(x for x in args if x % 2 == 0))

print(sum_even_values(1, 2, 3, 4, 5, 6) == 12)
print(sum_even_values(4, 2, 1, 10) == 16)
print(sum_even_values(1) == 0)

