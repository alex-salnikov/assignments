# 0. create file '5_letter_words.txt'
# https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
# https://www-cs-faculty.stanford.edu/~knuth/sgb.html

# 1. Implement a function word_list() that reads the 5_letter_words.txt file
# and returns a list of the words in the file.
def word_list():
    words = []
    with open("5_letter_words.txt", "r") as file:
    # read file line by line and output the lines
        for line in file:
            words.append(line.strip())
    return words

#all_words = word_list()
#print(all_words)


# 2. Implement a function random_word() that takes a list of words as a parameter
# and returns a random word from this list.
import random
def random_word(words):
    n = random.randint(0, len(words) - 1)
    return words[n]

#my_word = random_word(all_words)
#print(my_word)


# 3. Implement a function is_real_word() that takes two parameters, a guess
# and a word list and returns True if the word is in the word list
# and False otherwise.
def is_real_word(guess, words):
    exists = False
    if guess in words:
        exists = True
    return exists

# print(is_real_word(my_word, all_words))


# 4. Implement a function check_guess() that takes two parameters.
# The first is the guessed word and the second is the word the user has to find.
# check_guess() returns a string containing the following characters:
# - X for each character in the guess that is at the correct position.
# - O for each character in the guess that is in the word but not at the correct
# position.
# - _ for each character in the guess that is not part of the word.
# For example, check_guess("birds", "words") should return __XXX.
# - If a letter is used twice in the guessed word and exists only once in the word
# to be found, then only one letter in the return string is marked.
# In case one of the two letters is positioned correctly,
# then this letter is marked with an X in the return string.
# For example, check_guess("carat", "train") should return _OO_O.
# Another example, check_guess("taunt", "train") should return XO_O_

def check_guess(in_guess, in_secret):
    if(len(in_guess) != len(in_secret)):
        return 'error'

    guess = in_guess.lower()
    secret = in_secret.lower()

    mask = ''
    for i in range(0, len(guess)):
        m = '_'
        if guess[i] == secret[i]:
            m = 'X'
        mask += m

    for i in range(0, len(guess)):
        if(mask[i] != 'X'):
            mask2 = ''
            match = False
            for j in range(0, len(guess)):
                m = mask[j]
                if(match == False and m == '_'):
                    if guess[j] == secret[i]:
                        m = 'O'
                        match = True
                mask2 += m
            mask = mask2
            #print(':' + mask)
    return mask

#print(check_guess('Birds', 'Words'))    # __XXX
#print(check_guess("carat", "train"))    # _OO_O
#print(check_guess("taunt", "train"))    # XO_O_
#print(check_guess("crops", "visor"))    # _OO_O


# 5. Implement a function next_guess() that takes a word list as a parameter.
# The function asks the user for a guess, converts the guess to lower case
# and checks if the guess is in the word list. If this is the case,
# the guess is returned. Otherwise, the function asks the user for another guess.
def next_guess(words):
    while(True):
        new_guess = input('Please enter a guess: ').lower()
        if new_guess in words:
            return new_guess

#print(next_guess(all_words))


# 6. Implement a function play() that:
# - Uses the functions word_list and random_word to select a random 5 letter word.
# - Asks the user for a guess using the next_guess function.
# - Checks each guess using the check_guess function and shows the result to the user.
# - Checks if the users guessed the right word with six guesses or less.
# If yes, the user wins and the function prints You won!.
# Otherwise the user loses and the function prints You lost!
# as well as The word was: followed by word the user had to find.

def play():
    all_words = word_list()
    secret = random_word(all_words)
    #secret = 'birds'
    print('secret:' + secret)
    count = 6
    win = False
    while(count > 0):
        guess = next_guess(all_words)
        mask  = check_guess(guess, secret)
        print(mask)
        if(mask == 'X'*len(secret)):
            print('You won!')
            return
        count -= 1
    print('You lost!')
    print('The word was: ' + secret)

play()
