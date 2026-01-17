def get_user_age():
    """
    Prompt the user for their age.
    Returns an integer if valid, otherwise None.
    """
    user_input = input("Enter your age: ")

    if not user_input.isdigit():
        return None

    age = int(user_input)

    if age < 0 or age > 120:
        return None

    return age


def analyze_life_stage(age):
    """
    Determine life stage based on age.
    Returns a dictionary with results.
    """
    result = {
        "age": age,
        "stage": "",
        "message": ""
    }

    if age < 13:
        result["stage"] = "Child"
        result["message"] = "You are in your childhood years."
    elif age < 18:
        result["stage"] = "Teenager"
        result["message"] = "You are a teenager, a phase of learning and growth."
    elif age < 30:
        result["stage"] = "Young Adult"
        result["message"] = "You are a young adult, building your future."
    elif age < 60:
        result["stage"] = "Adult"
        result["message"] = "You are an adult with experience and responsibility."
    else:
        result["stage"] = "Senior"
        result["message"] = "You are a senior, rich with life experience."

    return result


def display_result(result):
    print(f"Age: {result['age']}")
    print(f"Life Stage: {result['stage']}")
    print(result["message"])


def main():
    while True:
        age = get_user_age()

        if age is None:
            print("Invalid input. Please enter an age between 0 and 120.")
        else:
            analysis = analyze_life_stage(age)
            display_result(analysis)

        choice = input("Do you want to check another age? (y/n): ").lower()
        if choice != "y":
            print("Goodbye!")
            break


# Program entry point
main()
