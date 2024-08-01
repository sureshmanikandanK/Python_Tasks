import random

def generate_secret_number():
    return str(random.randint(1000, 9999))

def calculate_cows_and_bulls(secret_number, guess):
    cows = bulls = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def play_cows_and_bulls():
    secret_number = generate_secret_number()
    guess_count = 0
    
    print("Welcome to the Cows and Bulls Game!")
    
    while True:
        user_guess = input("Enter a 4-digit number: ")
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue

        guess_count += 1
        cows, bulls = calculate_cows_and_bulls(secret_number, user_guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {guess_count} guesses.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    play_cows_and_bulls()
