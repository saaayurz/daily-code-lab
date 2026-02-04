import os

# File used to store student scores between runs
DATA_FILE = "scores.txt"
CSV_FILE = "scores.csv"


def load_scores():
	print(f"Loaded {len(scores)} student record(s).")

    scores = {}

    if not os.path.exists(DATA_FILE):
        return scores

    with open(DATA_FILE, "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            scores[name] = int(score)

    return scores


def save_scores(scores):
    with open(DATA_FILE, "w") as file:
        for name, score in scores.items():
            file.write(f"{name},{score}\n")


def export_to_csv(scores):
    if not scores:
        print("No data to export.")
        return

    with open(CSV_FILE, "w") as file:
        file.write("name,score\n")
        for name, score in scores.items():
            file.write(f"{name},{score}\n")

    print(f"Scores exported to {CSV_FILE}.")


def show_menu():
    print("\n📘 Student Score Tracker")
    print("1. Add or update student score")
    print("2. View all scores")
    print("3. View statistics")
    print("4. Export scores to CSV")
    print("5. Exit")


def add_student(scores):
    name = input("Enter student name: ").strip()
    score_input = input("Enter score (0–100): ")

    if not score_input.isdigit():
        print("Invalid score. Must be a number.")
        return

    score = int(score_input)

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    scores[name] = score
    save_scores(scores)
    print(f"Score saved/updated for {name}.")


def view_scores(scores):
    if not scores:
        print("No scores available.")
        return

    print("\n📋 Student Scores:")
    for name, score in scores.items():
        print(f"{name}: {score}")


def view_statistics(scores):
    if not scores:
        print("No data to analyze.")
        return

    values = list(scores.values())
    average = sum(values) / len(values)

    print("\n📊 Statistics")
    print("Average score:", f"{average:.2f}")
    print("Highest score:", max(values))
    print("Lowest score:", min(values))


def main():
    scores = load_scores()

    while True:
        show_menu()
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_student(scores)
        elif choice == "2":
            view_scores(scores)
        elif choice == "3":
            view_statistics(scores)
        elif choice == "4":
            export_to_csv(scores)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–5.")


main()
