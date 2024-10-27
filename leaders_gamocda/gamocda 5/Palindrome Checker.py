# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False


def palindrome_checker(str):
    result = ''
    for i in str.lower():
        if i in "abcdefghijklmnopqrstuvwxyz":
            result += i
    return result == result[::-1]

print(palindrome_checker("Hello"))