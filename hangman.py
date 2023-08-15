from random_word import RandomWords

random_words = RandomWords()
word = random_words.get_random_word()

# Get the number of incorrect guesses allowed
while True:
    guesses = input('How many incorrect guesses allowed? ')
    try:
        guesses = int(guesses)
        if guesses <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive integer for the number of guesses.")

if guesses == 27042008:
    # Print secret message in green
    print("\033[92mYou have unlocked a secret message:")
    print("hello, from Sonny")
    print("\033[0m")  # Reset color to default
else:
    # Store the guessed letters
    guessed_letters = []

    # Main game loop
    while guesses > 0:
        print("Remaining guesses:", guesses)

        # Construct the guessed word with blanks for unguessed letters
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"
        print("Guessed word:", guessed_word)

        # Check if the word has been fully guessed
        if guessed_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        # Get the user's letter guess
        guess = input("Enter your letter guess: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is incorrect
        if guess not in word:
            guesses -= 1
            print("Incorrect guess. Try again.")

        # Check if the player has run out of guesses
        if guesses == 0:
            print("You ran out of guesses. The word was:", word)
