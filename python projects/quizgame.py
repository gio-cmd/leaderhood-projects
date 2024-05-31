percenatge = 0
score = 0

print("Welcome! This is words best quiz game")
 
game = input ("Do you want to play?: ")
if game.lower() != "yes":
    quit()
print("Good Choice")

anwer = input("what year is this: ")
if anwer == 2023:
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

anwer = input("What's my name?: ")
if anwer.lower() == "giorgi":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

anwer = input("What am i?: ")
if anwer.lower() == "human":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1



anwer = input("Were do i live?: ")
if anwer.lower() == "georgia":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

print("your total score is ", score, "points")
print("Out of this questions you got",percenatge,"procent correct")