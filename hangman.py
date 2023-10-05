import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in    guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
            else:
                attempts += 1
                print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()