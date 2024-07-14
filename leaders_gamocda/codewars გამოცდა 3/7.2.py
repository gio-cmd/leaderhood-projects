# How many are smaller than me?


def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        for j in arr[i+1:]:
            if j < arr[i]:
                count += 1
        result.append(count)
    return result
    
        