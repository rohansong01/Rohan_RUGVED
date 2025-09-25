text = input("Enter the text you want to analyze: ")

letter_count = 0
sentence_count = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    elif char in ['.', '!', '?']:
        sentence_count += 1

words = text.split()
word_count = len(words)

if word_count == 0:
    print("Grade Level: Before Grade 1 (No text entered)")
else:
    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    if grade >= 16:
        print("Grade Level: 16+")
    elif grade < 1:
        print("Grade Level: Before Grade 1")
    else:
        print(f"Grade Level: {grade}")