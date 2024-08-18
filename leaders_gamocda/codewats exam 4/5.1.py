def reverse_alternate(st):
    result = []
    lis = st.strip().split(' ')
    for i, element in enumerate(lis):
        if i % 2 == 1:
            result.append(element[::-1])
        else:
            result.append(element)
    return " ".join(result)