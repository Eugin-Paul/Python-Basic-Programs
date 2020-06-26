import sys
 
def welcome_msg():
     
     msg = '''This is the match between India and England.
     Yuvraj and Kaif is on the crease. 
     India need 10 runs to win from 3 balls.
     Let's start the match.\n
     '''
     print(msg)
     
def start():
    
    welcome_msg()
    game()
    
def game():
    
    choice = input('''
    Yuvraj is facing the 4th ball.
    Select your choice : 
        1. Yorker
        2. Bouncer
        3. Outswinger
        ''')
    if choice == "1" :
        yorker()
    elif choice == "2":
        bouncer()
    elif choice == "3":
        outswinger()
        
def yorker():
    
    print('''
    WOW,SIX!
    Missed Yorker. 
    Yuvraj is a master of hitting full lengths into sixes. 
    6 for India. 
    4 runs needed from 2 balls.
    Yuvraj is on crease.
    ''')
   
    choice = input('''
    5th ball, your choice :
        1.Inswinger
        2.Wide
        3.Leg Cutter
        ''')
    if choice == "1" :
        inswinger()
    elif choice == "2":
        wide()
    elif choice == "3":
        leg_cutter()

def inswinger():
    
    print('''
    Yuvraj is facing the 5th ball.
    2 runs.
    2 runs needed from 1 balls.
    Yuvraj is on crease.
    ''')
    
    choice = input('''
    Last ball, your choice :
        1.Leg Break
        2.Googly
        3.Top Spinner
        ''')
    if choice == "1" :
        leg_break()
    elif choice == "2":
        googly()
    elif choice == "3":
        top_spinner() 

def leg_break():
    
    print('''
    Yuvraj is facing the last ball.
    Unbelivable, its OUT!
    India loss the match by 2 runs.
    ''') 
    sys.exit
  

def googly():
    
    print('''
    Yuvraj is facing the last ball.
    2 runs.
    Oh, the match is DRAWN!
    ''') 
    sys.exit()
    
def top_spinner():
    
    print('''
    Yuvraj is facing the last ball.
    Smashed, its a FOUR!
    India won the match!
    ''') 
    sys.exit() 
    
        
def wide():
    
    print('''
    Yuvraj is facing the 5th ball.
    1 extra run.
    3 runs needed from 2 balls.
    Yuvraj is on crease.
    ''')   
      
    choice = input('''
    5th ball again, your choice :
        1.Flicker Ball
        2.Slider
        3.Flipper
        ''')
    if choice == "1" :
        flicker()
    elif choice == "2":
        slider()
    elif choice == "3":
        flipper() 
    
def flicker():
    
    print('''
    Yuvraj is facing the last ball.
    Smashed, its a FOUR!
    India won the match!
    ''') 
    sys.exit()

def slider():
    
    print('''
    Yuvraj is facing the last ball.
    WOW, SIX!
    India won the match!
    ''') 
    sys.exit()    
    
def flipper():
    
    print('''
    Yuvraj is facing the last ball.
    Smashed, its a FOUR!
    India won the match!
    ''') 
    sys.exit()          
    
def leg_cutter():
    
    print('''
    Yuvraj is facing the 5th ball.
    Hit it,its a FOUR!
    India win the game.
    ''')
    sys.exit()         
    
# 4th Ball:
    
def bouncer():   
    
    print('''
    Missed.
    10 runs needed from 2 balls.
    Yuvraj is on crease.
    Looks like India is losing the game
    ''')
   
    choice = input('''
    5th ball, your choice :
        1.Slower ball
        2.Reverse Swing
        3.Doosra
        ''')
    if choice == "1" :
        slower()
    elif choice == "2":
        reverse()
    elif choice == "3":
        doosra() 

def slower():
    
    print('''
    Four!!
    6 runs needed from 1 balls.
    Yuvraj is on crease.
    ''')
    
    choice = input('''
    Last ball, your choice :
        1.Arm Ball
        2.Slider Leg
        3.Carrom Ball
        ''')
    if choice == "1" :
        arm_ball()
    elif choice == "2":
        slider_leg()
    elif choice == "3":
        carrom_ball()  

def arm_ball():
    
    print('''
    Yuvraj is facing the last ball.
    Smashed, its a FOUR!
    India Lost the match by 2 runs!
    ''') 
    sys.exit()    

def slider_leg():
    
    print('''
    Yuvraj is facing the last ball.
    OUT!! 
    India Lost the match!
    ''') 
    sys.exit()  

def carrom_ball():
    
    print('''
    Yuvraj is facing the last ball.
    WOW, its a SIX!
    India Won the MAtch!!
    ''') 
    sys.exit()   
    
def reverse():
    
    print('''
    Ohh!!OUT!
    10 runs needed from 1 balls.
    India is losing the game.
    Dhoni comes into the crease.
    ''')
    
    choice = input('''
    Last ball, your choice :
        1.Leg Spinner
        2.Off Spinner
        3.Leg Cut
        ''')
    if choice == "1" :
        leg_spinner()
    elif choice == "2":
        off_spinner()
    elif choice == "3":
        leg_cut() 

           
def doosra():
    
    print('''
    Kaif is facing the 5th ball.
    Oh!! OUT!! 
    India Lost the match!
    ''') 
    sys.exit()   


def leg_spinner():
    
    print('''
    Dhoni is facing the last ball.
    Smashed, its a FOUR!
    India lost the match by 6 runs!
    ''') 
    sys.exit()    

def off_spinner():
    
    print('''
    Dhoni is facing the last ball.
    OUT!!Again!!
    India Lost the match by 10 runs!
    ''') 
    sys.exit()  

def leg_cut():
    
    print('''
    Dhoni is facing the last ball.
    Single! 
    India Lost the match by 9 runs!
    ''') 
    sys.exit() 

# 4th Ball :

def outswinger():
    
    print('''
    Ohh! Misfield! 5 runs.2 runs for overthrow.
    6 runs needed from 2 balls.
    Kaif is on crease.
    ''')
   
    choice = input('''
    5th ball, your choice :
        1.Off Cutter
        2.No Ball
        3.Knuckleball
        ''')
    if choice == "1" :
        off_cutter()
    elif choice == "2":
        no_ball()
    elif choice == "3":
        kunckleball() 

def off_cutter():
    
    print('''
    SIX!!A brilliant knock from Kaif!
    India won the match!
    ''')
    sys.exit()    

def no_ball():
    
    print('''
    Kaif is facing the 5th ball.
    Smashed, its a SIX!
    India won the match!
    ''') 
    sys.exit()    

def kunckleball():
    
    print('''
    Kaif is facing the 5th ball.
    WOW!!Its a SIX!!
    India Won the match!
    ''') 
    sys.exit()  

def leg_breaker():
    
    print('''
    Kaif is facing the last ball.
    2 runs!
    India won the match!
    ''') 
    sys.exit()   

def off_breaker():
    
    print('''
    Kaif is facing the last ball.
    Smashed, its a FOUR!
    India won the match!
    ''') 
    sys.exit()    

def swing():
    
    print('''
    Kaif is facing the last ball.
    OUT!! 
    India Lost the match!
    ''') 
    sys.exit()
    
         
if __name__ == "__main__":
    start()
      
        
        
        
        
        
        
        
        
        
        