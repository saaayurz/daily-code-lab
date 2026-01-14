age = input("Enter your age: ")

if age.isdigit():
    age = int(age)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")
else:
    print("Please enter a valid number.")
