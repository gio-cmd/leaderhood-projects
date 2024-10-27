# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def fibbonacci(num):
    result = [0, 1]
    # counter = 0
    for i in range(2, num):
        result.append(result[-1] + result[-2])
    return result


print(fibbonacci(7))