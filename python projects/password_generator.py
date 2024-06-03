import random

print("Create a strong and secured password")


symbols = 'abcdefghijklmnopqrstuvwxyz.,/()1234567890!@#$%&'

amount_of_passwords = int(input('Enter a number of passwords: '))
length_of_password = int(input('Enter The length of password: '))

for i in range(amount_of_passwords):
    password = ''
    for j in range(length_of_password):
        password += random.choice(symbols)
    print(password)