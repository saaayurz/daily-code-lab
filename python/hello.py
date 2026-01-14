age_input = input("Enter your age: ")

if not age_input.isdigit():
    print("Please enter a valid number.")
else:
    age = int(age_input)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        years_left = 18 - age
        print("You are not eligible to vote yet.")
        print("You can vote in", years_left, "years.")
