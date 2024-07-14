#Luck check

def luck_check(st):
    if not st or not st.isdigit():
        raise ValueError()
    
    half = len(st) // 2
    left = 0
    right = 0
    
    if len(st) % 2 == 0:
        for i in st[:half]:
            left += int(i)
        for i in st[half:]:
            right += int(i)
    elif len(st) % 2 == 1:
        for i in st[:half]:
            left += int(i)
        for i in st[half + 1:]:
            right += int(i)

    return right == left