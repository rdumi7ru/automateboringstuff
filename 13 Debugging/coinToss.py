#!/usr/bin/python3
# coinToss.py

import random

coin = ['heads', 'tails']
toss = str(random.choice(coin))
guess = input('You call it, heads or tails?\n')

while guess not in coin:
    print("Sorry, %s is not valid!" % (guess))
    guess = input('Go on then call it, heads or tails?\n')
win = 'That was it!'
if toss == guess:
    print(win)
else:
    print("That wasn't it! Guess again.")
    guess = input('Come on, heads or tails?\n')
    while guess not in coin:
        print('Sorry, %s is not valid!' % (guess))
        guess = input('heads or tails?\n')
    if toss == guess:
        print('%s, I was warried there for a second.' % (win))
    else:
        print('Congratulations! You have redefined failure')
