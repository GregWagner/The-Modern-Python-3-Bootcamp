import random

response = 'y'

while response.lower() == 'y':
    random_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != random_number:
        if guess < random_number:
            state = "low"
        else:
            state = "high"
        print(f"Too {state}, try again!")
        guess = int(input("Guess a number between 1 and 10: "))
    print("You guessed it! You won!")
    response = input("Do you want to keep playing? (y/n) ")
print("Thank you for playing")
