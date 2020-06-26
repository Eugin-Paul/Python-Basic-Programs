import sys
import random

def welcome_msg():
    
    msg = '''Welcome to Number Guessing game : 
       
        Only 5 chance will be allowed if guess is wrong \n'''
    print(msg)    
    
def start():
    
    num_small = 0
    num_large = 0
    count = 0
    welcome_msg()
    num = user_num()
    ran = random_num()
    num_new,count_new = checking(num,ran,count)
    # print("New num is " + str(num_new))
    # print("Count is " + str(count_new))
    repeat(num_new,ran,count_new)
    
def random_num():
    
    rand = random.randrange(1,20) 
    # print("Random Number is " + str(rand))
    return rand
    
def user_num():
    
    user = int(input("Enter the number : "))
    return user    
    
def checking(num,ran,count):

    maxi = 5
    new_num = 0
    if num == ran :
        print("Congragulations,You Guessed right \n")
        sys.exit()
    if count == 5 :
        print("You tried your maximum limit, Game Over")
        sys.exit()    
    if num < ran :
        new_num = int(input("You guessed the number smaller than the actual number. Please enter a large number : \n"))
        count_n = count + 1
        print(str(maxi-count-1) + " chance remaining")
        return new_num,count_n
    if num > ran :
        new_num = int(input("You guessed the number larger than the actual number. Please enter a small number : \n"))
        count_n = count + 1
        print(str(maxi-count-1) + " chance remaining")
        return new_num,count_n
     
    if (new_num == ran) :
        print("Congragulations,You Guessed right \n")
        sys.exit()
            
def repeat(num_new,ran,count_new) :
     
         num_new,count_new = checking(num_new,ran,count_new)
        #  print("New num is " + str(num_new))
        #  print("Count is " + str(count_new))
         repeat(num_new,ran,count_new)        
     

if __name__ == "__main__":
    start()     