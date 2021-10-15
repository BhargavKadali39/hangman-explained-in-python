import random

a = ['Gas', 'Food', 'Gym', 'Health']
word = random.choice(a)
your_guess = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in your_guess:
            print(char, end="")
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nguess a character:")
    your_guess += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print("\nYou Lose")
