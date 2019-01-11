from csv import reader

def find_user(first, last):
    with open("users.csv") as file:
        csv_reader = reader(file)
        index = 0
        for person in csv_reader:
            if person[0] == first and person[1] == last:
                return index
            index += 1
    return first + " " + last + " not found."

print(find_user("Colt", "Steele"))
print(find_user("Alan", "Turing"))
print(find_user("Not", "Here"))
