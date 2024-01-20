
def draw_game(board):
    
    game_continue = True
    
    if board[0].count('|__|') == 0 and board[1].count('|__|') == 0 and board[2].count('|__|') == 0:
        game_continue = False
    
    return game_continue
    
