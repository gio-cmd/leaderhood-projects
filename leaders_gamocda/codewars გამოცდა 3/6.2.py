# Sum of nested numbers

def sum_nested_numbers(arr, brackets=1):
    if not arr:
        return 0 
    
    sum1 = 0
    
    for i in arr:
        if isinstance(i, list):
            sum1 += sum_nested_numbers(i, brackets + 1)
        else:
            sum1 += i ** brackets
            
    return sum1