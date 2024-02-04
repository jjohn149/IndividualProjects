import random

def play():
    user = input("'r' for Rock , 'p' for Paper, 's' for Scissors \n ")
    computer_choice = random.choice(['r','p','s'])


    if user == "s" and computer_choice == "p":
        print(f'User chose {user} and the computer chose {computer_choice}. You won!')
    elif user == "p" and computer_choice == "s":
        print(f'User chose {user} and the computer chose {computer_choice}. The Computer won!')
    elif user == "r" and computer_choice == "s":
        print(f'User chose {user} and the computer chose {computer_choice}. You won!')
    elif user == "s" and computer_choice == "r":
        print(f'User chose {user} and the computer chose {computer_choice}. The Computer won!')
    elif user == "p" and computer_choice == "r":
        print(f'User chose {user} and the computer chose {computer_choice}. You won!')
    elif user == "r" and computer_choice == "p":
        print(f'User chose {user} and the computer chose {computer_choice}. The Computer won!')
    elif user == computer_choice:
        print(f'User chose {user} and the computer chose {computer_choice} so we have a Tie!')
    else:
        print("Invalid Selection. Choose from the following selection ('r','p','s')")
    
    

play()
    
