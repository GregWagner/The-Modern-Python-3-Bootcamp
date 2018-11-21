# create a list with the first letter of each name
answer = [c[0] for c in ["Elie", "Tim", "Matt"]]
print(answer)

# create a list of all the even vales
answer2 = [x for x in list(range(1, 7)) if x % 2 == 0]
print(answer2)

# create list of the intersection of 2 lists
answer = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]
print(answer)

# reverse and upper case each word
answer2 = [word.lower()[::-1] for word in ["Elie", "Tim", "Matt"]]
print(answer2)

# numbers divisible by 12 between 1 and 100
answer = [x for x in list(range(1, 101)) if x % 12 == 0]
print(answer)

# remove the vowels
answer = [c for c in "amazing" if c not in "aeiou"]
print(answer)

# create a nested list of [0, 1, 2] three times
answer = [[x for x in range(3)] for i in range(3)]
print(answer)

# create a 10x10 matrix
answer = [[x for x in range(10)] for i in range(10)]
print(answer)
