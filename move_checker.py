
def move_available(user_char,letter_index, number_index, current_board):
    '''This function determines wether the tile picked is already occupied.
    If it is, then the current board is returned, otherwise the it is updated
    and a new board is returned'''
    
    while current_board[number_index - 1][letter_index] == f'  X  ' or current_board[number_index - 1][letter_index] == f'  O  ':
        
        print('\n\nTile is Occupied!\n')
        print('\n\nYour turn was skipped!\n')
        
        return current_board
        
    else: 
        current_board[number_index - 1][letter_index] = f'  {user_char}  '
        
        new_board = current_board
        
        return new_board
        
    
    
