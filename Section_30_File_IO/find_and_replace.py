def find_and_replace(file_name, old, new):
    with open(file_name) as file:
        sentance = file.read()
    with open(file_name, 'w') as file:
        file.write(sentance.replace(old, new))

find_and_replace('story.txt', 'Alice', 'Colt')

