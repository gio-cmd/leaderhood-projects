# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']


def duplicate_remover(lis):
    result = []
    for i in lis:
        if i not in result:
            result.append(i)
    return result

print(duplicate_remover( ['a', 'b', 'a', 'c']))