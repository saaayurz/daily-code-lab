# Ask the user for their age (input is always text)
age_input = input("Enter your age: ")

# Check if the input contains only digits
if not age_input.isdigit():
    print("Please enter a valid number.")
else:
    # Convert text input to an integer
    age = int(age_input)

    # Check voting eligibility
    if age >= 18:
        print("You are eligible to vote.")
    else:
        years_left = 18 - age
        print("You are not eligible to vote yet.")
        print("You can vote in", years_left, "years.")
