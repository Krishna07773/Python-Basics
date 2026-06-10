def addtask():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Successfully added {task}")
    print()

def view():
    if not tasks:
        print("There is no any task")

    else:
        for i in range(0, len(tasks)):
            print(f"Your Tasks: {i+1}. {tasks[i]}")
            print()
    
    
def delete():
    num = int(input("enter task number to delete: "))
    num = num - 1
    if not tasks:
        print("there is no task to delete")
    elif 0 <= num < len(tasks):
        tasks.pop(num)
        print("sucessfully deleted")
    else:
        print("there is no task to delete")
        print()


tasks = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit") 
    print()   

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("enter a valid Number")
        continue

    if choice == 1:
        addtask()
    elif choice == 2:
        view()
    elif choice == 3:
        delete()
    elif choice == 4:
        print("Thanks for using To-Do Task Manager")
        break
    else:
        print("Invalid choice")