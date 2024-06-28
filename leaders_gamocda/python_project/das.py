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

def withdraw():
    accaunt_number = int(input("\nEnter your accaunt number: "))

    if accaunt_number in accaunts:
        money = input('Enter the amount to withdraw: ')
        while not money.isdigit():
            print("Enter withdraw amount using numbers!")
            money = input('Enter the amount to withdraw: ')
        money = float(money)
        if accaunts[accaunt_number]['balance'] >= money:
            accaunts[accaunt_number]['balance'] -= money
            print('Withdrawal succeful')
        else:
            print("Not enough balance to make this transaction")
    else:
        print("Accaunt not found")

def delete():
    accaunt_number = int(input("\nEnter your accaunt number: "))

    if accaunt_number in accaunts:
        accaunts.pop(accaunt_number)
    else:
        print("Accaunt not found")

def view():
    accaunt_number = int(input("\nEnter your accaunt number: "))

    if accaunt_number in accaunts:
        print(f"Accaunt name is: {accaunts[accaunt_number['name']]}")
        print(f"Your balance is: {accaunts[accaunt_number['balance']]}")
    else:
        print("Accaunt not found")

def user_accaunts():
    for i in accaunts:
        print(f"Accaunt name: {i['name']}, Balance: {i['balance']}")

while True:
    print('\nMenu')
    print("1. Create an account")
    print("2. Make a deposit")
    print('3. Transfer money')
    print('4. Withdraw money')
    print("5. View profile")
    print("6. Seach accounts")
    print("7. Delete an accaunt")
    print("8. Leave the bank")

    
    choice = int(input("\nEnter the number of the operation: "))

    if choice == 1:
        Create_accaunt()
    if choice == 2:
        deposit()
    if choice == 3:
        transaction()
    if choice == 4:
        withdraw()
    if choice == 5:
        view()
    if choice == 6:
        user_accaunts()
    if choice == 7:
        delete()
    if choice == 8:
        print("You are leaving the bank")
        break