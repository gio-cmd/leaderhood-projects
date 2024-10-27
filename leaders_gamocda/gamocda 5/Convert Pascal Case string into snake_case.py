# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"


def pascal_into_snake(str):
    result = ''
    for i in str:
        if i.isdigit() == True:
            result += i
        elif i == i.lower():
            result += i
        elif i == str[0]:
            result += i.lower()
        elif i == i.upper() and i != str[0]:
            result += "_" + i.lower()
    return result

print(pascal_into_snake("1"))




