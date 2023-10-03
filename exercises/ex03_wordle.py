"""EX03 - Structured Wordle."""

__author__ = "730561330"


def contains_char(secret: str, guess: str) -> bool:
    """Determines if a specific character is found anywhere in a given word."""
    assert len(guess) == 1
    char_present: bool = False
    idx: int = 0
    # checks for the guess's letter in each index of the secret word
    while idx < len(secret):
        if guess == secret[idx]:
            char_present = True
        idx += 1
    # returns the status of finding the character to the function
    if char_present is False:
        return False
    else:   # the character is not found in the secret word
        return True


def emojified(guess: str, secret: str) -> str:
    """Builds the emoji colored blocks of a guess."""
    assert len(guess) == len(secret)
    emoji_line: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji_line += "\U0001F7E9"
        # checks for the letter in different indexs of the word using contains_char function
        elif contains_char(secret, guess[idx]) is True:
            emoji_line += "\U0001F7E8"
        else:   # the letter is not found in word, contains_char function expresses False
            emoji_line += "\U00002B1C"
        idx += 1
    return emoji_line


def input_guess(expected_length: int) -> str:
    """Makes sure user's guess is the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = ""
    turn: int = 0
    # while there are more turns left and the word has not been guessed correctlty...
    while turn <= 5 and guess != secret:
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
    if secret == guess:
        print(f"You win in {turn}/6 turns!")
    else:   # user did not guess the word in 6 tries
        print("X/6 - Sorry, try again Tomorrow!")


# allows program to run as a module and for other programs to import/use functions
if __name__ == "__main__":
    main()