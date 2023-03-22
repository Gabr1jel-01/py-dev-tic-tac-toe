"""
Title:     Krizic - Kruzic / Tic Tac Toe
Author:    Pero Peric
Date:      2023-03-22
Version:   v0.1

"""

import random
import os 


game_board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
player = 1
player_label = 'X'
counter = 1


def display_board() -> None:
    #os.system('cls')
    print()
    print('\tALGEBRA d.o.o.')
    print()
    print('\t Krizic Kruzic')
    print()
    print('Igrac 1 (X)\t Igrac 2 (O)')
    print()
    #print(f'{"ALGEBRA d.o.o.":>25}')
    print('\t   |   |')
    print(f'\t {game_board[1]} | {game_board[2]} | {game_board[3]} ')
    print('\t___|___|___')
    print('\t   |   |   ')
    print(f'\t {game_board[4]} | {game_board[5]} | {game_board[6]} ')
    print('\t___|___|___')
    print('\t   |   |   ')
    print(f'\t {game_board[7]} | {game_board[8]} | {game_board[9]} ')
    print('\t   |   |   ')
    print()
    #print('\t   |   |   ')
    #print('\t   |   |   ')


def change_current_player():
    global player, player_label, counter
    if counter % 2 == 0:
        
        player = 1
        player_label = 'X'
    else:
        player = 2
        player_label = 'O'
    counter += 1


while  True:
    display_board()

    print(f'Igrac {player}  ({player_label}) je na potezu')
    board_field_number = int(input('Unesite broj polja na ploci: '))
    
    if board_field_number == 1 and game_board[board_field_number] == 1:
        game_board[board_field_number] = player_label
    elif board_field_number == 2 and game_board[board_field_number] == 2:
        game_board[board_field_number] = player_label
    elif board_field_number == 3 and game_board[board_field_number] == 3:
        game_board[board_field_number] = player_label
    elif board_field_number == 4 and game_board[board_field_number] == 4:
        game_board[board_field_number] = player_label
    elif board_field_number == 5 and game_board[board_field_number] == 5:
        game_board[board_field_number] = player_label
    elif board_field_number == 6 and game_board[board_field_number] == 6:
        game_board[board_field_number] = player_label
    elif board_field_number == 7 and game_board[board_field_number] == 7:
        game_board[board_field_number] = player_label
    elif board_field_number == 8 and game_board[board_field_number] == 8:
        game_board[board_field_number] = player_label
    elif board_field_number == 9 and game_board[board_field_number] == 9:
        game_board[board_field_number] = player_label
    else:
        print('Krivi unos')
        counter += 1
        
    
    
    
    change_current_player()
    
    #if player == 1:
        #player = 2
    #else:
        #player = 1 




