# Challenge:
#  Create a function that finds the length of the longest substring without repeating characters.
# Instructions:
# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").
# Test Cases:
# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3



def longest_substring(s):
    str = []
    count = 0 

    for i in s:
        while i in str:
            str.pop(0)
        str.append(i)
        count = max(count, len(str))

    return count

print(longest_substring("pwwkew"))


