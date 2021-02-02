#!/usr/bin/env python
"""This is a simple interactive Tic-tac-toe game."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.9"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Testing"

import random

# DEFINE THE GAME BOARD DISPLAY FUNCTION
def display_board(board):

    # PRINT EMPTY LINES TO CLEAR PREVIOUS VIEW
    print('\n' * 60)
    print('\t   BOARD   ')
    print('\t-----------')
    print('\t   |   |   ')
    print('\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t   |   |   ')
    print('\t-----------')
    print('\t   |   |   ')
    print('\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t   |   |   ')
    print('\t-----------')
    print('\t   |   |   ')
    print('\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t   |   |   ')
    print('\t-----------')
    print()

# DEFINE THE PLAYER MARKER SELECTION FUNCTION
# OUTPUT = (Player 1 marker, Player 2 marker)
def player_input():
    marker = ''

    # KEEP ASKING FOR PLAYER 1 MARKER
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Select which marker would you prefer to play (X / O): ').upper()
        print('\n' * 60)

    # ASSIGN AND RETURN PLAYER MARKERS
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

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
        return 'Player 1'
    else:
        return 'Player 2'

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
        position = int(input(
        '1|2|3\tAvailable\n'
        '-----\tpositions\n'
        '4|5|6\t<--------\n'
        '-----\tPlease enter your\n'
        '7|8|9\tdesired position (1-9): '))
    return position

# DEFINE THE REPLAY FUNCTION
def replay():
    restart = ''

    # KEEP ASKING FOR PLAYER CHOICE
    while restart != 'Y' and restart != 'N' :
        restart = input('Play again (Y / N): ').upper()[0]

    if restart == 'Y':
        print('\n' * 60)
        print('Here we go again. Good luck to both players!')
        return True
    else:
        print('\n' * 60)
        print('You have had enough for now. See you later!')
        return False

####################
# HERE IS THE GAME #
####################

# WELCOME PLAYER
print('\n' * 60)
print('Welcome to Tic-tac-toe!')

# START GAME
while True:

    # DEFINE VARIABLES
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # TUPLE UNPACKING FOR GETTING PLAYER MARKERS
    player1_marker, player2_marker = player_input()
    turn = choose_first()

    # VERIFY FIRST TURN
    print(turn + ' will go first.')

    # KEEP ASKING FOR PLAYER INPUT ON STARTING
    play_game = input('Do you wish to start the game now (Y / N): ').upper()[0]

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # START THE GAME
    while game_on:

        # PLAYER 1 MOVES
        if turn == 'Player 1':
                        
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            # PLAYER 1 WINS
            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:

                # CHECK FOR DRAW
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break

                # PASS THE TURN TO PLAYER 2
                else:
                    turn = 'Player 2'
        else:

            # PLAYER 2 MOVES
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            # PLAYER 2 WINS
            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations. Player 2 has won the game!')
                game_on = False
            else:

                # CHECK FOR DRAW
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break

                # PASS THE TURN TO PLAYER 1
                else:
                    turn = 'Player 1'

    # CHECK FOR REPLAY
    if not replay():
        break
