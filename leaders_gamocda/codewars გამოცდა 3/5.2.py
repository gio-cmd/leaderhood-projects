# Play with two Strings

def work_on_strings(a, b):
    list_a = list(a)
    list_b = list(b)
    
    for j in a:
        for i in range(len(list_b)):
            if list_b[i].lower() == j.lower():
                list_b[i] = list_b[i].swapcase()
    
    for j in b:
        for i in range(len(list_a)):
            if list_a[i].lower() == j.lower():
                list_a[i] = list_a[i].swapcase()
    
    return "".join(list_a) + "".join(list_b)