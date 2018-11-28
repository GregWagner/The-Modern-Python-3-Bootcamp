def triple_and_filter(l):
    return  [item  * 3 for item in l if item % 4 == 0]

print(triple_and_filter(range(1, 5)))
print(triple_and_filter(range(6, 13, 2)))
