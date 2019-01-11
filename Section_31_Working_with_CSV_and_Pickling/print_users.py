from csv import reader

with open("users.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for user in csv_reader:
        print(user[0], user[1])
