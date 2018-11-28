nums = range(2, 12, 2)

doubles = map(lambda x: x * 2, nums)
print(list(doubles))


people = ["Darcy", "Christina", "Dana"]
peeps = map(lambda name: name.upper(), people)
print(list(peeps))


names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}]
first_names = list(map(lambda x: x['first'], names))
print(first_names)
