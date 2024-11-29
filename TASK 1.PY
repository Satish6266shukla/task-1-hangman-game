import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'developer', 'code', 'algorithm']

# Function to choose a random word
def choose_word(word_list):
    return random.choice(word_list)

# Function to play the Hangman game
def play_hangman():
    word_to_guess = choose_word(word_list)
    guessed_word = ['_'] * len(word_to_guess)
    attempts_left = 6  # Number of allowed incorrect guesses
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Your word has", len(word_to_guess), "letters.")
    print(" ".join(guessed_word))

    while attempts_left > 0 and '_' in guessed_word:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            attempts_left -= 1
            print("Incorrect guess. You have", attempts_left, "attempts left.")

        print(" ".join(guessed_word))

    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Game over! The word was:", word_to_guess)

# Run the game
play_hangman()
