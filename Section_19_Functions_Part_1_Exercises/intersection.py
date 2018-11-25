def intersection(list1, list2):
    return [x for x in list1 if x in list2]

print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))
