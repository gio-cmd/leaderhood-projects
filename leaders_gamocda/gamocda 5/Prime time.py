# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            return False 
        
    return True

def orders(num):
    result = []
    for i in range(1, num+1):
        if is_prime(i):
            result.append(i)
    return result

print(orders(20))