import random

accounts = {}

def create_account():
    name = input("Enter your name: ")
    while name == '':
        print("")
        print("Name cannot be empty")
        name = input("Enter your name: ")
        continue
    password = input("Enter a password: ")
    while password == '':
        password = input("Enter a password: ")
        print("password cannot be empty")
        continue
    account_number = random.randint(1, 123123123)
    balance = 0
    accounts[account_number] = {'name': name, 'balance': balance, 'password': password}
    print(f"Account created successfully. Your account number is {account_number}")
    
    

def deposit_funds():
    account_number = int(input("Enter your account number: "))
    if account_number in accounts:
        deposit_amount = float(input("Enter the deposit amount: "))
        accounts[account_number]['balance'] += deposit_amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw_funds():
    account_number = int(input("Enter your account number: "))
    if account_number in accounts:
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        if accounts[account_number]['balance'] >= withdrawal_amount:
            accounts[account_number]['balance'] -= withdrawal_amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

def check_balance():
    account_number = int(input("Enter your account number: "))
    if account_number in accounts:
        print(f"Your balance is: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

def transfer():
    from_account = int(input("Enter your account number: "))
    if from_account in accounts:
        to_account = int(input("Enter the recipient's account number: "))
        if to_account in accounts:
            transfer_amount = float(input("Enter the amount to transfer: "))
            if accounts[from_account]['balance'] >= transfer_amount:
                accounts[from_account]['balance'] -= transfer_amount
                accounts[to_account]['balance'] += transfer_amount
                print("Transfer successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Recipient's account not found.")
    else:
        print("Account not found.")

while True:
    print("\nMenu:")
    print("1. Create an account")
    print("2. Deposit funds")
    print("3. Withdraw funds")
    print("4. Check balance")
    print("5. Transfer funds")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        deposit_funds()
    elif choice == 3:
        withdraw_funds()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        transfer()
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Error: Invalid choice.")