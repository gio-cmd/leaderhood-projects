# Challenge:
#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).
# Instructions:
# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.
# Test Cases:
# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True


def anagram_finder(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2

print(anagram_finder("triangle", "integral"))