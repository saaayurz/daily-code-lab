import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("🎲 Dice Rolling Game")
    print("Press Enter to roll the dice or type q to quit")

    while True:
        choice = input("Your choice: ").lower()

        if choice == "q":
            print("Game ended. Thanks for playing!")
            break

        dice_value = roll_dice()
        print("You rolled:", dice_value)

play_game()
