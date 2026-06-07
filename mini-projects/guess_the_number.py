import random
ran = random.randint(1,100)


while(True):
    n= int(input("enter a number between 1 to 100: "))
    if(n > ran):
        print("high")
        
    elif(n < ran):
        print("low")
    
    elif(ran == n):
        print("correct")
        break
    
    