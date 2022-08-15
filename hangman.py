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
    num_guesses = 6  # TODO: Change it to a global variable
    letters_guessed = []
    print("Welcome,", name + ", " + "to the game Hangman!")
    print("I am thinking of a word that is", num_letters, "letters long.")
    while not is_word_guessed(secret_word, letters_guessed):
        if num_guesses == 0:
            break
        print("----------------------")
        print("You have", num_guesses, "guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters:", available_letters)
        guessed_letter = input("Please guess a letter:  ")
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if str.isalpha(guessed_letter):
            guessed_letter = str.lower(guessed_letter)
            if guessed_letter not in available_letters:
                if num_warning == 0:
                    num_guesses -= 1
                    num_warning += 3
                    print("you have no warnings left so we have subtracted from your guesses and refilled your warnings now you have",
                          num_guesses, "guesses and", num_warning, "warnings")
                    print(guessed_word)
                else:
                    num_warning -= 1
                    print("Oops! You've already guessed that letter. You now have",
                          num_warning, "warnings:", guessed_word)
                    continue
            letters_guessed.append(guessed_letter)
            if guessed_letter in secret_word:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("good guess:", guessed_word)
            else:
                if isvowel(guessed_letter):
                    num_guesses -= 2
                else:
                    num_guesses -= 1
                print("Oops! That letter is not in my word:", guessed_word)
        else:
            if num_warning == 0:
                num_guesses -= 1
                num_warning += 3
                print("you have no warnings left so we have subtracted from your guesses and refilled your warnings now you have",
                      num_guesses, "guesses and", num_warning, "warnings")
            else:
                num_warning -= 1
                print("Oops! That is not a valid letter." "You have",
                      num_warning, "warnings left:", guessed_word)

    if is_word_guessed(secret_word, letters_guessed):
        print(" Congratulations, you won!")
        num_unique_letters = unique_letter(secret_word)
        score = calc_score(num_guesses, num_unique_letters)
        print("Your total score for this game is", score)
    else:
        print("Sorry, you ran out of guesses.The word was", secret_word)


def hangman_with_hints(secret_word):
    name = input("What's your name?   ")
    num_letters = len(secret_word)
    num_warning = 3
    num_guesses = 6  # TODO: Change it to a global variable
    letters_guessed = []
    print("Welcome,", name + ", " + "to the game Hangman!")
    print("I am thinking of a word that is", num_letters, "letters long.")
    while not is_word_guessed(secret_word, letters_guessed):
        if num_guesses == 0:
            break
        print("----------------------")
        print("You have", num_guesses, "guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters:", available_letters)
        guessed_letter = input("Please guess a letter:  ")
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if str.isalpha(guessed_letter):
            guessed_letter = str.lower(guessed_letter)
            if guessed_letter not in available_letters:
                if num_warning == 0:
                    num_guesses -= 1
                    num_warning += 3
                    print("you have no warnings left so we have subtracted from your guesses and refilled your warnings now you have",
                          num_guesses, "guesses and", num_warning, "warnings")
                    print(guessed_word)
                else:
                    num_warning -= 1
                    print("Oops! You've already guessed that letter. You now have",
                          num_warning, "warnings:", guessed_word)
                    continue
            letters_guessed.append(guessed_letter)
            if guessed_letter in secret_word:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("good guess:", guessed_word)
            else:
                if isvowel(guessed_letter):
                    num_guesses -= 2
                else:
                    num_guesses -= 1
                print("Oops! That let                                                                                                     ter is not in my word:", guessed_word)
        elif guessed_letter == '*':
            show_possible_matches(guessed_word)   
        else:
            if num_warning == 0:
                num_guesses -= 1
                num_warning += 3
                print("you have no warnings left so we have subtracted from your guesses and refilled your warnings now you have",
                        num_guesses, "guesses and", num_warning, "warnings")
            else:
                num_warning -= 1
                print("Oops! That is not a valid letter." "You have",
                        num_warning, "warnings left:", guessed_word)


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


def isvowel(letter):
    vowels = "auieo"
    if letter in vowels:
        return True
    else:
        return False


def unique_letter(word):
    str = ""
    num = 0
    for letter in word:
        if letter not in str:
            str += letter
            num += 1
    return num

# def unique_letter_2(word):
#     s = set(word)
#     return len(s)


def calc_score(num_guesses, num_unique_letters):
    return num_guesses * num_unique_letters * 100


def match_with_gaps(guessed_word, other_word):
    guessed_word = guessed_word.replace(" ", "")
    if len(guessed_word) == len(other_word):
        for i in range(len(guessed_word)):
            letter = guessed_word[i]
            if letter == '_':
                if other_word[i] in guessed_word:
                    return False
                guessed_word.index(letter) 
                continue
            else:
                if letter == other_word[i]:
                    continue
                else:
                    return False
    else:
        return False
    return True


def show_possible_matches(guessed_word):
    list = ""
    for word in wordlist:
        if match_with_gaps(guessed_word, word):
            list += word + " "
    print(list)


        



wordlist = load_words()
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
#uncomment the next line after implementing the function

#hangman(secret_word)
hangman_with_hints(secret_word)

