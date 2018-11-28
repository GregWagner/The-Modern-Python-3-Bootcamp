def max_magitude(l):
    return abs(max(l, key=lambda item: abs(item)))

print(max_magitude([300, 20, -900]))
