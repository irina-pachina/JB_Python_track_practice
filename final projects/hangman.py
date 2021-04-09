# implementation of the game of guessing word letter by letter
# program asks the user to enter the letters, prints word with uncovered letters and counts misses
# game ends when the word is uncovered or the user spends 8 'lives'
import random


def play():
    possible_words = ['python', 'java', 'kotlin', 'javascript']
    current_word = random.choice(possible_words)
    need_print = []
    guessed_letters = []
    lives = 8

    while lives != 0:
        print()
        progress = "".join([x if x in need_print else "-" for x in current_word])
        if "-" in progress:
            print(progress)
        else:
            print(progress)
            print("You guessed the word!\nYou survived!")
            break

        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter.isupper() or not letter.isalpha():
            print("Please enter a lowercase English letter")
        elif letter in guessed_letters:
            print("You've already guessed this letter")
        elif letter not in current_word:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            need_print.append(letter)

        guessed_letters.append(letter)

    if lives == 0:
        print("You lost!")


print("H A N G M A N")
choice = input('Type "play" to play the game, "exit" to quit:')

while 1:
    if choice == "play":
        play()
        choice = input('Type "play" to play the game, "exit" to quit:')
    elif choice == "exit":
        exit()
    else:
        choice = input('Type "play" to play the game, "exit" to quit:')
