# Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.
# Examples:
# 5 --> 120
# 0 --> 1


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result

print(factorial(10))
