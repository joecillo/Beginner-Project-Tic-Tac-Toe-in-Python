
import input_checker

def select_move():
    column = input_checker.check_input_3_choice('\nPlease select a column  A  B  C: ', 'A', 'B', 'C')
    row = input_checker.check_input_3_choice('\nPlease select a row  1  2  3: ', '1', '2', '3')
    selected_move = column + row
    return selected_move
    

