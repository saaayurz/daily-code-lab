def get_valid_age():
    """
    Ask the user for their age.
    Return an integer if valid.
    Return None if invalid.
    """
    user_input = input("Enter your age: ")

    # Check if input contains only digits
    if not user_input.isdigit():
        return None

    age = int(user_input)

    # Age should not be negative or unrealistically high
    if age < 0 or age > 120:
        return None

    return age

def analyze_voting_eligibility(age):
    """
    Analyze voting eligibility.
    Returns a dictionary with detailed results.
    """
    result = {
        "age": age,
        "eligible": False,
        "years_left": 0
    }

    if age >= 18:
        result["eligible"] = True
    else:
        result["years_left"] = 18 - age

    return result

def display_result(analysis):
    """
    Display voting eligibility result in a friendly format.
    """
    if analysis["eligible"]:
        print(f"You are eligible to vote at age {analysis['age']}.")
    else:
        print(f"You are not eligible to vote at age {analysis['age']}.")
        print(f"You can vote in {analysis['years_left']} years.")

def main():
    while True:
        age = get_valid_age()

        if age is None:
            print("Invalid age. Please enter a valid number between 0 and 120.")
        else:
            analysis = analyze_voting_eligibility(age)
            display_result(analysis)

        choice = input("Do you want to check another age? (y/n): ").lower()
        if choice != "y":
            print("Goodbye!")
            break


# Program entry point
main()
