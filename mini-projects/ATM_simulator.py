balance = 5000

while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice= int(input("enter your choice: "))

        if(choice == 1):
            print("Your Balance: ", balance)
            

        elif(choice == 2):
            if(amt > 0):
                amt = int(input("Enter amount to Deposit: "))
                balance = balance + amt
                print("Total Balance", balance)
            else:
                print("Invalid Amount")

        
        elif(choice == 3):
            withdraw = int(input("Enter Amount to Withdraw: "))
            if(withdraw <= balance):
                balance = balance - withdraw
                print("Total Balance", balance)
            else:
                print("Insufficient Balance")

        elif(choice == 4):
            print("Thank You")
            break
        
        else:
            print("Invalid choice")
            
        