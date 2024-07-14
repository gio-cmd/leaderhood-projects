# Anagram Detection

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    if len(test) != len(original):
        return False
    
    test_count = {}
    original_count = {}
    
    for i in test:
        test_count[i] = test_count.get(i, 0) + 1
    for i in original:
        original_count[i] = original_count.get(i, 0) + 1
        
    return original_count == test_count