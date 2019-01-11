from csv import reader, writer

def delete_users(old_first, old_last):
    update_count = 0
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)
        with open("users.csv", "w") as file1:
            csv_writer = writer(file1)
            csv_writer.writerow(["First Name","Last Name"])
            for person in csv_reader:
                if person[0] == old_first and person[1] == old_last:
                    update_count += 1
                else:
                    csv_writer.writerow(person)
    return "Users deleted: {}.".format(update_count)

delete_users("Grace", "Hopper", "Hello", "World")
