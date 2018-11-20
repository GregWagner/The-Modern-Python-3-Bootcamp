import random

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer selects {computer}")

if player1 == computer:
    print("Its a tie!")

elif player1 == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")

elif player1 == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")

elif player1 == "scissors":
    if computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

else:
    print("Something went wrong")
