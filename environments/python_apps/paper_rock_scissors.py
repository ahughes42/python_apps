from random import randint
import sys


valid_choices = ['r', 'p', 's']
player = input('rock (r), paper (p), or scissors (s)?')

while player not in valid_choices:
    print('Player must choose r, p, or s!')
    print('Try again!')
    player = input ('rock (r), paper (p), or scissors (s)?')
else:
    print(player, 'vs', end=' ')

chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if player == computer:
    print('Its a draw!')
elif player == 'r' and computer == 'p':
    print('Computer Wins!')
elif player == 'r' and computer == 's':
    print('Player Wins!')
elif player == 'p' and computer == 'r':
    print('Player Wins!')
elif player == 'p' and computer == 's':
    print('Computer Wins!')
elif player == 's' and computer == 'r':
    print('Computer Wins!')
elif player == 's' and computer == 'p':
    print('Player Wins!')