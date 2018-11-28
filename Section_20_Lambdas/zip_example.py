midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# create a dictionary with student and their high score
#final_grades = [max(pair) for pair in zip(midterms, finals)]
final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades)

# could also be done as;
scores = dict(zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
))
print(scores)
