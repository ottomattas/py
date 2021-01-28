#!/usr/bin/env python
"""This is a simple interactive Tic-tac-toe game."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.2"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

import random

# DEFINE THE GAME BOARD DISPLAY FUNCTION
def display_board(board):
    # PRINT EMPTY LINES TO CLEAR PREVIOUS VIEW
    print('\n' * 40)
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')

# DEFINE THE PLAYER MARKER SELECTION FUNCTION
def player_input():
    marker = ''

    # KEEP ASKING FOR PLAYER 1 MARKER
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Select which marker would you prefer to play (X / O): ').upper()

    # ASSIGN AND RETURN PLAYER MARKERS
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

    # RETURN A TUPLE FOR ASSIGNING THE MARKERS DIRECTLY TO A VARIABLE LATER
    return(player1 , player2)

# ASSIGN A MARKER VARIABLE RETURNED FROM THE INPUT FUNCTION
player1_marker , player2_marker = player_input()

# DEFINE THE MARKER PLACEMENT FUNCTION
def place_marker(board, marker, position):
    board[position] = marker

# DEFINE THE WIN VALIDATION FUNCTION
def win_check(board, marker):
    if (board[1] == board[2] == board[3] == marker) or \
    (board[4] == board[5] == board[6] == marker) or \
    (board[7] == board[8] == board[9] == marker) or \
    (board[1] == board[5] == board[9] == marker) or \
    (board[3] == board[5] == board[7] == marker) or \
    (board[1] == board[4] == board[7] == marker) or \
    (board[2] == board[5] == board[8] == marker) or \
    (board[3] == board[6] == board[9] == marker):
        return True
    else:
        return False

# DEFINE THE FUNCTION TO ASSIGN THE FIRST MOVER
def choose_first():
    if random.randint(1 , 2) == 1:
        return player1_marker
    else:
        return player2_marker

# DEFINE THE SPACE CHECKING FUNCTION
def space_check(board, position):
    return board[position] == ' '

# DEFINE THE FULL BOARD CHECKING FUNCTION
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
        return False
    return True

# DEFINE THE PLAYER NEXT MOVE CHOICE FUNCTION
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please enter your desired position (1-9): '))
            return position

# DEFINE THE REPLAY FUNCTION
def replay():
    restart = ''
    # KEEP ASKING FOR PLAYER CHOICE
    while restart != 'Y' and restart != 'N' :
        restart = input('Play again (Y / N): ')

    if restart == 'Y':
        print('Here we go again. Good luck to both players!')
        return True
    else:
        print('You have had enough for now. See you later!')
        return False

####################
# HERE IS THE GAME #
####################

while True:

    # DEFINE VARIABLES
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    game_on = ' '

    # VERIFY FIRST TURN
    print(turn + ' will go first.')

    # KEEP ASKING FOR PLAYER INPUT ON STARTING
    while game_on != 'Y' and game_on != 'N' :
        game_on = input('Do you wish to start the game now (Y / N): ')

    #while game_on:
        # Player 1 Turn
        
        
        # Player2's turn.
            #pass

    if not replay():
        break
