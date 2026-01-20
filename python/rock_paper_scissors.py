# Simple rock-paper-scissors game to practice basic game logic


import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("🎮 Rock, Paper, Scissors Game")
    print("Type rock, paper, or scissors")

    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

play_game()
