import random

player_wins = 0
computer_wins = 0
winning_score = 2

while computer_wins < winning_score and player_wins < winning_score:
    print(f"\nPlayer Score: {player_wins}, Computer Score: {computer_wins}")
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
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    elif player1 == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    elif player1 == "scissors":
        if computer == "paper":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    else:
        print("Something went wrong")

if player_wins > computer_wins:
    print("Congradulations, You WON!!!")
else:
    print("Oh no, the computer won :(")
