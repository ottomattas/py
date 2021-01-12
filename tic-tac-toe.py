#!/usr/bin/env python
"""This is a simple interactive Tic-tac-toe game."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

import random

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

    # KEEP ASKING FOR PLAYER 1 MARKER
    while marker != 'X' and marker != 'O' :
        marker = input('Select which marker would you prefer to play first (X / O): ')

    # ASSIGN PLAYER 1 MARKER
    player1 = marker

    # ASSIGN PLAYER 2 MARKER
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
    if board[position] == ' ':
        return True
    else:
        return False

# DEFINE THE FULL BOARD CHECKING FUNCTION
def full_board_check(board):
    if board[1] and board[2] and board[3] and \
       board[4] and board[5] and board[6] and \
       board[7] and board[8] and board[9] != ' ':
        return True
    else:
        return False

# DEFINE THE PLAYER NEXT MOVE CHOICE FUNCTION
def player_choice(board):
    position = ''
    within_range = False
    
    while position.isdigit() == False or within_range == False or space_check() == False:
        position = input("Please enter your desired position (1-9): ")
        
        if position.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if position.isdigit() == True:
            if int(position) in range(1,9):
                within_range = True
            else:
                within_range = False

        if space_check() == True:
            return position
        else:
            print('The position is already taken, choose another one.')
            return False

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

# HERE IS THE GAME
print('Welcome to Tic-tac-toe!')

while True:
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    display_board()


    #while game_on:
        # Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break
