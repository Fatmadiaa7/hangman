import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to
    finish.
    """
    print("Loading word list from file…")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("", len(wordlist), " words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
    partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    name = input("What's your name?   ")
    num_letters = len(secret_word)
    num_warning = 3
    num_guesses = 6 # TODO: Change it to a global variable 
    letters_guessed = []
    print("Welcome,", name + ", " + "to the game Hangman!")
    print("I am thinking of a word that is", num_letters, "letters long.")
    while not is_word_guessed(secret_word, letters_guessed):
        print("----------------------")
        print("You have", num_guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter:  ")
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if str.isalpha(guessed_letter):
            guessed_letter = str.lower(guessed_letter)
            letters_guessed.append(guessed_letter)
            if guessed_letter in secret_word:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("good guess:", guessed_word)
            else:
                num_guesses-=1
                print("Oops! That letter is not in my word:", guessed_word)
        else:
            if num_warning == 0:
                num_guesses -= 1
                num_warning +=3 
                print("you have no warnings left so we have subtracted from your guesses and refilled your warnings now you have", num_guesses,"guesses and", num_warning,"warnings")
            else:
                num_warning -= 1
                print("Oops! That is not a valid letter." "You have", num_warning, "warnings left:", guessed_word)
        
        

        
        


    return 1



def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_ "
    return word 

def get_available_letters(letters_guessed):
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, "")
    return available_letters




wordlist = load_words()
# if __name__ == "__main__":
#     secret_word = choose_word(wordlist)
# uncomment the next line after implementing the function
secret_word = "apple"
hangman(secret_word)
