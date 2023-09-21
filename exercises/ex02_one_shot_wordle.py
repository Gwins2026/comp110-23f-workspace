"""EX02 - One-Shot Wordle"""

__author__ = "730561330"

secret: str = "python"

# prompts user for their guess
guess: str = input(f"What is your {len(secret)}-letter guess? ")
str(guess)

# makes sure the lengths of the word guessed and the secret word are the same
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
 
guess_idx: int = 0
blocks: str = ""
# goes through each letter of the guessed word
while guess_idx < len(secret):
    # checks to see if the guessed word is the same as the secret word
    if guess[guess_idx] == secret[guess_idx]:
        blocks += "\U0001F7E9"
    else:
        character_present: bool = False
        alt_idx: int = 0
        # goes through every letter of the secret word and checks for the guessed letter
        while character_present is False and alt_idx < len(secret):
            if guess[guess_idx] == secret[alt_idx]:
                character_present = True
            else:
                alt_idx += 1
        # adds a yellow block (correct, but wrong place) or white (incorrect) block to block string 
        if character_present is True:
            blocks += "\U0001F7E8"
        else:
            blocks += "\U00002B1C"
    guess_idx += 1
print(blocks)

# tells user if they guessed the word correctly or not
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite play again soon!")
