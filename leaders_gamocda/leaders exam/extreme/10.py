# Challenge:
#  Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2. You have three operations allowed: insertion, deletion, or substitution.
# Instructions:
# Input: Two strings word1 and word2 (e.g., "horse", "ros").
# Output: The minimum number of operations required to convert word1 into word2.
# Test Cases:
# assert min_distance("horse", "ros") == 3
# assert min_distance("intention", "execution") == 5
# assert min_distance("kitten", "sitting") == 3

def changer(str1, str2):
    if not str1:
        return len(str2)
    if not str2: 
        return len(str1)


    if str1[0] == str2[0]:
        return changer(str1[1:], str2[1:])
    
    insert = changer(str1, str2[1:])   + 1

    delete = changer(str1[1:], str2) + 1
    replace = changer(str1[1:], str2[1:]) + 1

    return min(insert, delete, replace)

print(changer("kitten", "sitting"))
