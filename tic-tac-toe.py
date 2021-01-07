#!/usr/bin/env python
"""This is a simple interactive Tic-tac-toe game."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE GAME BOARD DISPLAY FUNCTION
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')

# DEFINE THE PLAYER MARKER SELECTION FUNCTION
def player_input():
    marker = ''

    # KEEP ASKIGN FOR PLAYER 1 MARKER
    while marker != 'X' and marker != 'O' :
        marker = input('Select which marker would you prefer to play first (X / O): ')

    # ASSIGN PLAYER 2 MARKER
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    # VERIFY PLAYER MARKERS
    print(player1 + ' goes first, then ' + player2)

    # RETURN A TUPLE FOR ASSIGNING THE MARKERS DIRECTLY TO A VARIABLE LATER
    return(player1 , player2)

# ASSIGN A MARKER VARIABLE RETURNED FROM THE INPUT FUNCTION
player1_marker , player2_marker = player_input()