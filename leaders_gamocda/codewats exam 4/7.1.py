def multiply_all(lis):
    def inner_func(num):
        result = []
        for i in lis:
            result.append(i * num)
        return result
    return inner_func