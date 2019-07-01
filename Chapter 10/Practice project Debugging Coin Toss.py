# The task given was to fix bugs in the given code. This is my solution
import random
guess = ''
guessDict = {'tails':0,'heads':1} #Map input to a number
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = str(input())
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guessDict[guess]: #Use dict to check if correct guess
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = str(input()) #Convert to string, also guess spelled wrong
    if toss == guessDict[guess]:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')