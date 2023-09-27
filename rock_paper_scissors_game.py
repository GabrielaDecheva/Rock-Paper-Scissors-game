import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')
if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again.')

computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_move == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f'The computer chose {computer_move}.')

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You win!')
elif player_move == computer_move:
    print('Draw! Play again!')
else:
    print('You lose!')

new_game = input('Type [yes] to play or [no] to quit:')
while new_game == 'yes':
    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again.')

    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_move == 1:
        computer_move = rock
    elif computer_move == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('You win!')
    elif player_move == computer_move:
        print('Draw! Play again!')
    else:
        print('You lose!')

    new_game = input('Type [yes] to play or [no] to quit:')
