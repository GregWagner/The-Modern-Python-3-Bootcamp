def isEven(num):
    return num % 2 == 0

def partition(l, func):
    list1 = []
    list2 = []
    for x in l:
        if func(x):
            list1.append(x)
        else:
            list2.append(x)
    return [list1, list2]


print(partition([1, 2, 3, 4], isEven) == [[2, 4], [1, 3]])
