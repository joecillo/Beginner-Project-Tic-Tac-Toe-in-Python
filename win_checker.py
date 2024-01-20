
def end_game(board):
    
    '''this function assess the board throughout the game if a player has already won'''
    
    game_continue = True
    
    if board[0] == ['  X  ','  X  ','  X  '] or board[0] == ['  O  ','  O  ','  O  ']:
        game_continue = False
    elif board[1] == ['  X  ','  X  ','  X  '] or board[1] == ['  O  ','  O  ','  O  ']:
        game_continue = False
    elif board[2] == ['  X  ','  X  ','  X  '] or board[2] == ['  O  ','  O  ','  O  ']:
        game_continue = False
    
    indexing_number = 0
    
    while indexing_number <= 2:
        vertical_counter = 0
        for line in board:
            if line[indexing_number] == '  X  ':
                vertical_counter += 1
                if vertical_counter == 3:
                    game_continue = False
                    
        indexing_number += 1
    
    indexing_number = 0
    
    while indexing_number <= 2:
        vertical_counter = 0
        for line in board:
            if line[indexing_number] == '  O  ':
                vertical_counter += 1
                if vertical_counter == 3:
                    game_continue = False
                    
        indexing_number += 1
    
    if board[0][0] == '  X  ' and board[1][1] == '  X  ' and board[2][2] == '  X  ':
        game_continue = False
    
    if board[2][0] == '  X  ' and board[1][1] == '  X  ' and board[0][2] == '  X  ':
        game_continue = False
    
    if board[0][0] == '  O  ' and board[1][1] == '  O  ' and board[2][2] == '  O  ':
        game_continue = False
    
    if board[2][0] == '  O  ' and board[1][1] == '  O  ' and board[0][2] == '  O  ':
        game_continue = False

    return game_continue
