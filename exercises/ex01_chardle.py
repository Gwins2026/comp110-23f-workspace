"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730561330"

word: str = input("Enter a 5-character word: ")
str(word)
if len(word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

letter: str = input("Enter a single character: ")
str(letter)
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)

num_of_letter: int = 0
if letter == word[0]:
    print(letter + " found at index 0")
    num_of_letter += 1
if letter == word[1]:
    print(letter + " found at index 1")
    num_of_letter += 1
if letter == word[2]:
    print(letter + " found at index 2")
    num_of_letter += 1
if letter == word[3]:
    print(letter + " found at index 3")
    num_of_letter += 1
if letter == word[4]:
    print(letter + " found at index 4")
    num_of_letter += 1

if num_of_letter == 0:
    print("No instances of " + letter + " found in " + word)
if num_of_letter == 1:
    print("1 instance of " + letter + " found in " + word)
if num_of_letter > 1:
    print(str(num_of_letter) + " instances of " + letter + " found in " + word)