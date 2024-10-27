# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15


def binary_convertor(num):
    result = 0
    for i in str(num):
        result = result*2 + int(i)

    return result

print(binary_convertor(1111))