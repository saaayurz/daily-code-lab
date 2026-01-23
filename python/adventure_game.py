def start_game():
    print("🧭 Welcome to the Adventure Game")
    print("You are standing at a crossroad.")

    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        print("You walk into a forest 🌲")
        action = input("Do you climb a tree or walk forward? ").lower()

        if action == "climb":
            print("You see a beautiful view and find treasure! 🎉")
        elif action == "walk":
            print("You meet a friendly traveler and gain wisdom.")
        else:
            print("You got confused and returned home safely.")

    elif choice == "right":
        print("You reach a river 🌊")
        action = input("Do you swim or build a boat? ").lower()

        if action == "swim":
            print("The water is cold, but you make it across!")
        elif action == "boat":
            print("Your boat works perfectly. Smooth journey!")
        else:
            print("You wait too long and it gets dark.")

    else:
        print("Unable to decide, you stay where you are.")

start_game()
