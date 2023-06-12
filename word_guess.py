"""
File: word_guess.py
-------------------
This application will let the user guess a randomly picked word within the application one
alphabet at a time. When ever the user guesses the right alphabet the application will reward 
the user by ignoring the number of attempts, and on the other hand when ever the user guesses a
wrong alphabet the application will charge the user one attempt. which makes the number of attempts
fewer. The game will stop on two scenarios one, when the user runs out of attempt with out guessing
the whole word, and the second is when the user guesses the whole word in fewer attempts than the
user is allowed
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):
    """
    This function will recieve a single word input from the user and
    checks if it exists in the randomly picked word from the stored file
    list.
    """
    INITIAL_GUESSES = 8
    hidden_word = ""
    for word in secret_word:
        if word.isalpha():
            hidden_word += "- "
        else:
            hidden_word += word
    print("The word now looks like this: ", hidden_word)

# here we will ask the user to guess the word until the length of the
# secret word

    while INITIAL_GUESSES > 0:
        user_guess = str(
            input("Type a single letter here, then press enter: "))

        """
        Then we will check whether the user input is valid or not
        """
        if user_guess.isalpha() and len(user_guess) == 1:
            valid_input = False
            new_hidden_word = ""
            # here we will check if the user input exists in the secret word
            for i in range(len(secret_word)):
                if hidden_word[2 * i] != "-":
                    new_hidden_word += hidden_word[2 * i] + " "
                elif user_guess.upper() == secret_word[i].upper():
                    new_hidden_word += secret_word[i] + " "
                    valid_input = True
                else:
                    new_hidden_word += "- "
            if valid_input:
                print("That guess is correct.")
            else:
                INITIAL_GUESSES -= 1
                print("You have", INITIAL_GUESSES, "guesses left.")
                print("There are no", user_guess.upper() + "'s in the word.")

            hidden_word = new_hidden_word
            print("The word now looks like this:", hidden_word)

            if "- " not in hidden_word:
                print("Congratulations! You guessed the word correctly!")
                break

            if INITIAL_GUESSES == 0:
                print("Sorry, you ran out of guesses. The word was:", secret_word)
                break


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    #here we open the file with a read right 
    with open(LEXICON_FILE, 'r') as file:
        word_list = file.read().splitlines()

    # Here we will randomly choose a word from the opened file
    secret_word = random.choice(word_list)

    return secret_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
