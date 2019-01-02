def statistics(file_name):
    stats = {}
    with open(file_name) as file:
        lines = file.readlines()
        stats['lines'] = len(lines)
        file.seek(0)
        text = file.read()
        stats['characters'] = len(text)
        words = 0
        for sentance in lines:
            words += len(sentance.split(' '))
        stats['words'] = words
    return stats

print(statistics('story.txt'))
