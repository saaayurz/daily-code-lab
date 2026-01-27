def count_words():
    text = input("Enter a sentence or paragraph:\n")

    characters = len(text)
    words = len(text.split())
    lines = text.count("\n") + 1

    print("\n📊 Text Analysis")
    print("Characters:", characters)
    print("Words:", words)
    print("Lines:", lines)


count_words()
