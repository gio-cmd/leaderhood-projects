def is_divisible(*args):
    for i in args[1:]:
        if args[0] % i != 0:
            return False
    return True
    