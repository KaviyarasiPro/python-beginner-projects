import random

words = ["python", "computer", "developer", "programming", "keyboard"]

word = random.choice(words)
guessed_letters = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("Game over!")
    print("The word was:", word)

