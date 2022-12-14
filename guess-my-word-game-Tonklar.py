# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)


# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    """
    loop for each letter in secret word:
        if the letter is not in the list:
            return False
    return True
    """


    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True




### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE..

    """
    guess_string = blank
    for every letter in secrec_word
        if the letter is in letter_guessed
            concatenate the letter on to guess_string
        else
            comcatenate "_ " on to guess_string
    
    """

    guess = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else:
            guess += "_ "

    return guess

# Testcases
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
#print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...


    """
    
    rest_word is blank 
    available is lower case alphabet
    for each letter in available 
        if the letter is not in:
            add letter to the rest_word
    return rest_word
    
    """

    rest_word = ""
    available = string.ascii_lowercase
    for letter in available:
        if letter not in letters_guessed:
            rest_word += letter
    return rest_word



# Testcases
#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))

def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print("Let the game begin!")
    print(f"I am thinking of a word with {len(secret_word)} letters.",end="\n\n")

    remaining_guess = 8
    guessed_letter = []

    while True:
        print(f"You have {remaining_guess} guesses remaining.")
        print(f"Letters available to you: {get_available_letters(guessed_letter)}")
        in_letter = input("Guess a letter: " )

        if len(in_letter) != 1 or in_letter.isalpha() == False:
            print("input ONE LETTER ONLY")
        else:
            if in_letter in guessed_letter:
                print("You fool! You tried this letter already:", end=" ")
            else:
                guessed_letter.append(in_letter)
                if in_letter in secret_word:
                    print("Correct:", end=" ")
                else:
                    print("Incorrect, this letter is not in my word:", end=" ")
                remaining_guess -= 1
        print(get_guessed_word(secret_word, guessed_letter), end="\n\n")

        if remaining_guess < 1:
            print(f"GAME OVER ! out of attempt The word was {secret_word}")
            break
        if is_word_guessed(secret_word, guessed_letter) == True:
            print(f"YOU WIN!")








def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)



# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()