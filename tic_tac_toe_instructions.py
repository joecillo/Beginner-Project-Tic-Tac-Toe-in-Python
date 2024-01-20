
column_letters = '      A      B       C '
top_border = '     __      __      __'
row_1 = ['|__|','|__|','|__|']
row_2 = ['|__|','|__|','|__|']
row_3 = ['|__|','|__|','|__|']

board = [row_1, row_2, row_3]


def show_instructions():
    
    print('''\n888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  \n\nCreated by Joe Cillo\n\n''')
    
    print('Welcome to Tic Tac Toe!\n')
    print(f'{column_letters}\n{top_border}\n1 {board[0]}\n2 {board[1]}\n3 {board[2]}\n\n')
    print('Win by getting 3 consecutive linear or diagonal Xs or Os!\n\n')
    
