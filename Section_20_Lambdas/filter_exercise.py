def remove_negatives(l):
    return list(filter(lambda x: x > 0, l))

print(remove_negatives([-1, 3, 4, -99]))
