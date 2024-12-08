# Challenge:
#  Find all unique triplets in an array that sum up to zero.
# Instructions:
# Input: A list of integers (e.g., [-1, 0, 1, 2, -1, -4]).
# Output: A list of unique triplets that sum to zero.
# Test Cases:
# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert three_sum([1, 2, -2, -1]) == []



def unique_triplets(arr):
    arr.sort()
    result = set()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr) - 1):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            for x in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[x] == 0:
                    result.add((arr[i], arr[j], arr[x]))

    return [list(i) for i in result]

print(unique_triplets([-1, 0, 1, 2, -1, -4]))