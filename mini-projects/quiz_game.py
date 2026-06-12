import random

lst = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": 2
    },
    {
        "question": "\nWhich planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": 3
    },
    {
        "question": "\nWho is known as the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose"],
        "answer": 2
    },
    {
        "question": "\nWhich is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": 3
    },
    {
        "question": "\nHow many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": 3
    }
 ]

random.shuffle(lst) #To shuffle questions

score = 0
for q in lst:
    print(q["question"])
    
    for i, options in enumerate(q["options"], start = 1): 
        #Enumrate used to print options with their index 
        #start = 1 to start index with 1
        print(f"{i}. {options}")

    while True:    
        try:
            n = int(input("enter option: "))
            if n >= 1 and n <= 4:
                break
            else:
                print("enter valid input number 1-4")
        except:
            print("enter valid number")
            

    

    if n == q["answer"]:
        score +=1
        print("Correct, your current score is", score)
    else:
        print(f"not correct,correct answer is {q["answer"]}")
        print("your current score is", score)
    
    
    

print(f"\nyour total score is {score}/5")

if score >=4:
    print("Excellent\n")
elif score >=2:
    print("good\n")
elif score >= 0:
    print("try again\n")