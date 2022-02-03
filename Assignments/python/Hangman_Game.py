#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

words=["habited","jacked","Robots","machine","nanny","fact","icon","labor","administrator","bellflower","docker","knowledge","early",
       "pace","sacred","unconditional","window"]

def hangman(tries):
    hangmans = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']

    print(hangmans[tries])

def select_word():
    word_selected = random.choice(words)
    word_selected = list(word_selected.upper())
    return word_selected

selected_word = select_word()
guessed_word = ['*'] * len(selected_word)
tries = 0


print("Welcome to python hangman game")
print("#" * 100)
hangman(6)

print("Guess this letter: ",  " ".join(guessed_word), "\n")

while True:
    print("")
    
    user_guess = input("Guess the letter of a word: ").upper()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("\n Invalid Character Try again")
        continue

    if user_guess not in selected_word:
        print("\nIncorrect guess")
        hangman(tries)
        tries = tries + 1

        if tries > 6:
            print("You lost the game")
            break

    elif user_guess in selected_word:
        if user_guess in guessed_word:
            print("\n Already Guessed try another")
            continue
        elif user_guess not in guessed_word:
            print("\n great!")
            for index, letter in enumerate(selected_word):
                if letter == user_guess:
                    guessed_word[index] = letter

            print("Guessing: ",  " ".join(guessed_word), "\n")

            if guessed_word == selected_word:
                print(" You Won the game !")
                break


# In[ ]:




