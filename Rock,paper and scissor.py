import random

#Input user's selection
def user_choice():
    print("Choose any one of the following choices:")
    print("1:Rock")
    print("2:Paper")
    print("3:Scissors")
    choice=int(input("Your choice(1/2/3): "))
    if choice in [1,2,3]:
        return choice
    else:
        print("Invalid choice,please  options between 1 to 3")
        return user_choice()

#Input computer's selection
def computer_choice():
    return random.randint(1,3)

#Final result
def result(user,computer):
    choices={1:"Rock",2:"Paper",3:"Scissor"}
    print(f"Your choice is {choices[user]}")
    print(f"Computer's choice is {choices[computer]}")
    
    if user==computer:
        return "The game resulted in tie!"
    elif (user==1 and computer==3) or(user==2 and computer==1) or (user==3 and computer==2):
        return "Congratulations! You Win."
    else:
        return "Oops!Computer Wins,Better Luck Next Time."

#Let's Play Game
def play():
    user_input=user_choice()
    comp_input=computer_choice()
    final_result=result(user_input,comp_input)
    print(final_result)

#main code
play()

