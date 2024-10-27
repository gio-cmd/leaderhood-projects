# 10) "Eureka" numbers (5 ქულა)

# The Eureka numbers are numbers like this: 135 = 1 * 1 + 3 * 2 + 5 ** 3. Which means that we have to take a number and sum its digits raised to the consecutive powers.
# First digit to power 1, second to power 2 and so on... If the result of that sum is the same as the number itself that means that number is Eureka.

# Create a function which receives a range like (a, b) and outputs every Eureka number in it.

# NOTE: Every number which have one digit is Eureka, because for example 5 = 5 ** 1...

# Examples:
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

def is_eurika(num):
    if len(str(num)) == 1:
        return True
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i]) ** (i + 1)
    return sum == num

def eurikas(a, b):
    result = []
    for i in range(a, b + 1):
        if is_eurika(i):
            result.append(i)
    return result

print(eurikas(1, 100))