def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in set(word)}


print(multiple_letter_count("awesome"))
