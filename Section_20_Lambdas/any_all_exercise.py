def is_all_strings(iterable):
    return all(type(i) == str for i in iterable)

print(is_all_strings(['a', 'b', 'c']) == True)
print(is_all_strings([2, 'a', 'b', 'c']) == False)
print(is_all_strings(['hello', 'goodbye']) == True)
