import sys
import time

def welcome_msg():

    msg = '''Welcome to ATM'''
    print(msg)

def start():
    
    welcome_msg()
    pin_num = 1234
    pin_checking(pin_num)
        
def pin_condition():
    
        # initialisation
        option = int(input("Select option : \n 1.View Balance \n 2.Withdraw \n 3.Deposit \n 4.Cancel \n 5.Pin Change \n"))
        balance = 100
        check1 = ""
        check2 = ""
        withdraw = 0
        withdraw_change = 0
        
        updated_balance = condition_check(withdraw,withdraw_change,check1,check2,option,balance)
        # for finding return value
        print ("Return updated value is " + str(updated_balance))
        pin_change(option)
        repeat(withdraw,withdraw_change,check1,check2,updated_balance)
        
def pin_checking(pin_num):
    
    # pin validation 
    pin = int(input("Enter your pin : "))
    if pin != pin_num :
       print("You entered wrong pin")
       pin_checking(pin_num)
    if pin == pin_num :
        pin_condition()
    
def condition_check(withdraw,withdraw_change,check1,check2,option,balance):
    update_balance = balance

    # condition for balance check
    if (option == 1) :
        print("Balance is , " + str(update_balance))
        return update_balance
    
    # condition for withdraw 
    if (option == 2) :
        withdraw = int(input("Enter the amount to withdraw : "))
        # check if the amount is correct or not  
        check1 = input("Click Y/N if the amount is corect or not : ")
    if (check1 == "Y") :
        # condition checking if the withdraw balance is less than balance or not
        while withdraw < update_balance :
            update_balance = update_balance - withdraw
            print("Updated balance is ", update_balance)
            return update_balance
        while withdraw > update_balance :
            print("Your balance is low") 
            return update_balance
    if (check1 == "N") :
        withdraw_change = int(input("Enter the correct amount : "))
        while withdraw_change < update_balance :
            update_balance = update_balance - withdraw_change
            print("Updated balance is ", update_balance)
            return update_balance
        while withdraw_change > update_balance :
            print("Your balance is low") 
            return update_balance

    # condition for deposit
    if (option == 3) :
        deposit = int(input("Enter the amount to deposit : "))
        check2 = input("Click Y/N if the amount is corect or not : ")
    if (check2 == "Y") :
        update_balance = update_balance + deposit
        print("Updated balance is ", + update_balance)
        return update_balance
    elif (check2 == "N") :
        deposit_change = int(input("Enter the correct amount : "))
        update_balance += deposit_change
        print("Updated balance is ", + update_balance)
        return update_balance
    else :
        pass

    if (option == 4) :
        # exit from the program if click on cancel
        sys.exit()
        
def pin_change(option):
    
    if (option == 5) :
        # for pin change
        Number = int(input("Enter the mobile number : "))
        print("OTP has been send to the mobile number ", + Number ,"\nUse OTP to change pin number")
        OTP = int(input("Enter the OTP Number : "))
        new_pin = int(input("Enter new pin : "))
        pin_num = new_pin
        print("Pin Changed Successfully")
        print("The Changed Pin is ," + str(pin_num))
        sys.exit()

        
        
def repeat(withdraw,withdraw_change,check1,check2,updated_balance) :
    
    # for another transaction
    again = input("Press Y/N for another transaction : ")
    if again == "N" :
        sys.exit()
    elif again == "Y" :
        option = int(input("Select option : \n 1.View Balance \n 2.Withdraw \n 3.Deposit \n 4.Cancel \n 5.Pin Change \n"))
        updated_balance = condition_check(withdraw,withdraw_change,check1,check2,option,updated_balance)
        print ("Return value is " + str(updated_balance))
        pin_change(option)
        repeat(withdraw,withdraw_change,check1,check2,updated_balance,)
    else :
        sys.exit()    
        
        

if __name__ == "__main__":
    start()