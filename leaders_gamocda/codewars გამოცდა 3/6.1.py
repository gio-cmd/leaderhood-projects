# Unique In Order

def unique_in_order(sequence):
    result = []
    for i in sequence:
        if not result:
            result.append(i)
        if result[-1] != i:
            result.append(i)
    return result