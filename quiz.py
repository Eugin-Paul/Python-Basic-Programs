import sys


def welcome_msg():
    
    msg = '''Welcome to Quiz Game :
        Rules : 1.You will get a point if the answer is true
                2.You will loss a point if the answer is false'''
    print(msg)
    
def get_name():   
    
    name = input("Enter your name : \n")
    return name
    
def start():
    
    welcome_msg()
    user_name = get_name()
    print("Hi " + user_name + " , Let's play the game \n")
    display_score,display_true_count,display_false_count = conditions_check()
    display(display_score,display_true_count,display_false_count)
    
    
    
def conditions_check():
    
    print("Please enter T or F for the following questions \n")
    score = 0
    true_count = 0
    false_count = 0
    user_choice = input("Q1.The Gotthard Base Tunnel is the longest rail tunnel in the world : \n")
    new_score,new_true_count,new_false_count = true_condition(user_choice,score,true_count,false_count)
    
    user_choice = input("Q2.There are McDonald’s one every continent except one : \n")
    new_score,new_true_count,new_false_count = true_condition(user_choice,new_score,new_true_count,new_false_count)
    
    user_choice = input("Q3.Earth Rotation is also called annual motion of the earth : \n")
    new_score,new_true_count,new_false_count = false_condition(user_choice,new_score,new_true_count,new_false_count)
    
    user_choice = input("Q4.Humans are the only animals that bury their dead : \n")
    new_score,new_true_count,new_false_count = false_condition(user_choice,new_score,new_true_count,new_false_count)
    
    user_choice = input("Q5.The currency of France is Euro : \n")
    new_score,new_true_count,new_false_count = true_condition(user_choice,new_score,new_true_count,new_false_count)
    
    user_choice = input("Q6.Japan and Russia did not sign a peace treaty after World War Two so are technically still at war : \n")
    new_score,new_true_count,new_false_count = true_condition(user_choice,new_score,new_true_count,new_false_count)
    
    user_choice = input("Q7.Goldfish only have a memory of three seconds : \n")
    new_score,new_true_count,new_false_count = false_condition(user_choice,new_score,new_true_count,new_false_count)
    
    return new_score,new_true_count,new_false_count
    
    
def true_condition(user_choice,score,true_count,false_count):
    
    # if the user_choice and correct answer is True
    if user_choice == "T" :
        score = score + 1
        # print("score is " + str(score))  
        true_count = true_count + 1
    elif user_choice == "F" :
        score = score - 1
        # print("score is " + str(score))  
        false_count = false_count + 1
    else :
        print("Please enter T or F")
    return score,true_count,false_count   
        
def false_condition(user_choice,score,true_count,false_count):
    
    # if the user_choice and correct answer is False
    if user_choice == "T" :
        score = score - 1
        # print("score is " + str(score)) 
        false_count = false_count + 1
    elif user_choice == "F" :
        score = score + 1
        # print("score is " + str(score))  
        true_count = true_count + 1
    else :
        print("Please enter T or F")  
    return score,true_count,false_count     
    
def display(display_score,display_true_count,display_false_count):
    
    print("Your Score is " + str(display_score))
    print("Your True answer is " + str(display_true_count))
    print("Your False answer is " + str(display_false_count))
    sys.exit()
    

if __name__ == "__main__":
    start()
    