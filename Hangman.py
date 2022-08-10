# Amirreza Pazira
# 19 Nov 2020
# Assignment - 3 Problem - 2

# Importing packages for sys arguments and generating random word
import sys
import random
# Writing our variables
guess = 8
list_lexicon = []
incorrect2 = []
correct2 = []
inc = False
finish = 0
game = True
# Opening our text file and reading every line and put it in a list
file_input = open(sys.argv[1], "r")
lexicon = file_input.readline()
while lexicon != "":
    lexicon = lexicon.rstrip()
    list_lexicon.append(lexicon)
    lexicon = file_input.readline()
# Let the computer choose a random word (above 4 characters) from our file
b = random.choice(list_lexicon)
while len(b) < 4:   
    b = random.choice(list_lexicon)
# listing every character in a word and putting dash instead of them in another list
char = list(b)
dash = len(char)
word = list('_'*dash)
print('Welcome to CPSC 231 Console Hangman!')
# Making function to see if a character is in our word and finishing the game when the word is guessed
def check_guess(a):
    if a in char:
        print()
        print('Nice guess!')
        for i in range(len(char)):
            if char[i] == a:
                word[i] = a
                correct2.append(a)
                global finish
                finish = finish + 1
    if finish == len(word):
        global game
        game = False
        print()
        print('Congratulations!')
        print()
        print('You guessed the secret word:',b)
    elif a not in char:
        print()
        print('Sorry, there is no ',str(a),'.')
        incorrect2.append(a)
        global guess
        guess = guess - 1
        global inc
        inc = True
        
# Main game while loop when game = False the game will end    
while game:
    print()
    print('The secret word looks like:',*word)
    if inc:
        print()
        print('Your bad guesses so far:',*incorrect2)
    print()
    print('You have',guess,'guesses remaining.')
    print()
    choice = input('What’s your next guess? ')
    if choice in correct2:
        print()
        print('You have guessed this letter before guess again!')
    if choice in incorrect2:
        print()
        print('You have guessed this letter before guess again!')
    if choice not in correct2 and choice not in incorrect2:
        check_guess(choice)
    if guess == 0:
        print()
        print('The secret word was:',b)
        print('You lost try again!')
        break
# Closing our file
file_input.close()