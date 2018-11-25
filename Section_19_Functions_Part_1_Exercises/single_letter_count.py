def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("greg", 'g'))
print(single_letter_count("greg", 'f'))
