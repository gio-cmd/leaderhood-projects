def encode(st):
    nums = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    result = ''
    for i in st:
        if i in nums:
            result += str(nums[i])
        else:
            result += i
    return result


def decode(st):
    nums = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    result = ''
    for i in st:
        if i in nums:
            result += str(nums[i])
        else:
            result += i
    return result