def interleave(s1, s2):
    return ''.join((''.join(item) for item in zip(s1, s2)))

print(interleave('hi', 'no'))
