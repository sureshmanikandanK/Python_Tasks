def display_word_progress(secret_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def play_hangman():
    secret_word = "EVAPORATE"
    guessed_letters = set()
    correct_letters = set(secret_word)

    print("Welcome to Hangman!")
    print(display_word_progress(secret_word, guessed_letters))

    while correct_letters != guessed_letters:
        guess = input("Guess your letter: ").upper()
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in secret_word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            print("Incorrect!")
        
        print(display_word_progress(secret_word, guessed_letters))

    print(f"Congratulations! You've guessed the word: {secret_word}")

if __name__ == "__main__":
    play_hangman()
