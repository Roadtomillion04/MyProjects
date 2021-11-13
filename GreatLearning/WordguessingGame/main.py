# Basic of hangman
import random
from words import words

def get_valid_word(words:list):
    word = random.choice(words)
    while '-' in word or ' ' in word: # to remove non-letter stuff
        word = random.choice(words)
    return word

word = get_valid_word(words)
lives = 20
correct_guess: list = ['_' for _ in range(len(word))]
print(correct_guess)

complete_word = '' # for win statement

while lives >= 0:
    if lives == 0:
        print('Game Over!')
        print(f'The actual word is {word}')
        break

    if complete_word == word:
        print('YOU win! yay..')
        print(f'You completed with {lives} lives left.')
        break

    ask_guess = input('Enter a letter: ')
    assert len(ask_guess) == 1, 'Please Enter a letter!'

    if ask_guess in word:
        print(f'{ask_guess} letter is at {word.index(ask_guess)}')

        correct_guess.pop(word.index(ask_guess))
        correct_guess.insert(word.index(ask_guess), ask_guess)
        print(correct_guess)
                                           # count - now replaces only 1 letter if there are 2
        if word.count(ask_guess) > 1:
            word = word.replace(ask_guess, '_', 1)
        #print(word)

        if correct_guess.count('_') == 0: # the dashes are replaced
            complete_word = word


    else:
        lives -=1
        print(f'you have {lives} lives left!')
        continue

