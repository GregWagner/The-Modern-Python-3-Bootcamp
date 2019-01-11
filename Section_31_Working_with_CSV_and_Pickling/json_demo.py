import json

# convert python data into json
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(j)

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Chales", "Tabby")
j = json.dumps(c.__dict__)
print(j)
