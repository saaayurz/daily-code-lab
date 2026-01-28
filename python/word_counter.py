# Simple word counter utility
# Counts characters, words, and lines in user input

def count_words():
    # Take text input from the user
    text = input("Enter a sentence or paragraph:\n")

    # Count total characters
    characters = len(text)

    # Count words by splitting on spaces
    words = len(text.split())

    # Count lines based on newline characters
    lines = text.count("\n") + 1

    # Display results
    print("\n📊 Text Analysis")
    print("Characters:", characters)
    print("Words:", words)
    print("Lines:", lines)


count_words()
