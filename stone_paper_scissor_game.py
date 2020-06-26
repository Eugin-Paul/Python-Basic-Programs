import time
import random
import sys

Game = ["stone","paper","scissor"]

def welcome_msg():
 
    msg = '''Welcome to the Game :
        
        Rules : 
            1.Paper should cover Stone
            2.Stone should hit Scissor
            3.Scissor should cut Paper
             '''
    
    print(msg)
    

def start():

   welcome_msg()
   player = get_name()
   game(player)

def get_name():
  
    # giving player name  
    player = None
    player = input("Enter player name : \n")

    return player

def get_value():

    # random value for computer
    value = random.choice(Game)
    if value == "stone":
     return 1
    if value == "paper":
     return 2
    if value == "scissor":
     return 3
 

def get_checking(player,player_choice,computer_choice):

    # condition checking for player_choice and computer_choice
    if (player_choice == computer_choice):
        print("Match Drawn \n")
        print("Computer also entered " + str(computer_choice))
    elif player_choice == 1 and computer_choice == 2:
        print("Computer selected Paper \n")
        print("Paper cover stone,Computer wins \n")
    elif(player_choice == 1 and computer_choice == 3):
        print("Computer selected Scissor \n")
        print("Stone hit scissor," + player + " wins \n")
    elif(player_choice == 2 and computer_choice == 1):
        print("Computer selected Stone \n")
        print("Paper cover stone," + player + " wins \n")
    elif(player_choice == 2 and computer_choice == 3):
        print("Computer selected Scissor \n")
        print("Scissor cuts paper,Computer wins \n")
    elif(player_choice == 3 and computer_choice == 1):
        print("Computer selected Stone \n")
        print("Stone hit scissor,Computer wins \n")
    elif(player_choice == 3 and computer_choice == 2):
        print("Computer selected Paper \n")
        print("Scissor cuts paper,"+ player + " wins \n")
    else:
        print("You entered an invalid value \n")
        
def game(player):
  
   # selecting choice for player   
   player_choice = int(input("Hi " + player + ", Enter your choice : \n 1.Stone \n 2.Paper \n 3.Scissor \n \n"))
   computer_choice = get_value()
   get_checking(player,player_choice,computer_choice)
   new_game(player)

def again(player):

   # function call for game   
   game(player)
    
def new_game(player):
    
    # function block for play again
    play_again = input("Do you want to play again(Y/N)")    
    if play_again == "Y":
        again(player) 
    elif play_again == "No":
        sys.exit()


if __name__ == "__main__":
    start()















 
   