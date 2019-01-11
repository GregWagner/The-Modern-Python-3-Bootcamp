from csv import reader
from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)        # skip header
    for fighter in csv_reader:
        # each row is a list
        print(f"{fighter[0]} is from {fighter[1]} and is {fighter[2]} cm")

print('-' * 40)

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    next(csv_reader)        # skip header
    for fighter in csv_reader:
        # each row is an OrderedDict
        print(fighter['Name'])
