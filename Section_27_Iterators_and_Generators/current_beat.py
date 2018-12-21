def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        i = 0 if i >= len(nums) else i
        yield nums[i]
        i += 1

counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
