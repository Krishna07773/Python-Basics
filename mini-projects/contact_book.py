def addcontact():
    
    name = input("Enter name: ").title()
    number = input("contact number: ")

    contact[name] = number

    print(f"sucessfully added {name} : {contact[name]}")

def searchcontact():
    
    name = input("enter name: ").title()
    if name in contact:
        print(name, ":" ,contact[name])
    else:
        print("contact not found")

def viewall():
    
    for name, number in contact.items():
        print(name, ":", number)            

def deletecontact():
    
    name = input("enter name to delete: ").title()
    if name in contact:
        del contact[name]
        print("contact successfully deleted")
    else: 
        print("No contact available")

    

contact = {
    "Rahul" : "635728XXXX",
    "Aman" : "875728XXXX",
    "Aditya" : "675728XXXX"
}

while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
 
        try:
            choice = int(input("enter your choice: "))
        except:
            print("please enter a valid number")
            continue
            

        if choice == 1:
            addcontact()
        elif choice == 2:
            searchcontact()
        elif choice == 3:
            viewall()
        elif choice == 4:
            deletecontact()
        elif choice == 5:
            print("Thank you for using Contact book")
            break
        else:
            print("Invalid choice")

    