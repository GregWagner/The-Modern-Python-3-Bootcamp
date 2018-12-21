def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

f = count_up_to(5)
for value in f:
    print(value)
