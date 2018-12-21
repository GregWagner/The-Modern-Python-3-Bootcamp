def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

print(fib_list(10))

def fib_gen(max):
    x, y = 0, 1
    count = 1
    while count < max:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_gen(1000000):
    print(n)
