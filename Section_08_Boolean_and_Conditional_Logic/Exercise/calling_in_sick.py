from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = False

if sick_days > 0:
    if actually_sick:
        calling_in_sick = True
    elif kinda_sick:
        calling_in_sick = True
    elif hate_your_job:
        calling_in_sick = True
