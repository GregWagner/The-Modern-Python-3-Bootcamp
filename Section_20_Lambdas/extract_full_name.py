def extract_full_name(l):
    return [name['first'] + ' ' + name['last'] for name in l]

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
