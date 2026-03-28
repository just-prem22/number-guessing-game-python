import random

def play_game():
    number = random.randint(1, 100)
    level = input("Which level do you want HARD or EASY: ").lower()

    if level == "hard":
        total_lives = 5
    else:
        total_lives = 10

    while total_lives > 0:
        print(f"\nLives left: {total_lives}")
        guessed_number = int(input("Pick a number between 1 to 100: "))

        if guessed_number == number:
            print("Congratulations! You Won")
            break

        difference = abs(guessed_number - number)

        if guessed_number > number:
            if difference >= 20:
                print("TOO HIGH, try a smaller number")
            elif difference <= 5:
                print("TOO CLOSE, try a slightly smaller number")
            else:
                print("Keep guessing, you are close")
        else:
            if difference >= 20:
                print("TOO SMALL, try a larger number")
            elif difference <= 5:
                print("TOO CLOSE, try a slightly larger number")
            else:
                print("Keep guessing, you are close")

        total_lives -= 1

    if total_lives == 0:
        print("\n Game Over")
        print("The actual number was:", number)
play_game()
play_again = input("\nType 'yes' to play the game again: ").lower()
if play_again == "yes":
    print("\n" * 20)
    play_game()
