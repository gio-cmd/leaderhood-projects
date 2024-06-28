import random


# we will store every accaunt here
accaunts = {}

# letting the user create an account
def Create_accaunt():
    name = input('\nEnter your name: ')

    # Check if user didnt fill the name input
    while name == "":
        print("\nWrong input, please enter your name")
        name = input('Enter your name: ')

    password = input('Enter your password: ')
    # Check if user didnt fill the password input
    while password == "":
        print("\nWrong input, please enter your password")
        name = input('Enter your password: ')
    
    # Give user unic number which will be used for login in the future
    accaunt_number = random.randint(1, 100000)
    print(f"you will be given an accaunt number: {accaunt_number}")

    balance = 0

    accaunts[accaunt_number] = {'name': name, "balance": balance}
    print('Accaunt succefuly created!')


def deposit():
    accaunt_number = int(input("\nEnter your accaunt number: "))

    if accaunt_number in accaunts:
        money = input('Enter the amount to deposit: ')
        while not money.isdigit():
            print("Enter deposit amount using numbers!")
            money = input('Enter the amount to deposit: ')
        accaunts[accaunt_number]['balance'] += float(money) 
        print('Deposit succeful')
    else:
        print("Accaunt not found")

def transaction():
    giver = int(input("\nEnter your accaunt number: "))
    if giver in accaunts:
        reciver = int(input("Enter reciver's accaunt number: "))
        if reciver in accaunts:
            money = input('Enter the amount to transfer: ')
            while not money.isdigit():
                print("Enter transfer amount using numbers!")
                money = input('Enter the amount to transfer: ')
            money = float(money)
            if accaunts[giver]["balance"] >= money:
                accaunts[giver]["balance"] -= money
                accaunts[reciver]["balance"] += money
                print("Transfer succeful")
            else:
                print("Not enough balance to make this transaction")
        else:
            print('Recivers accaunt not found')
    else:
        print("Accaunt not found")
    

while True:
    print('\nMenu')
    print("1. Create an account")
    print("2. Make a deposit")
    print('3. Transfer money')

    choice = int(input("\nEnter the number of the operation: "))

    if choice == 1:
        Create_accaunt()
    if choice == 2:
        deposit()
    if choice == 3:
        transaction()