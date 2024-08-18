def going(n):
    sum = 1
    num = 1
    
    for i in range(n-1):
        num *= 1/(n-i)
        sum += num
    return sum