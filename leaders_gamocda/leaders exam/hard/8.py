# Challenge:
#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Instructions:
# Input: A list of integers (e.g., [100, 4, 200, 1, 3, 2]).
# Output: The length of the longest consecutive sequence (e.g., 4).
# Test Cases:
# assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
# assert longest_consecutive([0, 0]) == 1
# assert longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9


def consecutive_sequence(arr):
    nums = set(arr)
    max1 = 0

    for num in nums:
        if num - 1 not in nums:
            length = 1
            while num + length in nums:
                length += 1
            max1 = max(max1, length)
    
    return max1

print(consecutive_sequence([100, 4, 200, 1, 3, 2]))

# wesit mushaobs 