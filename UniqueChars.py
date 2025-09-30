def find_unique_letters(word):
    word = word.lower()  # make it case-insensitive
    unique_letters = []

    for letter in word:
        if word.count(letter) == 1 and letter.isalpha():
            unique_letters.append(letter)

    return unique_letters

# Example usage
word = input("Enter a word: ")
unique = find_unique_letters(word)

print("Unique letters:", unique)
