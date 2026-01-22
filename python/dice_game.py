import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    score = 0
    print("🎲 Dice Rolling Game")
    print("Press Enter to roll | type q to quit")

    while True:
        choice = input("Your choice: ").lower()

        if choice == "q":
            print("Game over! Your total rolls:", score)
            break

        dice_value = roll_dice()
        score += 1
        print("You rolled:", dice_value)

play_game()
