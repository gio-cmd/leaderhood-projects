# Age Range Compatibility Equation

def dating_range(age):
    if age >= 14: 
        min_age = age / 2 + 7
        max_age = (age - 7) * 2
        return f"{int(min_age)}-{max_age}"
    else:
        min_age = age  - 0.10 * age
        max_age = age + 0.10 * age
        return f"{int(min_age)}-{int(max_age)}"