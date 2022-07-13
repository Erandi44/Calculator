#-------------------------------------------------------------------------------------------------------------

# This program function as a simple calculator. 
# Functions available : +, -, *, /, remainder, power
# Author: Erandika Karunaratne
# Date : 2022-02-03

#-------------------------------------------------------------------------------------------------------------

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2
    
def multiply(num1, num2):
    return num1*num2
    
def divide(num1, num2):
    if not num2 ==0:
        return num1/num2
    
def power(num1, num2):
    return num1**int(num2)
    
def remainder(num1, num2):
    if not num == 0:
        return num1%num2
    
    
def calculate(choice, num1, num2): 
    # Perform aritmatic operation based on the operator
    if choice =='+':
        return add(num1,num2)
    
    elif choice =='-':
        return subtract(num1,num2)

    elif choice =='*':
        return multiply(num1,num2)
    
    elif choice =='/':
        if num2 ==0:
            print("float division by zero")
            print(float(num1),"/",float(num2) ,"=","None")
        else:
            return divide(num1,num2)
    
    elif choice =='^':
        result = power(num1,num2)
    
    elif choice =='%':
        if num1 and num2 ==0:
            print("float division by zero")
            print(float(num1),"%",float(num2) ,"=","None")
        else:
            return remainder(num1,num2)
    else:
        print("Something went wrong")
    
def history(choice):
    if choice == "?":
        if len(history_operations) ==0:
            print("No past calculations to show")
        else:
             print(*history_operations, sep="\n")
 

history_operations = []

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("9.History  : ? ")
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    
    #Check validity of operation
    if choice == "#":
        #program ends here
        print("Done. Terminating")
        break
    elif choice == "$":
        continue
    elif choice == "?":
        history(choice)
        continue
    elif choice not in ("+","-","*","/","^","%","#","$"):
        print("Unrecognized operation")
        continue
    
   
    num1 = (input("Enter first number: "));
    print(num1)
    
    # check if input is a valid number
    if num1 =="#":
        print("Done. Terminating")
        break
    if num1 =="$":
        continue
    elif isfloat(num1) ==False:
        print("Not a valid input. Please Enter again")
        continue
    

    num2 = (input("Enter second number: "))
    print(num2)
    
    # check if input is a valid number
    if num2 =="#":
        print("Done. Terminating")
        break
    if num2 =="$":
        continue
    elif isfloat(num2) ==False:
        print("Not a valid input. Please Enter again")
        continue
    
    num1 = float(num1)
    num2 = float(num2)
    
    result = calculate (choice, num1, num2)
    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
    print(last_calculation )
    history_operations.append(last_calculation)
    #print(history_operations)
    
    
  
   
    
  


    
