#!/usr/bin/python

import random

def check_guess(guess):
    if guess == 'tails':
        return 0
    elif guess == 'heads':
        return 1

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)     # 0 is tails, 1 is heads

guess = check_guess(guess)

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()

    guess = check_guess(guess)

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
