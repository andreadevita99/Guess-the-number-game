import random

def main():
    print("Welcome to the 'Guess the Number' game!")
    print("I have thought of a number between 1 and 100. Can you guess it?")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")

        if guess.lower() == 'exit':
            print("You have decided to end the game. See you next time!")
            break

        try:
            guess = int(guess)
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again!")
            elif guess > number_to_guess:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()