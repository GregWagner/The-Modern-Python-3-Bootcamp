from csv import reader, writer

def update_users(old_first, old_last, new_first, new_last):
    update_count = 0
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)
        with open("users.csv", "w") as file1:
            csv_writer = writer(file1)
            csv_writer.writerow(["First Name","Last Name"])
            for person in csv_reader:
                if person[0] == old_first and person[1] == old_last:
                    csv_writer.writerow([new_first, new_last])
                    update_count += 1
                else:
                    csv_writer.writerow(person)
    return "Users updated: {}.".format(update_count)

update_users("Grace", "Hopper", "Hello", "World")
