
import time
import random
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)
# A List Of Secret Words for picking so don't peek here
words = ['funny', 'gossip', 'pixel', 'quiz', 'hangman', 'cycle', 'boggle', 'unknown', 'vortex', 'wave', 'youthful',
         'zombie', 'strength', 'equip', 'scratch', 'joking', 'jigsaw']
word = random.choice(words)
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nguess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print("\nYou Lose")
            print(f"The word was \'{word}\'")
