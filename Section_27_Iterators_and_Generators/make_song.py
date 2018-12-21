def make_song(count, beverage):
    current = count
    while current >= 0:
        if current:
            yield "{} bottles of {} on the wall".format(current, beverage)
        else:
            yield "No more {}".format(beverage)
        current -= 1
    return StopIteration

s = make_song(5, "beer")
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
