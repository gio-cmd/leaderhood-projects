# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# if choice in ('1', '2', '3', '4'):
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         print(num1, "+", num2, "=", num1 + num2)
#     elif choice == '2':
#         print(num1, "-", num2, "=", num1 - num2)
#     elif choice == '3':
#         print(num1, "*", num2, "=", num1 * num2)
#     elif choice == '4':
#         if num2 == 0:
#             print("Error! Division by zero!")
#         else:
#             print(num1, "/", num2, "=", num1 / num2)
# else:
#     print("Invalid Input")













# a = 11
# b = 10

# if a > b:
#     print("a > b")


# a = 10
# b = 11

# if a < b:
#     print("hello")


# user1 = input("Enter your gender(Male/Female):").lower()

# if user1 == "male":
#     print("User1 is male")
# elif user1 == "female":
#     print("You are female")
# else:
#     print("Choose the correct gender")

# x = 30

# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")




print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero!")
        else:
            print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid Input")