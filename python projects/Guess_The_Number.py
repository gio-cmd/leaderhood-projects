import random
top_of_range =input("Type a correct number!:") #this code makes user choose highest value from where we can generate random number
if top_of_range.isdigit(): #this code checks if number inputed is digit
    top_of_range = int(top_of_range) #this code will make inputed digit integer
    if top_of_range <= 0:
        print("type a number higher than 0")
        quit()
else:
    print("please type a number")
    quit()
random_number = random.randint(0,top_of_range)
guess_number = 0
while True:
    guess_number += 1
    guess =input("Guess the correct number!:")
    if guess.isdigit(): #this code checks if number inputed is digit
        guess = int(guess) #this code will make inputed digit integer
    else:
        print("please type a number")

    if guess == random_number:
         print("You got it")
         break
    elif guess < random_number:
        print("random number is higher number. try larger one :)")
    else:
        print("random number is lower number. try smaller one :)")

print(guess_number)