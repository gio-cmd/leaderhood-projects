#Simple Fun #352: Reagent Formula

def isValid(formula):
    if (not 7 in formula) and (not 8 in formula):
        return False
    if (1 in formula) and (2 in formula):
        return False
    if (3 in formula) and (4 in formula):
        return False
    if (5 in formula) and (6 not in formula) or (5 not in formula and 6 in formula):
        return False
    return True