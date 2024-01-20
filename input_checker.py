
def check_input_2_choice(prompt, choice_1, choice_2):
    
    choice = (input(prompt)).upper()
    
    while choice != choice_1 and choice != choice_2:
        print(f'\n\nWrong Input! Please enter only {choice_1} or {choice_2}\n')
        choice = (input(prompt)).upper()
    
    if choice == choice_1:
        return choice
    
    elif choice == choice_2:
        return choice
    
    
def check_input_3_choice(prompt, choice_1, choice_2, choice_3):
    
    choice = (input(prompt)).upper()
    
    while choice != choice_1 and choice != choice_2 and choice != choice_3:
        print(f'\n\nWrong Input! Please enter only {choice_1} or {choice_2} or {choice_3}.\n')
        choice = (input(prompt)).upper()
        
    if choice == choice_1:
        return choice
    
    elif choice == choice_2:
        return choice
    
    elif choice == choice_3:
        return choice
    
    
