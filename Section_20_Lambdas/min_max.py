names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

# find size of longest name
# print(max(len(name) for name in names))

# find longest name
print(max(names, key=lambda n: len(n)))
