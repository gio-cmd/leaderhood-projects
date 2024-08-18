def cakes(recipe, available):
    result = []
    
    for i in recipe:
        if i in available:
            amount = available[i] // recipe[i]
            result.append(amount)
        if i not in available:
            return 0
    
    return min(result)