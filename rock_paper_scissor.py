import random

def game(choice):
    comp = random.randint(-1,1)
    if comp == -1:
        print("Computer choose = Rock")
    elif comp == 0:
        print("Computer choose = paper")
    elif comp == 1:
        print("Computer choose = scissor")
    valid_input = [-1,0,1]
    if choice in valid_input:
        if choice == comp:
            print("TIE 😑") 
        elif (comp == -1 and choice == 0) or (comp == 0 and choice == 1) or (comp == 1 and choice == -1):
            print("YOU WON 🥳😇")
            return 1
        else:
            print("YOU LOSE 😭😭")
    else:
        print("Invalid input😡")
       
ans = "yes"
score = 0
while ans =="yes":
    print("Enter -1 for rock")
    print("Enter 0 for paper")
    print("Enter 1 for scissor")
    user_choice = int(input("Enter your choice:"))
    a = game(user_choice)
    if a == 1:
        score+=1
    ans = input("Do you want to play again?:").lower().strip()
print(f"Your final score is {score}") 

