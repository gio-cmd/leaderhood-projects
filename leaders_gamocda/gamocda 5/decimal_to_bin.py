# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111

def decimal_to_bin(num):
    if num == 0:
        return 0
    result = []
    while num > 0:
        result.insert(0, str(num % 2))
        num = num // 2
    return int(''.join(result))


print(decimal_to_bin(15))