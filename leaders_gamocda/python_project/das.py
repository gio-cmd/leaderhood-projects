import random

# We will store every account here
accounts = {}

# Letting the user create an account
def create_account():
    name = input('\nEnter your name: ')

    # Check if user didn't fill the name input
    while name == "":
        print("\nWrong input, please enter your name")
        name = input('Enter your name: ')

    password = input('Enter your password: ')
    # Check if user didn't fill the password input
    while password == "":
        print("\nWrong input, please enter your password")
        password = input('Enter your password: ')
    
    # Give user unique number which will be used for login in the future
    account_number = random.randint(1, 100000)
    print(f"You will be given an account number: {account_number}")

    balance = 0

    accounts[account_number] = {'name': name, "balance": balance}
    print('Account successfully created!')

# Create a function for deposit
def deposit():
    account_number = input("\nEnter your account number: ")
    # Check if input is valid integer and then make it int so we avoid error
    while not account_number.isdigit():
        print("Please enter a valid account number.")
        account_number = input("Enter your account number: ")
    account_number = int(account_number)

    #check if accaunt number is in our storage, if so we add inputed value to it
    if account_number in accounts:  
        money = input('Enter the amount to deposit: ')
        while not money.isdigit():
            print("Enter deposit amount using numbers!")
            money = input('Enter the amount to deposit: ')
        accounts[account_number]['balance'] += float(money) 
        print('Deposit successful')
    else:
        print("Account not found")


# transaction funcy
def transaction():
    # find bank accaunt of the guy who makes transaction
    giver = input("\nEnter your account number: ")
    # Check if input is valid integer
    while not giver.isdigit():
        print("Please enter a valid account number.")
        giver = input("Enter your account number: ")
    giver = int(giver)

    if giver in accounts:
        # find bank accaunt of the guy who is reciving the money
        receiver = input("Enter receiver's account number: ")
        # Check if input is valid integer
        while not receiver.isdigit():
            print("Please enter a valid account number.")
            receiver = input("Enter receiver's account number: ")
        receiver = int(receiver)

        # check if reciver's accaunt is in our bank's safe (accounts variable)
        if receiver in accounts:
            money = input('Enter the amount to transfer: ')
            # Check if input is valid integer
            while not money.isdigit():
                print("Enter transfer amount using numbers!")
                money = input('Enter the amount to transfer: ')
            money = float(money)

            # check if user has more money or equal than the value he inputed
            if accounts[giver]["balance"] >= money:
                # substract the amount from his balance
                accounts[giver]["balance"] -= money
                # append the recivers balance
                accounts[receiver]["balance"] += money
                print("Transfer successful")
            else:
                print("Not enough balance to make this transaction")
        else:
            print("Receiver's account not found")
    else:
        print("Account not found")

def withdraw():
    account_number = input("\nEnter your account number: ")
    # Check if input is valid integer
    while not account_number.isdigit():
        print("Please enter a valid account number.")
        account_number = input("Enter your account number: ")
    account_number = int(account_number)

    if account_number in accounts:
        money = input('Enter the amount to withdraw: ')
        # Check if input is valid integer
        while not money.isdigit():
            print("Enter withdraw amount using numbers!")
            money = input('Enter the amount to withdraw: ')
        money = float(money)

        # check if users balance is larger than money cuz otherwise he wont make that transaction/withdrawal
        if accounts[account_number]['balance'] >= money:
            accounts[account_number]['balance'] -= money
            print('Withdrawal successful')
        else:
            print("Not enough balance to make this transaction")
    else:
        print("Account not found")

# pretty simple delete func
def delete():
    account_number = input("\nEnter your account number: ")
    # Check if input is valid integer
    while not account_number.isdigit():
        print("Please enter a valid account number.")
        account_number = input("Enter your account number: ")
    account_number = int(account_number)

    # if acaunt is found then we just pop it from the accounts dict
    if account_number in accounts:
        accounts.pop(account_number)
        print("Account successfully deleted")
    else:
        print("Account not found")

# we view user credentials (high class words :DD) btw you should credentials with french accent
def view():
    account_number = input("\nEnter your account number: ")
    # Check if input is valid integer
    while not account_number.isdigit():
        print("Please enter a valid account number.")
        account_number = input("Enter your account number: ")
    account_number = int(account_number)

    # if accaunt is found we display account name and balance
    if account_number in accounts:
        print(f"Account name is: {accounts[account_number]['name']}")
        print(f"Your balance is: {accounts[account_number]['balance']}")
    else:
        print("Account not found")

# we see every account in storage
def user_accounts():
    # iterate over accounts dict and get every accounts name and balance and account number, so much stuffys
    for account_number, details in accounts.items():
        print(f"Account number: {account_number}, Name: {details['name']}, Balance: {details['balance']}")

while True:
    # menu were user can choose some different options
    print('\nMenu')
    print("1. Create an Account")
    print("2. Deposit Money")
    print("3. Transfer Money")
    print("4. Withdraw Money")
    print("5. View Account Details")
    print("6. List All Accounts")
    print("7. Delete an Account")
    print("8. Exit")

    # input were user chooses whatever he wants and we also check if the inputed value is number in range of 1 thru 9
    choice = input("\nPlease select an option (1-8): ")
    while not choice.isdigit() or int(choice) not in range(1, 9):
        print('Invalid input, please try again')
        choice = input("\nPlease select an option (1-8): ")

    choice = int(choice)
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        transaction()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        view()
    elif choice == 6:
        user_accounts()
    elif choice == 7:
        delete()
    elif choice == 8:
        print("You are leaving the bank")
        break
