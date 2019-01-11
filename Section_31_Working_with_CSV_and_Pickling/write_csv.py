from csv import writer, DictWriter

with open("fighters2.csv", 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])

with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })
