from csv import reader, writer

with open('fighters.csv') as file:
    csv_reader = reader(file)
    with open('shout.csv', 'w') as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
