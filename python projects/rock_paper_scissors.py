import random

while True:
    user_input = input("type rock/paper or scissors to make a move:").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("computer has choosen",computer_choice)
    if user_input == computer_choice:
        print("WOW Its a tie")
    elif (user_input == "rock" and computer_choice == "scissors" or user_input == "paper" and computer_choice == "rock" or user_input == "scissors" and computer_choice == "paper"):
        print("Congrats you win")
    else:
        print("Aww sorry fo you loss cuz")
        print("computer won")
    
    
    
    continue1 = input("do u want to continue? yes/no:").lower()
    if continue1 != "yes":
        break