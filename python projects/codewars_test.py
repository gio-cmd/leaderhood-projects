#  1
def nearest_sq(n):
    if n ** 0.5 == int(n ** 0.5):
        return n
    return round(n ** 0.5) ** 2

# 2


def human_years_cat_years_dog_years(human_years):
    result = [human_years]
    cat_years = 0
    dog_years = 0
    for i in range(human_years):
        if i == 0:
            cat_years += 15
            dog_years += 15
        elif i == 1:
            cat_years += 9
            dog_years += 9
        elif i >= 2:
            cat_years += 4
            dog_years += 5
            
    result.append(cat_years)
    result.append(dog_years)


# 3


def repeats(arr):
    result = 0
    for i in arr:
        if arr.count(i) == 1:
            result += i
    return result

# 4

def triangular(n):
    if n <= 0:
        return 0
    return (n + 1) * n // 2

# 5

def mine_location(field):
    result = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                result = [i, j]
    return result

# 6

def dig_pow(n, p):
    num = str(n)
    result = 0
    for i in range(len(num)):
        result += int(num[i]) ** (p + i)
    if result % n == 0:
        return result // n
    else:
        return -1
    

# 7 

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 5 and number != 4 and number != 2:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    num1 = 5
    while num1 * num1 <= number:
        if number % num1 == 0 or number % (num1 + 2) == 0:
            return False
        num1 += 6
    return True


def backwards_prime(start, stop):
    result = []
    for i in range(start, stop + 1):
        reversed_i = int(str(i)[::-1])
        if (is_prime(i) and is_prime(reversed_i)) and i != reversed_i:
            result.append(i)


# 8

def generate_hashtag(s):
    list = s.split()
    list = [word.capitalize() for word in list]
    word = '#'
    
    for i in list:
        word += i
        
    if not s or len(word) > 140:
        return False
        
    return word

# 9

def rot13(message):
    result = ''
    for i in message.lower():
        if i in "abcdefghijklmnopqrstuvwxyz":
            i = chr((ord(i) + 13 - ord('a')) % 26 + ord("a"))
        elif i in "abcdefghijklmnopqrstuvwxyz".upper():
            i = chr((ord(i) + 13 - ord('A')) % 26 + ord("A"))
        result += i
    return result 

    

# 10

def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    result = 0
    for i in numbers:
        result += (i - mean) ** 2
    return result / len(numbers)
    
# 11

def permutations(s):
    result = set([s])
    if len(s) == 1:
        result = set([s])
    elif len(s) == 2:
        result.add(s[1] + s[0])
    
    elif len(s) > 2:
        for i, element in enumerate(s):
            for j in permutations(s[:i] + s[i + 1:]):
                result.add(element + j)
    return result
    
    
    

