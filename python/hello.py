age_input = input("Enter your age: ")

if not age_input.isdigit():
    print("Please enter a valid number.")
else:
    age = int(age_input)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")
