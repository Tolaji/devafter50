import string

print("\n~~~ WORD PUZZLE ~~~")
print("~~~ Milestone ~~~\n")


# Set the secret word
secret_word = "pathwayconnect"

# Set up variables for the game
guess_count = 0
guessed_letters = set()
hidden_letter = ["_" for letter in secret_word]

# Welcome the player
print("Welcome to the word puzzle game! Can you guess the secret word?")
print("*" * 65)

# Loop until the player guesses the secret word
while "".join(hidden_letter) != secret_word:
    # Ask the player for a guess
    guess = input("Enter a letter: ").lower()

    # Count the number of attempts at guessing wrongly
    guess_count += 1
    print(f"Your guess count is {guess_count}")

    # Checks if guessed letter is a single letter and in lowercase
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("Please enter a single lowercase letter.")
        print("-" * 65)
        continue

    # Checks if guessed letter is a single letter and uppercase
    if len(guess) != 1 or guess in string.ascii_uppercase:
        print("Please enter a single lowercase letter.")
        print("-" * 65)
        continue

    # Check if the guess has already been made
    if guess in guessed_letters:
        print("You already guessed that letter, try again!")
        print("-" * 65)
        continue

    # Check if the guess is in the secret word
    if guess in secret_word:
        print("Great! You guessed a correct letter!")
        guessed_letters.add(guess)
        print("-" * 65)

    for i, letter in enumerate(secret_word):
        if letter == guess:
            hidden_letter[i] = letter.upper()

            print("".join(hidden_letter))
            print("-" * 65)
            break

    # Informs player the guess isn't in the secret word, increases the guess count
    else:
        print(f"The secret word is {len(secret_word)} characters")
        print("Your guessed word should be the same length as the secret word")
        print("Your guessed letter was not correct. Please try again.")
        print("-" * 65)
        print()

        # guessed_letters.add(guess)
        guess_count += 1

        # Print the current state of the hidden word and guessed letters
        print(" ".join(hidden_letter))
        print("Guessed letters:", " ".join(guessed_letters))
        print()
        print("-" * 60)

# If the player guesses the secret word, congratulate them and tell them how many guesses it took
print(f"Congratulations! You guessed the word in {guess_count} attempts.")
