import random
import character_selector
import tic_tac_toe_instructions
import move_selector
import comp_char
import indexing
import move_checker
import win_checker
import show
import draw_checker

game_active = True

tic_tac_toe_instructions.show_instructions()

column_letters = '      A      B       C '
top_border = '     __      __      __'
row_1 = ['|__|','|__|','|__|']
row_2 = ['|__|','|__|','|__|']
row_3 = ['|__|','|__|','|__|']

board = [row_1, row_2, row_3]

user_char = character_selector.char_select()

computer_char = comp_char.return_char(user_char, 'X', 'O')

while game_active:
    
    print('\n\nYour Turn:\n')
    
    move_select = move_selector.select_move()
    letter_index = indexing.letter_indexing(move_select[0])
    number_index = int(move_select[1])
    board = move_checker.move_available(user_char, letter_index, number_index, board)
    
    show.show_board(column_letters, top_border, board)
    
    game_active = draw_checker.draw_game(board)
    
    if game_active == False:
        print('\n\nDRAW MATCH!\n\n')
        break
            
    game_active = win_checker.end_game(board)
    
    if game_active == False:
        print('\n\nYOU WIN!\n\n')
        break
    
    print('Player 2 Turn:\n')
    
    move_select = move_selector.select_move()
    letter_index = indexing.letter_indexing(move_select[0])
    number_index = int(move_select[1])
    board = move_checker.move_available(computer_char, letter_index, number_index, board)
    
    show.show_board(column_letters, top_border, board)
    
    game_active = draw_checker.draw_game(board)
    
    if game_active == False:
        print('\n\nDRAW MATCH!\n\n')
        break

    game_active = win_checker.end_game(board)
    
    if game_active == False:
        print('\n\nPLAYER 2 WIN!\n\n')
        break
        
